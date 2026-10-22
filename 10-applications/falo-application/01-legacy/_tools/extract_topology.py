#!/usr/bin/env python3
"""Topology extraction for falo-application (legacy sources).

Usage: python extract_topology.py <source dir> <output dir>

<source dir> holds one folder per legacy repository of the application
(falo-skeleton, the Spring Boot monolith; falo-unities, the Vue SPA), so
every path seen and written starts with the repository folder. The script
reads only that directory, uses no network, writes <output dir>/topology.json
and prints a summary.

Reference patterns detected (one function per pattern, derived from the
repositories' own conventions, not from a hand-written list of files):

Backend, falo-skeleton (Java / Spring Boot):
  * module graph from `import` lines and from capitalized identifier
    references resolved against the declared classes/interfaces/enums;
  * wildcard imports (`import x.y.z.*;`) resolve to the package's module;
  * Pipelinr command dispatch: `pipeline.send(XxxCommand...)` resolved to
    the `XxxCommandHandler` class by the framework's naming convention
    (kind "dispatch");
  * REST entry points: `@RestController` + `@RequestMapping` route table,
    used to resolve the SPA's `api.get('...')` calls across repositories;
  * Kafka: `@KafkaListener(topics = KafkaTopic.X)` and
    `kafkaTemplate.send(KafkaTopic.X, ...)` resolved through the
    `static final String` topic constants -> topic datastore nodes
    (write from producer, read into consumer; consumers are entry points);
  * JPA data dependencies: `@Table(schema=..., name=...)` entities and
    Spring Data repositories (`extends BaseRepository<JpaEntity,...>`),
    plus schema-qualified tables inside native `@Query(...,nativeQuery=true)`
    SQL -> per-PostgreSQL-schema datastore nodes (read/write);
  * PostgreSQL / Redis / Kafka / Mailgun / S3 datastores from the keys of
    `application*.yml` (only logical names are emitted, never config values);
  * `public static void main(` as the application entry point.
  For fixed-column sources (COBOL columns 8-72, RPG) the code area is
  sliced and comment lines stripped before matching.

Frontend, falo-unities (Vue 3 / TypeScript):
  * `@/`-aliased and relative import resolution against the file tree
    (vite alias `@` -> src, tsconfig paths);
  * `api.get/post/put/delete/patch('...')` URL literals matched against the
    backend route table -> cross-repository call edges;
  * vue-router lazy `import('@/views/...')` route components -> screen
    leaves and entry points; `src/main.ts` is the bootstrap entry point.

Dead-end candidates: modules with no inbound edge, excluding entry points,
Pipelinr command handlers and Kafka consumers (they are targets of
framework dispatch that static matching may miss), SPA screens and
components under `components/` (targets of vue-router programmatic
navigation and of the unplugin component auto-import configured in
vite.config.ts), and datastores.

Source code is treated strictly as data by this script.
"""

import json
import os
import re
import sys
from collections import defaultdict

HEADER = ("Legacy sources falo-skeleton@3fc7e7014615030021a2e33ad254c91cec92ca22,"
          "falo-unities@53bc9e727e3e014f4ed0d721ee16b697fbbf14fd")

# --------------------------------------------------------------------------
# Vocabulary
# --------------------------------------------------------------------------

CODE_LANG = {
    ".java": "java", ".kt": "kotlin", ".groovy": "groovy",
    ".ts": "typescript", ".tsx": "typescript", ".js": "javascript",
    ".vue": "vue", ".py": "python", ".rb": "ruby", ".go": "go",
    ".cs": "csharp", ".php": "php", ".sql": "sql",
}
# Files that carry configuration or build logic are read for stores only.
CONFIG_BASENAMES = re.compile(
    r"^(application(-\w+)?\.(yml|yaml|properties)|vite\.config|tsconfig|"
    r"postcss\.config|tailwind\.config|webpack\.config|nuxt\.config|"
    r"package(-lock)?\.json|build\.gradle|settings\.gradle|gradle\.properties|"
    r"docker-compose(\.\w+)?|Dockerfile(\.\w+)?|\.env(\.\w+)?|"
    r"\.eslintrc|\.prettierrc|env\.d\.ts|module\.d\.ts|index\.d\.ts|"
    r"auto-imports\.d\.ts|components\.d\.ts)$"
)
SKIP_DIRS = {".git", "node_modules", "dist", "build", "out", "target",
             ".gradle", ".idea", ".husky", "coverage", ".vscode"}
