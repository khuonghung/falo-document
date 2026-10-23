---
module: "other"
name: "Other"
items: 13
---

# Other

## other/components: Dashboard statistic cards and task icons

Shared widgets: dashboard statistic cards and the task, label and priority icons used across the workspace.

- **kind:** module
- **status:** active
- **loc:** 438
- **complexity:** medium
- **digest:** `sha256:ca90b7b452742401bc27468a7e8e038cc81db91c25b870c6f0a3fbe15ee6a60f`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/dashboard | falo-unities/src/components/dashboard | module | falo-unities/src/components/dashboard | 238 |  |
| falo-unities/src/components/icon | falo-unities/src/components/icon | module | falo-unities/src/components/icon | 284 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| employee-and-organization-account-administration/api | call | 1 |

### Used by

- `other/elements`
- `other/falo-unities-src-views-common-dashboard-dashboardpage-vue`
- `project-workspace-and-task-management/task-3`
- `volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-dashboard-memberor`
- `volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-dashboard-volunteerdashboar`

### Files

- `falo-unities/src/components/dashboard/DashboardItemCard.vue`
- `falo-unities/src/components/dashboard/DashboardPublicationStatisticTable.vue`
- `falo-unities/src/components/dashboard/DashboardStatisticTable.vue`
- `falo-unities/src/components/dashboard/DashboardTaskStatisticTable.vue`
- `falo-unities/src/components/icon/CommonProjectLabelIcon.vue`
- `falo-unities/src/components/icon/CommonTaskInfoIcon.vue`
- `falo-unities/src/components/icon/HighPriorityIcon.vue`
- `falo-unities/src/components/icon/LowPriorityIcon.vue`
- `falo-unities/src/components/icon/LowestPriorityIcon.vue`
- `falo-unities/src/components/icon/MediumPriorityIcon.vue`
- `falo-unities/src/components/icon/TaskIcon.vue`
- `falo-unities/src/components/icon/UrgentPriorityIcon.vue`


## other/elements: Shared UI kit

Reusable components: buttons, inputs, selects, tables, file upload, editor, viewer, pagination, phone and search widgets.

- **kind:** module
- **status:** active
- **loc:** 2683
- **complexity:** high
- **digest:** `sha256:41e55f55147f526bb24df2603d0b93f0814c13056633d44687b4566ca4ecb248`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/common/breadcumb/EBreadcrumb.vue | falo-unities/src/components/common/breadcumb/EBreadcrumb.vue | module | falo-unities/src/components/common/breadcumb/EBreadcrumb.vue | 42 |  |
| falo-unities/src/components/common/elements/avatar | falo-unities/src/components/common/elements/avatar | module | falo-unities/src/components/common/elements/avatar | 195 |  |
| falo-unities/src/components/common/elements/button | falo-unities/src/components/common/elements/button | module | falo-unities/src/components/common/elements/button | 105 |  |
| falo-unities/src/components/common/elements/ckeditor/CKEditor.vue | falo-unities/src/components/common/elements/ckeditor/CKEditor.vue | module | falo-unities/src/components/common/elements/ckeditor/CKEditor.vue | 177 |  |
| falo-unities/src/components/common/elements/collapse/CollapseContent.vue | falo-unities/src/components/common/elements/collapse/CollapseContent.vue | module | falo-unities/src/components/common/elements/collapse/CollapseContent.vue | 72 |  |
| falo-unities/src/components/common/elements/file | falo-unities/src/components/common/elements/file | module | falo-unities/src/components/common/elements/file | 216 |  |
| falo-unities/src/components/common/elements/form | falo-unities/src/components/common/elements/form | module | falo-unities/src/components/common/elements/form | 342 |  |
| falo-unities/src/components/common/elements/image/CommonImageViewer.vue | falo-unities/src/components/common/elements/image/CommonImageViewer.vue | module | falo-unities/src/components/common/elements/image/CommonImageViewer.vue | 137 |  |
| falo-unities/src/components/common/elements/input | falo-unities/src/components/common/elements/input | module | falo-unities/src/components/common/elements/input | 184 |  |
| falo-unities/src/components/common/elements/list/CommonListTitle.vue | falo-unities/src/components/common/elements/list/CommonListTitle.vue | module | falo-unities/src/components/common/elements/list/CommonListTitle.vue | 25 |  |
| falo-unities/src/components/common/elements/loader/BaseLoader.vue | falo-unities/src/components/common/elements/loader/BaseLoader.vue | module | falo-unities/src/components/common/elements/loader/BaseLoader.vue | 77 |  |
| falo-unities/src/components/common/elements/pagination/CommonPagination.vue | falo-unities/src/components/common/elements/pagination/CommonPagination.vue | module | falo-unities/src/components/common/elements/pagination/CommonPagination.vue | 102 |  |
| falo-unities/src/components/common/elements/pdf/CommonPDFViewer.vue | falo-unities/src/components/common/elements/pdf/CommonPDFViewer.vue | module | falo-unities/src/components/common/elements/pdf/CommonPDFViewer.vue | 193 |  |
| falo-unities/src/components/common/elements/phone/GlobalPhone.vue | falo-unities/src/components/common/elements/phone/GlobalPhone.vue | module | falo-unities/src/components/common/elements/phone/GlobalPhone.vue | 300 |  |
| falo-unities/src/components/common/elements/search/CommonSearch.vue | falo-unities/src/components/common/elements/search/CommonSearch.vue | module | falo-unities/src/components/common/elements/search/CommonSearch.vue | 77 |  |
| falo-unities/src/components/common/elements/select | falo-unities/src/components/common/elements/select | module | falo-unities/src/components/common/elements/select | 659 |  |
| falo-unities/src/components/common/elements/table | falo-unities/src/components/common/elements/table | module | falo-unities/src/components/common/elements/table | 218 |  |
| falo-unities/src/components/common/elements/tooltip/CommonTooltip.vue | falo-unities/src/components/common/elements/tooltip/CommonTooltip.vue | module | falo-unities/src/components/common/elements/tooltip/CommonTooltip.vue | 23 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/components | call | 1 |
| other/falo-unities-src-store-modules | call | 4 |
| platform-services/falo-unities-src-store-modules-master-master-ts | call | 1 |
| platform-services/src | call | 15 |

