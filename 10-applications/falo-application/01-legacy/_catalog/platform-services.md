---
module: "platform-services"
name: "Platform services"
items: 20
---

# Platform services

## platform-services/aggregate-2: Configuration and address master-data domain

Config/ConfigItem and Country/District/Province/Ward entities with their repositories and services (Redis-cached lookups).

- **kind:** module
- **status:** active
- **loc:** 347
- **complexity:** low
- **digest:** `sha256:eb48d75ed142e527e766b63329d140158e8cf40119d1e4a983d4b42a2575b471`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/domain/aggregate/configs | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/configs | module | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/configs | 47 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/aggregate/master | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/master | module | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/master | 118 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/repositories/config | falo-skeleton/src/main/java/com/falo/server/domain/repositories/config | module | falo-skeleton/src/main/java/com/falo/server/domain/repositories/config | 84 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/repositories/master | falo-skeleton/src/main/java/com/falo/server/domain/repositories/master | module | falo-skeleton/src/main/java/com/falo/server/domain/repositories/master | 43 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/configs | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/configs | module | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/configs | 53 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/mail | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/mail | module | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/mail | 473 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/master | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/master | module | falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/master | 91 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| organization-registration-and-verification/organization-register | call | 1 |
| platform-services/application | call | 2 |
| platform-services/config | call | 7 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 3 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-3 | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| platform-services/infrastructure-2 | call | 1 |

### Used by

- `auth-and-access-control/auth`
- `employee-and-organization-account-administration/commands`
- `organization-registration-and-verification/organization-register`
- `organization-registration-and-verification/queue`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-2`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-registration-and-verification/project-register`
- `project-registration-and-verification/queue`
- `volunteer-recruitment-and-interviews/queue`
- `volunteer-recruitment-and-interviews/volunteer`

### Data stores

| Store | Access |
| --- | --- |
| ds:postgres:admin | read, write |
| ds:postgres:master | read, write |

### Files

- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/configs/Config.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/configs/ConfigItem.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/master/Country.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/master/District.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/master/Province.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/master/Ward.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/config/ConfigItemsRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/config/ConfigRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/master/CountryRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/master/DistrictRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/master/ProvinceRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/master/WardRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/configs/ConfigItemService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/configs/ConfigService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/master/CountryService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/master/DistrictService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/master/ProvinceService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/master/WardService.java`


## platform-services/application: Core utilities, exceptions and API envelope

libs/core helpers: global exception handler, paging/JSON/ID/time/URI utilities, ApiResponse/PaginationResponse envelope and the NanoIds generator.

- **kind:** module
- **status:** active
- **loc:** 676
- **complexity:** medium
- **digest:** `sha256:e26762a9d3dcf6eb79a037168fcc63e30b5e93f566d6704c434385612f12466b`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/libs/core/src/main/java/com/falo/core/application/enums | falo-skeleton/libs/core/src/main/java/com/falo/core/application/enums | module | falo-skeleton/libs/core/src/main/java/com/falo/core/application/enums | 43 |  |
| falo-skeleton/libs/core/src/main/java/com/falo/core/application/exceptions | falo-skeleton/libs/core/src/main/java/com/falo/core/application/exceptions | module | falo-skeleton/libs/core/src/main/java/com/falo/core/application/exceptions | 242 |  |
| falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils | falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils | module | falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils | 456 |  |
| falo-skeleton/libs/core/src/main/java/com/falo/core/application/viewmodel | falo-skeleton/libs/core/src/main/java/com/falo/core/application/viewmodel | module | falo-skeleton/libs/core/src/main/java/com/falo/core/application/viewmodel | 100 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/config | call | 1 |

### Used by

- `auth-and-access-control/auth`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-application-cont`
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
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `organization-registration-and-verification/organization-register`
- `organization-registration-and-verification/queue`
- `other/viewmodel`
- `platform-services/aggregate-2`
- `platform-services/config`
- `platform-services/falo-skeleton-libs-core-src-main-java-com-falo-core-domain-s-2`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-3`
- `platform-services/infrastructure-2`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-registration-and-verification/project-register`
- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-servi`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-5`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `project-workspace-and-task-management/label`
- `project-workspace-and-task-management/project-3`
- `project-workspace-and-task-management/state`
- `project-workspace-and-task-management/task`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3`
- `volunteer-recruitment-and-interviews/queue`
- `volunteer-recruitment-and-interviews/volunteer`

### Files

- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/enums/SystemConfigItemsKey.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/enums/SystemFont.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/enums/SystemRole.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/exceptions/GlobalExceptionHandlerController.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/exceptions/ServerErrorException.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/exceptions/SystemBadRequestException.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/exceptions/SystemNotFoundException.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/exceptions/SystemRuntimeException.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/exceptions/SystemUnAuthorizationException.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/exceptions/SystemValidatorException.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/exceptions/package-info.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils/ApiClientUtil.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils/EventHandlerUtil.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils/FileUtil.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils/FilterUtil.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils/IdsUtil.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils/JsonUtil.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils/MD5Util.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils/PagingUtil.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils/TimeUtil.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils/UriUtil.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils/ValidationMessageUtil.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils/VersionUtil.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/utils/package-info.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/viewmodel/ApiResponse.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/viewmodel/BaseVM.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/viewmodel/PaginationResponse.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/viewmodel/WsAuthenticate.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/application/viewmodel/WsResponse.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/generator/NanoIdsGenerator.java`


## platform-services/config: Core framework configuration

libs/core wiring: Pipelinr CQRS pipeline with logging and transactional middlewares, Redis cache config, base entity/repository/service classes, Kafka consumer config, message helpers and application.yml/logback resources.

