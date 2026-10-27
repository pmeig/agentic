# Spring Boot best practices: application layering and structure

- `controller` (web: DTOs, validation `@Valid`, status codes) → `service` (business rules, `@Transactional` boundaries) → `repository` (Spring Data) → entities. A controller never touches a repository; a service never sees `HttpServletRequest`/`ServerWebExchange`.
- Package by feature (`order/`, `customer/`), each with its controller/service/repository/dto; shared code in `core/` or `common/`.
- DTOs (records) at the edge, mapped explicitly (or MapStruct) to entities; never expose entities in the API.
- Validation with Jakarta Bean Validation on DTOs and `@Validated` on `@ConfigurationProperties`; fail fast at startup on missing config.