# Backend tests and frontend test files are excluded from the topology.
TEST_PATH_RE = re.compile(
    r"(^|/)(src/test/|test/|tests/|__tests__/)|\.(spec|test)\.[a-z]+$", re.I)
FIXED_COLUMN_EXT = {".cbl", ".cblle", ".cob", ".cobol", ".cpy", ".rpgle",
                    ".rpg", ".rpgle"}  # code area: columns 8-72, '*' comments

# Domains found by the structure step of this application; modules are
# grouped under them. First matching rule wins per file (ordered, specific
# before general). Inferred from the domain directory layout; the regexes
# match repository-relative paths.
DOMAIN_ORDER = [
    "auth", "notifications", "organization-registration",
    "project-registration", "volunteer", "publication", "project-workspace",
    "administration", "platform", "other",
]
DOMAIN_NAMES = {
    "auth": "Auth and access control",
    "notifications": "Notifications and realtime",
    "organization-registration": "Organization registration and verification",
    "project-registration": "Project registration and verification",
    "volunteer": "Volunteer recruitment and interviews",
    "publication": "Publication and public portal",
    "project-workspace": "Project workspace and task management",
    "administration": "Employee and organization-account administration",
    "platform": "Platform services",
    "other": "Other",
}
DOMAIN_RULES = [
    ("auth", re.compile(
        r"/(controller/auth/|commands/auth/|queries/(auth|token|user_case|account)/|"
        r"aggregate/auth/|Security|security/|JwtProvider|SystemUserCase|UserCaseController|"
        r"views/Auth/|api/auth/|api/axios\.ts|store/modules/auth\.ts|"
        r"constants/(auth|storage|role)\b|/auth/)")),
    ("notifications", re.compile(
        r"(Notification|notification|/socket/|socket-connect|SocketOpenConnection)")),
    ("organization-registration", re.compile(
        r"(organization_register|OrganizationRegister|sync_organization|"
        r"verifiedOrganization|views/Public/RegisterPage/|api/organization/|"
        r"views/Common/Organizations/|components/organizations/|update_feedback_type)")),
    ("project-registration", re.compile(
        r"(project_register|ProjectRegister|ProjectVerifier|sync_project|"
        r"RegisterProjectForm|views/Common/Projects/|api/project/register|"
        r"update_project_feedback_type)")),
    ("volunteer", re.compile(
        r"(volunteer|Volunteer|interview|Interview|recruit|Recruit|recruiment|"
        r"views/MemberOrganization/)")),
    ("publication", re.compile(
        r"(publication|Publication|RequestPublic|pubicProject|"
        r"views/Public/ProjectPage/)")),
    ("project-workspace", re.compile(
        r"(controller/(project|cycle|task|state|label|page|attachment|comment|tags|types)/|"
        r"services/(aggregate|commands|queries)/(project|cycle|task|state|label|page|"
        r"attachment|comment|tags|types)/|domain/aggregate/project/|"
        r"views/Common/Task/|components/(cycle|task)/|store/modules/(cycle|task)|"
        r"api/(cycle|task)/|api/project/|"
        r"repositories/(project|cycle|task|state|label|page|attachment|comment|tags|types)/)")),
    ("administration", re.compile(
        r"(controller/(employees|account|organization)/|OrganizationAccount|"
        r"commands/(employee|account|organization)/|queries/(employee|organization)/|"
        r"repositories/(organization|employees?|account)/|"
        r"aggregate/(employees?|organization)/|"
        r"views/Common/Employees/|views/SystemAdmin/|"
        r"api/(system-accounts|employee|account)/|components/employee/)")),
    ("platform", re.compile(
        r"(controller/(configs|master|s3)/|"
        r"services/(aggregate/(mail|configs|master)|s3|commands/(config|configItem|master|s3|mail))/|"
        r"/(config|configItem|configs|master|mail|s3)/|"
        r"libs/core/|infrastructure/helper/|/constants/|/plugins/|/models/|/locales/|/hooks/|/router/|"
        r"store/(index|modules/(masterData|config))|api/(systems|master|file|utilities|excel)/)")),
]

# --------------------------------------------------------------------------
# Generic helpers
# --------------------------------------------------------------------------


def read_text(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="latin-1") as fh:
            return fh.read()
    except OSError:
        return ""