- **kind:** module
- **status:** active
- **loc:** 572
- **complexity:** medium
- **digest:** `sha256:3b2425f4a67b7a585b17edd506824bc1fa32e86aeef495235bf8e4a412a9af85`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/common | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/common | module | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/common | 58 |  |
| falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/mail | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/mail | module | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/mail | 52 |  |
| falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/package-info.java | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/package-info.java | module | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/package-info.java | 1 |  |
| falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/BaseService.java | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/BaseService.java | module | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/BaseService.java | 84 |  |
| falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/cache | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/cache | module | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/cache | 57 |  |
| falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config | module | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config | 129 |  |
| falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/cqrs | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/cqrs | module | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/cqrs | 153 |  |
| falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/kafka/KafkaConsumerConfig.java | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/kafka/KafkaConsumerConfig.java | module | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/kafka/KafkaConsumerConfig.java | 23 |  |
| falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/redis | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/redis | module | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/redis | 97 |  |
| falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/helpers | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/helpers | module | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/helpers | 106 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| platform-services/application | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 1 |

### Used by

- `auth-and-access-control/auth`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s`
- `employee-and-organization-account-administration/commands`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-view`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `organization-registration-and-verification/organization-register`
- `organization-registration-and-verification/queue`
- `platform-services/aggregate-2`
- `platform-services/application`
- `platform-services/falo-skeleton-libs-core-src-main-java-com-falo-core-domain-s-2`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `platform-services/infrastructure-2`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-registration-and-verification/project-register`
- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-servi`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-5`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `project-workspace-and-task-management/label`
- `project-workspace-and-task-management/state`
- `project-workspace-and-task-management/task`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `volunteer-recruitment-and-interviews/queue`
- `volunteer-recruitment-and-interviews/volunteer`

### Files

- `falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/common/BaseEntity.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/common/BooleanTransformable.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/common/EntityHandle.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/package-info.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/domain/repository/BaseRepository.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/domain/repository/package-info.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/BaseService.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/cache/CacheDataImpl.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/cache/ICacheData.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/AppConfig.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/AsyncConfig.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/OpenApiConfig.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/cqrs/Command.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/cqrs/CommandHandler.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/cqrs/LoggingMiddleware.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/cqrs/PipelineConfig.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/cqrs/TxMiddleware.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/kafka/KafkaConsumerConfig.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/redis/RedisCacheConfig.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/redis/RedisConfigurationProperties.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/helpers/MessageHelper.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/helpers/RestHelper.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/helpers/VirtualThreadHelper.java`
- `falo-skeleton/src/main/resources/messages.properties`


## platform-services/falo-skeleton-libs-core-src-main-java-com-falo-core-domain-s-2: Excel export support (POI)

Apache POI workbook service (CommonExcelService) and the SPA download hook — the machinery behind the organization-account Excel export.

- **kind:** module
- **status:** active
- **loc:** 135
- **complexity:** low
- **digest:** `sha256:24670879a517325962af45d6fecaf90ca11960a9708428651212b43aefd8f8d8`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/excel/CommonExcelService.java | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/excel/CommonExcelService.java | module | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/excel/CommonExcelService.java | 148 |  |
| falo-unities/src/hooks/excel/index.ts | falo-unities/src/hooks/excel/index.ts | module | falo-unities/src/hooks/excel/index.ts | 28 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/application | call | 1 |
| platform-services/config | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 1 |

### Used by

- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6`

### Files

- `falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/excel/CommonExcelService.java`
- `falo-unities/src/hooks/excel/index.ts`


## platform-services/falo-skeleton-src-main-java-com-falo-server-application: falo-skeleton/src/main/java/com/falo/server/Application.java

- **kind:** module
- **status:** active
- **loc:** 16
- **complexity:** low
- **digest:** `sha256:4e2ac7e26ba6e70c202ee4f38f561f7c3b923951a5bf1d0441bfdb9f0d4d741f`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/Application.java | falo-skeleton/src/main/java/com/falo/server/Application.java | module | falo-skeleton/src/main/java/com/falo/server/Application.java | 20 | yes |

### Files

- `falo-skeleton/src/main/java/com/falo/server/Application.java`


## platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons: Backend constants, enums and converters

Kafka topics, cache keys, deep-link URL constants, notification actions, JPA converters and the shared status/priority/user-case enums (SystemUserCase UC001-UC111).

- **kind:** module
- **status:** active
- **loc:** 859
- **complexity:** medium
- **digest:** `sha256:db2e74bb194885c8b4e5e626188ae9ac671a1634fa49463adb3738fc0b89d5e7`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/constants | falo-skeleton/src/main/java/com/falo/server/application/constants | module | falo-skeleton/src/main/java/com/falo/server/application/constants | 221 |  |
| falo-skeleton/src/main/java/com/falo/server/application/converters | falo-skeleton/src/main/java/com/falo/server/application/converters | module | falo-skeleton/src/main/java/com/falo/server/application/converters | 551 |  |
| falo-skeleton/src/main/java/com/falo/server/application/enums | falo-skeleton/src/main/java/com/falo/server/application/enums | module | falo-skeleton/src/main/java/com/falo/server/application/enums | 232 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-view | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 3 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | call | 1 |
| employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 2 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 1 |
| organization-registration-and-verification/organization-register | call | 2 |
| organization-registration-and-verification/queue | call | 2 |
| other/viewmodel | call | 1 |
| platform-services/application | call | 1 |
| platform-services/config | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 2 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2 | call | 1 |
| project-registration-and-verification/project-register | call | 2 |
| project-registration-and-verification/queue | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 3 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6 | call | 1 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-7 | call | 1 |
| project-workspace-and-task-management/project-3 | call | 2 |
| volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |

### Used by

