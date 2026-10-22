---
module: "volunteer-recruitment-and-interviews"
name: "Volunteer recruitment and interviews"
items: 14
---

# Volunteer recruitment and interviews

## volunteer-recruitment-and-interviews/campaignpage: CampaignPage (2 leaves)

- **kind:** module
- **status:** active
- **loc:** 193
- **complexity:** low
- **digest:** `sha256:5a4d2fa1e63b81286a2d6eaa0a3d459a1028490984c16d649f2f90e58e8d5da5`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/Public/CampaignPage/CampaignDetailPage.vue | falo-unities/src/views/Public/CampaignPage/CampaignDetailPage.vue | screen | falo-unities/src/views/Public/CampaignPage/CampaignDetailPage.vue | 220 | yes |
| falo-unities/src/views/Public/CampaignPage/CampaignPage.vue | falo-unities/src/views/Public/CampaignPage/CampaignPage.vue | screen | falo-unities/src/views/Public/CampaignPage/CampaignPage.vue | 213 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/introducepage | call | 1 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/views/Public/CampaignPage/CampaignDetailPage.vue`
- `falo-unities/src/views/Public/CampaignPage/CampaignPage.vue`


## volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-application-cont: Volunteer REST API

Controllers and response view models for recruitment posts, volunteer registration, interviews and volunteer profiles.

- **kind:** module
- **status:** active
- **loc:** 570
- **complexity:** low
- **digest:** `sha256:87e4d2d1af5f6e5d223f74f680b0b79403b250e3c3b14d251b72410f106701e3`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/controller/volunteer | falo-skeleton/src/main/java/com/falo/server/application/controller/volunteer | module | falo-skeleton/src/main/java/com/falo/server/application/controller/volunteer | 342 | yes |
| falo-skeleton/src/main/java/com/falo/server/application/viewmodel/volunteer | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/volunteer | module | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/volunteer | 308 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 1 |
| platform-services/application | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 2 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3 | call | 1 |
| volunteer-recruitment-and-interviews/volunteer | call, dispatch | 13 |

### Used by

- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3`
- `volunteer-recruitment-and-interviews/volunteer`
- `volunteer-recruitment-and-interviews/volunteer-2`

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/controller/volunteer/InterviewController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/volunteer/VolunteerProfileController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/volunteer/VolunteerRecruitmentController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/volunteer/VolunteerRegisterController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/volunteer/InterviewVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/volunteer/ProfileVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/volunteer/RecruitmentVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/volunteer/VolunteerRegisterVM.java`


## volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate: Volunteer domain model and services

Volunteer entities (register, recruitment, interview, feedback, profile, achievement) with repositories and services.

- **kind:** module
- **status:** active
- **loc:** 783
- **complexity:** low
- **digest:** `sha256:3a92e909bc88df7bb785ee8a32c81f3aeab53b7bbe2d335aa01a2a3530a226e0`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/aggregate/volunteer | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/volunteer | module | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/volunteer | 184 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/repositories/volunteer | falo-skeleton/src/main/java/com/falo/server/domain/repositories/volunteer | module | falo-skeleton/src/main/java/com/falo/server/domain/repositories/volunteer | 487 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/volunteer | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/volunteer | module | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/volunteer | 208 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/config | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 3 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 3 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3 | call | 2 |

### Used by

- `employee-and-organization-account-administration/account`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `project-workspace-and-task-management/task`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3`
- `volunteer-recruitment-and-interviews/queue`
- `volunteer-recruitment-and-interviews/volunteer`

### Data stores

