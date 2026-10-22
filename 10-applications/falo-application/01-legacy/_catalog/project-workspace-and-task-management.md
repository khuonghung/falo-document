---
module: "project-workspace-and-task-management"
name: "Project workspace and task management"
items: 25
---

# Project workspace and task management

## project-workspace-and-task-management/comment-and-attachment-command-handlers: Comment and attachment command handlers

- **kind:** module
- **status:** active
- **loc:** 159
- **complexity:** low
- **digest:** `sha256:7ee249fe560bc6a9eb6669f203635c3ad354b3c381f11d0e42030fc46d3a70c3`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | 87 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | 93 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | 200 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | 61 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | 81 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | 127 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | 95 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | 76 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | 68 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | 164 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | 133 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | 76 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 5 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 10 |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| organization-registration-and-verification/organization-register | call | 1 |
| organization-registration-and-verification/queue | call | 2 |
| platform-services/application | call | 13 |
| platform-services/config | call | 13 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 12 |
| platform-services/infrastructure-2 | call | 5 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 2 |
| project-registration-and-verification/project-register | call | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 24 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | call | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | call | 1 |
| project-workspace-and-task-management/label | call | 2 |
| project-workspace-and-task-management/project-3 | call | 4 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 6 |

### Used by

- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `project-workspace-and-task-management/label`
- `project-workspace-and-task-management/state`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment/AttachmentCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment/AttachmentCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment/AttachmentCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment/CommentCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment/CommentCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment/CommentCommandValidator.java`


## project-workspace-and-task-management/cycle-command-handlers-create-update: Cycle command handlers (create, update)

- **kind:** module
- **status:** active
- **loc:** 224
- **complexity:** low
- **digest:** `sha256:d5b81532db2e90f31d00523c417653ef381351d1039a7ac702d6878aa9b1a1bf`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | 87 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | 93 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | 200 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | 61 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | 81 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | 127 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | 95 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | 76 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | 68 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | 164 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | 133 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | 76 |  |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/CreateCycleCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/CreateCycleCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/CreateCycleCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update/UpdateCycleCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update/UpdateCycleCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update/UpdateCycleCommandValidator.java`


## project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont: Workspace REST API

Twelve controllers exposing cycles, tasks, states, labels, pages, members, comments, attachments, tags and types endpoints (see parts).

- **kind:** module
- **status:** active
- **loc:** 664
- **complexity:** low
- **digest:** `sha256:deeb5fe593044c692e7107752f768443a25ef6f6ce00748e25720d0143bbe144`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/controller/project | falo-skeleton/src/main/java/com/falo/server/application/controller/project | module | falo-skeleton/src/main/java/com/falo/server/application/controller/project | 1047 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| organization-registration-and-verification/queue | call | 1 |
| other/viewmodel | call | 1 |
| platform-services/application | call | 2 |
| platform-services/config | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 2 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 1 |
| project-registration-and-verification/project-register | call, dispatch | 8 |
| project-registration-and-verification/queue | call | 1 |
| project-workspace-and-task-management/comment-and-attachment-command-handlers | call, dispatch | 24 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-servi | call, dispatch | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-5 | call, dispatch | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | call | 1 |
| project-workspace-and-task-management/label | call, dispatch | 4 |
| project-workspace-and-task-management/project-3 | call | 2 |
| project-workspace-and-task-management/state | call, dispatch | 4 |
| project-workspace-and-task-management/task | call, dispatch | 4 |

### Used by

- `organization-registration-and-verification/organization`
- `platform-services/utilities`
- `project-registration-and-verification/falo-unities-src-api-project-register`
- `project-workspace-and-task-management/falo-unities-src-api-cycle`
- `project-workspace-and-task-management/page`
- `project-workspace-and-task-management/project-2`
- `project-workspace-and-task-management/task-2`

### Parts

