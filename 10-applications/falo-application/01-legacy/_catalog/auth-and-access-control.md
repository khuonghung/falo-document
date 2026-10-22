---
module: "auth-and-access-control"
name: "Auth and access control"
items: 11
---

# Auth and access control

## auth-and-access-control/api: SPA auth API client and session interceptor

Typed login/refresh/password calls, the axios interceptor that refreshes expired tokens on 401, and auth response mappers.

- **kind:** module
- **status:** active
- **loc:** 175
- **complexity:** low
- **digest:** `sha256:d3b1abf029baa7589a6608456e3a2fe91c8fe856edc4d8d226a251f0270e060d`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/api/auth | falo-unities/src/api/auth | module | falo-unities/src/api/auth | 71 |  |
| falo-unities/src/api/axios.ts | falo-unities/src/api/axios.ts | module | falo-unities/src/api/axios.ts | 119 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| other/falo-unities-src-store-modules | call | 1 |
| platform-services/src | call | 1 |

### Used by

- `auth-and-access-control/auth-2`
- `employee-and-organization-account-administration/api`
- `organization-registration-and-verification/organization`
- `other/falo-unities-src-store-modules`
- `platform-services/falo-unities-src-api-systems-configs`
- `platform-services/utilities`
- `project-registration-and-verification/falo-unities-src-api-project-register`
- `project-workspace-and-task-management/falo-unities-src-api-cycle`
- `project-workspace-and-task-management/page`
- `project-workspace-and-task-management/project-2`
- `project-workspace-and-task-management/task-2`
- `publication-and-public-portal/falo-unities-src-api-publication`
- `volunteer-recruitment-and-interviews/volunteer-2`

### Files

- `falo-unities/src/api/auth/index.ts`
- `falo-unities/src/api/auth/types.ts`
- `falo-unities/src/api/axios.ts`
- `falo-unities/src/hooks/auth/index.ts`


## auth-and-access-control/auth: Login, refresh token and password command handlers

Pipelinr handlers for login, refresh token, three password-change flows, mail-token password reset and user-case updates, each with its validator.

- **kind:** module
- **status:** active
- **loc:** 656
- **complexity:** medium
- **digest:** `sha256:f4cb28301807a66ec91bb87a267de3606d6e30b044856db08e216cd7c1a0a5a5`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password | 111 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password_first | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password_first | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password_first | 99 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password_forgot | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password_forgot | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password_forgot | 139 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/login | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/login | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/login | 150 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/refresh_token | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/refresh_token | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/refresh_token | 70 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/reset_password | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/reset_password | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/reset_password | 115 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/user_case | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/user_case | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/user_case | 93 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 6 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 7 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 6 |
| other/viewmodel | call | 3 |
| platform-services/aggregate-2 | call | 1 |
| platform-services/application | call | 7 |
| platform-services/config | call | 15 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 5 |
| platform-services/infrastructure-2 | call | 2 |

### Used by

- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Parts

| Part | Kind | File |
| --- | --- | --- |
| Login and refresh-token handling |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/login/LoginCommandHandler.java:32 |
| Password change flows (first login, forgot, regular) |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password/ChangePasswordCommandHandler.java:25 |
| Mail-token password reset |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/reset_password/ResetPasswordCommandHandler.java:26 |
| User-case updates |  | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/user_case/UserCaseCommandHandle.java:14 |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password/ChangePasswordCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password/ChangePasswordCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password/ChangePasswordCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password_first/ChangePasswordFirstCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password_first/ChangePasswordFirstCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password_first/ChangePasswordFirstCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password_forgot/ChangePasswordForgotCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password_forgot/ChangePasswordForgotCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/change_password_forgot/ChangePasswordForgotCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/login/LoginCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/login/LoginCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/login/LoginCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/refresh_token/RefreshTokenCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/refresh_token/RefreshTokenCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/refresh_token/RefreshTokenCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/reset_password/ResetPasswordCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/reset_password/ResetPasswordCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/reset_password/ResetPasswordCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/user_case/UserCaseCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/user_case/UserCaseCommandHandle.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/auth/user_case/UserCaseCommandValidator.java`


## auth-and-access-control/auth-2: Login and password screens (SPA)

Sign-in, forgot-password and change-password pages with their dialog forms (ChangePasswordForm, login and forgot forms).

- **kind:** module
- **status:** active
- **loc:** 249
- **complexity:** low
- **digest:** `sha256:c837ccf4c5d87cc03c2c1e2691dcd1e8c66e3def6098124bf737aa3ec5ad6a6e`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/Auth/ChangePasswordPage.vue | falo-unities/src/views/Auth/ChangePasswordPage.vue | screen | falo-unities/src/views/Auth/ChangePasswordPage.vue | 17 | yes |
| falo-unities/src/views/Auth/ForgotPasswordPage.vue | falo-unities/src/views/Auth/ForgotPasswordPage.vue | screen | falo-unities/src/views/Auth/ForgotPasswordPage.vue | 107 | yes |
| falo-unities/src/views/Auth/LoginPage.vue | falo-unities/src/views/Auth/LoginPage.vue | screen | falo-unities/src/views/Auth/LoginPage.vue | 157 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/api | call | 2 |
| other/falo-unities-src-store-modules | call | 2 |
| platform-services/src | call | 2 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/views/Auth/ChangePasswordPage.vue`
- `falo-unities/src/views/Auth/ForgotPasswordPage.vue`
- `falo-unities/src/views/Auth/LoginPage.vue`