- `auth-and-access-control/auth`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s`
- `employee-and-organization-account-administration/account`
- `employee-and-organization-account-administration/commands`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-view`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `organization-registration-and-verification/organization-register`
- `organization-registration-and-verification/queue`
- `other/viewmodel`
- `platform-services/aggregate-2`
- `platform-services/config`
- `platform-services/falo-skeleton-libs-core-src-main-java-com-falo-core-domain-s-2`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-2`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-3`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `platform-services/infrastructure-2`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-registration-and-verification/project-register`
- `project-registration-and-verification/queue`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-servi`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-5`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `project-workspace-and-task-management/label`
- `project-workspace-and-task-management/project-3`
- `project-workspace-and-task-management/state`
- `project-workspace-and-task-management/task`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-aggregate`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3`
- `volunteer-recruitment-and-interviews/queue`
- `volunteer-recruitment-and-interviews/volunteer`

### Parts

| Part | Kind | File |
| --- | --- | --- |
| Kafka topic names |  | falo-skeleton/src/main/java/com/falo/server/application/constants/KafkaTopic.java:11 |
| Deep-link URL constants |  | falo-skeleton/src/main/java/com/falo/server/application/constants/ApiUrl.java:14 |
| Redis cache keys |  | falo-skeleton/src/main/java/com/falo/server/application/constants/CacheKey.java:3 |

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/constants/ApiUrl.java`
- `falo-skeleton/src/main/java/com/falo/server/application/constants/BooleanConvert.java`
- `falo-skeleton/src/main/java/com/falo/server/application/constants/CacheKey.java`
- `falo-skeleton/src/main/java/com/falo/server/application/constants/Entity.java`
- `falo-skeleton/src/main/java/com/falo/server/application/constants/KafkaTopic.java`
- `falo-skeleton/src/main/java/com/falo/server/application/constants/NotificationAction.java`
- `falo-skeleton/src/main/java/com/falo/server/application/constants/Project.java`
- `falo-skeleton/src/main/java/com/falo/server/application/constants/WsEvent.java`
- `falo-skeleton/src/main/java/com/falo/server/application/converters/CycleBuilders.java`
- `falo-skeleton/src/main/java/com/falo/server/application/converters/OrganizationConverter.java`
- `falo-skeleton/src/main/java/com/falo/server/application/converters/ProjectConverters.java`
- `falo-skeleton/src/main/java/com/falo/server/application/converters/StringListConverter.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/AccountStatusEnum.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/AchievementCategoryEnum.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/GenderEnum.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/IconEnum.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/InterviewStatusEnum.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/NotificationCategoryEnum.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/OAuthType.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/OrganizationFeedBackTypeEnum.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/OrganizationStatusEnum.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/OrganizationTypesEnum.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/ProjectFeedbackTypesEnum.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/ProjectStatus.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/RoleInProjectEnum.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/StateCategoryEnum.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/SystemUserCase.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/TaskFieldsEnum.java`
- `falo-skeleton/src/main/java/com/falo/server/application/enums/TaskPriorityEnum.java`


## platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont: Runtime configuration REST API and queries

ConfigController/ConfigItemController endpoints with commands, queries and models for runtime configuration items.

- **kind:** module
- **status:** active
- **loc:** 333
- **complexity:** low
- **digest:** `sha256:93fcc35cfa59f285b4dcbd1d65da88cbae6ee1b5698cc25ec47771bf94831c02`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/controller/configs | falo-skeleton/src/main/java/com/falo/server/application/controller/configs | module | falo-skeleton/src/main/java/com/falo/server/application/controller/configs | 110 | yes |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/config | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/config | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/config | 81 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/commands/configItem | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/configItem | module | falo-skeleton/src/main/java/com/falo/server/domain/services/commands/configItem | 83 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/configs | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/configs | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/configs | 90 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/configs/model | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/configs/model | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/configs/model | 25 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/auth | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 1 |
| platform-services/aggregate-2 | call | 5 |
| platform-services/application | call | 6 |
| platform-services/config | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 1 |
| platform-services/viewmodel | call | 2 |

### Used by

- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `platform-services/aggregate-2`
- `platform-services/falo-unities-src-api-systems-configs`
- `platform-services/infrastructure-2`

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/controller/configs/ConfigController.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/configs/ConfigItemController.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/config/ConfigCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/config/ConfigCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/config/ConfigCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/configItem/ConfigItemCommand.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/configItem/ConfigItemCommandHandler.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/commands/configItem/ConfigItemCommandValidator.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/configs/ConfigItemsQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/configs/ConfigQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/configs/model/ConfigItemsModel.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/configs/model/ConfigModel.java`


## platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-2: Address and country master-data API

MasterController and MasterQuery over provinces, districts, wards and countries, with CountryModel.

- **kind:** module
- **status:** active
- **loc:** 101
- **complexity:** low
- **digest:** `sha256:39fef445f75310a2369bb675d7c6ab26b8d99bbf854c767cb8dd4d47425e5df5`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/controller/master/MasterController.java | falo-skeleton/src/main/java/com/falo/server/application/controller/master/MasterController.java | module | falo-skeleton/src/main/java/com/falo/server/application/controller/master/MasterController.java | 36 | yes |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/master/MasterQuery.java | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/master/MasterQuery.java | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/master/MasterQuery.java | 77 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 1 |
| platform-services/aggregate-2 | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 1 |
| platform-services/viewmodel | call | 2 |

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/controller/master/MasterController.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/master/MasterQuery.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/master/model/CountryModel.java`


## platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-3: S3 file upload and download API

S3Controller endpoints and S3ServiceImpl/S3Service for upload, download and signed URLs, with the SPA file client.

