# Spring Boot best practices: reusable libraries (starters)

- One module per concern (`spring-<module>`, artifact versioned by property), no business logic, modules independent unless strictly needed; third-party integrations `optional` + `@ConditionalOnClass`.
- Register `@AutoConfiguration` classes in `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`; every bean `@ConditionalOnMissingBean` so the consumer can replace it; servlet/reactive variants with `@ConditionalOnWebApplication(type = SERVLET|REACTIVE)`; a module switch `@ConditionalOnBooleanProperty(prefix = "spring.plugins.pmeig", name = ["<module>"], matchIfMissing = true)`.
- Every web feature has its reactive twin (`Xxx` / `ReactiveXxx`) when the library supports both stacks.
- Test auto-configurations with `ApplicationContextRunner` / `WebApplicationContextRunner` (conditions on and off).
