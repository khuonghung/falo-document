---
module: "project-registration-and-verification"
name: "Project registration and verification"
items: 12
---

# Project registration and verification

## project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view: Project registration REST API

ProjectRegisterController (submit/update) and ProjectVerifierController (verify with feedback) plus their response view models.

- **kind:** module
- **status:** active
- **loc:** 386
- **complexity:** low
- **digest:** `sha256:b79218f5f6f26f1cd618f9d1c6ee18ccff659ec1a06806e4577c767b10899611`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project_register | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project_register | module | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project_register | 230 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| organization-registration-and-verification/queue | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 2 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| project-registration-and-verification/project-register | call | 1 |
| project-registration-and-verification/queue | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |

### Used by

- `employee-and-organization-account-administration/account`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `organization-registration-and-verification/organization-register`
- `organization-registration-and-verification/queue`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `platform-services/infrastructure-2`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-registration-and-verification/project-register`
- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-servi`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/controller/project/ProjectRegisterController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/project/ProjectVerifierController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project_register/FeedbackProjectVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project_register/FetchProjectRegisterVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project_register/ListFeedbackProjectVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project_register/ListProjectRegisterVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project_register/ProjectRegisterVM.java`


## project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate: Project registration domain

Registration entities (register, archives, main members, feedback, verifiers, update token) with repositories and services.

- **kind:** module
- **status:** active
- **loc:** 975
- **complexity:** medium
- **digest:** `sha256:3b8999fd817a598d2fa768dae8840d30e5782044115ea0e57a725e57b777f653`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project_register | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project_register | module | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project_register | 173 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/repositories/project_register | falo-skeleton/src/main/java/com/falo/server/domain/repositories/project_register | module | falo-skeleton/src/main/java/com/falo/server/domain/repositories/project_register | 621 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project_register | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project_register | module | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project_register | 283 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 2 |
| platform-services/application | call | 1 |
| platform-services/config | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 6 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 3 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 2 |
| project-registration-and-verification/project-register | call | 3 |
| project-registration-and-verification/queue | call | 3 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 3 |

### Used by

- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `platform-services/infrastructure-2`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-registration-and-verification/project-register`
- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-servi`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-5`

### Data stores