- **kind:** module
- **status:** active
- **loc:** 171
- **complexity:** low
- **digest:** `sha256:a832c641402f1076d9f1f9f88131fa4e16d857428cc6729358b594550ec130b3`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/object/S3Service.java | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/object/S3Service.java | module | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/object/S3Service.java | 96 |  |
| falo-skeleton/src/main/java/com/falo/server/application/controller/s3/S3Controller.java | falo-skeleton/src/main/java/com/falo/server/application/controller/s3/S3Controller.java | module | falo-skeleton/src/main/java/com/falo/server/application/controller/s3/S3Controller.java | 27 | yes |
| falo-skeleton/src/main/java/com/falo/server/domain/services/s3/S3ServiceImpl.java | falo-skeleton/src/main/java/com/falo/server/domain/services/s3/S3ServiceImpl.java | module | falo-skeleton/src/main/java/com/falo/server/domain/services/s3/S3ServiceImpl.java | 65 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 1 |
| platform-services/application | call | 3 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 1 |

### Used by

- `platform-services/aggregate-2`

### Files

- `falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/object/S3Service.java`
- `falo-skeleton/src/main/java/com/falo/server/application/controller/s3/S3Controller.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/s3/S3ServiceImpl.java`


## platform-services/falo-skeleton-src-main-java-com-falo-server-domain-aggregate: Mail delivery (Mailgun, Thymeleaf templates)

Outbound mail: Mailgun transport config, Thymeleaf rendering over the 15 templates in src/main/resources/mail, the sent-mail log (SentEmail/SentEmailRepository) and mail template/status constants.

- **kind:** module
- **status:** active
- **loc:** 3215
- **complexity:** high
- **digest:** `sha256:10c5096ea6d037db403f899728a10e8036476a84d542d4e290126826b4a0a19e`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/template/ThymeleafEngine.java | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/template/ThymeleafEngine.java | module | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/template/ThymeleafEngine.java | 57 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/aggregate/mail/SentEmail.java | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/mail/SentEmail.java | module | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/mail/SentEmail.java | 41 |  |
| falo-skeleton/src/main/java/com/falo/server/domain/services/queries/mail/SentEmailQuery.java | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/mail/SentEmailQuery.java | module | falo-skeleton/src/main/java/com/falo/server/domain/services/queries/mail/SentEmailQuery.java | 28 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/aggregate-2 | call | 1 |
| platform-services/config | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 2 |

### Used by

- `platform-services/aggregate-2`

### Parts

| Part | Kind | File |
| --- | --- | --- |
| Mailgun transport config |  | falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/MailgunConfig.java:10 |
| Thymeleaf template rendering |  | falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/template/ThymeleafEngine.java:15 |
| Sent-mail log |  | falo-skeleton/src/main/java/com/falo/server/domain/aggregate/mail/SentEmail.java:20 |
| Account-created mail template |  | falo-skeleton/src/main/resources/mail/account-created.html:1 |

### Files

- `falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/mail/Attachment.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/mail/Email.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/domain/aggregate/mail/Mailer.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/domain/service/template/ThymeleafEngine.java`
- `falo-skeleton/libs/core/src/main/java/com/falo/core/infrastructure/config/MailgunConfig.java`
- `falo-skeleton/src/main/java/com/falo/server/application/constants/MailStatus.java`
- `falo-skeleton/src/main/java/com/falo/server/application/constants/TemplateMail.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/aggregate/mail/SentEmail.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/repositories/mail/SentEmailRepository.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/mail/MailService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/aggregate/mail/SentEmailService.java`
- `falo-skeleton/src/main/java/com/falo/server/domain/services/queries/mail/SentEmailQuery.java`
- `falo-skeleton/src/main/resources/mail/account-created.html`
- `falo-skeleton/src/main/resources/mail/activate-account.html`
- `falo-skeleton/src/main/resources/mail/interview-time-set.html`
- `falo-skeleton/src/main/resources/mail/new-verified-account.html`
- `falo-skeleton/src/main/resources/mail/project-registration-rejected.html`
- `falo-skeleton/src/main/resources/mail/project-registration-verified.html`
- `falo-skeleton/src/main/resources/mail/register-success.html`
- `falo-skeleton/src/main/resources/mail/registration-rejected.html`
- `falo-skeleton/src/main/resources/mail/registration-verified.html`
- `falo-skeleton/src/main/resources/mail/registration-verifying.html`
- `falo-skeleton/src/main/resources/mail/reset-password.html`
- `falo-skeleton/src/main/resources/mail/set-password.html`
- `falo-skeleton/src/main/resources/mail/update-project-registration.html`
- `falo-skeleton/src/main/resources/mail/update-registration.html`
- `falo-skeleton/src/main/resources/mail/volunteer-register-success.html`


## platform-services/falo-unities-src-api-systems-configs: falo-unities/src/api/systems/configs

- **kind:** module
- **status:** active
- **loc:** 34
- **complexity:** low
- **digest:** `sha256:3a07a17329145ee66a39df333f5b0b2789608bf68831914b5b0b3ffea72edc71`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/api/systems/configs | falo-unities/src/api/systems/configs | module | falo-unities/src/api/systems/configs | 39 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/api | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| platform-services/src | call | 1 |

### Used by

- `other/falo-unities-src-store-modules`
- `platform-services/falo-unities-src-hooks-systems-config-index-ts`

### Files

- `falo-unities/src/api/systems/configs/index.ts`
- `falo-unities/src/api/systems/configs/types.ts`


## platform-services/falo-unities-src-components-admin-systems-configs: System configuration and logs admin screens

SystemAdmin console: runtime configuration pages (config tables/forms) and the system-logs (actuator logfile) page with their configs and be-logs API clients.

