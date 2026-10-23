---
app: "falo-application"
sources:
  - "falo-skeleton@3fc7e7014615030021a2e33ad254c91cec92ca22"
  - "falo-unities@53bc9e727e3e014f4ed0d721ee16b697fbbf14fd"
method: "static inventory (UTF-8, Latin-1 fallback); per-file decision keywords are counted as a language-neutral complexity proxy"
complexityIndexFormula: "2.94 × KSLOC^1.10"
fileCount: 1109
sourceFileCount: 1079
totalBytes: 5320698
totalLines: 78747
sloc: 67882
ksloc: 67.882
complexity: 3327
complexityPerKsloc: 49.01
complexityIndex: 304.28
directoryDepth: 1
codeFiles: 1077
medianSloc: 28
halfComplexityFiles: 115
topTenShare: 0.1169
oversized: 2
---

# Inventory of falo-application

Measured at `falo-skeleton@3fc7e7014615030021a2e33ad254c91cec92ca22`, `falo-unities@53bc9e727e3e014f4ed0d721ee16b697fbbf14fd`: 1,079 source files, 67,882 lines of code. The per-file records stay in the run; this document keeps the figures of record and their roll-ups.

## Languages

| Language | Files | Lines | SLOC | Complexity |
| --- | --- | --- | --- | --- |
| Java | 617 | 34845 | 30068 | 1133 |
| Vue | 209 | 29762 | 25192 | 1539 |
| TypeScript | 209 | 9298 | 8383 | 461 |
| HTML | 16 | 2897 | 2648 | 134 |
| SQL | 1 | 943 | 817 | 1 |
| YAML | 3 | 227 | 205 | 3 |
| CSS | 3 | 175 | 113 | 3 |
| Groovy | 4 | 123 | 110 | 4 |
| XML | 8 | 123 | 107 | 10 |
| Markdown | 3 | 147 | 83 | 12 |
| Batch | 1 | 94 | 71 | 16 |
| Shell | 2 | 63 | 43 | 8 |
| JavaScript | 2 | 32 | 29 | 2 |
| Dockerfile | 1 | 18 | 13 | 1 |

## Directories

| Path | Files | SLOC | Complexity |
| --- | --- | --- | --- |
| falo-skeleton | 647 | 34035 | 1309 |
| falo-unities | 430 | 33847 | 2018 |

## Size distribution

| SLOC per file | Files |
| --- | --- |
| <50 | 711 |
| 50-99 | 187 |
| 100-249 | 138 |
| 250-499 | 29 |
| 500-999 | 10 |
| 1k-2.5k | 2 |
| 2.5k+ | 0 |

## Most complex files

