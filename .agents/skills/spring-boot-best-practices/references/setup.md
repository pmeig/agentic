# Spring Boot best practices: principles and project setup

- **Use Spring's own extension points before writing anything by hand**: customizers (`WebMvcConfigurer`, `RestClientCustomizer`,
  `JsonMapperBuilderCustomizer`, `OpenApiCustomizer`), `ResponseEntityExceptionHandler` + `ProblemDetail`, `AuditorAware`,
  `PasswordEncoder`, `HandlerMethodArgumentResolver`. If a request goes against a native mechanism, say so and propose it.
- Spring Boot 4 / Framework 7: Java 25 recommended, Jackson 3 (`tools.jackson.*`), JSpecify null-safety (`@NullMarked` packages),
  modular starters, built-in API versioning (`spring.mvc.apiversion.*`), HTTP service clients (`@HttpExchange` interfaces +
  `@ImportHttpServices`) instead of Feign/hand-written `RestTemplate`, native resilience (`@Retryable`, `@ConcurrencyLimit`,
  `@EnableResilientMethods` from `org.springframework.resilience`), OpenTelemetry starter for traces/metrics.
- Store Spring Boot configuration in YAML only: use `application.yaml` and `application-<profile>.yaml`; do not use `.properties` configuration files. Keep profiles per environment and load secrets from Vault (Spring Cloud Vault / env), never from the repository.

Language rules: `java-best-practices` / `kotlin-best-practices`.