| Store | Access |
| --- | --- |
| ds:postgres:auth | read |
| ds:postgres:employees | read |
| ds:postgres:mail | read |
| ds:postgres:organization | read |
| ds:postgres:project | read |
| ds:postgres:project_register | read, write |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project_register/ProjectArchive.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project_register/ProjectFeedback.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project_register/ProjectMainMember.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project_register/ProjectRegister.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project_register/ProjectUpdateToken.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project_register/ProjectVerifier.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project_register/ProjectArchiveRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project_register/ProjectFeedbackRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project_register/ProjectMainMemberRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project_register/ProjectRegisterRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project_register/ProjectUpdateTokenRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project_register/ProjectVerifierRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project_register/ProjectArchiveService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project_register/ProjectFeedbackService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project_register/ProjectMainMemberService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project_register/ProjectRegisterService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project_register/ProjectUpdateTokenService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project_register/ProjectVerifierService.java`


## project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2: Registration queries and models

Queries for registration lists, details and feedback plus tag and type dictionary lookups, with their models.

- **kind:** module
- **status:** active
- **loc:** 386
- **complexity:** medium
- **digest:** `sha256:e98412e9fec31cdf9ce9dbd3e2b477d263b35e30de9174988bdf6f2fbcfdd847`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register | 362 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register/model | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register/model | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register/model | 68 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 2 |
| organization-registration-and-verification/queue | call | 1 |
| other/viewmodel | call | 1 |
| platform-services/application | call | 4 |
| platform-services/config | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 3 |
| platform-services/infrastructure-2 | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| project-registration-and-verification/project-register | call | 1 |
| project-registration-and-verification/queue | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |

### Used by

- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-registration-and-verification/project-register`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register/ProjectFeedbackQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register/ProjectRegisterQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register/TagsQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register/TypesQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register/model/ArchiveModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register/model/AssigneeMapModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register/model/MainMemberModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register/model/ProjectRegisterModel.java`


## project-registration-and-verification/falo-unities-src-api-project-register: falo-unities/src/api/project/register

- **kind:** module
- **status:** active
- **loc:** 47
- **complexity:** low
- **digest:** `sha256:1c1246262dd20e2086f45744c22d9d339ef5b71699145204cba6931a68d9e1b6`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/api/project/register | falo-unities/src/api/project/register | module | falo-unities/src/api/project/register | 53 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/api | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |

### Used by

- `other/falo-unities-src-store-modules`
- `project-workspace-and-task-management/falo-unities-src-hooks-projects-index-ts`

### Files

- `falo-unities/src/api/project/register/index.ts`
- `falo-unities/src/api/project/register/types.ts`


## project-registration-and-verification/falo-unities-src-components-organizations-dialog-attacho: falo-unities/src/components/organizations/dialog/AttachOrganizationAccountDialog.vue

- **kind:** module
- **status:** active
- **loc:** 93
- **complexity:** low
- **digest:** `sha256:bc9c48a95ce118d876f4461d4274599a09165e49141aa9cf705e4646ba6c6aa5`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/organizations/dialog/AttachOrganizationAccountDialog.vue | falo-unities/src/components/organizations/dialog/AttachOrganizationAccountDialog.vue | module | falo-unities/src/components/organizations/dialog/AttachOrganizationAccountDialog.vue | 108 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/modules | call | 1 |
| platform-services/src | call | 2 |

### Files

- `falo-unities/src/components/organizations/dialog/AttachOrganizationAccountDialog.vue`


## project-registration-and-verification/falo-unities-src-components-projects-approval-request-at: falo-unities/src/components/projects/approval_request/attachment/FileAttachmentTable.vue

- **kind:** module
- **status:** active
- **loc:** 270
- **complexity:** medium
- **digest:** `sha256:fcca588563f57c4c9a3f586a3a929b0cb5b5c94cf3adb93e91d2b1bb62ed1577`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/projects/approval_request/attachment/FileAttachmentTable.vue | falo-unities/src/components/projects/approval_request/attachment/FileAttachmentTable.vue | module | falo-unities/src/components/projects/approval_request/attachment/FileAttachmentTable.vue | 323 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/src | call | 3 |

### Files

- `falo-unities/src/components/projects/approval_request/attachment/FileAttachmentTable.vue`


## project-registration-and-verification/falo-unities-src-components-projects-approval-request-me: falo-unities/src/components/projects/approval_request/member/ProjectMemberForm.vue

- **kind:** module
- **status:** active
- **loc:** 339
- **complexity:** low
- **digest:** `sha256:357d6c11710a3d2e94ece644f602f880b1a03d4699df8c41ad9adb7b5db015d0`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/projects/approval_request/member/ProjectMemberForm.vue | falo-unities/src/components/projects/approval_request/member/ProjectMemberForm.vue | module | falo-unities/src/components/projects/approval_request/member/ProjectMemberForm.vue | 383 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/elements | call | 1 |
| other/falo-unities-src-store-modules | call | 1 |
| other/modules | call | 1 |
| platform-services/src | call | 3 |

### Used by

- `project-registration-and-verification/falo-unities-src-views-organization-projects-registerproject`

### Files

- `falo-unities/src/components/projects/approval_request/member/ProjectMemberForm.vue`


## project-registration-and-verification/falo-unities-src-views-organization-projects-registerproject: Project registration submission form (SPA)

Organization's project registration form: main-member contacts, archive attachments, org-account attach dialog and its API client.

- **kind:** module
- **status:** active
- **loc:** 336
- **complexity:** medium
- **digest:** `sha256:8d074501d95a6188277702bb111bffc7c483118aefd207897a6bf4017438fd7f`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/Organization/Projects/RegisterProjectForm.vue | falo-unities/src/views/Organization/Projects/RegisterProjectForm.vue | screen | falo-unities/src/views/Organization/Projects/RegisterProjectForm.vue | 389 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 1 |
| platform-services/src | call | 3 |
| project-registration-and-verification/falo-unities-src-components-projects-approval-request-me | call | 1 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/views/Organization/Projects/RegisterProjectForm.vue`


