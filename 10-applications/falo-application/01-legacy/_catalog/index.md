---
app: "falo-application"
generatedBy: "reconcile_catalog.py"
sources:
  - "falo-skeleton@3fc7e7014615030021a2e33ad254c91cec92ca22"
  - "falo-unities@53bc9e727e3e014f4ed0d721ee16b697fbbf14fd"
modules: 10
items: 134
retired: 0
unassigned: 20
---

# Item catalog of falo-application

The items a person selects for analysis, module by module. Each module has its own document with one card per item; the ids are stable across assessments.

## Modules

| Module | Name | Items | Summary |
| --- | --- | --- | --- |
| auth-and-access-control | Auth and access control | 11 |  |
| employee-and-organization-account-administration | Employee and organization-account administration | 18 |  |
| notifications-and-realtime | Notifications and realtime | 4 |  |
| organization-registration-and-verification | Organization registration and verification | 10 |  |
| other | Other | 13 |  |
| platform-services | Platform services | 20 |  |
| project-registration-and-verification | Project registration and verification | 12 |  |
| project-workspace-and-task-management | Project workspace and task management | 25 |  |
| publication-and-public-portal | Publication and public portal | 7 |  |
| volunteer-recruitment-and-interviews | Volunteer recruitment and interviews | 14 |  |

## Items

