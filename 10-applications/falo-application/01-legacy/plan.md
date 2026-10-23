---
version: 1
app: "falo-application"
generatedBy: "plan_understand"
catalogSources: "falo-skeleton@3fc7e7014615030021a2e33ad254c91cec92ca22,falo-unities@53bc9e727e3e014f4ed0d721ee16b697fbbf14fd"
items: 134
open: 134
batches: 8
planned: 52
---

# Plan to understand falo-application

Understand foundations first along the backend dependency spine, then follow the assessment's rebuild order: platform-services core (fan-in 51/45/40 - every backend item cites it) -> auth (the UC001-UC111 interceptor stack where SEC-001/SEC-002 are Critical) -> the three registration pipelines in order (organization, project, volunteer) -> employee accounts and notifications (fan-in 23 aggregate plus SEC-004/SEC-006/SEC-014/SEC-015) -> the workspace domain, specified among the last backends so its 25 leaves can cite the aggregates they call -> and finally the falo-unities SPA spine, which no backend item depends on. The graph's 43-item backend cycle C0 and 18-item SPA cycle C2 both exceed the 8-item batch cap, so each is split along module lines and the resulting cross-batch gaps are named in every rationale; the only small cycle (comment-and-attachment-command-handlers + label) stays whole in batch 7. 52 of the 134 open items are planned; the other 82 - SPA screens and hooks, small helpers, and command handlers the graph records with no edges - are left out under the 8-batch plan.

## Batch 1: Platform services backend core (foundations, mail, S3)

Rule 2: these are the backend's deepest foundations - the constants/enums item is used by 51 items, core utilities by 45, framework config by 40, backend infrastructure config by 19 and the shared response models (other/viewmodel) by 13, all at depth 1. Mail delivery (3,215 LOC, Mailgun + 15 templates, assessment domain 9) and the S3 upload API (SEC-003, High: unauthenticated upload to the production bucket) are each reachable only through aggregate-2 (fan-in 11, the sole writer of ds:postgres:admin and ds:postgres:master), so they are understood with their only recorded caller. All eight item

- **risk:** high
- **loc:** 6571
- **high complexity:** 1
- **cohesion:** 0.41

### Items

- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `platform-services/application`
- `platform-services/config`
- `platform-services/infrastructure-2`
- `platform-services/aggregate-2`
- `other/viewmodel`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-3`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`

### Depends on outside

| Item | Used by |
| --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | platform-services/aggregate-2, platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons, platform-services/infrastructure-2 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons, platform-services/infrastructure-2 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-3, platform-services/infrastructure-2 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-view | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | platform-services/config |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | platform-services/aggregate-2, platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons, platform-services/infrastructure-2 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |
| organization-registration-and-verification/organization-register | platform-services/aggregate-2, platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |
| organization-registration-and-verification/queue | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont | platform-services/aggregate-2, platform-services/infrastructure-2 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons, platform-services/infrastructure-2 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons, platform-services/infrastructure-2 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |
| project-registration-and-verification/project-register | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |
| project-registration-and-verification/queue | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons, platform-services/infrastructure-2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |
| project-workspace-and-task-management/project-3 | other/viewmodel, platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons |

## Batch 2: Auth and access control backend

Assessment priority 1 and the only batch holding Critical findings: SEC-001 (the DEFAULT annotation passes tokenless requests, AuthenticationInterceptor.java:46-51) sits in the JWT/user-case authorization item (fan-in 16) and SEC-002 (unauthenticated password-set) in the auth REST API; the login/refresh/password handlers carry SEC-011 to SEC-013 and the blocking GAP-auth.jwt-01. The auth aggregate is used by 30 items and the auth repositories are the only writer of ds:postgres:auth (reading seven further schemas), so no later domain spec can be written without them. employee/.../account joins 

- **risk:** high
- **loc:** 1897
- **high complexity:** 0
- **cohesion:** 0.4

### Items

- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `auth-and-access-control/auth`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-repos`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `employee-and-organization-account-administration/account`

### Depends on outside

| Item | Used by |
| --- | --- |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | employee-and-organization-account-administration/account |
| organization-registration-and-verification/queue | employee-and-organization-account-administration/account |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | employee-and-organization-account-administration/account |
| project-registration-and-verification/project-register | employee-and-organization-account-administration/account |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | employee-and-organization-account-administration/account |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | employee-and-organization-account-administration/account |

## Batch 3: Organization registration pipeline

Assessment priority 2: register -> assign -> verify -> Kafka sync -> live organization + root account + mail is one chain, so its five items stay in one batch - the queue writes ds:kafka:register-organization, ds:kafka:sync-data-organization and ds:kafka:update-feedback-type, the REST API (fan-in 12, entry point) and command handlers drive it, and the domain item is the sole writer of ds:postgres:organization_register. Technical-debt item 5 (consumers log full PII payloads, OrganizationRegisterConsumer.java:41) and SEC-008 (update token not bound to the organization id) live here, and GAP-queu

- **risk:** high
- **loc:** 6852
- **high complexity:** 0
- **cohesion:** 0.34

### Items

- `organization-registration-and-verification/queue`
- `organization-registration-and-verification/organization-register`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`

### Depends on outside

| Item | Used by |
| --- | --- |
| employee-and-organization-account-administration/commands | organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-view | organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont, organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate, organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2, organization-registration-and-verification/organization-register, organization-registration-and-verification/queue |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2, organization-registration-and-verification/organization-register |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even | organization-registration-and-verification/organization-register |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | organization-registration-and-verification/organization-register, organization-registration-and-verification/queue |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate, organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 |
| project-registration-and-verification/project-register | organization-registration-and-verification/organization-register, organization-registration-and-verification/queue |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | organization-registration-and-verification/organization-register, organization-registration-and-verification/queue |

## Batch 4: Project registration pipeline

Assessment priority 3: the project pipeline mirrors batch 3 - the queue writes ds:kafka:register-project, ds:kafka:sync-data-project and ds:kafka:update-project-feedback-type, the domain is the sole writer of ds:postgres:project_register, and the flow creates the members and initial publication that the workspace and portal domains consume. Its items cite batch-3 items (organization-register, the org queue) exactly as the assessment's domain order prescribes, and they hand off to the workspace aggregate (3 edges from the domain) in batch 7. The hand-rolled role-based data scoping in ProjectReg

- **risk:** medium
- **loc:** 4051
- **high complexity:** 0
- **cohesion:** 0.33

### Items

- `project-registration-and-verification/queue`
- `project-registration-and-verification/project-register`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`

### Depends on outside

| Item | Used by |
| --- | --- |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate, project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2, project-registration-and-verification/project-register, project-registration-and-verification/queue |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | project-registration-and-verification/project-register, project-registration-and-verification/queue |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even | project-registration-and-verification/project-register |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view, project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate, project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2, project-registration-and-verification/project-register, project-registration-and-verification/queue |
| publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | project-registration-and-verification/queue |

## Batch 5: Employee accounts and realtime notifications

Rule 4 (risk early): this batch carries SEC-004 (unauthenticated organization PII read, employee REST API), SEC-014/SEC-015 (arbitrary role assignment plus a stale Redis auth cache, employee command handlers) and SEC-006 (socket JWTs logged in cleartext, Socket.IO fan-out used by 8 items with fan-out 19). The employee aggregate is used by 23 items and writes ds:postgres:organization and ds:postgres:employees - the workspace comment handlers alone cite it 10 times - so it must precede batch 7; the notifications aggregate is the sole writer of ds:postgres:notification, and the notification REST 

- **risk:** high
- **loc:** 2297
- **high complexity:** 0
- **cohesion:** 0.18

### Items

- `employee-and-organization-account-administration/commands`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`

### Depends on outside

| Item | Used by |
| --- | --- |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-view | employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-4 | employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-cont |
| platform-services/falo-skeleton-libs-core-src-main-java-com-falo-core-domain-s-2 | employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont | notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-cont |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6, notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even |
| volunteer-recruitment-and-interviews/queue | notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even |

## Batch 6: Volunteer registration pipeline

Assessment domain 6 and the third of the three registration pipelines the headline recommendation funds first: the queue writes ds:kafka:register-volunteer and ds:kafka:sync-data-volunteer, the REST API (entry point) dispatches 13 edges into the command handlers, and the domain is the sole writer of ds:postgres:volunteer - acceptance syncs account, profile and project membership. SEC-004's second half (unauthenticated volunteer PII read, VolunteerProfileController.java:66-71) and SEC-017 (presence-only validators) sit here. It runs after the employee batch because its sync creates accounts, an