| Store | Access |
| --- | --- |
| ds:postgres:auth | read |
| ds:postgres:organization | read |
| ds:postgres:project | read |
| ds:postgres:publication | read |
| ds:postgres:volunteer | read, write |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/volunteer/Interview.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/volunteer/InterviewFeedback.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/volunteer/VolunteerAchievement.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/volunteer/VolunteerProfile.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/volunteer/VolunteerRecruitment.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/volunteer/VolunteerRegister.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/volunteer/InterviewFeedbackRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/volunteer/InterviewRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/volunteer/VolunteerAchievementRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/volunteer/VolunteerProfileRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/volunteer/VolunteerRecruitmentRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/volunteer/VolunteerRegisterRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/volunteer/InterviewFeedbackService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/volunteer/InterviewService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/volunteer/VolunteerAchievementService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/volunteer/VolunteerProfileService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/volunteer/VolunteerRecruitmentService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/volunteer/VolunteerRegisterService.java`


## volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3: Volunteer queries and models

Queries and models for the interview calendar, back-office registration lists, recruitments and public volunteer pages.

- **kind:** module
- **status:** active
- **loc:** 503
- **complexity:** medium
- **digest:** `sha256:3074cf32e3dec0997cbe7f407b497dd78bfbc821fe069128023920c37407250c`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer | 422 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/model | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/model | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/model | 131 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| platform-services/application | call | 4 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 2 |
| platform-services/infrastructure-2 | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |

### Used by

- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `volunteer-recruitment-and-interviews/volunteer`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/InterviewQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/RecruitmentQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/VolunteerQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/VolunteerRegisterQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/model/FeedbackHistoryModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/model/InterviewCalendarModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/model/RecruitmentForPublicPageModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/model/RecruitmentsForBackOfficeModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/model/VolunteerAchievementProjectModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/model/VolunteerProfileModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/model/VolunteerRegisterDetailsModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/volunteer/model/VolunteerRegisterModel.java`


## volunteer-recruitment-and-interviews/falo-unities-src-components-common-layout-profile-dialog: falo-unities/src/components/common/layout/Profile/dialog

- **kind:** module
- **status:** active
- **loc:** 474
- **complexity:** low
- **digest:** `sha256:b5400a52b4f01b68378af241cf38399523278802b0b1af7af345d2253d150e5b`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/common/layout/Profile/dialog | falo-unities/src/components/common/layout/Profile/dialog | module | falo-unities/src/components/common/layout/Profile/dialog | 559 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/elements | call | 1 |
| platform-services/src | call | 4 |
| volunteer-recruitment-and-interviews/volunteer-2 | call | 1 |

### Files

- `falo-unities/src/components/common/layout/Profile/dialog/ProfileAchievementDialog.vue`
- `falo-unities/src/components/common/layout/Profile/dialog/ProfileInformationDialog.vue`


## volunteer-recruitment-and-interviews/falo-unities-src-components-public-recruitment-publicrecruit: Public recruitment campaign screens (SPA)

Campaign list/detail pages, public recruitment cards and the apply-CV form with CV upload and notify-login dialog.

- **kind:** module
- **status:** active
- **loc:** 574
- **complexity:** medium
- **digest:** `sha256:a6f27108de8a59e2190377a8085c77a9f421bfe49b4b30f34f8e4efb55511511`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/public/recruitment/PublicRecruitmentCard.vue | falo-unities/src/components/public/recruitment/PublicRecruitmentCard.vue | module | falo-unities/src/components/public/recruitment/PublicRecruitmentCard.vue | 125 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-views-public-homepage-homepage-vue | call | 1 |
| platform-services/src | call | 2 |

### Used by

- `publication-and-public-portal/projectpage`

### Files

- `falo-unities/src/components/public/campaign/ApplyCVForm.vue`
- `falo-unities/src/components/public/campaign/NotifyLogin.vue`
- `falo-unities/src/components/public/campaign/VolunteerCVFileUpload.vue`
- `falo-unities/src/components/public/recruitment/PublicRecruitmentCard.vue`


## volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-dashboard-memberor: falo-unities/src/views/MemberOrganization/Dashboard/MemberOrganizationDashboardPage.vue