| Item | Name | Kind | Status | LOC | Complexity | Files |
| --- | --- | --- | --- | --- | --- | --- |
| auth-and-access-control/api | SPA auth API client and session interceptor | module | active | 175 | low | 4 |
| auth-and-access-control/auth | Login, refresh token and password command handlers | module | active | 656 | medium | 21 |
| auth-and-access-control/auth-2 | Login and password screens (SPA) | module | active | 249 | low | 3 |
| auth-and-access-control/common | Common (2 leaves) | module | active | 395 | low | 2 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-application-cont | Authentication and user-case REST API | module | active | 114 | low | 2 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | Auth domain model and services | module | active | 79 | low | 3 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-repos | falo-skeleton/src/main/java/com/falo/server/domain/repositories/auth | module | active | 379 | low | 3 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/auth | module | active | 106 | low | 3 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | Token and user-case queries | module | active | 53 | low | 2 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | JWT token issuing and user-case authorization | module | active | 230 | low | 5 |
| auth-and-access-control/falo-unities-src-components-auth-changepasswordform-vue | falo-unities/src/components/auth/ChangePasswordForm.vue | module | active | 172 | low | 1 |
| employee-and-organization-account-administration/account | account (2 leaves) | module | active | 280 | low | 8 |
| employee-and-organization-account-administration/api | SPA account administration API clients and hooks | module | active | 154 | low | 7 |
| employee-and-organization-account-administration/commands | Account and employee command handlers | module | active | 535 | medium | 9 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-cont | System, employee and organization account REST API | module | active | 313 | low | 3 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-view | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization | module | active | 122 | low | 4 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | Employee and organization account domain | module | active | 516 | low | 18 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-4 | Account administration queries, statistics and Excel export | module | active | 90 | low | 2 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization | module | active | 224 | low | 3 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization/model | module | active | 84 | low | 6 |
| employee-and-organization-account-administration/falo-unities-src-components-admin-account | falo-unities/src/components/admin/account | module | active | 241 | low | 2 |
| employee-and-organization-account-administration/falo-unities-src-components-organizations-account-organi | falo-unities/src/components/organizations/account/OrganizationAccountForm.vue | module | active | 285 | low | 1 |
| employee-and-organization-account-administration/falo-unities-src-hooks-employee-index-ts | falo-unities/src/hooks/employee/index.ts | module | active | 42 | low | 1 |
| employee-and-organization-account-administration/falo-unities-src-hooks-organizations-accounts-index-ts | falo-unities/src/hooks/organizations/accounts/index.ts | module | active | 74 | low | 1 |
| employee-and-organization-account-administration/falo-unities-src-hooks-system-accounts-index-ts | falo-unities/src/hooks/system-accounts/index.ts | module | active | 40 | low | 1 |
| employee-and-organization-account-administration/falo-unities-src-views-common-employees-employeespage-vue | Employee administration screens | module | active | 545 | medium | 3 |
| employee-and-organization-account-administration/falo-unities-src-views-organization-account-organizationacco | Organization account screens | module | active | 176 | low | 2 |
| employee-and-organization-account-administration/falo-unities-src-views-systemadmin-systemaccount-adminaccoun | System account administration screens | module | active | 57 | low | 1 |
| employee-and-organization-account-administration/falo-unities-src-views-systemadmin-utilities-usercasepage-vu | User-case role matrix screens | module | active | 300 | low | 3 |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-cont | Notification REST API | module | active | 156 | low | 7 |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even | Socket.IO event fan-out | module | active | 365 | low | 4 |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | Notification domain | module | active | 104 | low | 6 |
| notifications-and-realtime/falo-unities-src-socket | SPA socket client and notification API | module | active | 66 | low | 4 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont | Organization registration REST API | module | active | 386 | low | 8 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | Organization registration domain | module | active | 781 | medium | 18 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | Registration queries and list models | module | active | 1599 | low | 9 |
| organization-registration-and-verification/falo-unities-src-hooks-organizations-register-index-ts | falo-unities/src/hooks/organizations/register/index.ts | module | active | 180 | low | 1 |
| organization-registration-and-verification/falo-unities-src-views-public-registerpage-organizationregis | Public organization registration form and status pages | module | active | 605 | medium | 1 |
| organization-registration-and-verification/organization | SPA organization registration API clients | module | active | 230 | low | 10 |
| organization-registration-and-verification/organization-register | Organization registration command handlers | module | active | 1111 | medium | 13 |
| organization-registration-and-verification/organizations | Organization registration back-office screens | module | active | 1676 | high | 10 |
| organization-registration-and-verification/queue | Organization registration Kafka pipeline | module | active | 2975 | medium | 10 |
| organization-registration-and-verification/statuspage | StatusPage (3 leaves) | module | active | 48 | low | 3 |
| other/components | Dashboard statistic cards and task icons | module | active | 438 | medium | 12 |
| other/elements | Shared UI kit | module | active | 2683 | high | 32 |
| other/error | Error and status pages (SPA) | module | active | 196 | low | 6 |
| other/falo-unities | SPA build configuration and static assets | module | active | 249 | low | 31 |
| other/falo-unities-src | SPA application shell | module | active | 194 | low | 13 |
| other/falo-unities-src-store-modules | SPA domain state stores (Pinia) | module | active | 2252 | high | 19 |
| other/falo-unities-src-views-common-dashboard-dashboardpage-vue | Role dashboard screens | module | active | 155 | low | 3 |
| other/falo-unities-src-views-public-homepage-homepage-vue | Public home and landing hero (SPA) | module | active | 375 | low | 4 |
| other/introducepage | Public information pages (SPA) | module | active | 603 | medium | 8 |
| other/layout | Shared layout and page chrome | module | active | 2144 | high | 26 |
| other/modules | SPA layout and organization stores | module | active | 553 | medium | 4 |
| other/utilities | Project tags and types admin screens | module | active | 599 | medium | 6 |
| other/viewmodel | Backend response models (auth, accounts, employees, projects) | module | active | 362 | low | 20 |
| platform-services/aggregate-2 | Configuration and address master-data domain | module | active | 347 | low | 18 |
| platform-services/application | Core utilities, exceptions and API envelope | module | active | 676 | medium | 30 |
| platform-services/config | Core framework configuration | module | active | 572 | medium | 24 |
| platform-services/falo-skeleton-libs-core-src-main-java-com-falo-core-domain-s-2 | Excel export support (POI) | module | active | 135 | low | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application | falo-skeleton/src/main/java/com/falo/server/Application.java | module | active | 16 | low | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | Backend constants, enums and converters | module | active | 859 | medium | 29 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont | Runtime configuration REST API and queries | module | active | 333 | low | 12 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-2 | Address and country master-data API | module | active | 101 | low | 3 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-3 | S3 file upload and download API | module | active | 171 | low | 3 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | Mail delivery (Mailgun, Thymeleaf templates) | module | active | 3215 | high | 27 |
| platform-services/falo-unities-src-api-systems-configs | falo-unities/src/api/systems/configs | module | active | 34 | low | 2 |
| platform-services/falo-unities-src-components-admin-systems-configs | System configuration and logs admin screens | module | active | 201 | low | 4 |
| platform-services/falo-unities-src-hooks-systems-config-index-ts | falo-unities/src/hooks/systems/config/index.ts | module | active | 51 | low | 1 |
| platform-services/falo-unities-src-router-index-ts | SPA routes and role-based navigation | module | active | 651 | low | 1 |
| platform-services/falo-unities-src-store-modules-master-master-ts | SPA master address data (client, store) | module | active | 51 | low | 4 |
| platform-services/infrastructure-2 | Backend application configuration | module | active | 369 | low | 8 |
| platform-services/src | SPA shared models, constants and plugins | module | active | 1642 | high | 63 |
| platform-services/systems | Systems (2 leaves) | module | active | 129 | low | 2 |
| platform-services/utilities | SPA dictionary API clients and hooks | module | active | 147 | low | 10 |
| platform-services/viewmodel | Configuration and master-data response models | module | active | 102 | low | 6 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | Project registration REST API | module | active | 386 | low | 7 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | Project registration domain | module | active | 975 | medium | 18 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | Registration queries and models | module | active | 386 | medium | 8 |
| project-registration-and-verification/falo-unities-src-api-project-register | falo-unities/src/api/project/register | module | active | 47 | low | 2 |
| project-registration-and-verification/falo-unities-src-components-organizations-dialog-attacho | falo-unities/src/components/organizations/dialog/AttachOrganizationAccountDialog.vue | module | active | 93 | low | 1 |
| project-registration-and-verification/falo-unities-src-components-projects-approval-request-at | falo-unities/src/components/projects/approval_request/attachment/FileAttachmentTable.vue | module | active | 270 | medium | 1 |
| project-registration-and-verification/falo-unities-src-components-projects-approval-request-me | falo-unities/src/components/projects/approval_request/member/ProjectMemberForm.vue | module | active | 339 | low | 1 |
| project-registration-and-verification/falo-unities-src-views-organization-projects-registerproject | Project registration submission form (SPA) | module | active | 336 | medium | 1 |
| project-registration-and-verification/project-register | Project registration command handlers | module | active | 1025 | medium | 13 |
| project-registration-and-verification/projects | Project registration back-office screens (SPA) | module | active | 513 | medium | 2 |
| project-registration-and-verification/projects-2 | projects (3 leaves) | module | active | 996 | medium | 7 |
| project-registration-and-verification/queue | Project registration Kafka pipeline | module | active | 1279 | low | 9 |
| project-workspace-and-task-management/comment-and-attachment-command-handlers | Comment and attachment command handlers | module | active | 159 | low | 6 |
| project-workspace-and-task-management/cycle-command-handlers-create-update | Cycle command handlers (create, update) | module | active | 224 | low | 6 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont | Workspace REST API | module | active | 664 | low | 12 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | Workspace domain layer | module | active | 1545 | medium | 48 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-servi | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/tag | module | active | 117 | low | 3 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-5 | Project tag and type command handlers | module | active | 106 | low | 3 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | Workspace queries and response models | module | active | 976 | medium | 10 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model | module | active | 223 | low | 12 |
| project-workspace-and-task-management/falo-unities-src-api-cycle | SPA workspace API clients and hooks | module | active | 91 | low | 5 |
| project-workspace-and-task-management/falo-unities-src-hooks-projects-index-ts | falo-unities/src/hooks/projects/index.ts | module | active | 149 | low | 1 |
| project-workspace-and-task-management/falo-unities-src-hooks-task-labels-index-ts | falo-unities/src/hooks/task/labels/index.ts | module | active | 22 | low | 1 |
| project-workspace-and-task-management/falo-unities-src-hooks-task-sidebar-cycle-index-ts | falo-unities/src/hooks/task/sidebar/cycle/index.ts | module | active | 26 | low | 1 |
| project-workspace-and-task-management/falo-unities-src-hooks-task-states-index-ts | falo-unities/src/hooks/task/states/index.ts | module | active | 29 | low | 1 |
| project-workspace-and-task-management/falo-unities-src-store-modules-task | SPA board state stores | module | active | 176 | low | 3 |
| project-workspace-and-task-management/label | Label command handlers (create, update) | module | active | 158 | low | 6 |
| project-workspace-and-task-management/page | page (4 leaves) | module | active | 46 | low | 8 |
| project-workspace-and-task-management/project | Page, editor and lock command handlers | module | active | 323 | low | 9 |
| project-workspace-and-task-management/project-2 | project (4 leaves) | module | active | 159 | low | 8 |
| project-workspace-and-task-management/project-3 | project (2 leaves) | module | active | 331 | low | 8 |
| project-workspace-and-task-management/project-end-feedback-command-handlers-send-post | Project-end feedback command handlers (send, post) | module | active | 196 | low | 7 |
| project-workspace-and-task-management/project-member-command-handlers-add-update-remove | Project member command handlers (add, update, remove) | module | active | 200 | low | 9 |
| project-workspace-and-task-management/state | State command handlers (create, update) | module | active | 187 | low | 6 |
| project-workspace-and-task-management/task | Task command handlers (create, update) | module | active | 356 | low | 6 |
| project-workspace-and-task-management/task-2 | task (4 leaves) | module | active | 139 | low | 8 |
| project-workspace-and-task-management/task-3 | Task workspace screens and board (SPA) | module | active | 4800 | high | 24 |
| publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont | Publication REST API and commands | module | active | 551 | low | 11 |
| publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | Publication domain | module | active | 419 | low | 3 |
| publication-and-public-portal/falo-unities-src-api-publication | SPA publication API client and hooks | module | active | 181 | low | 3 |
| publication-and-public-portal/falo-unities-src-components-public-feedback-projectfeedb | falo-unities/src/components/public/feedback/ProjectFeedbackCard.vue | module | active | 57 | low | 1 |
| publication-and-public-portal/falo-unities-src-views-organization-profile-organization | falo-unities/src/views/Organization/Profile/OrganizationProfilePage.vue | module | active | 108 | low | 1 |
| publication-and-public-portal/projectpage | Public portal screens | module | active | 627 | medium | 6 |
| publication-and-public-portal/publication-2 | Publication management screens | module | active | 999 | medium | 5 |
| volunteer-recruitment-and-interviews/campaignpage | CampaignPage (2 leaves) | module | active | 193 | low | 2 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-application-cont | Volunteer REST API | module | active | 570 | low | 8 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | Volunteer domain model and services | module | active | 783 | low | 18 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3 | Volunteer queries and models | module | active | 503 | medium | 12 |
| volunteer-recruitment-and-interviews/falo-unities-src-components-common-layout-profile-dialog | falo-unities/src/components/common/layout/Profile/dialog | module | active | 474 | low | 2 |
| volunteer-recruitment-and-interviews/falo-unities-src-components-public-recruitment-publicrecruit | Public recruitment campaign screens (SPA) | module | active | 574 | medium | 4 |
| volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-dashboard-memberor | falo-unities/src/views/MemberOrganization/Dashboard/MemberOrganizationDashboardPage.vue | module | active | 57 | low | 1 |
| volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-recruitment-volunt | Recruitment posting screens (SPA) | module | active | 459 | medium | 3 |
| volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-dashboard-volunteerdashboar | falo-unities/src/views/Volunteer/Dashboard/VolunteerDashboardPage.vue | module | active | 45 | low | 1 |
| volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-profile-volunteerprofilepag | Volunteer profile and dashboard screens | module | active | 286 | low | 1 |
| volunteer-recruitment-and-interviews/queue | Volunteer registration Kafka pipeline | module | active | 928 | low | 8 |
| volunteer-recruitment-and-interviews/volunteer | Volunteer command handlers | module | active | 755 | medium | 21 |
| volunteer-recruitment-and-interviews/volunteer-2 | SPA volunteer data layer | module | active | 773 | medium | 24 |
| volunteer-recruitment-and-interviews/volunteer-3 | Volunteer registration and interview back-office screens | module | active | 1692 | medium | 11 |

