# Spring Boot best practices: beans and configuration

- Constructor injection only (Lombok `@RequiredArgsConstructor` / Kotlin primary constructor), no field `@Autowired`, no `@Value` scattered: one `@ConfigurationProperties` class per concern, prefix `spring.<module>.pmeig.*` for the user's libraries, defaults in the class, documented by the configuration processor.
- Strategy pattern: inject `List<Strategy>` ordered with `@Order` and fold/iterate, choose an implementation with `@ConditionalOnProperty(havingValue = ...)`; no if/else on configuration.
- Composed meta-annotations (`@AliasFor`) for repeated annotation sets (`@Get` = `@RequestMapping` + `@Operation`).
