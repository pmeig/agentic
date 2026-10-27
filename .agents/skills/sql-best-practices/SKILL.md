---
name: sql-best-practices
description: "MANDATORY for any schema, migration or query (PostgreSQL first) and SQL vs NoSQL choices: numbered migrations, constraints, indexes, transactions."
---
# SQL and NoSQL best practices (router)
PostgreSQL-first practice; the project's own rules win. Layering: controller → service → repository (Spring: `spring-boot-best-practices`). Load only the row(s) that match the task; never load every reference.
## Need -> file
| Need (what the agent is doing) | Load |
|---|---|
| Writing a migration, migration tooling | `references/migrations.md` |
| Designing tables, types, constraints, indexes, audit columns | `references/data.md` |
| Writing or reviewing queries, pagination, search | `references/queries.md` |
| Transactions, isolation, idempotent writes | `references/transactions.md` |
| Choosing a NoSQL store (MongoDB, Redis, ...) | `references/nosql.md` |
| Monthly refresh, sources | `references/maintenance.md` |
