# Spring Boot best practices: data (JPA, transactions, schema)

- Spring Data JPA: entities extend the user's `@MappedSuperclass` bases (id + audit columns `created_by`, `created`, `updated_by`, `updated`) with `@EntityListeners(AuditingEntityListener::class)` and `@EnableJpaAuditing`; equals/hashCode on the id; `FetchType.LAZY` by default, fetch joins / entity graphs against N+1; `open-in-view: false`.
- Read-only transactions `@Transactional(readOnly = true)` on queries, write transactions on the service method; never call a `@Transactional` method from the same bean expecting a proxy.
- Schema with Flyway or Liquibase migrations (never `ddl-auto: update` outside a sandbox); SQL rules: `sql-best-practices`.