| Path | Language | Lines | SLOC | Complexity |
| --- | --- | --- | --- | --- |
| falo-unities/src/components/cycle/dialog/ProjectCycleDialogViewTask.vue | Vue | 950 | 814 | 75 |
| falo-unities/src/components/cycle/dialog/ProjectCycleDialogViewSubTask.vue | Vue | 892 | 756 | 69 |
| falo-unities/src/store/modules/cycle.ts | TypeScript | 679 | 643 | 58 |
| falo-unities/src/views/Common/Task/CyclesPage.vue | Vue | 691 | 590 | 39 |
| falo-unities/src/views/Public/RegisterPage/OrganizationRegisterForm.vue | Vue | 691 | 605 | 30 |
| falo-unities/src/views/Public/ProjectPage/ProjectDetailPage.vue | Vue | 308 | 246 | 26 |
| falo-unities/src/components/projects/approval_request/attachment/FileAttachmentTable.vue | Vue | 323 | 270 | 24 |
| falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project_register/ProjectRegisterService.java | Java | 147 | 134 | 23 |
| falo-skeleton/src/test/java/domain/services/commands/organization_register/create/OrganizationRegisterTest.java | Java | 548 | 391 | 23 |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project_register/feedback/ProjectFeedbackCommandHandler.java | Java | 284 | 250 | 22 |
| falo-unities/src/views/Organization/Projects/RegisterProjectForm.vue | Vue | 389 | 336 | 22 |
| falo-unities/src/views/Common/Task/ProjectSettingInformationPage.vue | Vue | 242 | 186 | 21 |
| falo-unities/src/views/Organization/RequestPublic/RequestPublicForm.vue | Vue | 391 | 339 | 20 |
| falo-unities/src/components/common/layout/Common/UserMenu.vue | Vue | 171 | 158 | 19 |
| falo-unities/src/components/projects/recruiment/dialog/PostRecruitmentDialog.vue | Vue | 355 | 308 | 19 |
| falo-unities/src/views/Common/Volunteer/VolunteerRegistrationDetailPage.vue | Vue | 610 | 541 | 19 |
| falo-unities/src/components/employee/EmployeeForm.vue | Vue | 378 | 330 | 18 |
| falo-unities/src/views/Common/Organizations/OrganizationRegistrationDetailPage.vue | Vue | 410 | 367 | 18 |
| falo-unities/src/views/Common/Task/ProjectSettingStatesPage.vue | Vue | 198 | 158 | 18 |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/ProjectQuery.java | Java | 350 | 327 | 17 |
| falo-unities/src/components/projects/approval_request/member/ProjectMemberForm.vue | Vue | 383 | 339 | 17 |
| falo-unities/src/views/Common/Projects/ProjectRegistrationDetailPage.vue | Vue | 444 | 382 | 17 |
| falo-unities/src/views/Volunteer/Profile/VolunteerProfilePage.vue | Vue | 348 | 286 | 17 |
| falo-skeleton/gradlew.bat | Batch | 94 | 71 | 16 |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization_register/feedback/FeedBackRegisterCommandHandler.java | Java | 270 | 237 | 16 |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project_register/ProjectRegisterQuery.java | Java | 197 | 184 | 16 |
| falo-unities/src/components/organizations/table/OrganizationsRegistrationsTable.vue | Vue | 140 | 130 | 16 |
| falo-unities/src/components/task/labels/TaskLabelForm.vue | Vue | 192 | 157 | 16 |
| falo-unities/src/views/Common/Publication/PublicationProjectForm.vue | Vue | 304 | 260 | 16 |
| falo-skeleton/src/main/resources/mail/reset-password.html | HTML | 220 | 216 | 15 |
| falo-skeleton/src/main/resources/mail/set-password.html | HTML | 219 | 215 | 15 |
| falo-unities/src/components/organizations/detail/RegisterStatusHistory.vue | Vue | 152 | 132 | 15 |
| falo-unities/src/components/projects/detail/ProjectRegisterStatusHistory.vue | Vue | 152 | 132 | 15 |
| falo-unities/src/views/Common/Task/PageForm.vue | Vue | 216 | 180 | 15 |
| falo-unities/src/components/common/elements/form/AddressSelectForm.vue | Vue | 307 | 260 | 14 |
| falo-unities/src/components/common/elements/phone/GlobalPhone.vue | Vue | 300 | 249 | 14 |
| falo-unities/src/components/common/layout/Common/NotificationsDropDown.vue | Vue | 170 | 165 | 14 |
| falo-unities/src/components/public/campaign/ApplyCVForm.vue | Vue | 348 | 301 | 14 |
| falo-unities/src/components/task/pages/PageList.vue | Vue | 183 | 162 | 14 |
| falo-unities/src/components/volunteer/detail/UpdateInterviewStatusForm.vue | Vue | 229 | 210 | 14 |
| falo-unities/src/views/Common/Task/PagesPage.vue | Vue | 164 | 127 | 14 |
| falo-unities/src/views/Common/Task/ProjectSettingLabelsPage.vue | Vue | 150 | 121 | 14 |
| falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization_register/OrganizationRegisterService.java | Java | 82 | 73 | 13 |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/AccountQuery.java | Java | 244 | 223 | 13 |
| falo-skeleton/src/test/java/domain/services/commands/project_register/create/ProjectRegisterTest.java | Java | 360 | 269 | 13 |
| falo-unities/src/api/axios.ts | TypeScript | 119 | 104 | 13 |
| falo-unities/src/components/admin/account/AccountDetailForm.vue | Vue | 190 | 166 | 13 |
| falo-unities/src/components/projects/table/ProjectMemberTable.vue | Vue | 164 | 138 | 13 |
| falo-unities/src/components/projects/table/ProjectRegistrationsTable.vue | Vue | 118 | 106 | 13 |
| falo-unities/src/components/task/state/ProjectStateFormDialog.vue | Vue | 227 | 205 | 13 |