| Part | Kind | File |
| --- | --- | --- |
| Cycle and task endpoints |  | falo-skeleton/src/main/java/com/falo/server/application/controller/project/CycleController.java:21 |
| Task endpoints |  | falo-skeleton/src/main/java/com/falo/server/application/controller/project/TaskController.java:20 |
| Page and comment endpoints |  | falo-skeleton/src/main/java/com/falo/server/application/controller/project/PageController.java:23 |
| Member and attachment endpoints |  | falo-skeleton/src/main/java/com/falo/server/application/controller/project/ProjectMemberController.java:23 |
| Tags and types dictionary endpoints |  | falo-skeleton/src/main/java/com/falo/server/application/controller/project/TagsController.java:23 |

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/controller/project/AttachmentController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/project/CommentController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/project/CycleController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/project/LabelController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/project/PageController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/project/ProjectController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/project/ProjectFeedbackController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/project/ProjectMemberController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/project/StateController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/project/TagsController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/project/TaskController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/project/TypesController.java`


## project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate: Workspace domain layer

Sixteen JPA entities (project, cycle, task, state, label, page, member, comment, attachment...), sixteen repositories with cross-schema native SQL and their services.

- **kind:** module
- **status:** active
- **loc:** 1545
- **complexity:** medium
- **digest:** `sha256:9d8e467b9e3adab8cc75e5cd0852168297bdb3eb9d2d409c5f26d47a01962ade`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project | module | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project | 423 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/repositories/project | falo-skeleton/src/main/java/com/falo/server/domain/repositories/project | module | falo-skeleton/src/main/java/com/falo/server/domain/repositories/project | 875 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project | module | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project | 466 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | call | 2 |
| organization-registration-and-verification/queue | call | 3 |
| platform-services/application | call | 1 |
| platform-services/config | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 4 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 3 |
| project-registration-and-verification/project-register | call | 3 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | call | 2 |
| project-workspace-and-task-management/project-3 | call | 1 |

### Used by

- `employee-and-organization-account-administration/account`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `organization-registration-and-verification/organization-register`
- `organization-registration-and-verification/queue`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `platform-services/infrastructure-2`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-registration-and-verification/project-register`
- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-servi`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-5`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `project-workspace-and-task-management/label`
- `project-workspace-and-task-management/state`
- `project-workspace-and-task-management/task`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3`
- `volunteer-recruitment-and-interviews/queue`
- `volunteer-recruitment-and-interviews/volunteer`

### Data stores

| Store | Access |
| --- | --- |
| ds:postgres:auth | read |
| ds:postgres:organization | read |
| ds:postgres:project | read, write |
| ds:postgres:publication | read |
| ds:postgres:volunteer | read |

### Parts

| Part | Kind | File |
| --- | --- | --- |
| JPA entities (Task, Cycle, Page, State, Label...) |  | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/Task.java:18 |
| Repositories with cross-schema native SQL |  | falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/ProjectRepository.java:16 |
| Domain services |  | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/TaskService.java:12 |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/Cycle.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/Label.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/Page.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/PageEditor.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/Project.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/ProjectFeedbackEnd.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/ProjectMember.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/RegisteredProjectArchive.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/RegisteredProjectMainMember.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/State.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/Tags.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/Task.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/TaskAttachment.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/TaskChangesRecord.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/TaskComment.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/project/Types.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/CycleRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/LabelRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/PageEditorRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/PageRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/ProjectFeedbackEndRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/ProjectMemberRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/ProjectRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/RegisteredProjectArchiveRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/RegisteredProjectMainMemberRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/StateRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/TagRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/TaskAttachmentRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/TaskChangesRecordRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/TaskCommentRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/TaskRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/project/TypeRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/CycleService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/LabelService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/PageEditorService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/PageService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/ProjectFeedbackEndService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/ProjectMemberService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/ProjectService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/RegisteredProjectArchiveService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/RegisteredProjectMainMemberService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/StateService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/TagService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/TaskAttachmentService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/TaskChangesRecordService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/TaskCommentService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/TaskService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/project/TypeService.java`


## project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-servi: falo-skeleton/src/main/java/com/falo/server/domain/services/commands/tag

- **kind:** module
- **status:** active
- **loc:** 117
- **complexity:** low
- **digest:** `sha256:76b5ff83e3a209bf2756584c26e1cc0dc449693a521dcadc1daaa4a8e84b2d5e`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/tag | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/tag | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/tag | 133 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| organization-registration-and-verification/queue | call | 1 |
| platform-services/application | call | 1 |
| platform-services/config | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| project-registration-and-verification/project-register | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |

### Used by

- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/tag/TagCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/tag/TagCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/tag/TagCommandValidator.java`


## project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-5: Project tag and type command handlers

Handlers that maintain the project tag and type dictionaries (TagCommandHandler, TypeCommandHandler).

- **kind:** module
- **status:** active
- **loc:** 106
- **complexity:** low
- **digest:** `sha256:3be2c617b3d59eb5cc414fda92103fe80b9bc695e41bbc86d5c7114674bd1c81`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/types | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/types | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/types | 124 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/application | call | 1 |
| platform-services/config | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |

### Used by

- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/types/TypeCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/types/TypeCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/types/TypeCommandValidator.java`


## project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6: Workspace queries and response models

Read side: ProjectQuery with cross-schema joins into publication, cycle/task/page/member/comment queries, their result models and response view models.

- **kind:** module
- **status:** active
- **loc:** 976
- **complexity:** medium
- **digest:** `sha256:394d77ea491e21c12573ce616810451bb5216fb8cd617c4a35396f32c6e20db9`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project | 1075 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-view | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | call | 1 |
| organization-registration-and-verification/queue | call | 1 |
| other/viewmodel | call | 1 |
| platform-services/application | call | 4 |
| platform-services/config | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 3 |
| platform-services/infrastructure-2 | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 1 |
| project-registration-and-verification/project-register | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | call | 1 |
| project-workspace-and-task-management/project-3 | call | 2 |
| publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |

### Used by

- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `project-workspace-and-task-management/state`
- `project-workspace-and-task-management/task`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/CommentQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/CycleQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/LabelQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/PageQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/ProjectFeedbackEndQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/ProjectMemberQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/ProjectQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/StateQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/TaskAttachmentsQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/TaskQuery.java`


## project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-7: falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model

- **kind:** module
- **status:** active
- **loc:** 223
- **complexity:** low
- **digest:** `sha256:1a8ca4516694786ac9f0c3d9d636b76f9fb1b4abeaaa73203de7aee171f37cd4`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model | 248 |  |

### Used by

- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model/CycleModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model/LabelStatisticModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model/ListFeedbackModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model/ListPageModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model/MemberStatisticModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model/ProjectMemberModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model/ProjectModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model/ProjectPublicationModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model/PublicationForVerifyModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model/PublicationImportModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model/PublicationModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/project/model/TaskStatisticModel.java`


## project-workspace-and-task-management/falo-unities-src-api-cycle: SPA workspace API clients and hooks

Typed clients for cycles, tasks, pages and projects plus the task label/state/sidebar and project response hooks.

- **kind:** module
- **status:** active
- **loc:** 91
- **complexity:** low
- **digest:** `sha256:e5648f0af9a638daa00525ede5e5a1137799e1e4dbad4e85ab809e14ac8fff91`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/api/cycle | falo-unities/src/api/cycle | module | falo-unities/src/api/cycle | 73 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/api | call | 1 |
| platform-services/src | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |

### Used by

- `other/falo-unities-src-store-modules`
- `project-workspace-and-task-management/falo-unities-src-store-modules-task`
- `project-workspace-and-task-management/task-3`

### Files

- `falo-unities/src/api/cycle/index.ts`
- `falo-unities/src/api/cycle/type.ts`
- `falo-unities/src/hooks/task/cycle/index.ts`
- `falo-unities/src/hooks/task/sidebar/index.ts`
- `falo-unities/src/hooks/task/sidebar/page/index.ts`


## project-workspace-and-task-management/falo-unities-src-hooks-projects-index-ts: falo-unities/src/hooks/projects/index.ts

- **kind:** module
- **status:** active
- **loc:** 149
- **complexity:** low
- **digest:** `sha256:2dfaf61b2f7f953062ea031b2927f067676d0689df48922ce1be5ca808401480`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/hooks/projects/index.ts | falo-unities/src/hooks/projects/index.ts | module | falo-unities/src/hooks/projects/index.ts | 155 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/src | call | 1 |
| project-registration-and-verification/falo-unities-src-api-project-register | call | 1 |
| project-workspace-and-task-management/project-2 | call | 3 |

### Used by

- `other/falo-unities-src-store-modules`

### Files

- `falo-unities/src/hooks/projects/index.ts`


## project-workspace-and-task-management/falo-unities-src-hooks-task-labels-index-ts: falo-unities/src/hooks/task/labels/index.ts