def slice_code_area(rel, text):
    """Fixed-column sources: keep columns 8-72, drop comment lines."""
    ext = os.path.splitext(rel)[1].lower()
    if ext not in FIXED_COLUMN_EXT:
        return text
    out = []
    for line in text.splitlines():
        if len(line) >= 2 and line[:1] in ("*", "/"):
            out.append("")
            continue
        out.append(line[7:72] if len(line) > 7 else "")
    return "\n".join(out)


def norm_path(p):
    p = p.split("?")[0].split("#")[0].strip()
    if not p:
        return ""
    if not p.startswith("/"):
        p = "/" + p
    while "//" in p:
        p = p.replace("//", "/")
    if len(p) > 1:
        p = p.rstrip("/")
    return p.lstrip("/")


def domain_of(rel):
    for key, pattern in DOMAIN_RULES:
        if pattern.search(rel):
            return key
    return "other"


# --------------------------------------------------------------------------
# Walk
# --------------------------------------------------------------------------


def walk_repositories(src_dir):
    """-> list of (repo, relpath, abspath) for module-bearing source files,
    and a dict of configuration texts keyed by (repo, relpath)."""
    code_files = []
    config_files = {}
    for repo in sorted(os.listdir(src_dir)):
        repo_abs = os.path.join(src_dir, repo)
        if not os.path.isdir(repo_abs) or repo in SKIP_DIRS:
            continue
        for root, dirs, names in os.walk(repo_abs):
            dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
            for name in sorted(names):
                abs_path = os.path.join(root, name)
                rel = os.path.relpath(abs_path, src_dir).replace(os.sep, "/")
                if name.startswith(".") or name.endswith(".d.ts"):
                    # Dotfiles and ambient type declarations are not modules.
                    continue
                if CONFIG_BASENAMES.match(name):
                    config_files[(repo, rel)] = read_text(abs_path)
                    continue
                ext = os.path.splitext(name)[1].lower()
                if ext == ".sql":
                    # DDL / script files feed the datastore inventory.
                    config_files[(repo, rel)] = read_text(abs_path)
                    continue
                if ext not in CODE_LANG:
                    continue
                if TEST_PATH_RE.search(rel):
                    continue
                code_files.append((repo, rel, abs_path))
    return code_files, config_files


# --------------------------------------------------------------------------
# Backend (Java): classes, dispatch, routes, Kafka, JPA
# --------------------------------------------------------------------------

JAVA_PKG_RE = re.compile(r"^\s*package\s+([\w.]+)", re.M)
JAVA_TYPE_RE = re.compile(r"\b(?:class|interface|enum|record)\s+(\w+)")
JAVA_IMPORT_RE = re.compile(r"^\s*import\s+(?:static\s+)?([\w.]+)(\.\*)?\s*;", re.M)
JAVA_TOKEN_RE = re.compile(r"\b([A-Z][A-Za-z0-9_]{2,})\b")
CONST_RE = re.compile(
    r"(?:static\s+final|final\s+static)\s+String\s+(\w+)\s*=\s*\"([^\"]*)\"")
REST_CTRL_RE = re.compile(r"@RestController\b")
# Method mappings may be written bare (`@GetMapping` with no parentheses) or
# with a path argument; both forms occur in these controllers.
REQ_MAPPING_RE = re.compile(r"@RequestMapping(?:\s*\(([^)]*)\))?")
METHOD_MAPPING_RE = re.compile(
    r"@(Get|Post|Put|Delete|Patch|Head|Options|Request)Mapping"
    r"(?:\s*\(([^)]*)\))?")
QUOTED_RE = re.compile(r"\"([^\"]*)\"")
PIPELINE_SEND_RE = re.compile(r"\bpipeline\s*\.\s*send\s*\(\s*([A-Z]\w+)")
KAFKA_LISTENER_RE = re.compile(r"@KafkaListener\s*\(([^)]*)\)")
KAFKA_SEND_RE = re.compile(r"kafkaTemplate\s*\.\s*send\s*\(\s*([^,)]+)")
KAFKA_TOPIC_REF_RE = re.compile(r"\bKafkaTopic\.(\w+)\b")
TABLE_RE = re.compile(r"@Table\s*\(([^)]*)\)")
SCHEMA_ATTR_RE = re.compile(r"schema\s*=\s*\"(\w+)\"")
REPO_EXTENDS_RE = re.compile(
    r"extends\s+(?:BaseRepository|JpaRepository|CrudRepository|"
    r"PagingAndSortingRepository)\s*<\s*(\w+)")
