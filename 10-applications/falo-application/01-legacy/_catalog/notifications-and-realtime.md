---
module: "notifications-and-realtime"
name: "Notifications and realtime"
items: 4
---

# Notifications and realtime

## notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-cont: Notification REST API

Endpoints to list a user's notifications and mark them read, with the SetIsRead command, NotificationQuery and its model.

- **kind:** module
- **status:** active
- **loc:** 156
- **complexity:** low
- **digest:** `sha256:058bb750577f3d160f6769044e9515bb5325756aa9b58dcc274eb2e93b5f854a`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/controller/notification/NotificationController.java | falo-skeleton/src/main/java/com/falo/server/application/controller/notification/NotificationController.java | module | falo-skeleton/src/main/java/com/falo/server/application/controller/notification/NotificationController.java | 38 | yes |
| falo-skeleton/src/main/java/com/falo/server/application/viewmodel/notification/NotificationVM.java | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/notification/NotificationVM.java | module | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/notification/NotificationVM.java | 19 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/notification | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/notification | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/notification | 70 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/notification/NotificationQuery.java | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/notification/NotificationQuery.java | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/notification/NotificationQuery.java | 42 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 1 |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even | call | 1 |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 4 |
| platform-services/application | call | 3 |
| platform-services/config | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| platform-services/infrastructure-2 | call | 2 |

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/controller/notification/NotificationController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/notification/NotificationVM.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/notification/SetIsReadNotificationCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/notification/SetIsReadNotificationCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/notification/SetIsReadNotificationCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/notification/NotificationQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/notification/model/NotificationModel.java`


## notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even: Socket.IO event fan-out

Application event fan-out: NotificationEvent persists notifications and pushes them to each receiver's Socket.IO room (register/interview/task events); includes the netty-socketio config and JWT-authenticated connection manager.

- **kind:** module
- **status:** active
- **loc:** 365
- **complexity:** low
- **digest:** `sha256:6b4dd6f68ef70aec4ec570ebe77dd57cbd0ec8418f2b5426fef2091e830f6758`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/socket/SocketIOConfig.java | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/socket/SocketIOConfig.java | module | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/socket/SocketIOConfig.java | 28 | yes |
| falo-skeleton/src/main/java/com/falo/server/application/events/NotificationEvent.java | falo-skeleton/src/main/java/com/falo/server/application/events/NotificationEvent.java | module | falo-skeleton/src/main/java/com/falo/server/application/events/NotificationEvent.java | 294 |  |
| falo-skeleton/src/main/java/com/falo/server/application/events/model/NotificationModel.java | falo-skeleton/src/main/java/com/falo/server/application/events/model/NotificationModel.java | module | falo-skeleton/src/main/java/com/falo/server/application/events/model/NotificationModel.java | 19 |  |
| falo-skeleton/src/main/java/com/falo/server/infrastructure/socket/SocketOpenConnection.java | falo-skeleton/src/main/java/com/falo/server/infrastructure/socket/SocketOpenConnection.java | module | falo-skeleton/src/main/java/com/falo/server/infrastructure/socket/SocketOpenConnection.java | 79 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 1 |
| employee-and-organization-account-administration/account | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | call | 1 |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 1 |
| organization-registration-and-verification/queue | call | 1 |
| platform-services/application | call | 4 |
| platform-services/config | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 3 |
| platform-services/infrastructure-2 | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 1 |
| project-registration-and-verification/project-register | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| volunteer-recruitment-and-interviews/queue | call | 1 |

### Used by

- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `organization-registration-and-verification/organization-register`
- `project-registration-and-verification/project-register`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/task`
- `volunteer-recruitment-and-interviews/queue`
- `volunteer-recruitment-and-interviews/volunteer`

### Parts

| Part | Kind | File |
| --- | --- | --- |
| Event fan-out to persisted notifications and socket rooms |  | falo-skeleton/src/main/java/com/falo/server/application/events/NotificationEvent.java:43 |

### Files

- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/socket/SocketIOConfig.java`
- `falo-skeleton/src/main/java/com/falo/server/application/events/NotificationEvent.java`
- `falo-skeleton/src/main/java/com/falo/server/application/events/model/NotificationModel.java`
- `falo-skeleton/src/main/java/com/falo/server/infrastructure/socket/SocketOpenConnection.java`


## notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-domain-aggregate: Notification domain

Notification and NotificationReceiver entities with repositories and services that persist notifications and their receivers.

- **kind:** module
- **status:** active
- **loc:** 104
- **complexity:** low
- **digest:** `sha256:804254c2632a439e4d31db580df39b5e9529e76dd1ad6545c8c334b2812e7245`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/aggregate/notification | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/notification | module | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/notification | 50 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/repositories/notification | falo-skeleton/src/main/java/com/falo/server/domain/repositories/notification | module | falo-skeleton/src/main/java/com/falo/server/domain/repositories/notification | 31 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/notification | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/notification | module | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/notification | 43 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even | call | 2 |
| platform-services/config | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 2 |

### Used by

- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `platform-services/config`

### Data stores

| Store | Access |
| --- | --- |
| ds:postgres:auth | read |
| ds:postgres:notification | read, write |
| ds:postgres:organization | read |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/notification/Notification.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/notification/NotificationReceiver.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/notification/NotificationReceiverRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/notification/NotificationRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/notification/NotificationReceiverService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/notification/NotificationService.java`


## notifications-and-realtime/falo-unities-src-socket: SPA socket client and notification API

socket.io client connection and authentication (socket.ts, socket-connect.ts) plus the notification REST client.

- **kind:** module
- **status:** active
- **loc:** 66
- **complexity:** low
- **digest:** `sha256:9cd51f679e72b29c3eb25387fab5301a4dc37934ecf1a8c3ad388f71b8b8b64f`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/socket | falo-unities/src/socket | module | falo-unities/src/socket | 64 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/src | call | 1 |

### Used by

- `other/layout`
- `project-workspace-and-task-management/task-3`

### Files

- `falo-unities/src/api/notification/index.ts`
- `falo-unities/src/api/notification/type.ts`
- `falo-unities/src/socket/socket-connect.ts`
- `falo-unities/src/socket/socket.ts`