- **kind:** module
- **status:** active
- **loc:** 201
- **complexity:** low
- **digest:** `sha256:028a0b7700e27e455002c3b8a98824ccef4308ad072a6458605efda4b465bbed`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/components/admin/systems/configs | falo-unities/src/components/admin/systems/configs | module | falo-unities/src/components/admin/systems/configs | 240 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 1 |
| platform-services/src | call | 4 |

### Used by

- `platform-services/systems`

### Files

- `falo-unities/src/api/systems/be-logs/index.ts`
- `falo-unities/src/components/admin/systems/configs/ConfigItemsForm.vue`
- `falo-unities/src/components/admin/systems/configs/ConfigItemsTable.vue`
- `falo-unities/src/components/admin/systems/configs/ConfigsTable.vue`


## platform-services/falo-unities-src-hooks-systems-config-index-ts: falo-unities/src/hooks/systems/config/index.ts

- **kind:** module
- **status:** active
- **loc:** 51
- **complexity:** low
- **digest:** `sha256:28d9fc2f65b1e4a7349d8772e8bba7313768866a56e4507cad6ec1c3a7a30198`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/hooks/systems/config/index.ts | falo-unities/src/hooks/systems/config/index.ts | module | falo-unities/src/hooks/systems/config/index.ts | 56 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/falo-unities-src-api-systems-configs | call | 1 |
| platform-services/src | call | 1 |

### Used by

- `other/falo-unities-src-store-modules`

### Files

- `falo-unities/src/hooks/systems/config/index.ts`


## platform-services/falo-unities-src-router-index-ts: SPA routes and role-based navigation

Vue Router table: role-based back offices (system admin, admin, manager, staff, organization, member, volunteer), the task workspace and the public portal (see parts).

- **kind:** module
- **status:** active
- **loc:** 651
- **complexity:** low
- **digest:** `sha256:d9b6158e1eed5e8575a57d9fb7538db56fc85a2983141c4b0b5e263d2cc93474`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/router/index.ts | falo-unities/src/router/index.ts | module | falo-unities/src/router/index.ts | 679 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/auth-2 | call, dispatch | 6 |
| auth-and-access-control/common | call, dispatch | 4 |
| employee-and-organization-account-administration/falo-unities-src-views-common-employees-employeespage-vue | call, dispatch | 2 |
| employee-and-organization-account-administration/falo-unities-src-views-organization-account-organizationacco | call, dispatch | 2 |
| employee-and-organization-account-administration/falo-unities-src-views-systemadmin-systemaccount-adminaccoun | call, dispatch | 2 |
| employee-and-organization-account-administration/falo-unities-src-views-systemadmin-utilities-usercasepage-vu | call, dispatch | 2 |
| organization-registration-and-verification/falo-unities-src-views-public-registerpage-organizationregis | call, dispatch | 2 |
| organization-registration-and-verification/organizations | call, dispatch | 4 |
| organization-registration-and-verification/statuspage | call, dispatch | 6 |
| other/error | call, dispatch | 6 |
| other/falo-unities-src-views-common-dashboard-dashboardpage-vue | call, dispatch | 4 |
| other/falo-unities-src-views-public-homepage-homepage-vue | call, dispatch | 2 |
| other/introducepage | call, dispatch | 16 |
| other/layout | call, dispatch | 4 |
| other/utilities | call, dispatch | 4 |
| platform-services/src | call | 2 |
| platform-services/systems | call, dispatch | 4 |
| project-registration-and-verification/falo-unities-src-views-organization-projects-registerproject | call, dispatch | 2 |
| project-registration-and-verification/projects | call, dispatch | 4 |
| project-workspace-and-task-management/task-3 | call, dispatch | 16 |
| publication-and-public-portal/falo-unities-src-views-organization-profile-organization | call, dispatch | 2 |
| publication-and-public-portal/projectpage | call, dispatch | 4 |
| publication-and-public-portal/publication-2 | call, dispatch | 6 |
| volunteer-recruitment-and-interviews/campaignpage | call, dispatch | 2 |
| volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-dashboard-memberor | call, dispatch | 2 |
| volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-recruitment-volunt | call, dispatch | 2 |
| volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-dashboard-volunteerdashboar | call, dispatch | 2 |
| volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-profile-volunteerprofilepag | call, dispatch | 2 |
| volunteer-recruitment-and-interviews/volunteer-3 | call, dispatch | 6 |

### Used by

- `other/error`
- `other/falo-unities-src`
- `volunteer-recruitment-and-interviews/volunteer-3`

### Parts

| Part | Kind | File |
| --- | --- | --- |
| System admin routes |  | falo-unities/src/router/index.ts:81 |
| Manager back office routes |  | falo-unities/src/router/index.ts:166 |
| Task workspace routes |  | falo-unities/src/router/index.ts:398 |
| Public portal routes |  | falo-unities/src/router/index.ts:471 |

### Files

- `falo-unities/src/router/index.ts`


## platform-services/falo-unities-src-store-modules-master-master-ts: SPA master address data (client, store)

Master Pinia store, api/master client and its response hooks for address selects.

- **kind:** module
- **status:** active
- **loc:** 51
- **complexity:** low
- **digest:** `sha256:2fe01b3fd09cba38df76a7d342c31c1d9cc453e589d114fd8120771d3a733953`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/store/modules/master/master.ts | falo-unities/src/store/modules/master/master.ts | module | falo-unities/src/store/modules/master/master.ts | 33 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| platform-services/src | call | 1 |

### Used by

- `organization-registration-and-verification/falo-unities-src-views-public-registerpage-organizationregis`
- `other/elements`

### Files

- `falo-unities/src/api/master/index.ts`
- `falo-unities/src/api/master/types.ts`
- `falo-unities/src/hooks/master/index.ts`
- `falo-unities/src/store/modules/master/master.ts`


## platform-services/infrastructure-2: Backend application configuration