NATIVE_QUERY_RE = re.compile(
    r"@Query\s*\((.*?)nativeQuery\s*=\s*true", re.S)
SQL_TABLE_RE = r"\b({schemas})\.(\w+)\b"
SQL_WRITE_RE = re.compile(
    r"\binsert\s+into\b|\bdelete\s+from\b|\bupdate\s+[\w.]+\s+set\b|"
    r"\bdo\s+update\s+set\b|\bmerge\s+into\b", re.I)
MAIN_RE = re.compile(r"public\s+static\s+void\s+main\s*\(")
COMMAND_HANDLER_RE = re.compile(r"^\w+CommandHandler$")
# Socket / listener beans declared as @Bean returning a *Server* type are
# started from deployment configuration (e.g. the Socket.IO server bean).
BEAN_SERVER_RE = re.compile(r"@Bean\s+public\s+\w*Server\b", re.S)
# Pipelinr binds a command to the Spring bean implementing
# Command.Handler<Cmd, R>; in this codebase handlers extend
# CommandHandler.Default<Cmd> and are named <Cmd>Handler. Both the naming
# convention and the declared generic type are used to resolve the target.
HANDLER_GENERIC_RE = re.compile(r"CommandHandler(?:\.Default)?\s*<\s*(\w+)")


def parse_java(repo, rel, text):
    text = slice_code_area(rel, text)
    pkg_m = JAVA_PKG_RE.search(text)
    pkg = pkg_m.group(1) if pkg_m else ""
    types = JAVA_TYPE_RE.findall(text)
    return {"repo": repo, "rel": rel, "pkg": pkg, "types": types, "text": text}


def java_indexes(java_files):
    """class simple name -> [file keys]; package -> dir; constants;
    command class -> files declaring a CommandHandler<Cmd> generic."""
    simple = defaultdict(list)
    packages = {}
    consts = {}
    handler_cmds = defaultdict(list)
    for jf in java_files:
        key = (jf["repo"], jf["rel"])
        pkg_dir = os.path.dirname(jf["rel"])
        if jf["pkg"]:
            packages.setdefault((jf["repo"], jf["pkg"]), pkg_dir)
        for t in jf["types"]:
            simple[t].append(key)
        for name, value in CONST_RE.findall(jf["text"]):
            consts.setdefault(name, value)
        for m in HANDLER_GENERIC_RE.finditer(jf["text"]):
            handler_cmds[m.group(1)].append(key)
    return simple, packages, consts, handler_cmds


def resolve_topics(blob, consts):
    out = []
    for c in KAFKA_TOPIC_REF_RE.findall(blob):
        out.append(consts.get(c, c))
    for lit in QUOTED_RE.findall(blob):
        if re.fullmatch(r"[\w\-.]+", lit):
            out.append(lit)
    return out


def rest_routes(java_files):
    """-> {path: set(leaf keys)}, set(controller file keys)"""
    routes = defaultdict(set)
    controllers = set()
    for jf in java_files:
        if not REST_CTRL_RE.search(jf["text"]):
            continue
        controllers.add((jf["repo"], jf["rel"]))
        prefixes = [""]
        rm = REQ_MAPPING_RE.search(jf["text"])
        skip_spans = [rm.span()] if rm else []
        if rm and rm.group(1) is not None:
            quoted = QUOTED_RE.findall(rm.group(1))
            prefixes = [norm_path(q) for q in quoted] or [""]
        for mm in METHOD_MAPPING_RE.finditer(jf["text"]):
            if any(mm.start() >= s and mm.end() <= e for s, e in skip_spans):
                continue
            quoted = QUOTED_RE.findall(mm.group(2) or "")
            paths = [norm_path(q) for q in quoted] or [""]
            for prefix in prefixes:
                for path in paths:
                    full = norm_path(prefix + "/" + path)
                    routes[full].add((jf["repo"], jf["rel"]))
    return routes, controllers


def route_regex(route):
    segs = ["[^/]+" if ("{" in s or "*" in s) else re.escape(s)
            for s in route.split("/")]
    return re.compile("^" + "/".join(segs) + "$")


def match_route(path, route_entries, cache):
    """-> set of controller file keys, or None."""
    if path in route_entries:
        return route_entries[path]
    if path not in cache:
        hits = set()
        for route, keys in route_entries.items():
            if "{" in route or "*" in route:
                rx = cache.setdefault(("rx", route), route_regex(route))
                if rx.match(path):
                    hits |= keys
        if not hits:
            for route, keys in route_entries.items():
                if route.startswith(path + "/"):
                    hits |= keys
            if len(hits) > 5:
                # Too loose a prefix match to name one caller -> report it
                # as an unresolved dynamic reference instead of guessing.
                hits = set()
        cache[path] = hits or None
    return cache[path]