- **kind:** module
- **status:** active
- **loc:** 57
- **complexity:** low
- **digest:** `sha256:a29641c2e5a7f9958b6081c7072910058a1a547379a8b135a242fa85dccef83e`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/MemberOrganization/Dashboard/MemberOrganizationDashboardPage.vue | falo-unities/src/views/MemberOrganization/Dashboard/MemberOrganizationDashboardPage.vue | screen | falo-unities/src/views/MemberOrganization/Dashboard/MemberOrganizationDashboardPage.vue | 63 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| employee-and-organization-account-administration/api | call | 1 |
| other/components | call | 1 |
| other/falo-unities-src-store-modules | call | 1 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/views/MemberOrganization/Dashboard/MemberOrganizationDashboardPage.vue`


## volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-recruitment-volunt: Recruitment posting screens (SPA)

Member-organization recruitment list page with its post dialog and table.

- **kind:** module
- **status:** active
- **loc:** 459
- **complexity:** medium
- **digest:** `sha256:1e57ff97ffc6306845b85d1cc399060e1250d420db19a2034e2ec682f28263c8`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/projects/recruiment/dialog/PostRecruitmentDialog.vue | falo-unities/src/components/projects/recruiment/dialog/PostRecruitmentDialog.vue | module | falo-unities/src/components/projects/recruiment/dialog/PostRecruitmentDialog.vue | 355 |  |
| falo-unities/src/components/projects/recruiment/table/VolunteerRecruitmentTable.vue | falo-unities/src/components/projects/recruiment/table/VolunteerRecruitmentTable.vue | module | falo-unities/src/components/projects/recruiment/table/VolunteerRecruitmentTable.vue | 75 |  |
| falo-unities/src/views/MemberOrganization/Recruitment/VolunteerRecruitmentPage.vue | falo-unities/src/views/MemberOrganization/Recruitment/VolunteerRecruitmentPage.vue | screen | falo-unities/src/views/MemberOrganization/Recruitment/VolunteerRecruitmentPage.vue | 111 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 2 |
| platform-services/src | call | 9 |
| publication-and-public-portal/publication-2 | call | 1 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/components/projects/recruiment/dialog/PostRecruitmentDialog.vue`
- `falo-unities/src/components/projects/recruiment/table/VolunteerRecruitmentTable.vue`
- `falo-unities/src/views/MemberOrganization/Recruitment/VolunteerRecruitmentPage.vue`


## volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-dashboard-volunteerdashboar: falo-unities/src/views/Volunteer/Dashboard/VolunteerDashboardPage.vue

- **kind:** module
- **status:** active
- **loc:** 45
- **complexity:** low
- **digest:** `sha256:70950a8a7f889ac38eb1c07f93eef66308df5d6d5262532805b93f0efc14907a`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/Volunteer/Dashboard/VolunteerDashboardPage.vue | falo-unities/src/views/Volunteer/Dashboard/VolunteerDashboardPage.vue | screen | falo-unities/src/views/Volunteer/Dashboard/VolunteerDashboardPage.vue | 51 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| employee-and-organization-account-administration/api | call | 1 |
| other/components | call | 1 |
| other/falo-unities-src-store-modules | call | 1 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/views/Volunteer/Dashboard/VolunteerDashboardPage.vue`


## volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-profile-volunteerprofilepag: Volunteer profile and dashboard screens

Public volunteer profile with achievement/information dialogs, plus volunteer and member-organization dashboards.

- **kind:** module
- **status:** active
- **loc:** 286
- **complexity:** low
- **digest:** `sha256:d1d2c655dcf7c64b08a5194578165c1e3c3e881393b15e9b79def4865b7d04d6`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/Volunteer/Profile/VolunteerProfilePage.vue | falo-unities/src/views/Volunteer/Profile/VolunteerProfilePage.vue | screen | falo-unities/src/views/Volunteer/Profile/VolunteerProfilePage.vue | 348 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/src | call | 3 |
| volunteer-recruitment-and-interviews/volunteer-2 | call | 1 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/views/Volunteer/Profile/VolunteerProfilePage.vue`


## volunteer-recruitment-and-interviews/queue: Volunteer registration Kafka pipeline

Producers and consumers for register-volunteer (register plus interview shell) and sync-data-volunteer (on acceptance creates account, profile, project member) with consumer tests.

