Legacy sources falo-skeleton@3fc7e7014615030021a2e33ad254c91cec92ca22,falo-unities@53bc9e727e3e014f4ed0d721ee16b697fbbf14fd

# Assessment of falo-application (legacy stage)

## Executive Summary

falo-application ("Falo Hub") is a volunteer-development and community-building platform: a Spring Boot 3 monolith REST API plus Socket.IO server (`falo-skeleton`) consumed by a Vue 3 single-page app (`falo-unities`), organised into nine functional domains from organization/project registration through a kanban-style project workspace to volunteer recruitment and interviews. By the static-inventory method it is mid-sized — 1,079 source files, 67,882 SLOC, complexity index 304.28 — but densely wired: three registration pipelines run HTTP → Kafka → consumer → database → mail → websocket, and authorization is a database-driven use-case matrix (UC001–UC111) rather than code. The risk profile is **high**: the only authentication gate lets requests through with no token on every `DEFAULT`-annotated endpoint including password-set and file-upload (`falo-skeleton/src/main/java/com/falo/server/infrastructure/security/AuthenticationInterceptor.java:46-51`), production-shaped credentials are committed in `.env.example` and `application.yml`, and a Redis cache key shared by all users can serve one user's data to another (`falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/ProjectQuery.java:301`). **Headline recommendation:** treat this as a rebuild, not a migration — rotate the exposed credentials now, and fund the rebuild domain-by-domain starting with auth/access control and the three registration pipelines, which every other domain depends on.

## System Inventory

Figures of record from `inventory.md`, measured by the **static inventory method** (UTF-8 with Latin-1 fallback; per-file decision keywords counted as a language-neutral complexity proxy). No file was re-measured in this assessment.

| Figure | Value |
| --- | --- |
| Repositories read (pinned commits) | `falo-skeleton@3fc7e7014615030021a2e33ad254c91cec92ca22`, `falo-unities@53bc9e727e3e014f4ed0d721ee16b697fbbf14fd` — **both read** by all three analysis jobs |
| Files | 1,109 total; 1,079 source files |
| Size | 5,320,698 bytes; 78,747 lines; 67,882 SLOC (67.9 KSLOC) |
| Languages | Java 617 files / 30,068 SLOC; Vue 209 / 25,192; TypeScript 209 / 8,383; HTML 16 (mail templates); 1 SQL DDL (943 lines); YAML, Groovy, XML, CSS, Batch, Shell, JS, Dockerfile |
| Split | `falo-skeleton` 647 files / 34,035 SLOC (backend); `falo-unities` 430 files / 33,847 SLOC (SPA) |
| Shape | Median file 28 SLOC; 711 files under 50 SLOC; 2 oversized files; top-10 files hold 11.7 % of complexity |
| Stack | Spring Boot 3.2.9 / Java 21 / Gradle (Pipelinr CQRS); Vue 3.5 / TypeScript 5.5 / Vite / Pinia / Element Plus; PostgreSQL (12 schemas, 54 tables, one DDL dump `falo-skeleton/database/falo_non_mvp.sql`), Redis, Kafka (8 topics), netty-socketio, Mailgun, AWS S3 |
| Tests | 9 backend JUnit classes (Kafka consumers, register commands); **zero** frontend tests; no coverage tooling in either repository |

Deployment context: single deployable backend + static SPA; local infra via docker-compose (`falo-skeleton/configs/environment-setup.yml`); CI is GitHub Actions running `./gradlew build` (`falo-skeleton/.github/workflows/gradle.yml`).

## Architecture at a Glance

Two repositories, one backend, nine functional domains (structure notes; each claim confirmed there against source). The diagram is in `architecture.mmd` (same folder); the table is its text form.