### Used by

- `employee-and-organization-account-administration/falo-unities-src-components-organizations-account-organi`
- `employee-and-organization-account-administration/falo-unities-src-views-common-employees-employeespage-vue`
- `organization-registration-and-verification/falo-unities-src-views-public-registerpage-organizationregis`
- `organization-registration-and-verification/organizations`
- `other/falo-unities-src-views-public-homepage-homepage-vue`
- `project-registration-and-verification/falo-unities-src-components-projects-approval-request-me`
- `project-registration-and-verification/projects`
- `project-registration-and-verification/projects-2`
- `project-workspace-and-task-management/task-3`
- `volunteer-recruitment-and-interviews/falo-unities-src-components-common-layout-profile-dialog`
- `volunteer-recruitment-and-interviews/volunteer-3`

### Files

- `falo-unities/src/components/common/breadcumb/EBreadcrumb.vue`
- `falo-unities/src/components/common/elements/avatar/CommonAvatar.vue`
- `falo-unities/src/components/common/elements/avatar/CommonAvatarUpload.vue`
- `falo-unities/src/components/common/elements/button/BaseButton.vue`
- `falo-unities/src/components/common/elements/button/BaseButtonCloseIcon.vue`
- `falo-unities/src/components/common/elements/ckeditor/CKEditor.vue`
- `falo-unities/src/components/common/elements/collapse/CollapseContent.vue`
- `falo-unities/src/components/common/elements/file/CommonFileDisplay.vue`
- `falo-unities/src/components/common/elements/file/CommonFileUpload.vue`
- `falo-unities/src/components/common/elements/form/AddressSelectForm.vue`
- `falo-unities/src/components/common/elements/form/FileUploadForm.vue`
- `falo-unities/src/components/common/elements/image/CommonImageViewer.vue`
- `falo-unities/src/components/common/elements/input/CommonEditor.vue`
- `falo-unities/src/components/common/elements/input/CommonInputEdit.vue`
- `falo-unities/src/components/common/elements/list/CommonListTitle.vue`
- `falo-unities/src/components/common/elements/loader/BaseLoader.vue`
- `falo-unities/src/components/common/elements/pagination/CommonPagination.vue`
- `falo-unities/src/components/common/elements/pdf/CommonPDFViewer.vue`
- `falo-unities/src/components/common/elements/phone/GlobalPhone.vue`
- `falo-unities/src/components/common/elements/search/CommonSearch.vue`
- `falo-unities/src/components/common/elements/select/AddEditorSelectDialog.vue`
- `falo-unities/src/components/common/elements/select/CommonSelectCycle.vue`
- `falo-unities/src/components/common/elements/select/CommonSelectState.vue`
- `falo-unities/src/components/common/elements/select/CommonSelectStateCategory.vue`
- `falo-unities/src/components/common/elements/select/CommonSelectTaskLabel.vue`
- `falo-unities/src/components/common/elements/select/CommonSelectTaskPriority.vue`
- `falo-unities/src/components/common/elements/select/CommonSelectWeek.vue`
- `falo-unities/src/components/common/elements/select/CommonSelectWithAvatar.vue`
- `falo-unities/src/components/common/elements/select/CycleSelect.vue`
- `falo-unities/src/components/common/elements/table/CommonTable.vue`
- `falo-unities/src/components/common/elements/table/CommonTableWithCheckRow.vue`
- `falo-unities/src/components/common/elements/tooltip/CommonTooltip.vue`