Spring Boot bootstrap (Application.java), application.yml and logging resources, web security config, cached ConfigHelper, scheduling and security helpers.

- **kind:** module
- **status:** active
- **loc:** 369
- **complexity:** low
- **digest:** `sha256:fe534fd9c09be1eb0ffef17ba79397bde520c38e3e41f2efc7184cb3ae38a42e`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/infrastructure/config | falo-skeleton/src/main/java/com/falo/server/infrastructure/config | module | falo-skeleton/src/main/java/com/falo/server/infrastructure/config | 94 |  |
| falo-skeleton/src/main/java/com/falo/server/infrastructure/helper | falo-skeleton/src/main/java/com/falo/server/infrastructure/helper | module | falo-skeleton/src/main/java/com/falo/server/infrastructure/helper | 185 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-domain-services | call | 1 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-infrastructure-s | call | 2 |
| organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| platform-services/application | call | 1 |
| platform-services/config | call | 2 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cons | call | 1 |
| platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-application-view | call | 1 |
| project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-aggregate | call | 2 |

### Used by

- `auth-and-access-control/auth`
- `employee-and-organization-account-administration/account`
- `employee-and-organization-account-administration/commands`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-4`
- `employee-and-organization-account-administration/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `notifications-and-realtime/falo-skeleton-src-main-java-com-falo-server-application-even`
- `organization-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `organization-registration-and-verification/organization-register`
- `platform-services/aggregate-2`
- `project-registration-and-verification/falo-skeleton-src-main-java-com-falo-server-domain-services-2`
- `project-registration-and-verification/project-register`
- `project-workspace-and-task-management/comment-and-attachment-command-handlers`
- `project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-domain-services-6`
- `project-workspace-and-task-management/task`
- `publication-and-public-portal/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `volunteer-recruitment-and-interviews/falo-skeleton-src-main-java-com-falo-server-domain-services-3`
- `volunteer-recruitment-and-interviews/volunteer`

### Files

- `falo-skeleton/src/main/java/com/falo/server/infrastructure/config/SpringSecurityAuditorAware.java`
- `falo-skeleton/src/main/java/com/falo/server/infrastructure/config/WebSecurityConfig.java`
- `falo-skeleton/src/main/java/com/falo/server/infrastructure/helper/ConfigHelper.java`
- `falo-skeleton/src/main/java/com/falo/server/infrastructure/helper/ScheduleHelper.java`
- `falo-skeleton/src/main/java/com/falo/server/infrastructure/helper/SecurityHelper.java`
- `falo-skeleton/src/main/resources/application.yml`
- `falo-skeleton/src/main/resources/banner.txt`
- `falo-skeleton/src/main/resources/logback-spring.xml`


## platform-services/src: SPA shared models, constants and plugins

Shared TypeScript domain models, role/status/priority/date constants, and the i18n and file plugins.

- **kind:** module
- **status:** active
- **loc:** 1642
- **complexity:** high
- **digest:** `sha256:46981216440798fa0199f978ca89e18c3618d82047f0c71a88604986954641ec`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/constants | falo-unities/src/constants | module | falo-unities/src/constants | 611 |  |
| falo-unities/src/constants/components | falo-unities/src/constants/components | module | falo-unities/src/constants/components | 76 |  |
| falo-unities/src/constants/layout | falo-unities/src/constants/layout | module | falo-unities/src/constants/layout | 54 |  |
| falo-unities/src/models | falo-unities/src/models | module | falo-unities/src/models | 598 |  |
| falo-unities/src/models/cycle | falo-unities/src/models/cycle | module | falo-unities/src/models/cycle | 276 |  |
| falo-unities/src/models/format/useFormat.ts | falo-unities/src/models/format/useFormat.ts | module | falo-unities/src/models/format/useFormat.ts | 90 |  |
| falo-unities/src/models/master | falo-unities/src/models/master | module | falo-unities/src/models/master | 26 |  |
| falo-unities/src/models/task | falo-unities/src/models/task | module | falo-unities/src/models/task | 34 |  |
| falo-unities/src/models/utilities | falo-unities/src/models/utilities | module | falo-unities/src/models/utilities | 18 |  |
| falo-unities/src/plugins | falo-unities/src/plugins | module | falo-unities/src/plugins | 49 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 1 |

### Used by

