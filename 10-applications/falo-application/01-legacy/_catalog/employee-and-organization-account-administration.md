---
module: "employee-and-organization-account-administration"
name: "Employee and organization-account administration"
items: 18
---

# Employee and organization-account administration

## employee-and-organization-account-administration/account: account (2 leaves)

- **kind:** module
- **status:** active
- **loc:** 280
- **complexity:** low
- **digest:** `sha256:8dbc264a15f46c32e8e8cfd5e4e4512a4ec7bcc7d8984c9448c2674bec7b97e5`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/AccountQuery.java | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/AccountQuery.java | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/AccountQuery.java | 244 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/model | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/model | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/model | 66 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 4 |
| organization-registration-and-verification/queue | call | 1 |
| other/viewmodel | call | 1 |
| platform-services/application | call | 3 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 2 |
| platform-services/infrastructure-2 | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 1 |
| project-registration-and-verification/project-register | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |

### Used by

- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-repos`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/AccountQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/model/AccountInfoModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/model/AccountModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/model/AccountStatisticModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/model/MemberOrganizationStatisticModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/model/OrganizationStatisticModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/model/StaffManagerModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/account/model/VolunteerStatisticModel.java`


## employee-and-organization-account-administration/api: SPA account administration API clients and hooks

API clients, response mappers and hooks for account, employee, system-account and organization-account endpoints.

- **kind:** module
- **status:** active
- **loc:** 154
- **complexity:** low
- **digest:** `sha256:1ceeda2a5357c91704a9c2bcefb3af0294e9312178c601d5bc834d063fb42e1f`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/api/account | falo-unities/src/api/account | module | falo-unities/src/api/account | 100 |  |
| falo-unities/src/api/employee | falo-unities/src/api/employee | module | falo-unities/src/api/employee | 41 |  |
| falo-unities/src/api/system-accounts | falo-unities/src/api/system-accounts | module | falo-unities/src/api/system-accounts | 27 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/api | call | 3 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 3 |
| platform-services/src | call | 2 |

### Used by

- `employee-and-organization-account-administration/falo-unities-src-hooks-employee-index-ts`
- `employee-and-organization-account-administration/falo-unities-src-hooks-system-accounts-index-ts`
- `other/components`
- `other/falo-unities-src-store-modules`
- `other/falo-unities-src-views-common-dashboard-dashboardpage-vue`
- `volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-dashboard-memberor`
- `volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-dashboard-volunteerdashboar`

### Files

- `falo-unities/src/api/account/index.ts`
- `falo-unities/src/api/account/types.ts`
- `falo-unities/src/api/employee/index.ts`
- `falo-unities/src/api/employee/types.ts`
- `falo-unities/src/api/system-accounts/index.ts`
- `falo-unities/src/api/system-accounts/types.ts`
- `falo-unities/src/hooks/account/index.ts`


## employee-and-organization-account-administration/commands: Account and employee command handlers

Handlers that create and verify system accounts, save employee (staff/manager) accounts and maintain organization member accounts.

- **kind:** module
- **status:** active
- **loc:** 535
- **complexity:** medium
- **digest:** `sha256:8be877900a1b5581cfda75e8112b35cd174492d270e589528bf8b63d1f0dcdf7`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/account | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/account | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/account | 143 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/employee | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/employee | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/employee | 220 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization/organization_account | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization/organization_account | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization/organization_account | 252 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 3 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 3 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 2 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 4 |
| platform-services/aggregate-2 | call | 3 |
| platform-services/application | call | 5 |
| platform-services/config | call | 8 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 5 |
| platform-services/infrastructure-2 | call | 2 |

### Used by

- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/account/AccountCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/account/AccountCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/account/AccountCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/employee/EmployeeAccountCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/employee/EmployeeAccountCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/employee/EmployeeAccountCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization/organization_account/OrganizationAccountCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization/organization_account/OrganizationAccountCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/organization/organization_account/OrganizationAccountCommandValidator.java`


## employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-cont: System, employee and organization account REST API

AccountController (statistics, lists, role lookup), EmployeeAccountController and OrganizationAccountController endpoints for the back office.

- **kind:** module
- **status:** active
- **loc:** 313
- **complexity:** low
- **digest:** `sha256:61a2c09a11ff8eb2135dce299abb7a2f941fc4770fe9cfe46522cdd440eb2610`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/controller/account/AccountController.java | falo-skeleton/src/main/java/com/falo/server/application/controller/account/AccountController.java | module | falo-skeleton/src/main/java/com/falo/server/application/controller/account/AccountController.java | 105 | yes |
| falo-skeleton/src/main/java/com/falo/server/application/controller/employees/EmployeeAccountController.java | falo-skeleton/src/main/java/com/falo/server/application/controller/employees/EmployeeAccountController.java | module | falo-skeleton/src/main/java/com/falo/server/application/controller/employees/EmployeeAccountController.java | 85 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 2 |
| employee-and-organization-account-administration/account | call | 1 |
| employee-and-organization-account-administration/commands | call, dispatch | 4 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-4 | call | 1 |
| other/viewmodel | call | 2 |
| platform-services/application | call | 4 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 2 |
| platform-services/infrastructure-2 | call | 1 |

### Used by

- `employee-and-organization-account-administration/api`

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/controller/account/AccountController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/employees/EmployeeAccountController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/organization/OrganizationAccountController.java`


## employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-view: falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization

- **kind:** module
- **status:** active
- **loc:** 122
- **complexity:** low
- **digest:** `sha256:a9c8b0e75ca724ec824ec6ac479ee9633ac5fa51d712e0f87a22f885c5981aab`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization | module | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization | 139 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/config | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 1 |

### Used by

- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization/ExportOrganizationAccountVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization/FetchOrganizationAccountVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization/OrganizationAccountVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/organization/OrganizationProfileVM.java`


## employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate: Employee and organization account domain

EmployeeAccount and organization entities (OrganizationAccount, assignees, contacts, projects) with their repositories and services.

- **kind:** module
- **status:** active
- **loc:** 516
- **complexity:** low
- **digest:** `sha256:95c8934c316f86463b258349c2922175072198d54b2479d04d4482b3abf828eb`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/aggregate/employees/EmployeeAccount.java | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/employees/EmployeeAccount.java | module | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/employees/EmployeeAccount.java | 31 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization | module | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization | 159 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/repositories/employees/EmployeeAccountRepository.java | falo-skeleton/src/main/java/com/falo/server/domain/repositories/employees/EmployeeAccountRepository.java | module | falo-skeleton/src/main/java/com/falo/server/domain/repositories/employees/EmployeeAccountRepository.java | 73 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization | falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization | module | falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization | 174 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/employees/EmployeeAccountService.java | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/employees/EmployeeAccountService.java | module | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/employees/EmployeeAccountService.java | 37 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization | module | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization | 136 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | call | 2 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 3 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| organization-registration-and-verification/organization-register | call | 3 |
| platform-services/config | call | 4 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 3 |

### Used by

- `employee-and-organization-account-administration/account`
- `employee-and-organization-account-administration/commands`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-4`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `organization-registration-and-verification/organization-register`
- `organization-registration-and-verification/queue`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-registration-and-verification/project-register`
- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `project-workspace-and-task-management/task`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3`
- `volunteer-recruitment-and-interviews/queue`
- `volunteer-recruitment-and-interviews/volunteer`

### Data stores

| Store | Access |
| --- | --- |
| ds:postgres:auth | read |
| ds:postgres:employees | read, write |
| ds:postgres:organization | read, write |
| ds:postgres:project | read |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/employees/EmployeeAccount.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization/Organization.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization/OrganizationAccount.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization/RegisteredOrganizationAssignee.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization/RegisteredOrganizationContact.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/organization/RegisteredOrganizationProject.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/employees/EmployeeAccountRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization/OrganizationAccountRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization/OrganizationAssigneeRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization/OrganizationContactRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization/OrganizationProjectRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/organization/OrganizationRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/employees/EmployeeAccountService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization/OrganizationAccountService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization/OrganizationService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization/RegisteredOrganizationAssigneeService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization/RegisteredOrganizationContactService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/organization/RegisteredOrganizationProjectService.java`


## employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-4: Account administration queries, statistics and Excel export

Account statistics and lists feeding the dashboards, employee lookups, organization-account queries and the POI Excel export with their models and view models.

- **kind:** module
- **status:** active
- **loc:** 90
- **complexity:** low
- **digest:** `sha256:f2fd7480230161bcabf5f3a5337b3428d55493be61a35355c17fe803290575b6`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/employee/EmployeeAccountQuery.java | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/employee/EmployeeAccountQuery.java | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/employee/EmployeeAccountQuery.java | 87 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| other/viewmodel | call | 1 |
| platform-services/application | call | 3 |
| platform-services/infrastructure-2 | call | 1 |

### Used by

- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/employee/EmployeeAccountQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/employee/model/EmployeeAccountModel.java`


## employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6: falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization

- **kind:** module
- **status:** active
- **loc:** 224
- **complexity:** low
- **digest:** `sha256:6c48192a1f4259a1a9dcb4a527e420f996b9f717cbc197eb08d105102f270af0`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization | 260 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-view | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| organization-registration-and-verification/organization-register | call | 1 |
| platform-services/application | call | 3 |
| platform-services/falo-skeleton-libs-core-src-main-java-com-falo-core-domain-s-2 | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 1 |
| platform-services/infrastructure-2 | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |

### Used by

- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization/OrganizationAccountQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization/OrganizationQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization/RegisteredAssigneeQuery.java`


## employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7: falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization/model

- **kind:** module
- **status:** active
- **loc:** 84
- **complexity:** low
- **digest:** `sha256:1c8f19ce9cbfae202f420eb8b379115aab7d705398ca94c5be776cc280102e14`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization/model | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization/model | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization/model | 93 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 1 |

### Used by

- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `organization-registration-and-verification/organization-register`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-registration-and-verification/project-register`
- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization/model/AssigneeModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization/model/ContactModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization/model/OrganizationAccountModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization/model/OrganizationInformationModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization/model/OrganizationProfileModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/organization/model/RecruitingProjectModel.java`


## employee-and-organization-account-administration/falo-unities-src-components-admin-account: falo-unities/src/components/admin/account

- **kind:** module
- **status:** active
- **loc:** 241
- **complexity:** low
- **digest:** `sha256:238e1929b4c26802c0969da98843c5657133e89ef09ca5074abdec0e13115a9f`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/admin/account | falo-unities/src/components/admin/account | module | falo-unities/src/components/admin/account | 274 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 1 |
| platform-services/src | call | 4 |

### Files

- `falo-unities/src/components/admin/account/AccountDetailForm.vue`
- `falo-unities/src/components/admin/account/AccountTable.vue`


## employee-and-organization-account-administration/falo-unities-src-components-organizations-account-organi: falo-unities/src/components/organizations/account/OrganizationAccountForm.vue

- **kind:** module
- **status:** active
- **loc:** 285
- **complexity:** low
- **digest:** `sha256:a153cda93a775a52eb7dda7e31672f479b33405b1adf70c5c5aa526a2e809f1f`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/organizations/account/OrganizationAccountForm.vue | falo-unities/src/components/organizations/account/OrganizationAccountForm.vue | module | falo-unities/src/components/organizations/account/OrganizationAccountForm.vue | 320 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/elements | call | 1 |
| other/modules | call | 1 |
| platform-services/src | call | 4 |

### Files

- `falo-unities/src/components/organizations/account/OrganizationAccountForm.vue`


## employee-and-organization-account-administration/falo-unities-src-hooks-employee-index-ts: falo-unities/src/hooks/employee/index.ts

- **kind:** module
- **status:** active
- **loc:** 42
- **complexity:** low
- **digest:** `sha256:ff42a4548fb3d8eaefb46dfad9e8eb9994195756454901466bd7c6572916c86f`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/hooks/employee/index.ts | falo-unities/src/hooks/employee/index.ts | module | falo-unities/src/hooks/employee/index.ts | 43 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| employee-and-organization-account-administration/api | call | 1 |
| platform-services/src | call | 1 |

### Files

- `falo-unities/src/hooks/employee/index.ts`


## employee-and-organization-account-administration/falo-unities-src-hooks-organizations-accounts-index-ts: falo-unities/src/hooks/organizations/accounts/index.ts

- **kind:** module
- **status:** active
- **loc:** 74
- **complexity:** low
- **digest:** `sha256:542b313b077dcc08025443f6a3baed10b7081fdc9f4b59f95296d0740b7f3849`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/hooks/organizations/accounts/index.ts | falo-unities/src/hooks/organizations/accounts/index.ts | module | falo-unities/src/hooks/organizations/accounts/index.ts | 78 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| organization-registration-and-verification/organization | call | 1 |
| platform-services/src | call | 1 |

### Used by

- `other/modules`

### Files

- `falo-unities/src/hooks/organizations/accounts/index.ts`


## employee-and-organization-account-administration/falo-unities-src-hooks-system-accounts-index-ts: falo-unities/src/hooks/system-accounts/index.ts

- **kind:** module
- **status:** active
- **loc:** 40
- **complexity:** low
- **digest:** `sha256:0e0f6a797abee40dbe4d860a880c6f8912d7bcb3edf4379c799078d8ab69366c`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/hooks/system-accounts/index.ts | falo-unities/src/hooks/system-accounts/index.ts | module | falo-unities/src/hooks/system-accounts/index.ts | 43 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| employee-and-organization-account-administration/api | call | 1 |
| platform-services/src | call | 1 |

### Files

- `falo-unities/src/hooks/system-accounts/index.ts`


## employee-and-organization-account-administration/falo-unities-src-views-common-employees-employeespage-vue: Employee administration screens

Employee list page with its create/edit form and table (EmployeeForm, EmployeeTable).

- **kind:** module
- **status:** active
- **loc:** 545
- **complexity:** medium
- **digest:** `sha256:d2d199e05c70217c75918ec40e031d9459e69abe23dec2c36d5b4bed03d9438a`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/employee | falo-unities/src/components/employee | module | falo-unities/src/components/employee | 459 |  |
| falo-unities/src/views/Common/Employees/EmployeesPage.vue | falo-unities/src/views/Common/Employees/EmployeesPage.vue | screen | falo-unities/src/views/Common/Employees/EmployeesPage.vue | 180 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/elements | call | 1 |
| other/falo-unities-src-store-modules | call | 2 |
| platform-services/src | call | 7 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/components/employee/EmployeeForm.vue`
- `falo-unities/src/components/employee/EmployeeTable.vue`
- `falo-unities/src/views/Common/Employees/EmployeesPage.vue`