- **kind:** module
- **status:** active
- **loc:** 22
- **complexity:** low
- **digest:** `sha256:ff688247358242f2b8da6a2b4b24d4cd70f5898b922882784a087e012a6c21bd`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/hooks/task/labels/index.ts | falo-unities/src/hooks/task/labels/index.ts | module | falo-unities/src/hooks/task/labels/index.ts | 25 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/src | call | 1 |
| project-workspace-and-task-management/task-2 | call | 1 |

### Used by

- `project-workspace-and-task-management/falo-unities-src-store-modules-task`

### Files

- `falo-unities/src/hooks/task/labels/index.ts`


## project-workspace-and-task-management/falo-unities-src-hooks-task-sidebar-cycle-index-ts: falo-unities/src/hooks/task/sidebar/cycle/index.ts

- **kind:** module
- **status:** active
- **loc:** 26
- **complexity:** low
- **digest:** `sha256:6b5cd79d38a4d9090d4e9130361615aeff1583911b994c704bcaefbe4cd752c4`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/hooks/task/sidebar/cycle/index.ts | falo-unities/src/hooks/task/sidebar/cycle/index.ts | module | falo-unities/src/hooks/task/sidebar/cycle/index.ts | 29 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/src | call | 1 |

### Used by

- `other/falo-unities-src-store-modules`

### Files

- `falo-unities/src/hooks/task/sidebar/cycle/index.ts`


## project-workspace-and-task-management/falo-unities-src-hooks-task-states-index-ts: falo-unities/src/hooks/task/states/index.ts

- **kind:** module
- **status:** active
- **loc:** 29
- **complexity:** low
- **digest:** `sha256:23df7b69ab4a232ba27802b345841eddd8d41a5f0339d2fbfc5c3d367b34a896`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/hooks/task/states/index.ts | falo-unities/src/hooks/task/states/index.ts | module | falo-unities/src/hooks/task/states/index.ts | 32 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/src | call | 1 |
| project-workspace-and-task-management/task-2 | call | 1 |

### Used by

- `project-workspace-and-task-management/falo-unities-src-store-modules-task`

### Files

- `falo-unities/src/hooks/task/states/index.ts`


## project-workspace-and-task-management/falo-unities-src-store-modules-task: SPA board state stores

projectCycle, projectState and taskLabel Pinia stores backing the board.

- **kind:** module
- **status:** active
- **loc:** 176
- **complexity:** low
- **digest:** `sha256:d02a5005490e02f32d44bd17a2bf3efad3a50ed6a5b18af0944adac20a165c6b`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/store/modules/task | falo-unities/src/store/modules/task | module | falo-unities/src/store/modules/task | 215 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/src | call | 3 |
| project-workspace-and-task-management/falo-unities-src-api-cycle | call | 1 |
| project-workspace-and-task-management/falo-unities-src-hooks-task-labels-index-ts | call | 1 |
| project-workspace-and-task-management/falo-unities-src-hooks-task-states-index-ts | call | 1 |
| project-workspace-and-task-management/task-2 | call | 3 |

### Used by

- `project-workspace-and-task-management/task-3`

### Files

- `falo-unities/src/store/modules/task/projectCycle.ts`
- `falo-unities/src/store/modules/task/projectState.ts`
- `falo-unities/src/store/modules/task/taskLabel.ts`


## project-workspace-and-task-management/label: Label command handlers (create, update)

Create and update handlers for task labels.

- **kind:** module
- **status:** active
- **loc:** 158
- **complexity:** low
- **digest:** `sha256:e5d7026eaf4a71cf9ed86c6799bd08a7a4cd61c836326d37b3c4a5baff523535`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/label/create | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/label/create | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/label/create | 87 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/label/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/label/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/label/update | 98 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/application | call | 3 |
| platform-services/config | call | 3 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 2 |
| project-workspace-and-task-management/comment-and-attachment-command-handlers | call | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 4 |
| project-workspace-and-task-management/project-3 | call | 2 |

### Used by

- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/label/create/LabelCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/label/create/LabelCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/label/create/LabelCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/label/update/UpdateLabelCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/label/update/UpdateLabelCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/label/update/UpdateLabelCommandValidator.java`


## project-workspace-and-task-management/page: page (4 leaves)

- **kind:** module
- **status:** active
- **loc:** 46
- **complexity:** low
- **digest:** `sha256:9c2cd2390ce60b324c872c6388a4e2598051f5d623c78ffa4747840bb4977c19`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/api/task/page/assign | falo-unities/src/api/task/page/assign | module | falo-unities/src/api/task/page/assign | 18 |  |
| falo-unities/src/api/task/page/get | falo-unities/src/api/task/page/get | module | falo-unities/src/api/task/page/get | 16 |  |
| falo-unities/src/api/task/page/list | falo-unities/src/api/task/page/list | module | falo-unities/src/api/task/page/list | 14 |  |
| falo-unities/src/api/task/page/register | falo-unities/src/api/task/page/register | module | falo-unities/src/api/task/page/register | 6 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/api | call | 4 |
| platform-services/src | call | 4 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 4 |

### Used by

- `other/falo-unities-src-store-modules`

### Files

- `falo-unities/src/api/task/page/assign/index.ts`
- `falo-unities/src/api/task/page/assign/types.ts`
- `falo-unities/src/api/task/page/get/index.ts`
- `falo-unities/src/api/task/page/get/types.ts`
- `falo-unities/src/api/task/page/list/index.ts`
- `falo-unities/src/api/task/page/list/types.ts`
- `falo-unities/src/api/task/page/register/index.ts`
- `falo-unities/src/api/task/page/register/types.ts`


## project-workspace-and-task-management/project: Page, editor and lock command handlers

- **kind:** module
- **status:** active
- **loc:** 323
- **complexity:** low
- **digest:** `sha256:9f6c6a955ce8886a153b29233d1b6e74a3b19be68eb1ff3ac5ab521c0f62ea9b`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | 87 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | 93 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | 200 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | 61 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | 81 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | 127 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | 95 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | 76 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | 68 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | 164 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | 133 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | 76 |  |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/PageCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/PageCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/PageCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock/SetLockCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock/SetLockCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock/SetLockCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor/PageEditorCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor/PageEditorCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor/PageEditorCommandValidator.java`


## project-workspace-and-task-management/project-2: project (4 leaves)

- **kind:** module
- **status:** active
- **loc:** 159
- **complexity:** low
- **digest:** `sha256:0cf41c995e8238f8d0975813719cf6d8e2088d4a5658014638336787bca75ce2`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/api/project/assign | falo-unities/src/api/project/assign | module | falo-unities/src/api/project/assign | 42 |  |
| falo-unities/src/api/project/feedback-end | falo-unities/src/api/project/feedback-end | module | falo-unities/src/api/project/feedback-end | 24 |  |
| falo-unities/src/api/project/get | falo-unities/src/api/project/get | module | falo-unities/src/api/project/get | 82 |  |
| falo-unities/src/api/project/list | falo-unities/src/api/project/list | module | falo-unities/src/api/project/list | 43 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/api | call | 4 |
| platform-services/src | call | 3 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 4 |

### Used by

- `organization-registration-and-verification/falo-unities-src-hooks-organizations-register-index-ts`
- `other/falo-unities-src-store-modules`
- `project-registration-and-verification/projects-2`
- `project-workspace-and-task-management/falo-unities-src-hooks-projects-index-ts`

### Files

- `falo-unities/src/api/project/assign/index.ts`
- `falo-unities/src/api/project/assign/types.ts`
- `falo-unities/src/api/project/feedback-end/index.ts`
- `falo-unities/src/api/project/feedback-end/type.ts`
- `falo-unities/src/api/project/get/index.ts`
- `falo-unities/src/api/project/get/types.ts`
- `falo-unities/src/api/project/list/index.ts`
- `falo-unities/src/api/project/list/types.ts`


## project-workspace-and-task-management/project-3: project (2 leaves)

- **kind:** module
- **status:** active
- **loc:** 331
- **complexity:** low
- **digest:** `sha256:ba551dfa12d7fd2b716dd9c47ab1b321ee95150fa2d6968427a434d3f13b156e`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/cycle | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/cycle | module | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/cycle | 288 |  |
| falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/page | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/page | module | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/page | 86 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/viewmodel | call | 2 |
| platform-services/application | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 1 |

### Used by