## project-registration-and-verification/project-register: Project registration command handlers

Handlers for registration create/update, manager verification feedback and assignee updates (with ProjectRegisterTest).

- **kind:** module
- **status:** active
- **loc:** 1025
- **complexity:** medium
- **digest:** `sha256:f0841c94583ba180be81f2dbecafeafd7e450b6d7303c201883bcfb7397bd29e`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/create | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/create | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/create | 211 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/feedback | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/feedback | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/feedback | 362 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/update | 232 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/update_assignee | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/update_assignee | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/update_assignee | 71 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 3 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | call | 1 |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 1 |
| organization-registration-and-verification/queue | call | 2 |
| platform-services/aggregate-2 | call | 1 |
| platform-services/application | call | 6 |
| platform-services/config | call | 7 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 5 |
| platform-services/infrastructure-2 | call | 2 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 3 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 8 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 1 |
| project-registration-and-verification/queue | call | 5 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |

### Used by

- `employee-and-organization-account-administration/account`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `organization-registration-and-verification/organization-register`
- `organization-registration-and-verification/queue`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-servi`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Parts

| Part | Kind | File |
| --- | --- | --- |
| Create registration |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/create/ProjectRegisterCommandHandler.java:18 |
| Manager verification feedback |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/feedback/ProjectFeedbackCommandHandler.java:45 |
| Update registration |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/update/UpdateProjectRegisterCommandHandler.java:18 |
| Update assignee |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/update_assignee/UpdateAssigneeCommandHandler.java:12 |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/create/ProjectRegisterCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/create/ProjectRegisterCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/create/ProjectRegisterCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/feedback/ProjectFeedbackCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/feedback/ProjectFeedbackCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/feedback/ProjectFeedbackCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/update/UpdateProjectRegisterCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/update/UpdateProjectRegisterCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/update/UpdateProjectRegisterCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/update_assignee/UpdateAssigneeCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/update_assignee/UpdateAssigneeCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/update_assignee/UpdateAssigneeCommandValidator.java`
- `falo-skeleton/src/test/java/domain/services/commands/project_register/create/ProjectRegisterTest.java`


## project-registration-and-verification/projects: Project registration back-office screens (SPA)

Back-office list and detail screens: verification timeline, status changes, assignee/member assignment, member and archives tables.