- **kind:** module
- **status:** active
- **loc:** 928
- **complexity:** low
- **digest:** `sha256:d6c71bde5d3566a1b3254040d166a3fd770f831dc3a1dfb13105e4f6dd7c7247`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_volunteer_data | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_volunteer_data | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_volunteer_data | 122 | yes |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_volunteer_data/message/SyncVolunteerMessage.java | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_volunteer_data/message/SyncVolunteerMessage.java | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_volunteer_data/message/SyncVolunteerMessage.java | 24 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queue/volunteer_register | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/volunteer_register | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/volunteer_register | 85 | yes |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queue/volunteer_register/message/VolunteerRegisterMessage.java | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/volunteer_register/message/VolunteerRegisterMessage.java | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/volunteer_register/message/VolunteerRegisterMessage.java | 20 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even | call | 1 |
| platform-services/aggregate-2 | call | 1 |
| platform-services/application | call | 2 |
| platform-services/config | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 4 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 4 |
| volunteer-recruitment-and-interviews/volunteer | call | 1 |

### Used by

- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `volunteer-recruitment-and-interviews/volunteer`

### Data stores

| Store | Access |
| --- | --- |
| ds:kafka:register-volunteer | write |
| ds:kafka:sync-data-volunteer | write |

### Parts

| Part | Kind | File |
| --- | --- | --- |
| Register pipeline consumer (register plus interview shell) |  | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/volunteer_register/VolunteerRegisterConsumer.java:33 |
| Sync consumer (account, profile, member) |  | falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_volunteer_data/SyncVolunteerConsumer.java:43 |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_volunteer_data/SyncVolunteerConsumer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_volunteer_data/SyncVolunteerProducer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/sync_volunteer_data/message/SyncVolunteerMessage.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/volunteer_register/VolunteerRegisterConsumer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/volunteer_register/VolunteerRegisterProducer.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queue/volunteer_register/message/VolunteerRegisterMessage.java`
- `falo-skeleton/src/test/java/domain/services/queue/sync_volunteer_data/SyncVolunteerConsumerTest.java`
- `falo-skeleton/src/test/java/domain/services/queue/volunteer_register/VolunteerRegisterConsumerTest.java`


## volunteer-recruitment-and-interviews/volunteer: Volunteer command handlers

Handlers for recruitment posts, volunteer self-registration, interview feedback and time, profile updates and achievements.

- **kind:** module
- **status:** active
- **loc:** 755
- **complexity:** medium
- **digest:** `sha256:fe5a9bc2927466f4954595239a24b8f6721031b46cbc4fe3583dd1cf8bf3cf3c`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/interview_feedback | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/interview_feedback | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/interview_feedback | 175 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/recruitment | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/recruitment | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/recruitment | 141 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/register | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/register | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/register | 155 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/set_interview_time | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/set_interview_time | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/set_interview_time | 142 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_interview | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_interview | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_interview | 79 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_profile | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_profile | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_profile | 74 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_profile/save_achievement | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_profile/save_achievement | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_profile/save_achievement | 113 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even | call | 1 |
| platform-services/aggregate-2 | call | 2 |
| platform-services/application | call | 8 |
| platform-services/config | call | 9 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 6 |
| platform-services/infrastructure-2 | call | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 13 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3 | call | 1 |
| volunteer-recruitment-and-interviews/queue | call | 4 |

### Used by

- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `volunteer-recruitment-and-interviews/queue`

### Parts

| Part | Kind | File |
| --- | --- | --- |
| Post recruitment |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/recruitment/RecruitmentCommandHandler.java:11 |
| Volunteer self-registration |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/register/VolunteerRegisterCommandHandler.java:24 |
| Interview feedback (accept syncs account) |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/interview_feedback/FeedbackInterviewCommandHandler.java:31 |
| Set interview time |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/set_interview_time/SetInterviewTimeCommandHandler.java:23 |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/interview_feedback/FeedbackInterviewCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/interview_feedback/FeedbackInterviewCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/interview_feedback/FeedbackInterviewCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/recruitment/RecruitmentCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/recruitment/RecruitmentCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/recruitment/RecruitmentCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/register/VolunteerRegisterCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/register/VolunteerRegisterCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/register/VolunteerRegisterCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/set_interview_time/SetInterviewTimeCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/set_interview_time/SetInterviewTimeCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/set_interview_time/SetInterviewTimeCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_interview/UpdateInterviewCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_interview/UpdateInterviewCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_interview/UpdateInterviewCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_profile/UpdateProfileCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_profile/UpdateProfileCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_profile/UpdateProfileCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_profile/save_achievement/SaveAchievementCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_profile/save_achievement/SaveAchievementCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/volunteer/update_profile/save_achievement/SaveAchievementCommandValidator.java`