| # | Domain | Core responsibility | Key evidence |
| --- | --- | --- | --- |
| 1 | Auth and access control | Login (JWT access+refresh), password change/reset by mail token, UC001–UC111 user-case → role authorization | `falo-skeleton/src/main/java/com/falo/server/infrastructure/security/AuthenticationInterceptor.java:74-96` |
| 2 | Organization registration and verification | Public org sign-up → staff/manager assignment → verification feedback → Kafka sync materializes live organization + root account + credential mail | `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/organization_register/OrganizationRegisterConsumer.java:39-74` |
| 3 | Project registration and verification | Org submits project registration (members, archives); verify with feedback; sync creates live project, members, initial publication, member accounts | `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_project_data/SyncProjectConsumer.java:60-116` |
| 4 | Project workspace / task management | Kanban delivery workspace: cycles, tasks, states, labels, comments/attachments, collaborative pages with editor locks | `falo-skeleton/.../application/controller/project/` (11 controllers) |
| 5 | Publication and public portal | Versioned project publications (request → verify → public), public search pages | `falo-skeleton/src/main/java/com/falo/server/application/controller/publication/ProjectPublicationController.java` |
| 6 | Volunteer recruitment and interviews | Recruitment posts, apply-CV forms, volunteer self-registration via Kafka, interview scheduling; acceptance syncs account + profile + project membership | `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_volunteer_data/SyncVolunteerConsumer.java:43-60` |
| 7 | Notifications and realtime | Netty-Socket.IO server with JWT socket auth; persisted notifications; event fan-out across domains | `falo-skeleton/src/main/java/com/falo/server/infrastructure/socket/SocketOpenConnection.java:36-67` |
| 8 | Employee and organization-account administration | Back-office accounts, roles, statistics, Excel export | `falo-skeleton/src/main/java/com/falo/server/application/controller/organization/OrganizationAccountController.java` |
| 9 | Platform services | Runtime config, Vietnam address/country master data, Mailgun + 15 Thymeleaf templates, S3 upload, `libs/core` CQRS/cache plumbing | `falo-skeleton/libs/core/` (62 Java files) |

Cross-cutting facts a reader must hold: the whole backend depends on `libs/core`; every schema lives in one PostgreSQL instance, schema-per-domain (`auth`, `organization_register`, `organization`, `project_register`, `project`, `publication`, `volunteer`, `admin`, `notification`, `employee`, `master`, `mail`), with cross-schema native joins (e.g. `falo-skeleton/.../domain/repositories/project/ProjectRepository.java:19-44`); Kafka is used *inside* the monolith as async decoupling (producers and consumers both in `falo-skeleton`, topics at `falo-skeleton/.../application/constants/KafkaTopic.java:7-14`); Spring Security permits all URLs and defers entirely to the annotation interceptor (`falo-skeleton/src/main/java/com/falo/server/infrastructure/config/WebSecurityConfig.java:32-33`).

## Production Runtime Profile

**No telemetry available.** The inputs contain no APM export and no production batch logs (`00-inputs/` holds only an unfilled `INTENT.md`), so no p50/p95/p99 latency, throughput or error figures can be reported, and the highest-variance domain cannot be established from data.

What the code alone suggests as operational risk candidates (all *inferred*, to be confirmed or discarded once telemetry exists):

- The **project workspace / task management** domain (largest: 12,458 LOC per topology) serves the most chatty UI (kanban, socket events, Redis page locks) — likely latency-sensitive, unverified.
- The three **Kafka registration pipelines** have no visible retry/DLT configuration (`falo-skeleton/src/main/resources/application.yml:32-33`, `missing-topics-fatal: false` only) — failure behaviour under load is unknown (GAP-queue.retry-01).
- Cleanup (page-lock auto-unlock, token overdue handling) runs on an in-memory `ScheduledExecutorService` (`falo-skeleton/src/main/java/com/falo/server/infrastructure/helper/ScheduleHelper.java:51-78`) — schedules die with the JVM and never run on a second instance.

## Technical Debt

