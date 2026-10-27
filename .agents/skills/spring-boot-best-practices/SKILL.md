---
name: spring-boot-best-practices
description: "MANDATORY for any Spring Boot code (Java/Kotlin): Spring Boot 4, @ConfigurationProperties, constructor injection, ProblemDetail, JPA auditing."
---
# Spring Boot best practices (router)
Spring Boot 4 practice; the project's own rules win. Language rules: `java-best-practices` / `kotlin-best-practices`. Load only the row(s) that match the task; never load every reference.
## Need -> file
| Need (what the agent is doing) | Load |
|---|---|
| New Spring Boot app/module, Boot 4 baseline, extension points, YAML config files | `references/setup.md` |
| Layering, package by feature, DTOs, validation | `references/structure.md` |
| Beans, `@ConfigurationProperties`, strategy pattern | `references/config.md` |
| Reusable library / starter / auto-configuration | `references/starters.md` |
| Controllers, REST, errors (`ProblemDetail`), security, logging | `references/web.md` |
| JPA, auditing, transactions, Flyway/Liquibase | `references/data.md` |
| Writing or reviewing tests (slices, parameterized) | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