## volunteer-recruitment-and-interviews/volunteer-2: SPA volunteer data layer

Typed API clients, volunteer Pinia stores and interview/recruitment/register response hooks.

- **kind:** module
- **status:** active
- **loc:** 773
- **complexity:** medium
- **digest:** `sha256:4df3df4243a75875c7adf997ffe049e2cf27843c21e4ad84302b7b0f28e04a00`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/api/volunteer/accounts | falo-unities/src/api/volunteer/accounts | module | falo-unities/src/api/volunteer/accounts | 50 |  |
| falo-unities/src/api/volunteer/assign | falo-unities/src/api/volunteer/assign | module | falo-unities/src/api/volunteer/assign | 12 |  |
| falo-unities/src/api/volunteer/get | falo-unities/src/api/volunteer/get | module | falo-unities/src/api/volunteer/get | 62 |  |
| falo-unities/src/api/volunteer/recruitment | falo-unities/src/api/volunteer/recruitment | module | falo-unities/src/api/volunteer/recruitment | 56 |  |
| falo-unities/src/api/volunteer/register | falo-unities/src/api/volunteer/register | module | falo-unities/src/api/volunteer/register | 59 |  |
| falo-unities/src/api/volunteer/update | falo-unities/src/api/volunteer/update | module | falo-unities/src/api/volunteer/update | 34 |  |
| falo-unities/src/hooks/volunteer/account/index.ts | falo-unities/src/hooks/volunteer/account/index.ts | module | falo-unities/src/hooks/volunteer/account/index.ts | 87 |  |
| falo-unities/src/hooks/volunteer/get/index.ts | falo-unities/src/hooks/volunteer/get/index.ts | module | falo-unities/src/hooks/volunteer/get/index.ts | 41 |  |
| falo-unities/src/hooks/volunteer/index.ts | falo-unities/src/hooks/volunteer/index.ts | module | falo-unities/src/hooks/volunteer/index.ts | 89 |  |
| falo-unities/src/hooks/volunteer/recruitment/index.ts | falo-unities/src/hooks/volunteer/recruitment/index.ts | module | falo-unities/src/hooks/volunteer/recruitment/index.ts | 63 |  |
| falo-unities/src/hooks/volunteer/register/index.ts | falo-unities/src/hooks/volunteer/register/index.ts | module | falo-unities/src/hooks/volunteer/register/index.ts | 36 |  |
| falo-unities/src/store/modules/volunteer | falo-unities/src/store/modules/volunteer | module | falo-unities/src/store/modules/volunteer | 259 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/api | call | 6 |
| platform-services/src | call | 10 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 6 |

### Used by

- `other/falo-unities-src-store-modules`
- `other/falo-unities-src-views-public-homepage-homepage-vue`
- `other/layout`
- `volunteer-recruitment-and-interviews/falo-unities-src-components-common-layout-profile-dialog`
- `volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-profile-volunteerprofilepag`
- `volunteer-recruitment-and-interviews/volunteer-3`

### Files

- `falo-unities/src/api/interview/index.ts`
- `falo-unities/src/api/interview/type.ts`
- `falo-unities/src/api/volunteer/accounts/index.ts`
- `falo-unities/src/api/volunteer/accounts/types.ts`
- `falo-unities/src/api/volunteer/assign/index.ts`
- `falo-unities/src/api/volunteer/assign/types.ts`
- `falo-unities/src/api/volunteer/get/index.ts`
- `falo-unities/src/api/volunteer/get/type.ts`
- `falo-unities/src/api/volunteer/recruitment/index.ts`
- `falo-unities/src/api/volunteer/recruitment/types.ts`
- `falo-unities/src/api/volunteer/register/index.ts`
- `falo-unities/src/api/volunteer/register/type.ts`
- `falo-unities/src/api/volunteer/register/types.ts`
- `falo-unities/src/api/volunteer/update/index.ts`
- `falo-unities/src/api/volunteer/update/types.ts`
- `falo-unities/src/hooks/interview/index.ts`
- `falo-unities/src/hooks/volunteer/account/index.ts`
- `falo-unities/src/hooks/volunteer/assign/index.ts`
- `falo-unities/src/hooks/volunteer/get/index.ts`
- `falo-unities/src/hooks/volunteer/index.ts`
- `falo-unities/src/hooks/volunteer/recruitment/index.ts`
- `falo-unities/src/hooks/volunteer/register/index.ts`
- `falo-unities/src/store/modules/volunteer/volunteer.ts`
- `falo-unities/src/store/modules/volunteer/volunteerAccount.ts`