## other/error: Error and status pages (SPA)

403/404/500 views with their shared ErrorPage and StatusPage components.

- **kind:** module
- **status:** active
- **loc:** 196
- **complexity:** low
- **digest:** `sha256:571d814a3acb1974229f4d45b3a6e453b8e1148ef41c082377e8e2951e8932f0`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/common/page | falo-unities/src/components/common/page | module | falo-unities/src/components/common/page | 169 |  |
| falo-unities/src/views/Error/403Page.vue | falo-unities/src/views/Error/403Page.vue | screen | falo-unities/src/views/Error/403Page.vue | 19 | yes |
| falo-unities/src/views/Error/404Page.vue | falo-unities/src/views/Error/404Page.vue | screen | falo-unities/src/views/Error/404Page.vue | 19 | yes |
| falo-unities/src/views/Error/500Page.vue | falo-unities/src/views/Error/500Page.vue | screen | falo-unities/src/views/Error/500Page.vue | 18 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 3 |
| platform-services/falo-unities-src-router-index-ts | call | 1 |
| platform-services/src | call | 1 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/components/common/page/ErrorPage.vue`
- `falo-unities/src/components/common/page/StatusPage.vue`
- `falo-unities/src/components/common/page/confetti.ts`
- `falo-unities/src/views/Error/403Page.vue`
- `falo-unities/src/views/Error/404Page.vue`
- `falo-unities/src/views/Error/500Page.vue`


## other/falo-unities: SPA build configuration and static assets

package.json, Vite/Tailwind/TypeScript/ESLint configuration, husky hook and the public images, icons and robots file.

- **kind:** module
- **status:** active
- **loc:** 249
- **complexity:** low
- **digest:** `sha256:50615c1ad99307fccfe5c259a735b2628de3ca67004c86e7e9b9113ff5fa7c92`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities | falo-unities | module | falo-unities | 117 |  |

### Files

- `falo-unities/.env.example`
- `falo-unities/.eslintrc`
- `falo-unities/.gitignore`
- `falo-unities/.husky/pre-commit`
- `falo-unities/.prettierrc.json`
- `falo-unities/env.d.ts`
- `falo-unities/index.html`
- `falo-unities/package.json`
- `falo-unities/postcss.config.cjs`
- `falo-unities/public/images/banner-1.webp`
- `falo-unities/public/images/banner-3.webp`
- `falo-unities/public/images/fail.gif`
- `falo-unities/public/images/falo-logo.png`
- `falo-unities/public/images/favicon.ico`
- `falo-unities/public/images/login-image.jpeg`
- `falo-unities/public/images/register-banner.webp`
- `falo-unities/public/images/sample-icon.webp`
- `falo-unities/public/images/success.gif`
- `falo-unities/public/images/user.jpeg`
- `falo-unities/public/images/verified.png`
- `falo-unities/public/robots.txt`
- `falo-unities/public/svg/falo-light-bulb.svg`
- `falo-unities/public/svg/falo-question-mark.svg`
- `falo-unities/public/svg/falo-rocket.svg`
- `falo-unities/public/svg/falo-target.svg`
- `falo-unities/public/svg/falo-vision.svg`
- `falo-unities/tailwind.config.js`
- `falo-unities/tsconfig.json`
- `falo-unities/tsconfig.node.json`
- `falo-unities/update-authors.sh`
- `falo-unities/vite.config.ts`


## other/falo-unities-src: SPA application shell

App entry, root store, locales (en/vi), global styles and mock data — the shell every screen mounts in.

- **kind:** module
- **status:** active
- **loc:** 194
- **complexity:** low
- **digest:** `sha256:bdff1e55a237646da7f7336d347369c7b552771575c718f73a1cc8c46b391c40`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src | falo-unities/src | module | falo-unities/src | 70 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 1 |
| platform-services/falo-unities-src-router-index-ts | call | 1 |
| platform-services/src | call | 3 |

### Files

- `falo-unities/src/App.vue`
- `falo-unities/src/assets/css/main.scss`
- `falo-unities/src/assets/css/variables.scss`
- `falo-unities/src/assets/svg/create-team.svg`
- `falo-unities/src/assets/svg/empty-list.svg`
- `falo-unities/src/index.css`
- `falo-unities/src/index.d.ts`
- `falo-unities/src/locales/en.json`
- `falo-unities/src/locales/vi.json`
- `falo-unities/src/main.ts`
- `falo-unities/src/module.d.ts`
- `falo-unities/src/store/index.ts`
- `falo-unities/src/store/mock/sidebar-item.json`


## other/falo-unities-src-store-modules: SPA domain state stores (Pinia)

Pinia stores grouped here because each spans screens: auth/session, cycle, project, notification, volunteer, registration, accounts, tags/types and system stores (see parts).

- **kind:** module
- **status:** active
- **loc:** 2252
- **complexity:** high
- **digest:** `sha256:56dbd416dfd2f0acd83c347e12eb6a61f0b6376add884a4aa245ea8df0b84fff`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/store/modules | falo-unities/src/store/modules | module | falo-unities/src/store/modules | 2416 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/api | call | 1 |
| employee-and-organization-account-administration/api | call | 1 |
| organization-registration-and-verification/falo-unities-src-hooks-organizations-register-index-ts | call | 1 |
| organization-registration-and-verification/organization | call | 2 |
| platform-services/falo-unities-src-api-systems-configs | call | 1 |
| platform-services/falo-unities-src-hooks-systems-config-index-ts | call | 1 |
| platform-services/src | call | 5 |
| platform-services/utilities | call | 6 |
| project-registration-and-verification/falo-unities-src-api-project-register | call | 1 |
| project-workspace-and-task-management/falo-unities-src-api-cycle | call | 1 |
| project-workspace-and-task-management/falo-unities-src-hooks-projects-index-ts | call | 1 |
| project-workspace-and-task-management/falo-unities-src-hooks-task-sidebar-cycle-index-ts | call | 1 |
| project-workspace-and-task-management/page | call | 4 |
| project-workspace-and-task-management/project-2 | call | 4 |
| project-workspace-and-task-management/task-2 | call | 1 |
| publication-and-public-portal/falo-unities-src-api-publication | call | 2 |
| volunteer-recruitment-and-interviews/volunteer-2 | call | 3 |

### Used by

- `auth-and-access-control/api`
- `auth-and-access-control/auth-2`
- `auth-and-access-control/common`
- `auth-and-access-control/falo-unities-src-components-auth-changepasswordform-vue`
- `employee-and-organization-account-administration/falo-unities-src-components-admin-account`
- `employee-and-organization-account-administration/falo-unities-src-views-common-employees-employeespage-vue`
- `employee-and-organization-account-administration/falo-unities-src-views-systemadmin-systemaccount-adminaccoun`
- `employee-and-organization-account-administration/falo-unities-src-views-systemadmin-utilities-usercasepage-vu`
- `organization-registration-and-verification/organizations`
- `other/elements`
- `other/error`
- `other/falo-unities-src`
- `other/falo-unities-src-views-common-dashboard-dashboardpage-vue`
- `other/falo-unities-src-views-public-homepage-homepage-vue`
- `other/layout`
- `other/utilities`
- `platform-services/falo-unities-src-components-admin-systems-configs`
- `platform-services/src`
- `platform-services/systems`
- `project-registration-and-verification/falo-unities-src-components-projects-approval-request-me`
- `project-registration-and-verification/falo-unities-src-views-organization-projects-registerproject`
- `project-registration-and-verification/projects`
- `project-registration-and-verification/projects-2`
- `project-workspace-and-task-management/task-3`
- `publication-and-public-portal/falo-unities-src-views-organization-profile-organization`
- `publication-and-public-portal/projectpage`
- `publication-and-public-portal/publication-2`
- `volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-dashboard-memberor`
- `volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-recruitment-volunt`
- `volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-dashboard-volunteerdashboar`
- `volunteer-recruitment-and-interviews/volunteer-3`

### Parts

| Part | Kind | File |
| --- | --- | --- |
| Auth/session store |  | falo-unities/src/store/modules/auth.ts:38 |
| Cycle board store (58 branches) |  | falo-unities/src/store/modules/cycle.ts:112 |
| Notification store |  | falo-unities/src/store/modules/notification.ts:11 |
| Project store |  | falo-unities/src/store/modules/project.ts:62 |

### Files

- `falo-unities/src/store/modules/VolunteerRecruitment.ts`
- `falo-unities/src/store/modules/account.ts`
- `falo-unities/src/store/modules/auth.ts`
- `falo-unities/src/store/modules/config.ts`
- `falo-unities/src/store/modules/cycle.ts`
- `falo-unities/src/store/modules/employees.ts`
- `falo-unities/src/store/modules/file.ts`
- `falo-unities/src/store/modules/interview.ts`
- `falo-unities/src/store/modules/notification.ts`
- `falo-unities/src/store/modules/project.ts`
- `falo-unities/src/store/modules/projectFeedback.ts`
- `falo-unities/src/store/modules/projectTags.ts`
- `falo-unities/src/store/modules/projectTypes.ts`
- `falo-unities/src/store/modules/pubicProject.ts`
- `falo-unities/src/store/modules/systemAccount.ts`
- `falo-unities/src/store/modules/systemLogs.ts`
- `falo-unities/src/store/modules/userCase.ts`
- `falo-unities/src/store/modules/verifiedOrganization.ts`
- `falo-unities/src/store/modules/volunteerRegister.ts`


## other/falo-unities-src-views-common-dashboard-dashboardpage-vue: Role dashboard screens

Common, organization and system-admin dashboard pages (SystemAdminDashboardPage is not routed — that route renders ComingSoonPage).

- **kind:** module
- **status:** active
- **loc:** 155
- **complexity:** low
- **digest:** `sha256:a6363a42508dda99b3ea501d6a9bf9d1054e2286c7278539fa99a26e819cf828`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/Common/Dashboard/DashboardPage.vue | falo-unities/src/views/Common/Dashboard/DashboardPage.vue | screen | falo-unities/src/views/Common/Dashboard/DashboardPage.vue | 89 | yes |
| falo-unities/src/views/Organization/Dashboard/OrganizationDashboardPage.vue | falo-unities/src/views/Organization/Dashboard/OrganizationDashboardPage.vue | screen | falo-unities/src/views/Organization/Dashboard/OrganizationDashboardPage.vue | 79 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| employee-and-organization-account-administration/api | call | 2 |
| other/components | call | 2 |
| other/falo-unities-src-store-modules | call | 2 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/views/Common/Dashboard/DashboardPage.vue`
- `falo-unities/src/views/Organization/Dashboard/OrganizationDashboardPage.vue`
- `falo-unities/src/views/SystemAdmin/Dashboard/SystemAdminDashboardPage.vue`


