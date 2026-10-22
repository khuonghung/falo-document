---
module: "organization-registration-and-verification"
name: "Organization registration and verification"
items: 10
---

# Organization registration and verification

## organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont: Organization registration REST API

OrganizationRegisterController endpoints for submitting, updating and verifying registrations, with response view models.

- **kind:** module
- **status:** active
- **loc:** 386
- **complexity:** low
- **digest:** `sha256:0a07bab4603a858234f9f848c0506185895bfcc2affe25c29593a27fca0fc9cb`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/controller/organization | falo-skeleton/src/main/java/com/falo/server/application/controller/organization | module | falo-skeleton/src/main/java/com/falo/server/application/controller/organization | 384 | yes |
| falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization_register | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization_register | module | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization_register | 237 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 1 |
| employee-and-organization-account-administration/commands | call, dispatch | 2 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-view | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 1 |
| organization-registration-and-verification/organization-register | call, dispatch | 9 |
| organization-registration-and-verification/queue | call | 2 |
| platform-services/application | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 2 |

### Used by

- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `organization-registration-and-verification/organization`
- `organization-registration-and-verification/organization-register`
- `organization-registration-and-verification/queue`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/controller/organization/OrganizationRegisterController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization_register/AssigneeMapVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization_register/AssigneeVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization_register/FeedBackRegisterVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization_register/FeedbackHistoryVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization_register/FetchOrganizationVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization_register/ListOrganizationVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization_register/OrganizationRegisterVM.java`


## organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate: Organization registration domain

Registration entities (register, feedback, assignee, contacts, projects, update token) with repositories and services.

- **kind:** module
- **status:** active
- **loc:** 781
- **complexity:** medium
- **digest:** `sha256:4f1e21ba5f60df5cae7c8410a6742c4b36cbc79bdeefaf0b3f5da2ac20e44613`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization_register | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization_register | module | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization_register | 186 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization_register | falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization_register | module | falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization_register | 491 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization_register | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization_register | module | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization_register | 196 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 3 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 2 |
| organization-registration-and-verification/organization-register | call | 3 |
| platform-services/application | call | 1 |
| platform-services/config | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 2 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 2 |

### Used by

- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `organization-registration-and-verification/organization-register`
- `organization-registration-and-verification/queue`
- `platform-services/aggregate-2`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `platform-services/infrastructure-2`
- `project-registration-and-verification/project-register`

### Data stores

| Store | Access |
| --- | --- |
| ds:postgres:auth | read |
| ds:postgres:employees | read |
| ds:postgres:mail | read |
| ds:postgres:organization_register | read, write |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization_register/OrganizationAssignee.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization_register/OrganizationContact.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization_register/OrganizationProject.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization_register/OrganizationRegister.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization_register/OrganizationRegisterFeedback.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization_register/UpdateOrganizationToken.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization_register/OrganizationAssigneeRegisterRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization_register/OrganizationContactRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization_register/OrganizationProjectRegisterRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization_register/OrganizationRegisterFeedbackRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization_register/OrganizationRegisterRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization_register/UpdateOrganizationTokenRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization_register/OrganizationAssigneeService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization_register/OrganizationContactService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization_register/OrganizationProjectService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization_register/OrganizationRegisterFeedbackService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization_register/OrganizationRegisterService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization_register/UpdateOrganizationTokenService.java`


## organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2: Registration queries and list models

Queries and models for registration lists, details and staff/manager assignee lookups.

- **kind:** module
- **status:** active
- **loc:** 1599
- **complexity:** low
- **digest:** `sha256:883b953a5b92c3a1931d8a2ab0f54352a4ba1a517f9631ec0a02091f1f13616d`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register | 273 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register/model | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register/model | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register/model | 93 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| organization-registration-and-verification/organization-register | call | 1 |
| organization-registration-and-verification/queue | call | 2 |
| platform-services/application | call | 4 |
| platform-services/config | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 4 |
| platform-services/infrastructure-2 | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 2 |

### Used by

- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `organization-registration-and-verification/organization-register`
- `organization-registration-and-verification/queue`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-registration-and-verification/project-register`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register/AssigneeQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register/OrganizationRegisterQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register/model/AssigneeMapModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register/model/AssigneeModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register/model/ContactModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register/model/FeedBackHistoryModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register/model/OrganizationModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization_register/model/OrganizationWithContactAndAssigneeModel.java`
- `falo-skeleton/src/test/java/domain/services/queries/organization_register/OrganizationRegisterQueryTest.java`


## organization-registration-and-verification/falo-unities-src-hooks-organizations-register-index-ts: falo-unities/src/hooks/organizations/register/index.ts

- **kind:** module
- **status:** active
- **loc:** 180
- **complexity:** low
- **digest:** `sha256:10f13b6cfb4a0426abb082ab64c44eaaf6e0fcaf3d5665ee64719a772b94e956`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/hooks/organizations/register/index.ts | falo-unities/src/hooks/organizations/register/index.ts | module | falo-unities/src/hooks/organizations/register/index.ts | 188 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| organization-registration-and-verification/organization | call | 4 |
| platform-services/src | call | 1 |
| project-workspace-and-task-management/project-2 | call | 1 |

### Used by

- `other/falo-unities-src-store-modules`
- `other/modules`

### Files

- `falo-unities/src/hooks/organizations/register/index.ts`


## organization-registration-and-verification/falo-unities-src-views-public-registerpage-organizationregis: Public organization registration form and status pages

Public sign-up form (email-token create/update) plus the success and expired status pages it routes to.

- **kind:** module
- **status:** active
- **loc:** 605
- **complexity:** medium
- **digest:** `sha256:73df35782de6965677afe7b9b1d120914fe8e03ec19ca01543549c388cb72a17`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/Public/RegisterPage/OrganizationRegisterForm.vue | falo-unities/src/views/Public/RegisterPage/OrganizationRegisterForm.vue | screen | falo-unities/src/views/Public/RegisterPage/OrganizationRegisterForm.vue | 691 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| organization-registration-and-verification/organizations | call | 1 |
| other/elements | call | 1 |
| other/layout | call | 1 |
| other/modules | call | 1 |
| platform-services/falo-unities-src-store-modules-master-master-ts | call | 1 |
| platform-services/src | call | 4 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/views/Public/RegisterPage/OrganizationRegisterForm.vue`


## organization-registration-and-verification/organization: SPA organization registration API clients

Typed clients and response mappers for organization registration, listing, assignee and account endpoints.

- **kind:** module
- **status:** active
- **loc:** 230
- **complexity:** low
- **digest:** `sha256:ae5759a94091cef2925b666d90d179fb50f0ba5b70d730ac6c565067b19c2008`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/api/organization/accounts | falo-unities/src/api/organization/accounts | module | falo-unities/src/api/organization/accounts | 59 |  |
| falo-unities/src/api/organization/assign | falo-unities/src/api/organization/assign | module | falo-unities/src/api/organization/assign | 26 |  |
| falo-unities/src/api/organization/get | falo-unities/src/api/organization/get | module | falo-unities/src/api/organization/get | 89 |  |
| falo-unities/src/api/organization/list | falo-unities/src/api/organization/list | module | falo-unities/src/api/organization/list | 41 |  |
| falo-unities/src/api/organization/register | falo-unities/src/api/organization/register | module | falo-unities/src/api/organization/register | 53 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/api | call | 5 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 5 |
| platform-services/src | call | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 2 |

### Used by

- `employee-and-organization-account-administration/falo-unities-src-hooks-organizations-accounts-index-ts`
- `organization-registration-and-verification/falo-unities-src-hooks-organizations-register-index-ts`
- `organization-registration-and-verification/organizations`
- `other/falo-unities-src-store-modules`
- `other/modules`

### Files

- `falo-unities/src/api/organization/accounts/index.ts`
- `falo-unities/src/api/organization/accounts/types.ts`
- `falo-unities/src/api/organization/assign/index.ts`
- `falo-unities/src/api/organization/assign/types.ts`
- `falo-unities/src/api/organization/get/index.ts`
- `falo-unities/src/api/organization/get/type.ts`
- `falo-unities/src/api/organization/list/index.ts`
- `falo-unities/src/api/organization/list/types.ts`
- `falo-unities/src/api/organization/register/index.ts`
- `falo-unities/src/api/organization/register/types.ts`


## organization-registration-and-verification/organization-register: Organization registration command handlers

Handlers for creating/updating a registration, assigning staff/manager reviewers and recording verification feedback.

- **kind:** module
- **status:** active
- **loc:** 1111
- **complexity:** medium
- **digest:** `sha256:3b493efa9c68a79169f37e384d1b58a1cbcfb8fb6136ab5e6606b5f965ce1f77`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/assign_user | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/assign_user | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/assign_user | 83 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/create | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/create | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/create | 215 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/feedback | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/feedback | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/feedback | 345 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/update | 193 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 3 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | call | 1 |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 3 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 8 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 1 |
| organization-registration-and-verification/queue | call | 3 |
| platform-services/aggregate-2 | call | 1 |
| platform-services/application | call | 8 |
| platform-services/config | call | 8 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 8 |
| platform-services/infrastructure-2 | call | 3 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 1 |
| project-registration-and-verification/project-register | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |

### Used by

- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `organization-registration-and-verification/queue`
- `platform-services/aggregate-2`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`