## auth-and-access-control/common: Common (2 leaves)

- **kind:** module
- **status:** active
- **loc:** 395
- **complexity:** low
- **digest:** `sha256:e8735ec9673b43ebeb7bf1feccee8173595763533c5cdda90633677330f31c4c`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/common/layout/Common/ChangePasswordForgotForm.vue | falo-unities/src/components/common/layout/Common/ChangePasswordForgotForm.vue | screen | falo-unities/src/components/common/layout/Common/ChangePasswordForgotForm.vue | 222 | yes |
| falo-unities/src/components/common/layout/Common/ChangePasswordLoginForm.vue | falo-unities/src/components/common/layout/Common/ChangePasswordLoginForm.vue | screen | falo-unities/src/components/common/layout/Common/ChangePasswordLoginForm.vue | 205 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 2 |
| platform-services/src | call | 4 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/components/common/layout/Common/ChangePasswordForgotForm.vue`
- `falo-unities/src/components/common/layout/Common/ChangePasswordLoginForm.vue`


## auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-application-cont: Authentication and user-case REST API

AuthController and UserCaseController endpoints for sign-in, token refresh, password change/reset and user-case maintenance; every method carries an @Authentication user-case annotation.

- **kind:** module
- **status:** active
- **loc:** 114
- **complexity:** low
- **digest:** `sha256:fbcdba29f1637679998fcbbb88d31a952f194c68500c066700b7dbd7da785ded`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/controller/auth | falo-skeleton/src/main/java/com/falo/server/application/controller/auth | module | falo-skeleton/src/main/java/com/falo/server/application/controller/auth | 141 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/auth | call, dispatch | 14 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 2 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 1 |
| other/viewmodel | call | 2 |
| platform-services/application | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 1 |

### Used by

- `auth-and-access-control/api`
- `platform-services/utilities`

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/controller/auth/AuthController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/auth/UserCaseController.java`


## auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate: Auth domain model and services

Account, Token and UserCase entities with their services and repositories (AccountRepository, TokenRepository, UserCaseRepository) — the persistence core of authentication.

- **kind:** module
- **status:** active
- **loc:** 79
- **complexity:** low
- **digest:** `sha256:402a0871e937b94b7f4f1aa9d2314b96f8ba5710c106b266dc4c586d1e1ca18f`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/aggregate/auth | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/auth | module | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/auth | 103 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/config | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 3 |

### Used by

- `auth-and-access-control/auth`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-repos`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s`
- `employee-and-organization-account-administration/account`
- `employee-and-organization-account-administration/commands`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-4`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `organization-registration-and-verification/organization-register`
- `organization-registration-and-verification/queue`
- `platform-services/aggregate-2`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `platform-services/infrastructure-2`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-registration-and-verification/project-register`
- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `project-workspace-and-task-management/task`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3`
- `volunteer-recruitment-and-interviews/queue`
- `volunteer-recruitment-and-interviews/volunteer`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/auth/Account.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/auth/Token.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/auth/UserCase.java`


## auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-repos: falo-skeleton/src/main/java/com/falo/server/domain/repositories/auth

- **kind:** module
- **status:** active
- **loc:** 379
- **complexity:** low
- **digest:** `sha256:7efb31eda3716c96aa3f45efca00ab5f6ca108d7852b5816db78ee0e1955aa19`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/repositories/auth | falo-skeleton/src/main/java/com/falo/server/domain/repositories/auth | module | falo-skeleton/src/main/java/com/falo/server/domain/repositories/auth | 399 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| employee-and-organization-account-administration/account | call | 1 |

### Used by

- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services`

### Data stores

| Store | Access |
| --- | --- |
| ds:postgres:auth | read, write |
| ds:postgres:employees | read |
| ds:postgres:organization | read |
| ds:postgres:organization_register | read |
| ds:postgres:project | read |
| ds:postgres:project_register | read |
| ds:postgres:publication | read |
| ds:postgres:volunteer | read |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/auth/AccountRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/auth/TokenRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/auth/UserCaseRepository.java`


## auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services: falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/auth

- **kind:** module
- **status:** active
- **loc:** 106
- **complexity:** low
- **digest:** `sha256:74cd75ef1e7a345de6b28751e57e153467f9f701caf95c184d249548fc64e8c0`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/auth | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/auth | module | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/auth | 140 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-repos | call | 1 |
| employee-and-organization-account-administration/account | call | 1 |
| other/viewmodel | call | 1 |
| platform-services/application | call | 1 |
| platform-services/config | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 1 |

### Used by

- `auth-and-access-control/auth`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s`
- `employee-and-organization-account-administration/account`
- `employee-and-organization-account-administration/commands`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `organization-registration-and-verification/organization-register`
- `organization-registration-and-verification/queue`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `platform-services/infrastructure-2`
- `project-registration-and-verification/project-register`
- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `volunteer-recruitment-and-interviews/queue`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/auth/AccountService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/auth/TokenService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/auth/UserCaseService.java`


## auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services-2: Token and user-case queries

Read-side queries for sessions (TokenQuery) and the user-case matrix (UserCaseQuery) used by controllers and the authorization interceptor.

- **kind:** module
- **status:** active
- **loc:** 53
- **complexity:** low
- **digest:** `sha256:f10048b4c70eafe13e65ea74fbd555e4e79c346f1634598fb197b444bbfc5a2b`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/token/TokenQuery.java | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/token/TokenQuery.java | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/token/TokenQuery.java | 34 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/user_case/UserCaseQuery.java | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/user_case/UserCaseQuery.java | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/user_case/UserCaseQuery.java | 29 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 2 |
| other/viewmodel | call | 1 |
| platform-services/application | call | 1 |
| platform-services/config | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 1 |

### Used by

- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/token/TokenQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/user_case/UserCaseQuery.java`


## auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s: JWT token issuing and user-case authorization

JJWT token issuing and validation (JwtProvider) plus the Spring interceptor that maps the caller's user-cases from the auth.usercase table to roles; Spring Security defers all URL checks to it.

- **kind:** module
- **status:** active
- **loc:** 230
- **complexity:** low
- **digest:** `sha256:80c857dbbfde423f0661207c0dc6b14baf606b6337c9d28b103392ebdab8e209`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/security/JwtProvider.java | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/security/JwtProvider.java | module | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/security/JwtProvider.java | 96 |  |
| falo-skeleton/src/main/java/com/falo/server/infrastructure/security | falo-skeleton/src/main/java/com/falo/server/infrastructure/security | module | falo-skeleton/src/main/java/com/falo/server/infrastructure/security | 181 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 1 |
| platform-services/application | call | 1 |
| platform-services/config | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 2 |

### Used by

- `auth-and-access-control/auth`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `employee-and-organization-account-administration/commands`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-2`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-3`
- `platform-services/infrastructure-2`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3`
- `volunteer-recruitment-and-interviews/volunteer`

### Parts

| Part | Kind | File |
| --- | --- | --- |
| JWT signing and validation (JJWT) |  | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/security/JwtProvider.java:26 |
| User-case matching interceptor |  | falo-skeleton/src/main/java/com/falo/server/infrastructure/security/AuthenticationInterceptor.java:22 |

### Files

- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/security/JwtProvider.java`
- `falo-skeleton/src/main/java/com/falo/server/infrastructure/security/Authentication.java`
- `falo-skeleton/src/main/java/com/falo/server/infrastructure/security/AuthenticationConfig.java`
- `falo-skeleton/src/main/java/com/falo/server/infrastructure/security/AuthenticationInterceptor.java`
- `falo-skeleton/src/main/java/com/falo/server/infrastructure/security/UserDetailInformation.java`


## auth-and-access-control/falo-unities-src-components-auth-changepasswordform-vue: falo-unities/src/components/auth/ChangePasswordForm.vue

- **kind:** module
- **status:** active
- **loc:** 172
- **complexity:** low
- **digest:** `sha256:95d4daab6cab16f5a896d5737fb752a45e242bbb95195c7441597509cfd10998`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/auth/ChangePasswordForm.vue | falo-unities/src/components/auth/ChangePasswordForm.vue | module | falo-unities/src/components/auth/ChangePasswordForm.vue | 189 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 1 |
| platform-services/src | call | 2 |

### Files

- `falo-unities/src/components/auth/ChangePasswordForm.vue`