## other/falo-unities-src-views-public-homepage-homepage-vue: Public home and landing hero (SPA)

Public landing home page with its hero carousel, call-to-action and statistic sections.

- **kind:** module
- **status:** active
- **loc:** 375
- **complexity:** low
- **digest:** `sha256:b7ebda606f02bc4efaade9f09e81609b422015528dbd665398d75b04157b9020`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/public/HeroCarousel.vue | falo-unities/src/components/public/HeroCarousel.vue | module | falo-unities/src/components/public/HeroCarousel.vue | 105 |  |
| falo-unities/src/components/public/LandingPage | falo-unities/src/components/public/LandingPage | module | falo-unities/src/components/public/LandingPage | 298 |  |
| falo-unities/src/components/public/campaign | falo-unities/src/components/public/campaign | module | falo-unities/src/components/public/campaign | 544 |  |
| falo-unities/src/components/public/project | falo-unities/src/components/public/project | module | falo-unities/src/components/public/project | 329 |  |
| falo-unities/src/views/Public/HomePage/HomePage.vue | falo-unities/src/views/Public/HomePage/HomePage.vue | screen | falo-unities/src/views/Public/HomePage/HomePage.vue | 55 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/elements | call | 1 |
| other/falo-unities-src-store-modules | call | 2 |
| platform-services/src | call | 10 |
| volunteer-recruitment-and-interviews/volunteer-2 | call | 1 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`
- `volunteer-recruitment-and-interviews/falo-unities-src-components-public-recruitment-publicrecruit`

### Files

- `falo-unities/src/components/public/HeroCarousel.vue`
- `falo-unities/src/components/public/LandingPage/CallToAction.vue`
- `falo-unities/src/components/public/LandingPage/StatisticSection.vue`
- `falo-unities/src/views/Public/HomePage/HomePage.vue`


## other/introducepage: Public information pages (SPA)

Introduce, FALeAP story, executive board, FAQ, terms and privacy pages (several still render ComingSoonPage placeholders).

- **kind:** module
- **status:** active
- **loc:** 603
- **complexity:** medium
- **digest:** `sha256:8acc5375624de3aae7fb737aeaeb2d16f9178a8a458d58bded5a899ad456f679`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/Public/ComingSoonPage.vue | falo-unities/src/views/Public/ComingSoonPage.vue | screen | falo-unities/src/views/Public/ComingSoonPage.vue | 21 | yes |
| falo-unities/src/views/Public/IntroducePage/ExecutiveBoardPage.vue | falo-unities/src/views/Public/IntroducePage/ExecutiveBoardPage.vue | screen | falo-unities/src/views/Public/IntroducePage/ExecutiveBoardPage.vue | 13 | yes |
| falo-unities/src/views/Public/IntroducePage/FALEAPStoryPage.vue | falo-unities/src/views/Public/IntroducePage/FALEAPStoryPage.vue | screen | falo-unities/src/views/Public/IntroducePage/FALEAPStoryPage.vue | 13 | yes |
| falo-unities/src/views/Public/IntroducePage/IntroducePage.vue | falo-unities/src/views/Public/IntroducePage/IntroducePage.vue | screen | falo-unities/src/views/Public/IntroducePage/IntroducePage.vue | 250 | yes |
| falo-unities/src/views/Public/OtherPage/FAQPage.vue | falo-unities/src/views/Public/OtherPage/FAQPage.vue | screen | falo-unities/src/views/Public/OtherPage/FAQPage.vue | 235 | yes |
| falo-unities/src/views/Public/PoliciesPage/InformationUsePolicyPage.vue | falo-unities/src/views/Public/PoliciesPage/InformationUsePolicyPage.vue | screen | falo-unities/src/views/Public/PoliciesPage/InformationUsePolicyPage.vue | 22 | yes |
| falo-unities/src/views/Public/PoliciesPage/PrivatePolicyPage.vue | falo-unities/src/views/Public/PoliciesPage/PrivatePolicyPage.vue | screen | falo-unities/src/views/Public/PoliciesPage/PrivatePolicyPage.vue | 22 | yes |
| falo-unities/src/views/Public/PoliciesPage/TermsAndConditionsPage.vue | falo-unities/src/views/Public/PoliciesPage/TermsAndConditionsPage.vue | screen | falo-unities/src/views/Public/PoliciesPage/TermsAndConditionsPage.vue | 144 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/src | call | 6 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`
- `volunteer-recruitment-and-interviews/campaignpage`