### Parts

| Part | Kind | File |
| --- | --- | --- |
| Create registration |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/create/OrganizationRegisterCommandHandler.java:21 |
| Assign staff/manager reviewer |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/assign_user/AssignUserCommandHandler.java:14 |
| Record verification feedback |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/feedback/FeedBackRegisterCommandHandler.java:42 |
| Update registration (email token) |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/update/UpdateOrganizationRegisterCommandHandler.java:21 |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/assign_user/AssignUserCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/assign_user/AssignUserCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/assign_user/AssignUserCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/create/OrganizationRegisterCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/create/OrganizationRegisterCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/create/OrganizationRegisterCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/feedback/FeedBackRegisterCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/feedback/FeedBackRegisterCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/feedback/FeedBackRegisterCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/update/UpdateOrganizationRegisterCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/update/UpdateOrganizationRegisterCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/update/UpdateOrganizationRegisterCommandValidator.java`
- `falo-skeleton/src/test/java/domain/services/commands/organization_register/create/OrganizationRegisterTest.java`


## organization-registration-and-verification/organizations: Organization registration back-office screens

Back-office list and detail screens: assignee and status-change forms, registration timeline, status history and attach-profile/account tables.

- **kind:** module
- **status:** active
- **loc:** 1676
- **complexity:** high
- **digest:** `sha256:6598d4456f752e47f51c747907c7c9c9a3a78029feeae97018bb1cd8cd164f25`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/organizations/detail | falo-unities/src/components/organizations/detail | module | falo-unities/src/components/organizations/detail | 681 |  |
| falo-unities/src/components/organizations/register | falo-unities/src/components/organizations/register | module | falo-unities/src/components/organizations/register | 389 |  |
| falo-unities/src/components/organizations/table | falo-unities/src/components/organizations/table | module | falo-unities/src/components/organizations/table | 321 |  |
| falo-unities/src/views/Common/Organizations/OrganizationRegistrationDetailPage.vue | falo-unities/src/views/Common/Organizations/OrganizationRegistrationDetailPage.vue | screen | falo-unities/src/views/Common/Organizations/OrganizationRegistrationDetailPage.vue | 410 | yes |
| falo-unities/src/views/Common/Organizations/OrganizationsRegistrationsPage.vue | falo-unities/src/views/Common/Organizations/OrganizationsRegistrationsPage.vue | screen | falo-unities/src/views/Common/Organizations/OrganizationsRegistrationsPage.vue | 194 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| organization-registration-and-verification/organization | call | 1 |
| other/elements | call | 2 |
| other/falo-unities-src-store-modules | call | 1 |
| other/modules | call | 4 |
| platform-services/src | call | 13 |

### Used by

- `organization-registration-and-verification/falo-unities-src-views-public-registerpage-organizationregis`
- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/components/organizations/detail/AssignRegistrationsForm.vue`
- `falo-unities/src/components/organizations/detail/ChangeRegistrationStatusForm.vue`
- `falo-unities/src/components/organizations/detail/OrganizationRegisterTimeline.vue`
- `falo-unities/src/components/organizations/detail/RegisterStatusHistory.vue`
- `falo-unities/src/components/organizations/register/ProjectsForm.vue`
- `falo-unities/src/components/organizations/register/RepresentativeForm.vue`
- `falo-unities/src/components/organizations/table/AttachProfileTable.vue`
- `falo-unities/src/components/organizations/table/OrganizationsRegistrationsTable.vue`
- `falo-unities/src/views/Common/Organizations/OrganizationRegistrationDetailPage.vue`
- `falo-unities/src/views/Common/Organizations/OrganizationsRegistrationsPage.vue`


