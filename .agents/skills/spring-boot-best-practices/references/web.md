# Spring Boot best practices: web, errors, security, logging

- Errors: exception tree `TechnicalException(code)` → `BusinessException(code)`; one `@RestControllerAdvice` extending `ResponseEntityExceptionHandler` returning RFC 9457 `ProblemDetail` (`title`, `type`, `instance`, extra `errors` property); never return an exception object or a stack trace.
- REST: nouns and HTTP verbs, 201 + `Location` on create, 204 on delete, pagination with `Pageable`, versioning with the built-in API versioning, OpenAPI with springdoc (tags cleaned by an `OpenApiCustomizer`).
- Security: one `SecurityFilterChain` bean, stateless JWT or cookie per property, method security via annotations, CSRF on for cookie sessions, CORS explicit, passwords with `DelegatingPasswordEncoder`, secrets/keys never logged.
- Logging: SLF4J with placeholders, a correlation id in the MDC (filter + client interceptors), no `println`, no personal data in logs.