### Files

- `falo-unities/src/views/Public/ComingSoonPage.vue`
- `falo-unities/src/views/Public/IntroducePage/ExecutiveBoardPage.vue`
- `falo-unities/src/views/Public/IntroducePage/FALEAPStoryPage.vue`
- `falo-unities/src/views/Public/IntroducePage/IntroducePage.vue`
- `falo-unities/src/views/Public/OtherPage/FAQPage.vue`
- `falo-unities/src/views/Public/PoliciesPage/InformationUsePolicyPage.vue`
- `falo-unities/src/views/Public/PoliciesPage/PrivatePolicyPage.vue`
- `falo-unities/src/views/Public/PoliciesPage/TermsAndConditionsPage.vue`


## other/layout: Shared layout and page chrome

Landing, dashboard and task shells (sidebars, navbars), profile header/cards, notifications dropdown and TaskLayout/DashboardLayout.

- **kind:** module
- **status:** active
- **loc:** 2144
- **complexity:** high
- **digest:** `sha256:231cdf7607036e806cfc49111d735e6d70846d92942be51bf77c104eef52514d`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/common/layout/Common | falo-unities/src/components/common/layout/Common | module | falo-unities/src/components/common/layout/Common | 536 |  |
| falo-unities/src/components/common/layout/Dashboard | falo-unities/src/components/common/layout/Dashboard | module | falo-unities/src/components/common/layout/Dashboard | 180 |  |
| falo-unities/src/components/common/layout/Dashboard/DashboardLayout.vue | falo-unities/src/components/common/layout/Dashboard/DashboardLayout.vue | screen | falo-unities/src/components/common/layout/Dashboard/DashboardLayout.vue | 27 | yes |
| falo-unities/src/components/common/layout/LandingPage | falo-unities/src/components/common/layout/LandingPage | module | falo-unities/src/components/common/layout/LandingPage | 471 |  |
| falo-unities/src/components/common/layout/Profile | falo-unities/src/components/common/layout/Profile | module | falo-unities/src/components/common/layout/Profile | 989 |  |
| falo-unities/src/components/common/layout/Task | falo-unities/src/components/common/layout/Task | module | falo-unities/src/components/common/layout/Task | 279 |  |
| falo-unities/src/components/common/layout/Task/TaskLayout.vue | falo-unities/src/components/common/layout/Task/TaskLayout.vue | screen | falo-unities/src/components/common/layout/Task/TaskLayout.vue | 27 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| notifications-and-realtime/falo-unities-src-socket | call | 1 |
| other/falo-unities-src-store-modules | call | 4 |
| other/modules | call | 5 |
| platform-services/src | call | 12 |
| volunteer-recruitment-and-interviews/volunteer-2 | call | 1 |