## organization-registration-and-verification/queue: Organization registration Kafka pipeline

Producers and consumers for register-organization (consume then assign staff/manager), sync-data-organization (materialize live organization and root account) and update-feedback-type, with message DTOs and consumer tests.

- **kind:** module
- **status:** active
- **loc:** 2975
- **complexity:** medium
- **digest:** `sha256:93b6cf70e843a3f8b26fac01cc07ce68e521cfde5477809943cb7da6b866ec94`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queue/organization_register | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/organization_register | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/organization_register | 168 | yes |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_organization_data | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_organization_data | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_organization_data | 159 | yes |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_organization_data/message/SyncOrganizationMessage.java | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_organization_data/message/SyncOrganizationMessage.java | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_organization_data/message/SyncOrganizationMessage.java | 78 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_feedback_type | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_feedback_type | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_feedback_type | 66 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 2 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 3 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 4 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 1 |
| organization-registration-and-verification/organization-register | call | 2 |
| platform-services/aggregate-2 | call | 2 |
| platform-services/application | call | 2 |
| platform-services/config | call | 4 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 9 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 2 |
| project-registration-and-verification/project-register | call | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |

### Used by

- `employee-and-organization-account-administration/account`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `organization-registration-and-verification/organization-register`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-registration-and-verification/project-register`
- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-servi`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Data stores

| Store | Access |
| --- | --- |
| ds:kafka:register-organization | write |
| ds:kafka:sync-data-organization | write |
| ds:kafka:update-feedback-type | write |

### Parts

| Part | Kind | File |
| --- | --- | --- |
| Register pipeline consumer (assign staff/manager) |  | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/organization_register/OrganizationRegisterConsumer.java:39 |
| Sync consumer (materialize organization and root account) |  | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_organization_data/SyncOrganizationConsumer.java:40 |
| Feedback-type consumer |  | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_feedback_type/UpdateFeedbackTypeConsumer.java:23 |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/organization_register/OrganizationRegisterConsumer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/organization_register/OrganizationRegisterProducer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_organization_data/SyncOrganizationConsumer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_organization_data/SyncOrganizationProducer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_organization_data/message/SyncOrganizationMessage.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_feedback_type/UpdateFeedbackTypeConsumer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_feedback_type/UpdateFeedbackTypeProducer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/update_feedback_type/message/UpdateFeedbackTypeMessage.java`
- `falo-skeleton/src/test/java/domain/services/queue/organization_register/OrganizationRegisterConsumerTest.java`
- `falo-skeleton/src/test/java/domain/services/queue/sync_organization_data/SyncOrganizationConsumerTest.java`


## organization-registration-and-verification/statuspage: StatusPage (3 leaves)

- **kind:** module
- **status:** active
- **loc:** 48
- **complexity:** low
- **digest:** `sha256:a40a3ba7dd7693aa869128c5e82e7b7242bf547f20f9e6bee19b15f2c5d35a81`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/Public/StatusPage/RegisterOrganizationSuccess.vue | falo-unities/src/views/Public/StatusPage/RegisterOrganizationSuccess.vue | screen | falo-unities/src/views/Public/StatusPage/RegisterOrganizationSuccess.vue | 19 | yes |
| falo-unities/src/views/Public/StatusPage/UpdateOrganizationRegistrationExpired.vue | falo-unities/src/views/Public/StatusPage/UpdateOrganizationRegistrationExpired.vue | screen | falo-unities/src/views/Public/StatusPage/UpdateOrganizationRegistrationExpired.vue | 15 | yes |
| falo-unities/src/views/Public/StatusPage/UpdateOrganizationRegistrationSuccess.vue | falo-unities/src/views/Public/StatusPage/UpdateOrganizationRegistrationSuccess.vue | screen | falo-unities/src/views/Public/StatusPage/UpdateOrganizationRegistrationSuccess.vue | 25 | yes |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/views/Public/StatusPage/RegisterOrganizationSuccess.vue`
- `falo-unities/src/views/Public/StatusPage/UpdateOrganizationRegistrationExpired.vue`
- `falo-unities/src/views/Public/StatusPage/UpdateOrganizationRegistrationSuccess.vue`
