# SQL and NoSQL best practices: migrations

Based on PostgreSQL practice (SQL migrations with node-pg-migrate, Flyway or Liquibase; JPA for Spring) and current practice. Data access layering: controller → service → repository (see `spring-boot-best-practices` for Spring).

- Numbered files `NNN_snake_case_topic.sql` (or the tool's format: Flyway `V<n>__topic.sql`, node-pg-migrate), applied in order with a lock (`advisoryLockMode: 'wait'`) so several instances can start together; history table in a `config` schema.
- **An applied migration is never edited**: add a new one. Forward-only in production; a destructive change is split (add, back-fill, switch code, drop later).
- Header on every file: `-- NNN_name: one-line purpose`, then `--` lines on the design choices (why no FK, what NULL means, how existing rows are back-filled).
- Test a migration on a copy of the production data before merging when it rewrites rows or adds constraints; large tables: `CREATE INDEX CONCURRENTLY`, batched updates.