## volunteer-recruitment-and-interviews/volunteer-3: Volunteer registration and interview back-office screens

Back-office registration list/detail pages, CV table, interview note/time/status forms, calendar and interview feedback history page.

- **kind:** module
- **status:** active
- **loc:** 1692
- **complexity:** medium
- **digest:** `sha256:3cb8ec60d2827d4f689a2b04b01d5959b53aca12bd58c349cb6040d4b6fbd0a4`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/interview/TodoCalendar.vue | falo-unities/src/components/interview/TodoCalendar.vue | screen | falo-unities/src/components/interview/TodoCalendar.vue | 234 | yes |
| falo-unities/src/components/interview/detail | falo-unities/src/components/interview/detail | module | falo-unities/src/components/interview/detail | 130 |  |
| falo-unities/src/components/volunteer/approval_request/attachment/CVAttachmentTable.vue | falo-unities/src/components/volunteer/approval_request/attachment/CVAttachmentTable.vue | module | falo-unities/src/components/volunteer/approval_request/attachment/CVAttachmentTable.vue | 91 |  |
| falo-unities/src/components/volunteer/detail | falo-unities/src/components/volunteer/detail | module | falo-unities/src/components/volunteer/detail | 629 |  |
| falo-unities/src/components/volunteer/table/VolunteerRegisterBackOfficeTable.vue | falo-unities/src/components/volunteer/table/VolunteerRegisterBackOfficeTable.vue | module | falo-unities/src/components/volunteer/table/VolunteerRegisterBackOfficeTable.vue | 100 |  |
| falo-unities/src/views/Common/Volunteer/VolunteerRegisterForBackOfficePage.vue | falo-unities/src/views/Common/Volunteer/VolunteerRegisterForBackOfficePage.vue | screen | falo-unities/src/views/Common/Volunteer/VolunteerRegisterForBackOfficePage.vue | 141 | yes |
| falo-unities/src/views/Common/Volunteer/VolunteerRegistrationDetailPage.vue | falo-unities/src/views/Common/Volunteer/VolunteerRegistrationDetailPage.vue | screen | falo-unities/src/views/Common/Volunteer/VolunteerRegistrationDetailPage.vue | 610 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/elements | call | 1 |
| other/falo-unities-src-store-modules | call | 5 |
| platform-services/falo-unities-src-router-index-ts | call | 1 |
| platform-services/src | call | 14 |
| volunteer-recruitment-and-interviews/volunteer-2 | call | 3 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/components/interview/TodoCalendar.vue`
- `falo-unities/src/components/interview/detail/InterviewFeedbackHistory.vue`
- `falo-unities/src/components/interview/detail/InterviewResult.vue`
- `falo-unities/src/components/volunteer/approval_request/attachment/CVAttachmentTable.vue`
- `falo-unities/src/components/volunteer/detail/InterviewNoteForm.vue`
- `falo-unities/src/components/volunteer/detail/InterviewTimeForm.vue`
- `falo-unities/src/components/volunteer/detail/UpdateInterviewStatusForm.vue`
- `falo-unities/src/components/volunteer/table/VolunteerRegisterBackOfficeTable.vue`
- `falo-unities/src/views/Common/Volunteer/VolunteerRegisterForBackOfficePage.vue`
- `falo-unities/src/views/Common/Volunteer/VolunteerRegistrationDetailPage.vue`
- `falo-unities/src/views/Interview/InterviewFeedbackHistoryPage.vue`
