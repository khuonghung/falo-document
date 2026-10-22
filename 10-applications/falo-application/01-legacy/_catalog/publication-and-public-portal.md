---
module: "publication-and-public-portal"
name: "Publication and public portal"
items: 7
---

# Publication and public portal

## publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont: Publication REST API and commands

ProjectPublicationController endpoints with verify, set-public toggle and update command handlers and response models.

- **kind:** module
- **status:** active
- **loc:** 551
- **complexity:** low
- **digest:** `sha256:f4cdff4deb1915cd3b8bbffa282b8a5a0cb863fa2137cdb49fcf360960131727`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/controller/publication/ProjectPublicationController.java | falo-skeleton/src/main/java/com/falo/server/application/controller/publication/ProjectPublicationController.java | module | falo-skeleton/src/main/java/com/falo/server/application/controller/publication/ProjectPublicationController.java | 202 | yes |
| falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/publication/ProjectPublicationVM.java | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/publication/ProjectPublicationVM.java | module | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/publication/ProjectPublicationVM.java | 148 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication | 134 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/set_public | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/set_public | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/set_public | 66 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/verify | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/verify | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/verify | 91 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 1 |
| organization-registration-and-verification/queue | call | 2 |
| platform-services/application | call | 5 |
| platform-services/config | call | 3 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 6 |
| platform-services/infrastructure-2 | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 2 |
| project-registration-and-verification/project-register | call | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 4 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | call | 1 |
| publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 7 |

### Used by

- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `publication-and-public-portal/falo-unities-src-api-publication`

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/controller/publication/ProjectPublicationController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/publication/ProjectPublicationVM.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/UpdatePublicationCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/UpdatePublicationCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/UpdatePublicationCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/set_public/SetPublicStatusCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/set_public/SetPublicStatusCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/set_public/SetPublicStatusCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/verify/VerifyPublicationCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/verify/VerifyPublicationCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/publication/verify/VerifyPublicationCommandValidator.java`


## publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate: Publication domain

Versioned ProjectPublication entity with its repository (cross-schema joins to project) and service.

- **kind:** module
- **status:** active
- **loc:** 419
- **complexity:** low
- **digest:** `sha256:3a59f7ae10a99958679b6b3f4d8969ef4d0cda61362252d9d1906f04bab5b5dc`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/aggregate/publication/ProjectPublication.java | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/publication/ProjectPublication.java | module | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/publication/ProjectPublication.java | 41 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/repositories/publication/ProjectPublicationRepository.java | falo-skeleton/src/main/java/com/falo/server/domain/repositories/publication/ProjectPublicationRepository.java | module | falo-skeleton/src/main/java/com/falo/server/domain/repositories/publication/ProjectPublicationRepository.java | 301 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/publication/ProjectPublicationService.java | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/publication/ProjectPublicationService.java | module | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/publication/ProjectPublicationService.java | 103 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| platform-services/application | call | 1 |
| platform-services/config | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 4 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | call | 2 |

### Used by

- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Data stores

| Store | Access |
| --- | --- |
| ds:postgres:auth | read |
| ds:postgres:employees | read |
| ds:postgres:organization | read |
| ds:postgres:project | read |
| ds:postgres:project_register | read |
| ds:postgres:publication | read, write |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/publication/ProjectPublication.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/publication/ProjectPublicationRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/publication/ProjectPublicationService.java`


## publication-and-public-portal/falo-unities-src-api-publication: SPA publication API client and hooks

Typed publication API client and its response mappers.

- **kind:** module
- **status:** active
- **loc:** 181
- **complexity:** low
- **digest:** `sha256:17fbd9fbba9b0ed6075d25913c4ff6dcf2bffe1a07faef9c73efed35e9142caa`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/api/publication | falo-unities/src/api/publication | module | falo-unities/src/api/publication | 97 |  |
| falo-unities/src/hooks/publication/index.ts | falo-unities/src/hooks/publication/index.ts | module | falo-unities/src/hooks/publication/index.ts | 104 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/api | call | 1 |
| platform-services/src | call | 2 |
| publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |

### Used by

- `other/falo-unities-src-store-modules`

### Files

- `falo-unities/src/api/publication/index.ts`
- `falo-unities/src/api/publication/type.ts`
- `falo-unities/src/hooks/publication/index.ts`


## publication-and-public-portal/falo-unities-src-components-public-feedback-projectfeedb: falo-unities/src/components/public/feedback/ProjectFeedbackCard.vue