### Used by

- `organization-registration-and-verification/falo-unities-src-views-public-registerpage-organizationregis`
- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/components/common/layout/Common/CommonProfileDialog.vue`
- `falo-unities/src/components/common/layout/Common/NotificationsDropDown.vue`
- `falo-unities/src/components/common/layout/Common/RegisterOrganizationNote.vue`
- `falo-unities/src/components/common/layout/Common/UserMenu.vue`
- `falo-unities/src/components/common/layout/Common/WebsiteLanguage.vue`
- `falo-unities/src/components/common/layout/Dashboard/DashboardLayout.vue`
- `falo-unities/src/components/common/layout/Dashboard/NavBar.vue`
- `falo-unities/src/components/common/layout/Dashboard/SideBar.vue`
- `falo-unities/src/components/common/layout/LandingPage/AppFooter.vue`
- `falo-unities/src/components/common/layout/LandingPage/AppHeader.vue`
- `falo-unities/src/components/common/layout/LandingPage/AppImageSlider.vue`
- `falo-unities/src/components/common/layout/LandingPage/AppMain.vue`
- `falo-unities/src/components/common/layout/LandingPage/FooterBottom.vue`
- `falo-unities/src/components/common/layout/LandingPage/LandingPageLayout.vue`
- `falo-unities/src/components/common/layout/Profile/ProfileAboutCard.vue`
- `falo-unities/src/components/common/layout/Profile/ProfileCertificateCard.vue`
- `falo-unities/src/components/common/layout/Profile/ProfileEducationCard.vue`
- `falo-unities/src/components/common/layout/Profile/ProfileExperienceCard.vue`
- `falo-unities/src/components/common/layout/Profile/ProfileHeader.vue`
- `falo-unities/src/components/common/layout/Profile/ProfileInformationCard.vue`
- `falo-unities/src/components/common/layout/Profile/ProfileProjectCard.vue`
- `falo-unities/src/components/common/layout/Profile/ProfileSkillCard.vue`
- `falo-unities/src/components/common/layout/Profile/RecruitingProjectCard.vue`
- `falo-unities/src/components/common/layout/Task/TaskLayout.vue`
- `falo-unities/src/components/common/layout/Task/TaskNavBar.vue`
- `falo-unities/src/components/common/layout/Task/TaskSideBar.vue`


## other/modules: SPA layout and organization stores

Layout, task-sidebar, organization and organization-account Pinia stores.

- **kind:** module
- **status:** active
- **loc:** 553
- **complexity:** medium
- **digest:** `sha256:3a50424030e0fb8c8942947a1de060da6d811c3ce736fffab1f56c96abf0ad79`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/store/modules/layout | falo-unities/src/store/modules/layout | module | falo-unities/src/store/modules/layout | 123 |  |
| falo-unities/src/store/modules/organization | falo-unities/src/store/modules/organization | module | falo-unities/src/store/modules/organization | 466 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| employee-and-organization-account-administration/falo-unities-src-hooks-organizations-accounts-index-ts | call | 1 |
| organization-registration-and-verification/falo-unities-src-hooks-organizations-register-index-ts | call | 1 |
| organization-registration-and-verification/organization | call | 5 |
| platform-services/src | call | 4 |
| project-workspace-and-task-management/task-2 | call | 1 |

### Used by

- `employee-and-organization-account-administration/falo-unities-src-components-organizations-account-organi`
- `employee-and-organization-account-administration/falo-unities-src-views-organization-account-organizationacco`
- `organization-registration-and-verification/falo-unities-src-views-public-registerpage-organizationregis`
- `organization-registration-and-verification/organizations`
- `other/layout`
- `project-registration-and-verification/falo-unities-src-components-organizations-dialog-attacho`
- `project-registration-and-verification/falo-unities-src-components-projects-approval-request-me`
- `project-registration-and-verification/projects-2`
- `project-workspace-and-task-management/task-3`
- `publication-and-public-portal/falo-unities-src-views-organization-profile-organization`

### Files

- `falo-unities/src/store/modules/layout/layout.ts`
- `falo-unities/src/store/modules/layout/taskSidebar.ts`
- `falo-unities/src/store/modules/organization/organization.ts`
- `falo-unities/src/store/modules/organization/organizationAccount.ts`


## other/utilities: Project tags and types admin screens

Admin pages and form/table components for the project tag and type dictionaries (views/Admin/Utilities).

- **kind:** module
- **status:** active
- **loc:** 599
- **complexity:** medium
- **digest:** `sha256:4f67b5fb94993c116714c6e18495dfaf67fefbc245ce54da48fb2b110b1418ac`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/admin/utilities/project_types | falo-unities/src/components/admin/utilities/project_types | module | falo-unities/src/components/admin/utilities/project_types | 271 |  |
| falo-unities/src/components/admin/utilities/tags | falo-unities/src/components/admin/utilities/tags | module | falo-unities/src/components/admin/utilities/tags | 264 |  |
| falo-unities/src/components/admin/utilities/user_case | falo-unities/src/components/admin/utilities/user_case | module | falo-unities/src/components/admin/utilities/user_case | 238 |  |
| falo-unities/src/views/Admin/Utilities/ProjectTagsPage.vue | falo-unities/src/views/Admin/Utilities/ProjectTagsPage.vue | screen | falo-unities/src/views/Admin/Utilities/ProjectTagsPage.vue | 87 | yes |
| falo-unities/src/views/Admin/Utilities/ProjectTypesPage.vue | falo-unities/src/views/Admin/Utilities/ProjectTypesPage.vue | screen | falo-unities/src/views/Admin/Utilities/ProjectTypesPage.vue | 87 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 5 |
| platform-services/src | call | 16 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/components/admin/utilities/project_types/ProjectTypesForm.vue`
- `falo-unities/src/components/admin/utilities/project_types/ProjectTypesTable.vue`
- `falo-unities/src/components/admin/utilities/tags/TagsForm.vue`
- `falo-unities/src/components/admin/utilities/tags/TagsTable.vue`
- `falo-unities/src/views/Admin/Utilities/ProjectTagsPage.vue`
- `falo-unities/src/views/Admin/Utilities/ProjectTypesPage.vue`


