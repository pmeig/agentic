---
name: spring-boot-best-practices
description: MANDATORY for any Spring Boot code (Java/Kotlin): Spring Boot 4, @ConfigurationProperties, constructor injection, ProblemDetail, JPA auditing.
---

# Spring Boot best practices

Based on Spring Boot 4 practice. Language rules: `java-best-practices` / `kotlin-best-practices`.

## 1. Principles

- **Use Spring's own extension points before writing anything by hand**: customizers (`WebMvcConfigurer`, `RestClientCustomizer`,
  `JsonMapperBuilderCustomizer`, `OpenApiCustomizer`), `ResponseEntityExceptionHandler` + `ProblemDetail`, `AuditorAware`,
  `PasswordEncoder`, `HandlerMethodArgumentResolver`. If a request goes against a native mechanism, say so and propose it.
- Spring Boot 4 / Framework 7: Java 25 recommended, Jackson 3 (`tools.jackson.*`), JSpecify null-safety (`@NullMarked` packages),
  modular starters, built-in API versioning (`spring.mvc.apiversion.*`), HTTP service clients (`@HttpExchange` interfaces +
  `@ImportHttpServices`) instead of Feign/hand-written `RestTemplate`, native resilience (`@Retryable`, `@ConcurrencyLimit`,
  `@EnableResilientMethods` from `org.springframework.resilience`), OpenTelemetry starter for traces/metrics.
- Store Spring Boot configuration in YAML only: use `application.yaml` and `application-<profile>.yaml`; do not use `.properties` configuration files. Keep profiles per environment and load secrets from Vault (Spring Cloud Vault / env), never from the repository.

## 2. Application layering

- `controller` (web: DTOs, validation `@Valid`, status codes) → `service` (business rules, `@Transactional` boundaries) → `repository` (Spring Data) → entities. A controller never touches a repository; a service never sees `HttpServletRequest`/`ServerWebExchange`.
- Package by feature (`order/`, `customer/`), each with its controller/service/repository/dto; shared code in `core/` or `common/`.
- DTOs (records) at the edge, mapped explicitly (or MapStruct) to entities; never expose entities in the API.
- Validation with Jakarta Bean Validation on DTOs and `@Validated` on `@ConfigurationProperties`; fail fast at startup on missing config.

## 3. Beans and configuration

- Constructor injection only (Lombok `@RequiredArgsConstructor` / Kotlin primary constructor), no field `@Autowired`, no `@Value` scattered: one `@ConfigurationProperties` class per concern, prefix `spring.<module>.pmeig.*` for the user's libraries, defaults in the class, documented by the configuration processor.
- Strategy pattern: inject `List<Strategy>` ordered with `@Order` and fold/iterate, choose an implementation with `@ConditionalOnProperty(havingValue = ...)`; no if/else on configuration.
- Composed meta-annotations (`@AliasFor`) for repeated annotation sets (`@Get` = `@RequestMapping` + `@Operation`).

## 4. Reusable libraries (starters)

- One module per concern (`spring-<module>`, artifact versioned by property), no business logic, modules independent unless strictly needed; third-party integrations `optional` + `@ConditionalOnClass`.
- Register `@AutoConfiguration` classes in `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`; every bean `@ConditionalOnMissingBean` so the consumer can replace it; servlet/reactive variants with `@ConditionalOnWebApplication(type = SERVLET|REACTIVE)`; a module switch `@ConditionalOnBooleanProperty(prefix = "spring.plugins.pmeig", name = ["<module>"], matchIfMissing = true)`.
- Every web feature has its reactive twin (`Xxx` / `ReactiveXxx`) when the library supports both stacks.
- Test auto-configurations with `ApplicationContextRunner` / `WebApplicationContextRunner` (conditions on and off).

## 5. Web, errors, security

- Errors: exception tree `TechnicalException(code)` → `BusinessException(code)`; one `@RestControllerAdvice` extending `ResponseEntityExceptionHandler` returning RFC 9457 `ProblemDetail` (`title`, `type`, `instance`, extra `errors` property); never return an exception object or a stack trace.
- REST: nouns and HTTP verbs, 201 + `Location` on create, 204 on delete, pagination with `Pageable`, versioning with the built-in API versioning, OpenAPI with springdoc (tags cleaned by an `OpenApiCustomizer`).
- Security: one `SecurityFilterChain` bean, stateless JWT or cookie per property, method security via annotations, CSRF on for cookie sessions, CORS explicit, passwords with `DelegatingPasswordEncoder`, secrets/keys never logged.
- Logging: SLF4J with placeholders, a correlation id in the MDC (filter + client interceptors), no `println`, no personal data in logs.

## 6. Data

- Spring Data JPA: entities extend the user's `@MappedSuperclass` bases (id + audit columns `created_by`, `created`, `updated_by`, `updated`) with `@EntityListeners(AuditingEntityListener::class)` and `@EnableJpaAuditing`; equals/hashCode on the id; `FetchType.LAZY` by default, fetch joins / entity graphs against N+1; `open-in-view: false`.
- Read-only transactions `@Transactional(readOnly = true)` on queries, write transactions on the service method; never call a `@Transactional` method from the same bean expecting a proxy.
- Schema with Flyway or Liquibase migrations (never `ddl-auto: update` outside a sandbox); SQL rules: `sql-best-practices`.

## 7. Tests

- Unit tests without Spring (language skills: `@Nested` per public method, `should_..._when_...`).
- Slices: `@WebMvcTest` + `MockMvcTester`/`RestTestClient`, `@DataJpaTest` with Testcontainers (`@ServiceConnection`), `@SpringBootTest` only for end-to-end wiring (`*IT`, failsafe). `@MockitoBean` instead of the removed `@MockBean`.
- Test error and validation paths, not only 200, and one test of the security rules per endpoint family.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `@ParameterizedTest` (`@MethodSource`, `@CsvSource`, `@EnumSource`), also for controller validation cases with `MockMvcTester`. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the official sources, update only internet-derived guidance, keep user/project rules, add source URLs, update this date, report changes.