Top 10 by remediation value (from the debt job's notes, spot-checked against source; citations verified in this assessment unless marked).

1. **Authorization is optional-by-annotation; Spring Security permits everything.** CSRF off, `requestMatchers("/**").permitAll()`, CORS any-origin-with-credentials (`falo-skeleton/src/main/java/com/falo/server/infrastructure/config/WebSecurityConfig.java:30,32-33,53-54`); a handler without `@Authentication` fails closed invisibly, `DEFAULT` passes with no token (`falo-skeleton/src/main/java/com/falo/server/infrastructure/security/AuthenticationInterceptor.java:40-51`) — verified.
2. **Committed secrets and secret defaults.** JWT fallback signing key literal (`falo-skeleton/src/main/resources/application.yml:48`), Redis password fallback (`application.yml:68`), production-shaped values in `.env.example:2-27` (masked inventory in the restricted portal record) — verified.
3. **JWT expiry units inconsistent between config and code.** `JwtProvider.createToken` adds the raw config value as milliseconds (`falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/security/JwtProvider.java:43`) while refresh expiry divides by 1000/60 (`:90`); defaults `60`/`10080` read as minutes (`application.yml:47,50`) — verified; the deployed env must be compensating (GAP-auth.jwt-01, blocking).
4. **Cross-user Redis cache keys.** `@Cacheable("projectSideBarByOrganizationId")` with no key on a per-user query — first user's sidebar served to everyone (`falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/ProjectQuery.java:301`); other keys omit filter parameters (`:77`, `:99`) — verified.
5. **Kafka consumers log full payloads and swallow failures.** `System.out.println("Consumed message: " + message)` prints PII (`falo-skeleton/src/main/java/com/falo/server/domain/services/queue/organization_register/OrganizationRegisterConsumer.java:41`); catch blocks handle only `JsonProcessingException`; seven near-identical consumer classes must all be fixed (`falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_feedback_type/UpdateFeedbackTypeConsumer.java:25,44`) — verified.
6. **`System.out.println()` as the whole error strategy, ~25 sites.** Empty or print-only catches return half-built objects, e.g. `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/AccountQuery.java:63` (verified), `falo-skeleton/src/main/java/com/falo/server/application/converters/ProjectConverters.java:44,68`, `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/VolunteerQuery.java:83`.
7. **Frontend god components and copy-paste twins.** `falo-unities/src/components/cycle/dialog/ProjectCycleDialogViewTask.vue` (950 lines, complexity 75) and `falo-unities/src/components/cycle/dialog/ProjectCycleDialogViewSubTask.vue` (892, 69) are the same component twice; `falo-unities/src/store/modules/cycle.ts` (643 SLOC) is a god store holding cycles, tasks, pages, members and statistics (`:44-80`); Vue carries 1,539 of the app's 3,327 complexity.
8. **Stateful global exception handler leaking internals.** Mutable instance field shared by the singleton `@ControllerAdvice` (`falo-skeleton/libs/core/src/main/java/com/falo/core/application/exceptions/GlobalExceptionHandlerController.java:22`, verified); the catch-all returns `ex.getMessage()` verbatim with 500 (`:89-97`) — SQL/driver detail disclosure.
9. **Home-grown client-side crypto and JS-readable session cookies.** AES key is a `VITE_*` build variable shipped in the bundle (`falo-unities/src/store/modules/auth.ts:23`, verified); tokens in cookies without `Secure`/`SameSite`/`httpOnly` (`falo-unities/src/api/axios.ts:85-86`, verified).
10. **Dead code, debug leftovers, mock-as-real data.** Commented-out 500 handler (`axios.ts:108-109`, verified); production sidebar built from `@/store/mock/sidebar-item.json` (`src/store/modules/layout/layout.ts:2`); unused declared dependencies `quasar`, `smart-webcomponents` (`package.json:36,47`); unwritten validator `LabelCommandValidator.java:31`; scaffold test asserting nothing (`falo-skeleton/src/test/.../PostFeedbackCommandHandlerTest.java:21-31`).

Carried below the line: `dayLeft` computed from `Period.getDays()` wrong past one month (`falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/ProjectQuery.java:197`); role-based data scoping hand-rolled per query (`falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project_register/ProjectRegisterService.java:60-131`); dead Google/Facebook OAuth config; ~2.9k lines of copy-pasted email-builder HTML in 16 mail templates.

## Security Findings

Static manual review only — no SAST, secret scanner or dependency audit ran in this job. Full exploit scenarios are in the security job's notes; the table carries the material findings.

**Credential inventory in the restricted portal record (not committed; not for sharing)** — 11 committed credential-shaped values (DB, JWT, Mailgun, Google, Redis, MongoDB, pgAdmin, SPA key), all masked there with rotation advice. Highlights: a DB password and public DB host IP at `falo-skeleton/.env.example:2-3`, a JWT signing secret at `.env.example:9`, a Mailgun API key at `.env.example:13`, a hardcoded Redis password fallback at `application.yml:68`.

| ID | CWE | Severity | Location | Finding |
| --- | --- | --- | --- | --- |
| SEC-001 | CWE-306 | **Critical** | `falo-skeleton/.../security/AuthenticationInterceptor.java:46-51` (+ `WebSecurityConfig.java:33`) | `DEFAULT` annotation passes tokenless requests — "requires login" endpoints are anonymous (verified in source) |
| SEC-002 | CWE-306 | **Critical** | `falo-skeleton/.../controller/auth/AuthController.java:61-69` | Unauthenticated `POST /auth/change-password/new-account` sets any account's password and `verified=true` by accountId alone (verified) |
| SEC-003 | CWE-306 | High | `falo-skeleton/.../controller/s3/S3Controller.java:23-26` | Unauthenticated file upload to the production S3 bucket (verified) |
| SEC-004 | CWE-862/200 | High | `falo-skeleton/src/main/java/com/falo/server/application/controller/organization/OrganizationAccountController.java:36-38`; `falo-skeleton/src/main/java/com/falo/server/application/controller/volunteer/VolunteerProfileController.java:66-71` | Unauthenticated read of organization and volunteer PII by accountId |
| SEC-005 | CWE-79 | High | `falo-unities/src/components/cycle/dialog/ProjectCycleDialogViewTask.vue:844` + 4 more sinks; raw HTML stored by `falo-skeleton/.../comment/CommentCommandHandler.java:32-37` | Stored XSS: user HTML rendered via `v-html`, no server-side sanitization; tokens in JS-readable cookies make it a session-theft path |
| SEC-006 | CWE-532 | High | `falo-skeleton/.../socket/SocketOpenConnection.java:44` (verified); exposure `application.yml:102-103` | Socket JWTs logged in cleartext while `/actuator/logfile` is publicly exposed behind `permitAll` |
| SEC-007 | CWE-862 | High | `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/ProjectQuery.java:326-331`; `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove/RemoveProjectMemberCommandHandler.java:22-27` | BOLA: resources addressed only by ID; no object-level ownership checks |
| SEC-008 | CWE-639 | Medium | `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register/OrganizationRegisterQuery.java:47-63` | Update token validated but not bound to the requested organization id |
| SEC-009 | CWE-942 | Medium | `WebSecurityConfig.java:53-55` (verified) | CORS reflects any origin with credentials; CSRF disabled globally |
| SEC-010 | CWE-307 | Medium | `falo-skeleton/.../controller/auth/AuthController.java:31-36` | No rate limiting or lockout on login/token endpoints |
| SEC-011 | CWE-287 | Medium | `falo-skeleton/.../auth/login/LoginCommandHandler.java:75-92`; `.../security/UserDetailInformation.java:24-37` | Account status (ACTIVE/INACTIVE) never enforced at authentication or refresh |
| SEC-012 | CWE-613 | Medium | `falo-skeleton/.env.example:10-11`; `JwtProvider.java:45-53`; `RefreshTokenCommandHandler.java:31-40` | ~7-day access tokens validated purely offline; refresh tokens plaintext, never rotated |
| SEC-013 | CWE-521 | Medium | `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password_first/ChangePasswordFirstCommandValidator.java:16-18` | No server-side password policy; first-change validator is a no-op |
| SEC-014 | CWE-269 | Medium | `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/account/AccountCommandHandler.java:50` | `PUT /account` assigns arbitrary roles from the request body |
| SEC-015 | CWE-262 | Medium | `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/account/AccountCommandHandler.java:50-66`; `falo-skeleton/src/main/java/com/falo/server/infrastructure/security/UserDetailInformation.java:26-28` | Role/password changes do not invalidate the Redis auth cache (up to ~41-day stale roles) |
| SEC-016 | CWE-200/204 | Medium | `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/reset_password/ResetPasswordCommandHandler.java:68` | Reset token returned in the HTTP response body; unknown email → NPE 500 (enumeration) |
| SEC-017 | CWE-20 | Low | `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/register/VolunteerRegisterCommandValidator.java:18-57` | Validators check presence only; unbounded strings, arbitrary URL schemes |
| SEC-018 | CWE-693 | Low | `WebSecurityConfig.java:30-58`; `application.yml:106`; `Dockerfile:17` | No security headers; health details always shown; sample env enables Swagger; container runs as root |
| SEC-019 | CWE-116 | Low | `AuthenticationInterceptor.java:96-102` (verified) | Unescaped exception message/URI interpolated into JSON 401 body |
| SEC-020 | CWE-602 | Low | `falo-unities/src/router/index.ts:26-30`; `auth.ts:23,87` | SPA route gating trusts an AES cookie whose key ships in the bundle |
| SEC-021 | CWE-384/522 | Low-Med | `falo-unities/src/api/axios.ts:85-86` (verified) | Tokens in non-HttpOnly cookies without Secure/SameSite |
| SEC-022 | CWE-829 | Low (process) | `falo-unities/package.json` (no lock file); `falo-skeleton/build.gradle` (no lock file) | No dependency lock files — resolved versions unauditable |

Dependency posture (manifests only): Spring Boot 3.2.9 is on an OSS-EOL line (`falo-skeleton/build.gradle:5`); two conflicting google-api-client versions on the classpath (`dependence.gradle:44`); scanners recommended in the notes (npm audit, OWASP dependency-check, gitleaks, Semgrep, SpotBugs) **did not run** — no shell in this job. No instruction-shaped text aimed at automated review was found in either repository (confirmed by repo-wide reads in the security and debt jobs); the commented-out `@Authentication` annotations are authorization evidence, reported as findings, not followed as directives.

## Documentation Gaps

Comparing what the code does with what README, docs and comments say — the top five a new engineer would need explained:

1. **How to build, run and deploy anything.** `falo-skeleton/README.md:1` is a single title line; `falo-unities` has **no README at all** (file does not exist). The docker-compose stack, env vars and gateway arrangement have to be reverse-engineered from `configs/environment-setup.yml` and the `.env.example` files.
2. **The data-driven authorization model.** Every endpoint's access rule is `@Authentication(SystemUserCase.UCnnn)` resolved at runtime against the `auth.usercase` database table (`falo-skeleton/src/main/java/com/falo/server/infrastructure/security/AuthenticationInterceptor.java:74-96`); `falo-skeleton/src/main/java/com/falo/server/application/enums/SystemUserCase.java` enumerates UC001–UC111 as bare codes with only section comments, and the UC→role matrix exists only in the live database (unseeded in the repo, GAP-falo.data-01). This is the security backbone and it is documented nowhere.
3. **The three registration pipelines.** The register → assign → feedback → Kafka-sync → live-row + account + mail + socket-notification chains (domains 2, 3, 6) are the app's core business flow and exist only as code. The nearest doc, `falo-skeleton/docs/organization-register.md`, documents endpoints that do not exist (`GET management/organization/register` at :34 vs the real `/organization/all` at `OrganizationRegisterController.java:121`) and contains `// TOTO` placeholders (:13, :45) — verified.
4. **Comments that contradict the code on authentication.** `falo-skeleton/src/main/java/com/falo/server/application/enums/SystemUserCase.java:6` comments `DEFAULT` as "Default require login" while the interceptor passes it with no token (verified); `falo-skeleton/src/main/java/com/falo/server/application/controller/organization/OrganizationRegisterController.java:83-84` says "Public(with token)" with no token check anywhere in the flow; UCxxx annotations are commented out and replaced by DEFAULT in `falo-skeleton/src/main/java/com/falo/server/application/controller/project/TagsController.java:41-42`, `falo-skeleton/src/main/java/com/falo/server/application/controller/project/TypesController.java:41-42`, `falo-skeleton/src/main/java/com/falo/server/application/controller/volunteer/VolunteerProfileController.java:64-67`. An engineer trusting comments will misread the entire security posture.
5. **JWT lifetime semantics.** Config defaults read as minutes, code arithmetic assumes milliseconds, `.env.example` carries ~6.9-day access / ~41-day refresh values (`application.yml:47,50`; `JwtProvider.java:43,90`; `.env.example:10-11`, verified). Nothing documents the deployed truth; touching auth config without the SME answer (GAP-auth.jwt-01) will break login in production.

Also undocumented: the database lifecycle (one dump `falo-skeleton/database/falo_non_mvp.sql`, `ddl-auto: none`, no migration tool, no seed/ownership story for `master.*` and `auth.usercase`), and the notification "mark as read" contract mismatch (SPA sends a body, controller reads `@RequestParam` — `falo-unities/src/api/notification/index.ts:7` vs `falo-skeleton/src/main/java/com/falo/server/application/controller/notification/NotificationController.java:26-28`, verified).

## Relative Scale

For ranking against other applications **only** — this is an index, not a plan. It is not a timeline and not a cost; it carries no person-months, schedule, effort or date.

| Measure | Value | Basis |
| --- | --- | --- |
| Complexity index | **304.28** | Static inventory formula `2.94 × KSLOC^1.10` |
| KSLOC | 67.882 | Static inventory (67,882 SLOC) |
| Total complexity | 3,327 (49.01 per KSLOC) | Per-file decision-keyword proxy |
| Concentration | Top 10 files = 11.7 % of complexity; 2 oversized files | Static inventory |

Reading: the index is moderate-high for a two-repo application, driven less by any single monster file (median file is 28 SLOC) than by the number of moving parts — 30 controllers, ~290 command/query/aggregate classes, 9 Kafka consumer chains and a 12-schema database.

## Rebuild Outlook

Every application in this programme is rebuilt, so the question is what makes *this* one easy or hard. Easy: the stack is already modern (Java 21, Spring Boot 3, Vue 3, TypeScript) — there is no COBOL-era translation problem — and the backend is strikingly uniform (Pipelinr CQRS: validator → command handler → aggregate service → Spring Data repository), so once the pattern is understood it repeats mechanically. Hard: the real business rules are not in the code that looks like business rules — role-based data scoping is hand-rolled per query (`ProjectRegisterService.java:60-131`), the authorization matrix lives in a database nobody seeded in the repo, three Kafka pipelines encode implicit ordering (registration → verification → account creation → mail → notification) that only the producer/consumer pairs reveal, and the shared Redis cache is keyed wrongly, so cached behaviour must be *re-specified* from intent, not migrated. Data is the other risk: 12 schemas / 54 tables exist only as a static dump with no migration history and unknown live content, and cross-schema native SQL must be re-mapped domain by domain.

**Domains to understand first, and why:**

1. **Auth and access control** — the UC001–UC111 user-case matrix scopes *everything*; rebuild it (proper Spring Security with object-level authorization) before any other domain's rules can be stated.
2. **Organization registration and verification** — the first pipeline; it creates organizations and root accounts that domains 3–8 consume.
3. **Project registration and verification** — depends on 2; creates projects, members and the initial publication that domains 4–6 build on.
4. **Project workspace / task management** — largest domain (12,458 LOC per topology, 56 leaves); carries the most UI complexity and the cache-lock behaviour.
5. **Platform services** — `libs/core`, mail, S3 and config are cross-cutting; decide their target equivalents (managed services?) once, early.

**Main risks:** hidden business rules in hand-rolled scoping and DB-resident role data; live-data dependency (usercase/master seed, registration statuses, cached accounts); integrations to re-provision (Mailgun domain, AWS S3 bucket, Kafka topics, Socket.IO auth) with committed credentials that must be rotated during cut-over; and contract mismatches (notification mark-as-read, `/api` prefix) that mean the SPA and API have drifted and neither side is a trustworthy specification.

**What this assessment could not establish:** production JWT expiry semantics (GAP-auth.jwt-01), whether the cross-user cache key is the real behaviour or namespaced somewhere unseen (GAP-auth.cache-01), the gateway/`/api` arrangement (GAP-falo.deployment-01), the live contents and ownership of `auth.usercase` and `master.*` (GAP-falo.data-01), Kafka retry/DLT behaviour in deployment (GAP-queue.retry-01), test coverage (no tooling, no shell to run tests — GAP-falo.testing-01), dependency CVEs (no lock files; scanners did not run), and any production performance profile (no telemetry provided). The migration `INTENT.md` is an unfilled template, so nothing here is anchored to a declared modernization scope or target.

## Gaps and questions

| ID | Kind | Question | Where | Impact |
| --- | --- | --- | --- | --- |
| GAP-auth.jwt-01 | unresolved | What are the production values of `JWT_ACCESS_EXPIRATION` / `JWT_REFRESH_EXPIRATION` — milliseconds (as `JwtProvider` assumes) or minutes (as the yml defaults suggest)? | `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/security/JwtProvider.java:43,90` | blocking |
| GAP-auth.cache-01 | ambiguous | Is `projectSideBarByOrganizationId` served from a per-user key elsewhere, or does the single no-key `@Cacheable` really serve one user's sidebar to all users? | `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/ProjectQuery.java:301` | blocking |
| GAP-falo.deployment-01 | unresolved | Does a gateway strip the `/api` prefix in front of falo-skeleton, or do deployed frontends override `VITE_API_BASE_URL`? | `falo-unities/.env.example:29`, `falo-skeleton/src/main/resources/application.yml` | risk |
| GAP-falo.data-01 | unresolved | Who seeds and maintains `auth.usercase` (UC001–UC111 ↔ roles) and the `master.*` address tables? | `falo-skeleton/database/falo_non_mvp.sql:752-800` | risk |
| GAP-queue.retry-01 | unresolved | What is the Kafka listener retry/DLT configuration in the deployed environment? | `falo-skeleton/src/main/resources/application.yml:32-33` | risk |
| GAP-sched.token-01 | unresolved | What expires update/registration tokens across JVM restarts — is there a DB sweep job outside these repositories? | `falo-skeleton/src/main/java/com/falo/server/infrastructure/helper/ScheduleHelper.java:74` | risk |
| GAP-falo.testing-01 | unverified | Backend test coverage was not measured (no JaCoCo, no coverage report; no shell in this job to run `./gradlew test`); frontend has no tests at all. | `falo-skeleton/src/test/java/domain/services/` | risk |
| GAP-assessment.telemetry-01 | missing-source | Are APM exports or production batch logs available for this application? None were provided, so the Production Runtime Profile could not be quantified. | `steps/synthesis-a23f3e1e/in/10-applications/falo-application/00-inputs/` | risk |
| GAP-assessment.intent-01 | ambiguous | `INTENT.md` is an unfilled template — what scope, target platform and constraints does the team intend for this modernization? | `steps/synthesis-a23f3e1e/in/10-applications/falo-application/00-inputs/INTENT.md` | risk |