## other/viewmodel: Backend response models (auth, accounts, employees, projects)

View models (VMs) returned by the auth, account, employee and project controllers across several modules.

- **kind:** module
- **status:** active
- **loc:** 362
- **complexity:** low
- **digest:** `sha256:0a11d1d4034a5a44f832672e9ac92f9023c7a2fb105118188c0e791ff9f26dbc`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/viewmodel/account | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/account | module | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/account | 164 |  |
| falo-skeleton/src/main/java/com/falo/server/application/viewmodel/auth | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/auth | module | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/auth | 37 |  |
| falo-skeleton/src/main/java/com/falo/server/application/viewmodel/employee | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/employee | module | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/employee | 76 |  |
| falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project | module | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project | 150 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/application | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 2 |
| project-workspace-and-task-management/project-3 | call | 1 |

### Used by

- `auth-and-access-control/auth`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `employee-and-organization-account-administration/account`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-4`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `project-workspace-and-task-management/project-3`
- `project-workspace-and-task-management/task`

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/account/AccountInfoVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/account/AccountSelectVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/account/AccountStatisticVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/account/AccountVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/account/ChangePasswordFirstVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/account/ChangePasswordRequestVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/auth/AccountSignInRequestVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/auth/ChangePasswordWhenForgotVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/auth/ResetPasswordVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/auth/TokenRefreshRequestVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/auth/TokenVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/auth/UserCaseVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/employee/EmployeeAccountListVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/employee/ManagerListVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/employee/SaveEmployeeAccount.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/ProjectMemberVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/ProjectVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/SendFeedbackProjectEndVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/TagsVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/TypesVM.java`