- **kind:** module
- **status:** active
- **loc:** 513
- **complexity:** medium
- **digest:** `sha256:7dea9c4baaebe63cc339e28144ac250a9c6bb2e2680e627210c9f6b4a07ce3e1`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/Common/Projects/ProjectRegistrationDetailPage.vue | falo-unities/src/views/Common/Projects/ProjectRegistrationDetailPage.vue | screen | falo-unities/src/views/Common/Projects/ProjectRegistrationDetailPage.vue | 444 | yes |
| falo-unities/src/views/Common/Projects/ProjectRegistrationsPage.vue | falo-unities/src/views/Common/Projects/ProjectRegistrationsPage.vue | screen | falo-unities/src/views/Common/Projects/ProjectRegistrationsPage.vue | 158 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/elements | call | 1 |
| other/falo-unities-src-store-modules | call | 2 |
| platform-services/src | call | 5 |
| project-registration-and-verification/projects-2 | call | 1 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/views/Common/Projects/ProjectRegistrationDetailPage.vue`
- `falo-unities/src/views/Common/Projects/ProjectRegistrationsPage.vue`


## project-registration-and-verification/projects-2: projects (3 leaves)

- **kind:** module
- **status:** active
- **loc:** 996
- **complexity:** medium
- **digest:** `sha256:70d44ccc324d11b24ad2a4a3f337dc9c34f4de326ea780e02be548544d5a6444`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/projects/detail | falo-unities/src/components/projects/detail | module | falo-unities/src/components/projects/detail | 874 |  |
| falo-unities/src/components/projects/feedback-end | falo-unities/src/components/projects/feedback-end | module | falo-unities/src/components/projects/feedback-end | 236 |  |
| falo-unities/src/components/projects/table | falo-unities/src/components/projects/table | module | falo-unities/src/components/projects/table | 282 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/elements | call | 1 |
| other/falo-unities-src-store-modules | call | 3 |
| other/modules | call | 1 |
| platform-services/src | call | 12 |
| project-workspace-and-task-management/project-2 | call | 2 |

### Used by

- `project-registration-and-verification/projects`

### Files

- `falo-unities/src/components/projects/detail/AssignAssigneeForProjectForm.vue`
- `falo-unities/src/components/projects/detail/AssignMemberToProjectBoardForm.vue`
- `falo-unities/src/components/projects/detail/ChangeProjectRegistrationStatusForm.vue`
- `falo-unities/src/components/projects/detail/ProjectRegisterStatusHistory.vue`
- `falo-unities/src/components/projects/detail/ProjectRegisterTimeline.vue`
- `falo-unities/src/components/projects/table/ProjectMemberTable.vue`
- `falo-unities/src/components/projects/table/ProjectRegistrationsTable.vue`


## project-registration-and-verification/queue: Project registration Kafka pipeline

Producers and consumers for register-project, sync-data-project (creates live project, members, initial publication and member accounts) and update-project-feedback-type, with consumer tests.

- **kind:** module
- **status:** active
- **loc:** 1279
- **complexity:** low
- **digest:** `sha256:723b4ad3f112fe280e5afa2b892b046d80f9e9b2156895e5513c133b06451794`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queue/project_register | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/project_register | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/project_register | 91 | yes |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_project_data | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_project_data | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_project_data | 233 | yes |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_project_data/message/SyncProjectMessage.java | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_project_data/message/SyncProjectMessage.java | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_project_data/message/SyncProjectMessage.java | 65 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_project_feedback_type | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_project_feedback_type | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_project_feedback_type | 66 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 4 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| organization-registration-and-verification/organization-register | call | 1 |
| organization-registration-and-verification/queue | call | 1 |
| platform-services/aggregate-2 | call | 1 |
| platform-services/application | call | 2 |
| platform-services/config | call | 3 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 7 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 4 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 6 |
| project-registration-and-verification/project-register | call | 3 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |

### Used by

- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-registration-and-verification/project-register`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Data stores

| Store | Access |
| --- | --- |
| ds:kafka:register-project | write |
| ds:kafka:sync-data-project | write |
| ds:kafka:update-project-feedback-type | write |

### Parts

| Part | Kind | File |
| --- | --- | --- |
| Register pipeline consumer |  | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/project_register/ProjectRegisterConsumer.java:38 |
| Sync consumer (create project, members, publication, accounts) |  | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_project_data/SyncProjectConsumer.java:60 |
| Feedback-type consumer |  | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_project_feedback_type/UpdateProjectFeedbackTypeConsumer.java:23 |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/project_register/ProjectRegisterConsumer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/project_register/ProjectRegisterProducer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_project_data/SyncProjectConsumer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_project_data/SyncProjectProducer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_project_data/message/SyncProjectMessage.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_project_feedback_type/UpdateProjectFeedbackTypeConsumer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_project_feedback_type/UpdateProjectFeedbackTypeProducer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_project_feedback_type/message/UpdateProjectFeedbackTypeMessage.java`
- `falo-skeleton/src/test/java/domain/services/queue/sync_project_data/SyncProjectConsumerTest.java`