- `auth-and-access-control/api`
- `auth-and-access-control/auth-2`
- `auth-and-access-control/common`
- `auth-and-access-control/falo-unities-src-components-auth-changepasswordform-vue`
- `employee-and-organization-account-administration/api`
- `employee-and-organization-account-administration/falo-unities-src-components-admin-account`
- `employee-and-organization-account-administration/falo-unities-src-components-organizations-account-organi`
- `employee-and-organization-account-administration/falo-unities-src-hooks-employee-index-ts`
- `employee-and-organization-account-administration/falo-unities-src-hooks-organizations-accounts-index-ts`
- `employee-and-organization-account-administration/falo-unities-src-hooks-system-accounts-index-ts`
- `employee-and-organization-account-administration/falo-unities-src-views-common-employees-employeespage-vue`
- `employee-and-organization-account-administration/falo-unities-src-views-organization-account-organizationacco`
- `employee-and-organization-account-administration/falo-unities-src-views-systemadmin-systemaccount-adminaccoun`
- `employee-and-organization-account-administration/falo-unities-src-views-systemadmin-utilities-usercasepage-vu`
- `notifications-and-realtime/falo-unities-src-socket`
- `organization-registration-and-verification/falo-unities-src-hooks-organizations-register-index-ts`
- `organization-registration-and-verification/falo-unities-src-views-public-registerpage-organizationregis`
- `organization-registration-and-verification/organization`
- `organization-registration-and-verification/organizations`
- `other/elements`
- `other/error`
- `other/falo-unities-src`
- `other/falo-unities-src-store-modules`
- `other/falo-unities-src-views-public-homepage-homepage-vue`
- `other/introducepage`
- `other/layout`
- `other/modules`
- `other/utilities`
- `platform-services/falo-unities-src-api-systems-configs`
- `platform-services/falo-unities-src-components-admin-systems-configs`
- `platform-services/falo-unities-src-hooks-systems-config-index-ts`
- `platform-services/falo-unities-src-router-index-ts`
- `platform-services/falo-unities-src-store-modules-master-master-ts`
- `platform-services/systems`
- `platform-services/utilities`
- `project-registration-and-verification/falo-unities-src-components-organizations-dialog-attacho`
- `project-registration-and-verification/falo-unities-src-components-projects-approval-request-at`
- `project-registration-and-verification/falo-unities-src-components-projects-approval-request-me`
- `project-registration-and-verification/falo-unities-src-views-organization-projects-registerproject`
- `project-registration-and-verification/projects`
- `project-registration-and-verification/projects-2`
- `project-workspace-and-task-management/falo-unities-src-api-cycle`
- `project-workspace-and-task-management/falo-unities-src-hooks-projects-index-ts`
- `project-workspace-and-task-management/falo-unities-src-hooks-task-labels-index-ts`
- `project-workspace-and-task-management/falo-unities-src-hooks-task-sidebar-cycle-index-ts`
- `project-workspace-and-task-management/falo-unities-src-hooks-task-states-index-ts`
- `project-workspace-and-task-management/falo-unities-src-store-modules-task`
- `project-workspace-and-task-management/page`
- `project-workspace-and-task-management/project-2`
- `project-workspace-and-task-management/task-2`
- `project-workspace-and-task-management/task-3`
- `publication-and-public-portal/falo-unities-src-api-publication`
- `publication-and-public-portal/falo-unities-src-components-public-feedback-projectfeedb`
- `publication-and-public-portal/falo-unities-src-views-organization-profile-organization`
- `publication-and-public-portal/projectpage`
- `publication-and-public-portal/publication-2`
- `volunteer-recruitment-and-interviews/falo-unities-src-components-common-layout-profile-dialog`
- `volunteer-recruitment-and-interviews/falo-unities-src-components-public-recruitment-publicrecruit`
- `volunteer-recruitment-and-interviews/falo-unities-src-views-memberorganization-recruitment-volunt`
- `volunteer-recruitment-and-interviews/falo-unities-src-views-volunteer-profile-volunteerprofilepag`
- `volunteer-recruitment-and-interviews/volunteer-2`
- `volunteer-recruitment-and-interviews/volunteer-3`

### Files

- `falo-unities/src/constants/InterviewStatus.ts`
- `falo-unities/src/constants/achievementType.ts`
- `falo-unities/src/constants/auth.ts`
- `falo-unities/src/constants/components/loading.ts`
- `falo-unities/src/constants/components/notification.ts`
- `falo-unities/src/constants/components/progress.ts`
- `falo-unities/src/constants/date.ts`
- `falo-unities/src/constants/gender.ts`
- `falo-unities/src/constants/layout/contactInformation.ts`
- `falo-unities/src/constants/layout/copyright.ts`
- `falo-unities/src/constants/layout/redirect.ts`
- `falo-unities/src/constants/layout/responsive.ts`
- `falo-unities/src/constants/oAuthTypes.ts`
- `falo-unities/src/constants/organizationFeedbackType.ts`
- `falo-unities/src/constants/organizationStatus.ts`
- `falo-unities/src/constants/organizationType.ts`
- `falo-unities/src/constants/pagination.ts`
- `falo-unities/src/constants/priorityTypes.ts`
- `falo-unities/src/constants/projectBoardRole.ts`
- `falo-unities/src/constants/publicProjectStatus.ts`
- `falo-unities/src/constants/role.ts`
- `falo-unities/src/constants/status.ts`
- `falo-unities/src/constants/storage.ts`
- `falo-unities/src/constants/taskState.ts`
- `falo-unities/src/constants/validation-response.ts`
- `falo-unities/src/constants/validations.ts`
- `falo-unities/src/constants/visitor/visitorProjectStatus.ts`
- `falo-unities/src/models/Account.ts`
- `falo-unities/src/models/BaseModel.ts`
- `falo-unities/src/models/Config.ts`
- `falo-unities/src/models/Customer.ts`
- `falo-unities/src/models/Cycle.ts`
- `falo-unities/src/models/Employee.ts`
- `falo-unities/src/models/InterviewFeedbackHistory.ts`
- `falo-unities/src/models/Notification.ts`
- `falo-unities/src/models/Organization.ts`
- `falo-unities/src/models/OrganizationAccount.ts`
- `falo-unities/src/models/Pagination.ts`
- `falo-unities/src/models/Project.ts`
- `falo-unities/src/models/Publication.ts`
- `falo-unities/src/models/Role.ts`
- `falo-unities/src/models/Volunteer.ts`
- `falo-unities/src/models/VolunteerAccount.ts`
- `falo-unities/src/models/VolunteerRecruitment.ts`
- `falo-unities/src/models/VolunteerRegister.ts`
- `falo-unities/src/models/cycle/Cycle.ts`
- `falo-unities/src/models/cycle/Page.ts`
- `falo-unities/src/models/cycle/useDialog.ts`
- `falo-unities/src/models/cycle/useLoading.ts`
- `falo-unities/src/models/format/useFormat.ts`
- `falo-unities/src/models/interview/InterviewCalendarModel.ts`
- `falo-unities/src/models/master/Address.ts`
- `falo-unities/src/models/master/Country.ts`
- `falo-unities/src/models/task/ProjectCycle.ts`
- `falo-unities/src/models/task/ProjectSidebar.ts`
- `falo-unities/src/models/task/ProjectState.ts`
- `falo-unities/src/models/task/TaskLabel.ts`
- `falo-unities/src/models/utilities/ProjectTags.ts`
- `falo-unities/src/models/utilities/ProjectTypes.ts`
- `falo-unities/src/models/utilities/UserCase.ts`
- `falo-unities/src/models/visitor/VisitorCampaign.ts`
- `falo-unities/src/plugins/file.ts`
- `falo-unities/src/plugins/i18n.ts`