## Ambiguities

What a person should check.

- 338 units from one leaf each exceed the limit of 240: every leaf of a domain directory was grouped
- 29 unit(s) left out above the limit of 240 (smallest first: platform-services/falo-unities-src-api-systems-be-logs-index-ts)

## Unassigned files

Inventory files in no item: documentation, build files, or code the topology did not place.

- `falo-skeleton/.env.example`
- `falo-skeleton/.github/workflows/gradle.yml`
- `falo-skeleton/.gitignore`
- `falo-skeleton/Dockerfile`
- `falo-skeleton/README.md`
- `falo-skeleton/build.gradle`
- `falo-skeleton/configs/environment-setup.yml`
- `falo-skeleton/database/falo_non_mvp.sql`
- `falo-skeleton/dependence.gradle`
- `falo-skeleton/docs/organization-register.md`
- `falo-skeleton/docs/project-register.md`
- `falo-skeleton/gradle/wrapper/gradle-wrapper.jar`
- `falo-skeleton/gradle/wrapper/gradle-wrapper.properties`
- `falo-skeleton/gradlew`
- `falo-skeleton/gradlew.bat`
- `falo-skeleton/libs/core/build.gradle`
- `falo-skeleton/settings.gradle`
- `falo-skeleton/update-author.sh`
- `falo-unities/src/api/excel/types.ts`
- `falo-unities/src/api/file/index.ts`