# --------------------------------------------------------------------------
# Frontend (Vue/TS): imports, api calls, router screens
# --------------------------------------------------------------------------

FE_IMPORT_RE = re.compile(
    r"""(?:from\s+|import\s+|import\s*\(\s*)['"]([^'"]+)['"]""")
API_CALL_RE = re.compile(
    r"""api\s*\.\s*(get|post|put|delete|patch|head|options)\s*\(\s*['"`]([^'"`]*)""")
ROUTER_DYNAMIC_RE = re.compile(r"""import\s*\(\s*['"]@/([^'"]+)['"]\s*\)""")
FE_EXTS = [".ts", ".js", ".vue", ".tsx"]


def resolve_fe_spec(repo, spec, from_rel, fe_files):
    """Resolve an import specifier to a repository-relative file path."""
    base = None
    if spec.startswith("@/"):
        # rel paths already start with the repository folder, so qualify the
        # alias against the repository of the importing file.
        base = repo + "/src/" + spec[2:]
    elif spec.startswith("."):
        base = os.path.normpath(os.path.join(os.path.dirname(from_rel), spec))
        base = base.replace(os.sep, "/")
    if base is None:
        return None  # external package
    candidates = [base]
    for ext in FE_EXTS:
        candidates.append(base + ext)
    for ext in FE_EXTS:
        candidates.append(base + "/index" + ext)
    for cand in candidates:
        if (repo, cand) in fe_files:
            return cand
    return None


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------