## platform-services/systems: Systems (2 leaves)

- **kind:** module
- **status:** active
- **loc:** 129
- **complexity:** low
- **digest:** `sha256:01d6e469dab0cfc5afce7408fcedc6d72a6ea2e1442d936e6021480b7c6d8464`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/views/SystemAdmin/Systems/AdminConfigPage.vue | falo-unities/src/views/SystemAdmin/Systems/AdminConfigPage.vue | screen | falo-unities/src/views/SystemAdmin/Systems/AdminConfigPage.vue | 110 | yes |
| falo-unities/src/views/SystemAdmin/Systems/SystemLogsPage.vue | falo-unities/src/views/SystemAdmin/Systems/SystemLogsPage.vue | screen | falo-unities/src/views/SystemAdmin/Systems/SystemLogsPage.vue | 50 | yes |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| other/falo-unities-src-store-modules | call | 2 |
| platform-services/falo-unities-src-components-admin-systems-configs | call | 1 |
| platform-services/src | call | 2 |

### Used by

- `platform-services/falo-unities-src-router-index-ts`

### Files

- `falo-unities/src/views/SystemAdmin/Systems/AdminConfigPage.vue`
- `falo-unities/src/views/SystemAdmin/Systems/SystemLogsPage.vue`


## platform-services/utilities: SPA dictionary API clients and hooks

Typed clients and hooks for project tags, types and user-case lists (hooks/customer references an api/customer module that does not exist — dead code).

- **kind:** module
- **status:** active
- **loc:** 147
- **complexity:** low
- **digest:** `sha256:3442365e65b27f9d41ed2794117db05fd10bc454226e09bb77f8743f1e19ad4f`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-unities/src/api/utilities/project-tags | falo-unities/src/api/utilities/project-tags | module | falo-unities/src/api/utilities/project-tags | 25 |  |
| falo-unities/src/api/utilities/project-types | falo-unities/src/api/utilities/project-types | module | falo-unities/src/api/utilities/project-types | 25 |  |
| falo-unities/src/api/utilities/user-case | falo-unities/src/api/utilities/user-case | module | falo-unities/src/api/utilities/user-case | 22 |  |
| falo-unities/src/hooks/customer/index.ts | falo-unities/src/hooks/customer/index.ts | module | falo-unities/src/hooks/customer/index.ts | 37 |  |
| falo-unities/src/hooks/utilities/project_tags/index.ts | falo-unities/src/hooks/utilities/project_tags/index.ts | module | falo-unities/src/hooks/utilities/project_tags/index.ts | 19 |  |
| falo-unities/src/hooks/utilities/project_types/index.ts | falo-unities/src/hooks/utilities/project_types/index.ts | module | falo-unities/src/hooks/utilities/project_types/index.ts | 19 |  |
| falo-unities/src/hooks/utilities/user-case/index.ts | falo-unities/src/hooks/utilities/user-case/index.ts | module | falo-unities/src/hooks/utilities/user-case/index.ts | 20 |  |

### Depends on

| Item | Kinds | Edges |
| --- | --- | --- |
| auth-and-access-control/api | call | 3 |
| auth-and-access-control/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 1 |
| platform-services/src | call | 6 |
| project-workspace-and-task-management/falo-skeleton-src-main-java-com-falo-server-application-cont | call | 2 |

### Used by

- `other/falo-unities-src-store-modules`

### Files

- `falo-unities/src/api/utilities/project-tags/index.ts`
- `falo-unities/src/api/utilities/project-tags/types.ts`
- `falo-unities/src/api/utilities/project-types/index.ts`
- `falo-unities/src/api/utilities/project-types/types.ts`
- `falo-unities/src/api/utilities/user-case/index.ts`
- `falo-unities/src/api/utilities/user-case/types.ts`
- `falo-unities/src/hooks/customer/index.ts`
- `falo-unities/src/hooks/utilities/project_tags/index.ts`
- `falo-unities/src/hooks/utilities/project_types/index.ts`
- `falo-unities/src/hooks/utilities/user-case/index.ts`


## platform-services/viewmodel: Configuration and master-data response models

View models returned by the configuration and master-data endpoints (ListConfigsVM, SaveConfigsVM, Country/District/Province/Ward VMs).

- **kind:** module
- **status:** active
- **loc:** 102
- **complexity:** low
- **digest:** `sha256:4253b0583505412df74ee0a7cf85805d76894021b71cb7b6e752da1e604b6c28`
- **aliases:**

### Leaves

| Leaf | Name | Kind | File | LOC | Entry point |
| --- | --- | --- | --- | --- | --- |
| falo-skeleton/src/main/java/com/falo/server/application/viewmodel/configs | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/configs | module | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/configs | 70 |  |
| falo-skeleton/src/main/java/com/falo/server/application/viewmodel/master | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/master | module | falo-skeleton/src/main/java/com/falo/server/application/viewmodel/master | 52 |  |

### Used by

- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont`
- `platform-services/falo-skeleton-src-main-java-com-falo-server-application-cont-2`

### Files

- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/configs/ListConfigsVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/configs/SaveConfigsVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/master/CountryVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/master/DistrictVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/master/ProvinceVM.java`
- `falo-skeleton/src/main/java/com/falo/server/application/viewmodel/master/WardVM.java`