- **risk:** medium
- **loc:** 3539
- **high complexity:** 0
- **cohesion:** 0.39

### Items

- `volunteer-recruitment-and-interviews/queue`
- `volunteer-recruitment-and-interviews/volunteer`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3`

### Depends on outside

| Item | Used by |
| --- | --- |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate, volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3, volunteer-recruitment-and-interviews/queue, volunteer-recruitment-and-interviews/volunteer |

## Batch 7: Project workspace backend (kanban, comments, queries)

The largest domain (12,458 LOC per topology) and the home of the blocking GAP-auth.cache-01 (the no-key @Cacheable sidebar in the 976-LOC queries item, ProjectQuery.java:301) plus half of SEC-007 (BOLA, ProjectQuery.java:326-331); the comment handlers store the raw HTML behind SEC-005 and form the graph's only two-item cycle with label, kept whole here. The domain aggregate is used by 26 items and is the sole writer of ds:postgres:project, project-3 is used by 9, and the depth-0 query models item is used by 5 (including the publication domain). The REST API dispatches 24 edges to the comment h

- **risk:** high
- **loc:** 4412
- **high complexity:** 0
- **cohesion:** 0.34

### Items

- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-7`
- `project-workspace-and-task-management/project-3`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/label`
- `project-workspace-and-task-management/task`

### Depends on outside

| Item | Used by |
| --- | --- |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-view | project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-servi | project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-5 | project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont |
| project-workspace-and-task-management/state | project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont |
| publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont | project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6 |
| publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6 |

## Batch 8: falo-unities SPA core (models, stores, router, session)

Rule 2 on the frontend: the shared models/plugins item is used by 62 SPA items and the Pinia store modules by 31 (both inside the 18-item SPA cycle C2, whose other members are left out), and the auth session client by 13, so every later screen spec cites them instead of guessing. The router dispatches 29 edges to screens, carries the role-based route gating of SEC-020, and the axios session client carries SEC-021 (tokens in JS-readable cookies); the store modules hold the assessment's debt-7 god store and the auth.ts build-variable AES key (SEC-020). The 66-LOC socket client completes the noti

- **risk:** medium
- **loc:** 4786
- **high complexity:** 2
- **cohesion:** 0.07

### Items

- `platform-services/src`
- `other/falo-unities-src-store-modules`
- `platform-services/falo-unities-src-router-index-ts`
- `auth-and-access-control/api`
- `notifications-and-realtime/falo-unities-src-socket`

### Depends on outside

| Item | Used by |
| --- | --- |
| auth-and-access-control/auth-2 | platform-services/falo-unities-src-router-index-ts |
| auth-and-access-control/common | platform-services/falo-unities-src-router-index-ts |
| employee-and-organization-account-administration/api | other/falo-unities-src-store-modules |
| employee-and-organization-account-administration/falo-unities-src-views-common-employees-employeespage-vue | platform-services/falo-unities-src-router-index-ts |
| employee-and-organization-account-administration/falo-unities-src-views-organization-account-organizationacco | platform-services/falo-unities-src-router-index-ts |
| employee-and-organization-account-administration/falo-unities-src-views-systemadmin-systemaccount-adminaccoun | platform-services/falo-unities-src-router-index-ts |
| employee-and-organization-account-administration/falo-unities-src-views-systemadmin-utilities-usercasepage-vu | platform-services/falo-unities-src-router-index-ts |
| organization-registration-and-verification/falo-unities-src-hooks-organizations-register-index-ts | other/falo-unities-src-store-modules |
| organization-registration-and-verification/falo-unities-src-views-public-registerpage-organizationregis | platform-services/falo-unities-src-router-index-ts |
| organization-registration-and-verification/organization | other/falo-unities-src-store-modules |
| organization-registration-and-verification/organizations | platform-services/falo-unities-src-router-index-ts |
| organization-registration-and-verification/statuspage | platform-services/falo-unities-src-router-index-ts |
| other/error | platform-services/falo-unities-src-router-index-ts |
| other/falo-unities-src-views-common-dashboard-dashboardpage-vue | platform-services/falo-unities-src-router-index-ts |
| other/falo-unities-src-views-public-homepage-homepage-vue | platform-services/falo-unities-src-router-index-ts |
| other/introducepage | platform-services/falo-unities-src-router-index-ts |
| other/layout | platform-services/falo-unities-src-router-index-ts |
| other/utilities | platform-services/falo-unities-src-router-index-ts |
| platform-services/falo-unities-src-api-systems-configs | other/falo-unities-src-store-modules |
| platform-services/falo-unities-src-hooks-systems-config-index-ts | other/falo-unities-src-store-modules |
| platform-services/systems | platform-services/falo-unities-src-router-index-ts |
| platform-services/utilities | other/falo-unities-src-store-modules |
| project-registration-and-verification/falo-unities-src-api-project-register | other/falo-unities-src-store-modules |
| project-registration-and-verification/falo-unities-src-views-organization-projects-registerproject | platform-services/falo-unities-src-router-index-ts |
| project-registration-and-verification/projects | platform-services/falo-unities-src-router-index-ts |
| project-workspace-and-task-management/falo-unities-src-api-cycle | other/falo-unities-src-store-modules |
| project-workspace-and-task-management/falo-unities-src-hooks-projects-index-ts | other/falo-unities-src-store-modules |
| project-workspace-and-task-management/falo-unities-src-hooks-task-sidebar-cycle-index-ts | other/falo-unities-src-store-modules |
| project-workspace-and-task-management/page | other/falo-unities-src-store-modules |
| project-workspace-and-task-management/project-2 | other/falo-unities-src-store-modules |
| project-workspace-and-task-management/task-2 | other/falo-unities-src-store-modules |
| project-workspace-and-task-management/task-3 | platform-services/falo-unities-src-router-index-ts |
| publication-and-public-portal/falo-unities-src-api-publication | other/falo-unities-src-store-modules |
| publication-and-public-portal/falo-unities-src-views-organization-profile-organization | platform-services/falo-unities-src-router-index-ts |
| publication-and-public-portal/projectpage | platform-services/falo-unities-src-router-index-ts |
| publication-and-public-portal/publication-2 | platform-services/falo-unities-src-router-index-ts |
| volunteer-recruitment-and-interviews/campaignpage | platform-services/falo-unities-src-router-index-ts |
| volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-dashboard-memberor | platform-services/falo-unities-src-router-index-ts |
| volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-recruitment-volunt | platform-services/falo-unities-src-router-index-ts |
| volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-dashboard-volunteerdashboar | platform-services/falo-unities-src-router-index-ts |
| volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-profile-volunteerprofilepag | platform-services/falo-unities-src-router-index-ts |
| volunteer-recruitment-and-interviews/volunteer-2 | other/falo-unities-src-store-modules |
| volunteer-recruitment-and-interviews/volunteer-3 | platform-services/falo-unities-src-router-index-ts |

## Left out

| Item | Reason |
| --- | --- |
| auth-and-access-control/auth-2 | SPA login and password screens; depends on the batch-8 spine and no slot remains for domain screens. |
| auth-and-access-control/common | SPA common auth screens (2 leaves); deferred with the domain's other screens. |
| auth-and-access-control/falo-unities-src-components-auth-changepasswordform-vue | 172-LOC leaf component with fan-in 0; nothing cites it yet. |
| employee-and-organization-account-administration/api | SPA account-administration API client; deferred with the administration screens behind batch 8. |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-view | Organization response/view models (fan-in 4); batch 5 hit the 8-item cap. |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-4 | Statistics and Excel-export queries, fan-in 1; low value beside the batch-5 core. |
| employee-and-organization-account-administration/falo-unities-src-components-admin-account | SPA administration components with fan-in 0. |
| employee-and-organization-account-administration/falo-unities-src-components-organizations-account-organi | SPA form component with fan-in 0. |
| employee-and-organization-account-administration/falo-unities-src-hooks-employee-index-ts | 42-LOC SPA hook with fan-in 0. |
| employee-and-organization-account-administration/falo-unities-src-hooks-organizations-accounts-index-ts | 74-LOC SPA hook, fan-in 1; after the SPA spine. |
| employee-and-organization-account-administration/falo-unities-src-hooks-system-accounts-index-ts | 40-LOC SPA hook with fan-in 0. |
| employee-and-organization-account-administration/falo-unities-src-views-common-employees-employeespage-vue | Employee administration screens; SPA surface deferred behind batch 8. |
| employee-and-organization-account-administration/falo-unities-src-views-organization-account-organizationacco | Organization account screens; SPA surface deferred behind batch 8. |
| employee-and-organization-account-administration/falo-unities-src-views-systemadmin-systemaccount-adminaccoun | System account screens; SPA surface deferred behind batch 8. |
| employee-and-organization-account-administration/falo-unities-src-views-systemadmin-utilities-usercasepage-vu | Screens the data-driven UC001-UC111 matrix (assessment documentation gap 2) but is SPA-only; no slot after batch 8. |
| organization-registration-and-verification/falo-unities-src-hooks-organizations-register-index-ts | SPA hook for the registration form; batch 3 already carries the 6,852-LOC backend pipeline. |
| organization-registration-and-verification/falo-unities-src-views-public-registerpage-organizationregis | Public registration form and status screens; deferred with the domain's SPA side. |
| organization-registration-and-verification/organization | SPA API clients for registration (fan-in 5); deferred with the domain's SPA side. |
| organization-registration-and-verification/organizations | 1,676-LOC back-office screens; no slot after the backend pipeline batch. |
| organization-registration-and-verification/statuspage | 48-LOC standalone status page with fan-out 0. |
| other/components | Dashboard statistic cards (fan-in 5); SPA surface deferred behind batch 8. |
| other/elements | 2,683-LOC shared UI kit; too large to add and no batch remains. |
| other/error | SPA error pages; the router half of its 3-item cycle is in batch 8, screens deferred. |
| other/falo-unities | Build configuration and static assets with no recorded edges (fan-in 0, fan-out 0) - nothing to specify. |
| other/falo-unities-src | SPA application shell; deferred with the router's screens. |
| other/falo-unities-src-views-common-dashboard-dashboardpage-vue | Role dashboard screens; SPA surface deferred behind batch 8. |
| other/falo-unities-src-views-public-homepage-homepage-vue | Public landing screens; SPA surface deferred behind batch 8. |
| other/introducepage | Public information pages; SPA surface deferred behind batch 8. |
| other/layout | 2,144-LOC shared layout chrome; too large for a leftover slot. |
| other/modules | SPA layout/organization stores, fan-in 10; deferred behind the batch-8 spine. |
| other/utilities | Tags and types admin screens; SPA surface deferred behind batch 8. |
| platform-services/falo-skeleton-libs-core-src-main-java-com-falo-core-domain-s-2 | POI Excel-export helper with fan-in 1; small and reachable only via the employee export queries. |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application | 16-LOC Spring Boot main class with fan-in 0 - trivial. |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont | Runtime-config REST API dispatches into batch-2 auth and cites the unplanned platform viewmodels; batch 1 was already full at 8 items. |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-2 | Address/country master-data API with fan-in 0 in the graph. |
| platform-services/falo-unities-src-api-systems-configs | 34-LOC SPA configuration client. |
| platform-services/falo-unities-src-components-admin-systems-configs | Configuration and log admin screens; SPA surface deferred behind batch 8. |
| platform-services/falo-unities-src-hooks-systems-config-index-ts | 51-LOC SPA hook. |
| platform-services/falo-unities-src-store-modules-master-master-ts | 51-LOC address-data client/store; deferred with the master-data API. |
| platform-services/systems | Systems admin screens (2 leaves); SPA surface deferred behind batch 8. |
| platform-services/utilities | SPA dictionary clients and hooks, fan-in 1. |
| platform-services/viewmodel | Config response models used only by the unplanned runtime-config API (fan-in 2). |
| project-registration-and-verification/falo-unities-src-api-project-register | 47-LOC SPA API client. |
| project-registration-and-verification/falo-unities-src-components-organizations-dialog-attacho | Dialog component with fan-in 0. |
| project-registration-and-verification/falo-unities-src-components-projects-approval-request-at | Attachment table component with fan-in 0. |
| project-registration-and-verification/falo-unities-src-components-projects-approval-request-me | Member form component, fan-in 1; after the SPA spine. |
| project-registration-and-verification/falo-unities-src-views-organization-projects-registerproject | Registration submission form; SPA side deferred behind batch 8. |
| project-registration-and-verification/projects | Project registration back-office screens; SPA side deferred behind batch 8. |
| project-registration-and-verification/projects-2 | 996 LOC of project screens (3 leaves); SPA side deferred behind batch 8. |
| project-workspace-and-task-management/cycle-command-handlers-create-update | No recorded edges (fan-in 0, fan-out 0) - possibly dead code per assessment debt 10. |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-servi | Tag command handlers dispatched twice by the workspace API; batch 7 hit the 8-item cap. |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-5 | Project tag/type command handlers, fan-in 1; batch 7 hit the 8-item cap. |
| project-workspace-and-task-management/falo-unities-src-api-cycle | SPA workspace API clients; deferred behind batch 8. |
| project-workspace-and-task-management/falo-unities-src-hooks-projects-index-ts | SPA hook, fan-in 1; deferred behind batch 8. |
| project-workspace-and-task-management/falo-unities-src-hooks-task-labels-index-ts | 22-LOC SPA hook. |
| project-workspace-and-task-management/falo-unities-src-hooks-task-sidebar-cycle-index-ts | 26-LOC SPA hook. |
| project-workspace-and-task-management/falo-unities-src-hooks-task-states-index-ts | 29-LOC SPA hook. |
| project-workspace-and-task-management/falo-unities-src-store-modules-task | SPA board store; deferred behind batch 8. |
| project-workspace-and-task-management/page | 46-LOC SPA client (4 leaves); deferred behind batch 8. |
| project-workspace-and-task-management/project | Page/editor-lock command handlers with no recorded caller (fan-in 0, fan-out 0); revisit together with GAP-sched.token-01. |
| project-workspace-and-task-management/project-2 | SPA project clients (4 leaves); deferred behind batch 8. |
| project-workspace-and-task-management/project-end-feedback-command-handlers-send-post | No recorded edges (fan-in 0, fan-out 0). |
| project-workspace-and-task-management/project-member-command-handlers-add-update-remove | Holds RemoveProjectMemberCommandHandler cited by SEC-007 but the graph records no edges; could not place under the cap - reviewer should check whether it is dead code. |
| project-workspace-and-task-management/state | Dispatched with 4 edges by the workspace API, but batch 7 filled with higher fan-in items. |
| project-workspace-and-task-management/task-2 | SPA task clients (4 leaves); deferred behind batch 8. |
| project-workspace-and-task-management/task-3 | 4,800-LOC SPA board holding the god components of assessment debt 7; needs its own batch after batch 8. |
| publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont | Publication REST API and commands; no batch left after the pipelines - plan next with the portal domain. |
| publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | Sole writer of ds:postgres:publication, but deferred with its API under the 8-batch cap. |
| publication-and-public-portal/falo-unities-src-api-publication | SPA publication client; deferred behind batch 8. |
| publication-and-public-portal/falo-unities-src-components-public-feedback-projectfeedb | 57-LOC card component with fan-in 0. |
| publication-and-public-portal/falo-unities-src-views-organization-profile-organization | Organization profile page; SPA portal surface deferred. |
| publication-and-public-portal/projectpage | Public portal screens; SPA portal surface deferred. |
| publication-and-public-portal/publication-2 | Publication management screens; SPA portal surface deferred. |
| volunteer-recruitment-and-interviews/campaignpage | Public campaign screens (2 leaves); SPA side deferred behind batch 8. |
| volunteer-recruitment-and-interviews/falo-unities-src-components-common-layout-profile-dialog | Profile dialog component with fan-in 0. |
| volunteer-recruitment-and-interviews/falo-unities-src-components-public-recruitment-publicrecruit | Public recruitment screens, fan-in 1; after the SPA spine. |
| volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-dashboard-memberor | 57-LOC dashboard page; SPA side deferred behind batch 8. |
| volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-recruitment-volunt | Recruitment posting screens; SPA side deferred behind batch 8. |
| volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-dashboard-volunteerdashboar | 45-LOC dashboard page; SPA side deferred behind batch 8. |
| volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-profile-volunteerprofilepag | Volunteer profile screens; SPA side deferred behind batch 8. |
| volunteer-recruitment-and-interviews/volunteer-2 | 773-LOC SPA volunteer data layer (fan-in 6); deferred behind the batch-8 spine. |
| volunteer-recruitment-and-interviews/volunteer-3 | 1,692-LOC back-office screens in SPA cycle C3; deferred with the domain's screens. |