def main():
    if len(sys.argv) != 3:
        print("usage: extract_topology.py <source dir> <output dir>")
        return 2
    src_dir, out_dir = sys.argv[1], sys.argv[2]

    code_files, config_files = walk_repositories(src_dir)
    java_files = [parse_java(r, rel, read_text(p)) for r, rel, p in code_files
                  if rel.endswith(".java")]
    java_keys = {(jf["repo"], jf["rel"]) for jf in java_files}
    fe_files = {(r, rel) for r, rel, _ in code_files
                if not rel.endswith(".java")}

    simple, packages, consts, handler_cmds = java_indexes(java_files)
    routes, controllers = rest_routes(java_files)

    # --- leaves -----------------------------------------------------------
    # Screens: vue-router route components and anything under src/views/.
    router_files = {(r, rel) for r, rel in fe_files if "/router/" in rel}
    screen_files = set()
    for repo, rel in sorted(router_files):
        text = read_text(os.path.join(src_dir, rel))
        for spec in ROUTER_DYNAMIC_RE.findall(text):
            resolved = resolve_fe_spec(repo, "@" + "/" + spec, rel, fe_files)
            if resolved:
                screen_files.add((repo, resolved))
    for repo, rel in fe_files:
        if "/views/" in rel and rel.endswith(".vue"):
            screen_files.add((repo, rel))

    # Grouping: one leaf per directory, except single files and screens.
    dir_members = defaultdict(list)   # (repo, dir) -> [rel]
    leaf_file = {}                    # leaf id -> "file" field
    leaf_kind = {}
    leaf_lang = {}
    file_to_leaf = {}
    for repo, rel, _ in code_files:
        if (repo, rel) in screen_files:
            leaf = rel
            leaf_file[leaf] = rel
            leaf_kind[leaf] = "screen"
            leaf_lang[leaf] = CODE_LANG.get(os.path.splitext(rel)[1].lower(), "unknown")
            file_to_leaf[(repo, rel)] = leaf
            continue
        directory = os.path.dirname(rel)
        dir_members[(repo, directory)].append(rel)
    dir_to_leaf = {}
    for (repo, directory), members in sorted(dir_members.items()):
        if len(members) == 1:
            rel = members[0]
            leaf = rel
            leaf_file[leaf] = rel
            leaf_lang[leaf] = CODE_LANG.get(os.path.splitext(rel)[1].lower(), "unknown")
        else:
            leaf = directory or repo
            leaf_file[leaf] = directory or repo
            counts = defaultdict(int)
            for rel in members:
                counts[CODE_LANG.get(os.path.splitext(rel)[1].lower(), "unknown")] += 1
            leaf_lang[leaf] = max(sorted(counts.items()), key=lambda kv: kv[1])[0]
        leaf_kind[leaf] = "module"
        dir_to_leaf[(repo, directory)] = leaf
        for rel in members:
            file_to_leaf[(repo, rel)] = leaf

    def leaf_of(repo, rel):
        return file_to_leaf.get((repo, rel))

    # --- edges ------------------------------------------------------------
    edges = set()
    dispatch_targets = set()   # leaves that framework dispatch may target
    entry_points = set()
    unresolved = []             # samples of dynamic refs we could not resolve

    def add_edge(src, tgt, kind):
        if src and tgt and src != tgt:
            edges.add((src, tgt, kind))

    # Backend: class references (imports + direct uses) and wildcard imports.
    for jf in java_files:
        src = leaf_of(jf["repo"], jf["rel"])
        if not src:
            continue
        seen = set()
        for name in JAVA_TOKEN_RE.findall(jf["text"]):
            for key in simple.get(name, ()):
                if key == (jf["repo"], jf["rel"]) or key in seen:
                    continue
                seen.add(key)
                add_edge(src, leaf_of(*key), "call")
        for pkg, wildcard in JAVA_IMPORT_RE.findall(jf["text"]):
            if not wildcard:
                continue
            pkg_dir = packages.get((jf["repo"], pkg))
            if pkg_dir:
                add_edge(src, dir_to_leaf.get((jf["repo"], pkg_dir)), "call")

    # Backend: Pipelinr dispatch pipeline.send(XxxCommand) -> XxxCommandHandler.
    for jf in java_files:
        src = leaf_of(jf["repo"], jf["rel"])
        if not src:
            continue
        for cmd in PIPELINE_SEND_RE.findall(jf["text"]):
            handlers = simple.get(cmd + "Handler") or handler_cmds.get(cmd, [])
            if handlers:
                for key in handlers:
                    tgt = leaf_of(*key)
                    dispatch_targets.add(tgt)
                    add_edge(src, tgt, "dispatch")
            else:
                unresolved.append("%s: pipeline.send(%s) handler not found"
                                  % (jf["rel"], cmd))

    # Backend: Kafka listeners (entry points) and producers.
    topic_keys = {}
    for jf in java_files:
        src = leaf_of(jf["repo"], jf["rel"])
        if not src:
            continue
        for args in KAFKA_LISTENER_RE.findall(jf["text"]):
            tm = re.search(r"topics\s*=\s*(\{[^}]*\}|[^,)]+)", args)
            if not tm:
                continue
            for topic in resolve_topics(tm.group(1), consts):
                ds = "ds:kafka:" + topic
                topic_keys[topic] = ds
                add_edge(ds, src, "read")
                entry_points.add(src)
                dispatch_targets.add(src)
        for blob in KAFKA_SEND_RE.findall(jf["text"]):
            for topic in resolve_topics(blob, consts):
                ds = "ds:kafka:" + topic
                topic_keys[topic] = ds
                add_edge(src, ds, "write")

    # Backend: entry points.
    for jf in java_files:
        src = leaf_of(jf["repo"], jf["rel"])
        if not src:
            continue
        if MAIN_RE.search(jf["text"]):
            entry_points.add(src)
        if (jf["repo"], jf["rel"]) in controllers:
            entry_points.add(src)
        if BEAN_SERVER_RE.search(jf["text"]):
            entry_points.add(src)
        if COMMAND_HANDLER_RE.match(jf["types"][0] if jf["types"] else ""):
            dispatch_targets.add(src)

    # --- datastores -------------------------------------------------------
    datastores = {}   # id -> name

    def ds(id_, name):
        datastores[id_] = name
        return id_

    # Logical names only; configuration values are never copied.
    for key, text in config_files.items():
        if not key[1].split("/")[-1].startswith("application"):
            continue
        if re.search(r"jdbc:postgresql", text):
            ds("ds:postgres", "postgres")
        if re.search(r"^\s*redis\s*:", text, re.M) or "cache:" in text and "redis" in text:
            ds("ds:redis", "redis")
        if re.search(r"^\s*kafka\s*:", text, re.M) or "spring.kafka" in text \
                or re.search(r"^  kafka:", text, re.M):
            ds("ds:kafka", "kafka")
        if re.search(r"^mailgun\s*:", text, re.M) or "mailgun" in text:
            ds("ds:mailgun", "mailgun")
        if re.search(r"^\s*s3\s*:", text, re.M) or re.search(r"^aws\s*:", text, re.M):
            ds("ds:s3", "s3")

    # JPA entities -> PostgreSQL schemas.
    entity_schema = {}
    known_schemas = set()
    for jf in java_files:
        tm = TABLE_RE.search(jf["text"])
        if not tm:
            continue
        sm = SCHEMA_ATTR_RE.search(tm.group(1))
        schema = sm.group(1) if sm else "public"
        known_schemas.add(schema)
        ds("ds:postgres:" + schema, schema)
        if jf["types"]:
            entity_schema[jf["types"][0]] = schema
    # DDL snapshots (SQL files) may name more schemas.
    for (repo, rel), text in sorted(config_files.items()):
        if not rel.endswith(".sql"):
            continue
        for schema in re.findall(
                r"create\s+table\s+(?:if\s+not\s+exists\s+)?([a-z_]\w*)\.",
                text, re.I):
            known_schemas.add(schema)
            ds("ds:postgres:" + schema, schema)

    # Repositories: CRUD against the entity's schema; native SQL against
    # schema-qualified tables (read, or write when the SQL mutates).
    schema_pattern = None
    for jf in java_files:
        src = leaf_of(jf["repo"], jf["rel"])
        if not src:
            continue
        for entity in REPO_EXTENDS_RE.findall(jf["text"]):
            schema = entity_schema.get(entity)
            if schema:
                add_edge(src, "ds:postgres:" + schema, "read")
                add_edge(src, "ds:postgres:" + schema, "write")
        if known_schemas and "@Query" in jf["text"]:
            if schema_pattern is None:
                schema_pattern = re.compile(
                    SQL_TABLE_RE.format(schemas="|".join(
                        sorted(known_schemas, key=len, reverse=True))), re.I)
            for sql in NATIVE_QUERY_RE.findall(jf["text"]):
                for schema, _table in schema_pattern.findall(sql):
                    schema = schema.lower()
                    ds("ds:postgres:" + schema, schema)
                    kind = "write" if SQL_WRITE_RE.search(sql) else "read"
                    add_edge(src, "ds:postgres:" + schema, kind)

    # --- frontend edges ---------------------------------------------------
    route_cache = {}
    route_entries = {path: keys for path, keys in routes.items()}
    for repo, rel in sorted(fe_files):
        src = leaf_of(repo, rel)
        if not src:
            continue
        text = read_text(os.path.join(src_dir, rel))
        for spec in FE_IMPORT_RE.findall(text):
            resolved = resolve_fe_spec(repo, spec, rel, fe_files)
            if resolved:
                add_edge(src, leaf_of(repo, resolved), "call")
        for _verb, url in API_CALL_RE.findall(text):
            path = norm_path(url.split("${")[0])
            if not path:
                continue
            hit = match_route(path, route_entries, route_cache)
            if hit:
                for key in hit:
                    add_edge(src, leaf_of(*key), "call")
            else:
                unresolved.append("%s: api call '/%s' matches no backend route"
                                  % (rel, path))

    # Route map dispatch: vue-router lazy imports resolve a variable route
    # target to the screen component (kind "dispatch").
    for repo, rel in sorted(router_files):
        src = leaf_of(repo, rel)
        text = read_text(os.path.join(src_dir, rel))
        for spec in ROUTER_DYNAMIC_RE.findall(text):
            resolved = resolve_fe_spec(repo, "@/" + spec, rel, fe_files)
            if resolved:
                add_edge(src, leaf_of(repo, resolved), "dispatch")

    # Frontend entry points: router screens and the bootstrap.
    for repo, rel in sorted(screen_files):
        leaf = leaf_of(repo, rel)
        if leaf:
            entry_points.add(leaf)
    for repo, rel in fe_files:
        if rel.endswith(("src/main.ts", "src/main.js", "src/main.tsx")):
            leaf = leaf_of(repo, rel)
            if leaf:
                entry_points.add(leaf)

    # --- dead ends --------------------------------------------------------
    inbound = {t for _s, t, _k in edges}
    dynamic_candidates = set(dispatch_targets)
    for leaf, kind in leaf_kind.items():
        if kind == "screen" and "/views/" in leaf:
            dynamic_candidates.add(leaf)   # vue-router programmatic navigation
        if "/components/" in leaf:
            dynamic_candidates.add(leaf)   # unplugin component auto-import
    dead_ends = sorted(
        leaf for leaf, kind in leaf_kind.items()
        if kind in ("module", "screen")
        and leaf not in inbound
        and leaf not in entry_points
        and leaf not in dynamic_candidates)

    # --- assemble ---------------------------------------------------------
    leaf_domain = {}
    members_by_leaf = defaultdict(list)
    for (repo, rel), leaf in file_to_leaf.items():
        members_by_leaf[leaf].append(rel)
    for leaf, members in members_by_leaf.items():
        votes = defaultdict(int)
        for rel in members:
            votes[domain_of(rel)] += 1
        best = max(sorted(votes.items()),
                   key=lambda kv: (kv[1], -DOMAIN_ORDER.index(kv[0])))
        leaf_domain[leaf] = best[0]

    loc_by_leaf = defaultdict(int)
    for (repo, rel), leaf in file_to_leaf.items():
        try:
            with open(os.path.join(src_dir, rel), "rb") as fh:
                loc_by_leaf[leaf] += sum(1 for _ in fh)
        except OSError:
            pass

    def leaf_node(leaf):
        node = {"id": leaf, "name": leaf, "kind": leaf_kind[leaf],
                "language": leaf_lang.get(leaf, "unknown"),
                "loc": loc_by_leaf.get(leaf, 0), "file": leaf_file[leaf]}
        return node

    children = []
    for key in DOMAIN_ORDER:
        leaves = sorted(l for l, d in leaf_domain.items() if d == key)
        if not leaves:
            continue
        children.append({
            "id": "dom:" + key, "name": DOMAIN_NAMES[key], "kind": "domain",
            "children": [leaf_node(l) for l in leaves],
        })
    children.append({
        "id": "dom:data", "name": "Data stores", "kind": "domain",
        "children": [{"id": i, "name": n, "kind": "datastore"}
                     for i, n in sorted(datastores.items())],
    })

    topology = {
        "system": "falo-application",
        "root": {"id": "sys", "name": "falo-application", "kind": "system",
                 "children": children},
        "edges": [{"source": s, "target": t, "kind": k}
                  for s, t, k in sorted(edges)],
        "entryPoints": sorted(entry_points),
        "deadEnds": dead_ends,
        "observations": [],
        "flows": [],
    }

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "topology.json"), "w",
              encoding="utf-8") as fh:
        json.dump(topology, fh, indent=1, ensure_ascii=False)

    # --- summary ----------------------------------------------------------
    repos = sorted({r for r, _rel in file_to_leaf})
    by_kind = defaultdict(int)
    for _s, _t, k in edges:
        by_kind[k] += 1
    kind_totals = defaultdict(int)
    for kind in leaf_kind.values():
        kind_totals[kind] += 1
    print(HEADER)
    print("source dir: %s" % os.path.abspath(src_dir))
    print("repositories: %s" % ", ".join(repos))
    print("files walked: %d (java %d, frontend %d, config %d)"
          % (len(code_files), len(java_files), len(fe_files), len(config_files)))
    print("leaves: %d (modules %d, screens %d, datastores %d)"
          % (len(leaf_kind) + len(datastores), kind_totals["module"],
             kind_totals["screen"], len(datastores)))
    for key in DOMAIN_ORDER:
        count = sum(1 for d in leaf_domain.values() if d == key)
        if count:
            print("  domain %-26s %4d leaves" % (key, count))
    print("edges: %d (call %d, dispatch %d, read %d, write %d)"
          % (len(edges), by_kind["call"], by_kind["dispatch"],
             by_kind["read"], by_kind["write"]))
    cross = sum(1 for s, t, _k in edges
                if not s.startswith("ds:") and not t.startswith("ds:")
                and s.split("/", 1)[0] != t.split("/", 1)[0])
    print("  cross-repository edges: %d" % cross)
    print("  REST routes mapped: %d ; kafka topics: %d"
          % (len(routes), len(topic_keys)))
    print("entry points: %d" % len(entry_points))
    print("dead ends: %d" % len(dead_ends))
    for leaf in dead_ends[:40]:
        print("  %s" % leaf)
    if len(dead_ends) > 40:
        print("  ... and %d more" % (len(dead_ends) - 40))
    print("unresolved dynamic references: %d" % len(unresolved))
    for sample in unresolved[:15]:
        print("  %s" % sample)
    if len(unresolved) > 15:
        print("  ... and %d more" % (len(unresolved) - 15))
    return 0


if __name__ == "__main__":
    sys.exit(main())