## employee-and-organization-account-administration/falo-unities-src-views-organization-account-organizationacco: Organization account screens

Organization member account page with its form, attach-account dialog and account table.

- **kind:** module
- **status:** active
- **loc:** 176
- **complexity:** low
- **digest:** `sha256:d1cb458f9bce34f01cd131c499144792685fd9a54a1b0f3260899726dc72afe8`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/Organization/Account/OrganizationAccountPage.vue | falo-unities/src/views/Organization/Account/OrganizationAccountPage.vue | screen | falo-unities/src/views/Organization/Account/OrganizationAccountPage.vue | 141 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/modules | call | 1 |
| platform-services/src | call | 3 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/components/organizations/table/OrganizationAccountTable.vue`
- `falo-unities/src/views/Organization/Account/OrganizationAccountPage.vue`


## employee-and-organization-account-administration/falo-unities-src-views-systemadmin-systemaccount-adminaccoun: System account administration screens

System admin account list page with its detail form and table (AdminAccountPage, AccountDetailForm, AccountTable).

- **kind:** module
- **status:** active
- **loc:** 57
- **complexity:** low
- **digest:** `sha256:07fc3866593d60ec2de0d0e7902ba6e4ec973547769556f8db146404a18ecf39`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/SystemAdmin/SystemAccount/AdminAccountPage.vue | falo-unities/src/views/SystemAdmin/SystemAccount/AdminAccountPage.vue | screen | falo-unities/src/views/SystemAdmin/SystemAccount/AdminAccountPage.vue | 78 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 1 |
| platform-services/src | call | 2 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/views/SystemAdmin/SystemAccount/AdminAccountPage.vue`


## employee-and-organization-account-administration/falo-unities-src-views-systemadmin-utilities-usercasepage-vu: User-case role matrix screens

Admin screen that maintains the user-case to role matrix (UC001-UC111) with its form and table.

- **kind:** module
- **status:** active
- **loc:** 300
- **complexity:** low
- **digest:** `sha256:877fa1eb60c30742967d609fa155d3756fbd98eb308ea4d98c4155efb641e271`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/SystemAdmin/Utilities/UserCasePage.vue | falo-unities/src/views/SystemAdmin/Utilities/UserCasePage.vue | screen | falo-unities/src/views/SystemAdmin/Utilities/UserCasePage.vue | 123 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 1 |
| platform-services/src | call | 2 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/components/admin/utilities/user_case/UserCaseForm.vue`
- `falo-unities/src/components/admin/utilities/user_case/UserCaseTable.vue`
- `falo-unities/src/views/SystemAdmin/Utilities/UserCasePage.vue`