- **kind:** module
- **status:** active
- **loc:** 57
- **complexity:** low
- **digest:** `sha256:1e1ed63fa215b635ae87a048f37e09301ae3992c24b5156a4689b143217b098d`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/public/feedback/ProjectFeedbackCard.vue | falo-unities/src/components/public/feedback/ProjectFeedbackCard.vue | module | falo-unities/src/components/public/feedback/ProjectFeedbackCard.vue | 72 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/src | call | 2 |

### Files

- `falo-unities/src/components/public/feedback/ProjectFeedbackCard.vue`


## publication-and-public-portal/falo-unities-src-views-organization-profile-organization: falo-unities/src/views/Organization/Profile/OrganizationProfilePage.vue

- **kind:** module
- **status:** active
- **loc:** 108
- **complexity:** low
- **digest:** `sha256:5b7d150b521448d3c11a01974d8c7a38ea5a42e3cbc71a70b3e4faae6cb6526e`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/Organization/Profile/OrganizationProfilePage.vue | falo-unities/src/views/Organization/Profile/OrganizationProfilePage.vue | screen | falo-unities/src/views/Organization/Profile/OrganizationProfilePage.vue | 130 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 1 |
| other/modules | call | 1 |
| platform-services/src | call | 1 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/views/Organization/Profile/OrganizationProfilePage.vue`


## publication-and-public-portal/projectpage: Public portal screens

Public project list and detail pages with search, feedback cards and the public organization profile page.

- **kind:** module
- **status:** active
- **loc:** 627
- **complexity:** medium
- **digest:** `sha256:e7ed67bf06563c37dba86162a04c73637b7855437081fb936f0398df3811693a`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/Public/ProjectPage/ProjectDetailPage.vue | falo-unities/src/views/Public/ProjectPage/ProjectDetailPage.vue | screen | falo-unities/src/views/Public/ProjectPage/ProjectDetailPage.vue | 308 | yes |
| falo-unities/src/views/Public/ProjectPage/ProjectPage.vue | falo-unities/src/views/Public/ProjectPage/ProjectPage.vue | screen | falo-unities/src/views/Public/ProjectPage/ProjectPage.vue | 149 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 2 |
| platform-services/src | call | 4 |
| volunteer-recruitment-and-interviews/falo-unities-src-components-public-recruitment-publicrecruit | call | 1 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/components/public/project/ProjectCarousel.vue`
- `falo-unities/src/components/public/project/ProjectCarouselItem.vue`
- `falo-unities/src/components/public/project/ProjectListItems.vue`
- `falo-unities/src/components/public/project/SearchProject.vue`
- `falo-unities/src/views/Public/ProjectPage/ProjectDetailPage.vue`
- `falo-unities/src/views/Public/ProjectPage/ProjectPage.vue`


## publication-and-public-portal/publication-2: Publication management screens

Request-public form, staff publication list and publication history table.

- **kind:** module
- **status:** active
- **loc:** 999
- **complexity:** medium
- **digest:** `sha256:681226a05a587e75dc68464125cf4c3d5803e9607e5093b0e0f9985de3c45398`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/projects/public_project/table | falo-unities/src/components/projects/public_project/table | module | falo-unities/src/components/projects/public_project/table | 262 |  |
| falo-unities/src/views/Common/Publication/PublicProjectListPage.vue | falo-unities/src/views/Common/Publication/PublicProjectListPage.vue | screen | falo-unities/src/views/Common/Publication/PublicProjectListPage.vue | 227 | yes |
| falo-unities/src/views/Common/Publication/PublicationProjectForm.vue | falo-unities/src/views/Common/Publication/PublicationProjectForm.vue | screen | falo-unities/src/views/Common/Publication/PublicationProjectForm.vue | 304 | yes |
| falo-unities/src/views/Organization/RequestPublic/RequestPublicForm.vue | falo-unities/src/views/Organization/RequestPublic/RequestPublicForm.vue | screen | falo-unities/src/views/Organization/RequestPublic/RequestPublicForm.vue | 391 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 4 |
| platform-services/src | call | 14 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`
- `volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-recruitment-volunt`

### Files

- `falo-unities/src/components/projects/public_project/table/PublicProjectListTable.vue`
- `falo-unities/src/components/projects/public_project/table/PublicationHistoryTable.vue`
- `falo-unities/src/views/Common/Publication/PublicProjectListPage.vue`
- `falo-unities/src/views/Common/Publication/PublicationProjectForm.vue`
- `falo-unities/src/views/Organization/RequestPublic/RequestPublicForm.vue`