- `other/viewmodel`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `project-workspace-and-task-management/label`
- `project-workspace-and-task-management/state`
- `project-workspace-and-task-management/task`

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/cycle/CommentVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/cycle/CycleVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/cycle/LabelVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/cycle/StateVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/cycle/TaskAttachmentVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/cycle/TaskVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/page/PageEditorVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/project/page/PageVM.java`


## project-workspace-and-task-management/project-end-feedback-command-handlers-send-post: Project-end feedback command handlers (send, post)

- **kind:** module
- **status:** active
- **loc:** 196
- **complexity:** low
- **digest:** `sha256:022aa5a7d9641c2b5c1966493f7dc9a28176533d17ba10d8a64eb884ea501d96`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | 87 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | 93 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | 200 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | 61 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | 81 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | 127 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | 95 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | 76 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | 68 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | 164 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | 133 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | 76 |  |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/SendFeedbackProjectEndCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/SendFeedbackProjectEndCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/SendFeedbackProjectEndCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback/PostFeedbackCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback/PostFeedbackCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback/PostFeedbackCommandValidator.java`
- `falo-skeleton/src/test/java/domain/services/commands/project/feedback_project_end/post_feedback/PostFeedbackCommandHandlerTest.java`


## project-workspace-and-task-management/project-member-command-handlers-add-update-remove: Project member command handlers (add, update, remove)

- **kind:** module
- **status:** active
- **loc:** 200
- **complexity:** low
- **digest:** `sha256:9b2464552c006e0a3cf51719e245da0be2d378a7fbd7e9afe27528fef56b6204`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/attachment | 87 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/comment | 93 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle | 200 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/cycle/update | 61 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end | 81 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/feedback_project_end/post_feedback | 127 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member | 95 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove | 76 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update | 68 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page | 164 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page/set_lock | 133 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/page_editor | 76 |  |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/ProjectMemberCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/ProjectMemberCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/ProjectMemberCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove/RemoveProjectMemberCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove/RemoveProjectMemberCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/remove/RemoveProjectMemberCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update/UpdateProjectMemberCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update/UpdateProjectMemberCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/member/update/UpdateProjectMemberCommandValidator.java`


## project-workspace-and-task-management/state: State command handlers (create, update)

Create and update handlers for board states.

- **kind:** module
- **status:** active
- **loc:** 187
- **complexity:** low
- **digest:** `sha256:be5e30842c6300df09184cd2181318328a5fe92c794836551e28ff3dc08444c3`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/state/create | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/state/create | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/state/create | 130 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/state/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/state/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/state/update | 88 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/application | call | 2 |
| platform-services/config | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 3 |
| project-workspace-and-task-management/comment-and-attachment-command-handlers | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 4 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | call | 1 |
| project-workspace-and-task-management/project-3 | call | 2 |

### Used by

- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/state/create/StateCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/state/create/StateCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/state/create/StateCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/state/update/UpdateStateCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/state/update/UpdateStateCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/state/update/UpdateStateCommandValidator.java`


## project-workspace-and-task-management/task: Task command handlers (create, update)

Create and update handlers for tasks (TaskCommandHandler, UpdateTaskCommandHandler).

- **kind:** module
- **status:** active
- **loc:** 356
- **complexity:** low
- **digest:** `sha256:7ee4e9d45ec00b5d7d6392440270ebbbbb54d69cac6fe94e4ec1734c3d8804c6`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/task/create | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/task/create | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/task/create | 255 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/task/update | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/task/update | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/task/update | 146 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even | call | 1 |
| other/viewmodel | call | 1 |
| platform-services/application | call | 3 |
| platform-services/config | call | 4 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 3 |
| platform-services/infrastructure-2 | call | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 4 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | call | 1 |
| project-workspace-and-task-management/project-3 | call | 1 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |

### Used by

- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/task/create/TaskCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/task/create/TaskCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/task/create/TaskCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/task/update/UpdateTaskCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/task/update/UpdateTaskCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/project/task/update/UpdateTaskCommandValidator.java`


## project-workspace-and-task-management/task-2: task (4 leaves)

- **kind:** module
- **status:** active
- **loc:** 139
- **complexity:** low
- **digest:** `sha256:33f140e7f9bb8e69f28c60f92bbcbf7bd0b637c8912e2d0a8c6d08efd7b44220`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/api/task/cycle | falo-unities/src/api/task/cycle | module | falo-unities/src/api/task/cycle | 84 |  |
| falo-unities/src/api/task/labels | falo-unities/src/api/task/labels | module | falo-unities/src/api/task/labels | 26 |  |
| falo-unities/src/api/task/sidebar | falo-unities/src/api/task/sidebar | module | falo-unities/src/api/task/sidebar | 14 |  |
| falo-unities/src/api/task/states | falo-unities/src/api/task/states | module | falo-unities/src/api/task/states | 33 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/api | call | 4 |
| platform-services/src | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 4 |

### Used by

- `other/falo-unities-src-store-modules`
- `other/modules`
- `project-workspace-and-task-management/falo-unities-src-hooks-task-labels-index-ts`
- `project-workspace-and-task-management/falo-unities-src-hooks-task-states-index-ts`
- `project-workspace-and-task-management/falo-unities-src-store-modules-task`

### Files

- `falo-unities/src/api/task/cycle/index.ts`
- `falo-unities/src/api/task/cycle/types.ts`
- `falo-unities/src/api/task/labels/index.ts`
- `falo-unities/src/api/task/labels/types.ts`
- `falo-unities/src/api/task/sidebar/index.ts`
- `falo-unities/src/api/task/sidebar/types.ts`
- `falo-unities/src/api/task/states/index.ts`
- `falo-unities/src/api/task/states/types.ts`


## project-workspace-and-task-management/task-3: Task workspace screens and board (SPA)

Task board (TasksBoard), the cycle board with state columns and task/subtask dialogs, cycles/pages/settings pages and the project-end feedback form (see parts).

- **kind:** module
- **status:** active
- **loc:** 4800
- **complexity:** high
- **digest:** `sha256:16b0785fa78c3a1f5977d8821b691992c87a6d28bc0266aff15531c23c6f38b9`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/cycle/ProjectCycle.vue | falo-unities/src/components/cycle/ProjectCycle.vue | module | falo-unities/src/components/cycle/ProjectCycle.vue | 127 |  |
| falo-unities/src/components/cycle/column | falo-unities/src/components/cycle/column | module | falo-unities/src/components/cycle/column | 307 |  |
| falo-unities/src/components/cycle/dialog | falo-unities/src/components/cycle/dialog | module | falo-unities/src/components/cycle/dialog | 2095 |  |
| falo-unities/src/components/cycle/icon | falo-unities/src/components/cycle/icon | module | falo-unities/src/components/cycle/icon | 229 |  |
| falo-unities/src/components/cycle/subtask/CommonSubTaskDisplay.vue | falo-unities/src/components/cycle/subtask/CommonSubTaskDisplay.vue | module | falo-unities/src/components/cycle/subtask/CommonSubTaskDisplay.vue | 79 |  |
| falo-unities/src/components/task/cycle/ProjectCycleForm.vue | falo-unities/src/components/task/cycle/ProjectCycleForm.vue | module | falo-unities/src/components/task/cycle/ProjectCycleForm.vue | 188 |  |
| falo-unities/src/components/task/labels/TaskLabelForm.vue | falo-unities/src/components/task/labels/TaskLabelForm.vue | module | falo-unities/src/components/task/labels/TaskLabelForm.vue | 192 |  |
| falo-unities/src/components/task/pages/PageList.vue | falo-unities/src/components/task/pages/PageList.vue | module | falo-unities/src/components/task/pages/PageList.vue | 183 |  |
| falo-unities/src/components/task/state/ProjectStateFormDialog.vue | falo-unities/src/components/task/state/ProjectStateFormDialog.vue | module | falo-unities/src/components/task/state/ProjectStateFormDialog.vue | 227 |  |
| falo-unities/src/views/Common/Task/AddProjectMemberPage.vue | falo-unities/src/views/Common/Task/AddProjectMemberPage.vue | screen | falo-unities/src/views/Common/Task/AddProjectMemberPage.vue | 127 | yes |
| falo-unities/src/views/Common/Task/CyclesPage.vue | falo-unities/src/views/Common/Task/CyclesPage.vue | screen | falo-unities/src/views/Common/Task/CyclesPage.vue | 691 | yes |
| falo-unities/src/views/Common/Task/PageForm.vue | falo-unities/src/views/Common/Task/PageForm.vue | screen | falo-unities/src/views/Common/Task/PageForm.vue | 216 | yes |
| falo-unities/src/views/Common/Task/PagesPage.vue | falo-unities/src/views/Common/Task/PagesPage.vue | screen | falo-unities/src/views/Common/Task/PagesPage.vue | 164 | yes |
| falo-unities/src/views/Common/Task/ProjectSettingInformationPage.vue | falo-unities/src/views/Common/Task/ProjectSettingInformationPage.vue | screen | falo-unities/src/views/Common/Task/ProjectSettingInformationPage.vue | 242 | yes |
| falo-unities/src/views/Common/Task/ProjectSettingLabelsPage.vue | falo-unities/src/views/Common/Task/ProjectSettingLabelsPage.vue | screen | falo-unities/src/views/Common/Task/ProjectSettingLabelsPage.vue | 150 | yes |
| falo-unities/src/views/Common/Task/ProjectSettingStatesPage.vue | falo-unities/src/views/Common/Task/ProjectSettingStatesPage.vue | screen | falo-unities/src/views/Common/Task/ProjectSettingStatesPage.vue | 198 | yes |
| falo-unities/src/views/Common/Task/TasksBoard.vue | falo-unities/src/views/Common/Task/TasksBoard.vue | screen | falo-unities/src/views/Common/Task/TasksBoard.vue | 30 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| notifications-and-realtime/falo-unities-src-socket | call | 2 |
| other/components | call | 1 |
| other/elements | call | 14 |
| other/falo-unities-src-store-modules | call | 15 |
| other/modules | call | 5 |
| platform-services/src | call | 49 |
| project-workspace-and-task-management/falo-unities-src-api-cycle | call | 1 |
| project-workspace-and-task-management/falo-unities-src-store-modules-task | call | 6 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Parts

| Part | Kind | File |
| --- | --- | --- |
| Cycle board with state columns |  | falo-unities/src/components/cycle/ProjectCycle.vue:1 |
| Task detail dialog (largest Vue file, ~950 lines) |  | falo-unities/src/components/cycle/dialog/ProjectCycleDialogViewTask.vue:1 |
| Task board page |  | falo-unities/src/views/Common/Task/TasksBoard.vue:1 |
| Cycles page |  | falo-unities/src/views/Common/Task/CyclesPage.vue:1 |
| Project-end feedback form |  | falo-unities/src/components/projects/feedback-end/ProjectFeedbackEndForm.vue:1 |

### Files

- `falo-unities/src/components/cycle/ProjectCycle.vue`
- `falo-unities/src/components/cycle/column/ProjectCycleState.vue`
- `falo-unities/src/components/cycle/column/ProjectCycleStateWrapper.vue`
- `falo-unities/src/components/cycle/dialog/ProjectCycleDialogCreateTask.vue`
- `falo-unities/src/components/cycle/dialog/ProjectCycleDialogViewSubTask.vue`
- `falo-unities/src/components/cycle/dialog/ProjectCycleDialogViewTask.vue`
- `falo-unities/src/components/cycle/icon/ProjectCycleIconStateCategory.vue`
- `falo-unities/src/components/cycle/icon/ProjectCycleIconTaskLabel.vue`
- `falo-unities/src/components/cycle/icon/ProjectCycleIconTaskPriority.vue`
- `falo-unities/src/components/cycle/subtask/CommonSubTaskDisplay.vue`
- `falo-unities/src/components/projects/feedback-end/ProjectFeedbackEndForm.vue`
- `falo-unities/src/components/projects/feedback-end/ProjectFeedbackTable.vue`
- `falo-unities/src/components/task/cycle/ProjectCycleForm.vue`
- `falo-unities/src/components/task/labels/TaskLabelForm.vue`
- `falo-unities/src/components/task/pages/PageList.vue`
- `falo-unities/src/components/task/state/ProjectStateFormDialog.vue`
- `falo-unities/src/views/Common/Task/AddProjectMemberPage.vue`
- `falo-unities/src/views/Common/Task/CyclesPage.vue`
- `falo-unities/src/views/Common/Task/PageForm.vue`
- `falo-unities/src/views/Common/Task/PagesPage.vue`
- `falo-unities/src/views/Common/Task/ProjectSettingInformationPage.vue`
- `falo-unities/src/views/Common/Task/ProjectSettingLabelsPage.vue`
- `falo-unities/src/views/Common/Task/ProjectSettingStatesPage.vue`
- `falo-unities/src/views/Common/Task/TasksBoard.vue`
