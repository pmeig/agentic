---
name: php-best-practices
description: "MANDATORY for any PHP code (Symfony, Laravel, plain): strict types, layered by feature, DI, readonly/enums, PHPStan max, PHPUnit, PHP 8.5."
---
# PHP best practices (router)
Idiomatic PHP transposing the team's layering conventions; the project's own rules win. Load only the row(s) that match the task; never load every reference.

## Need -> file
| Need (what the agent is doing) | Load |
|---|---|
| Creating a project / Composer, PHP version, tooling, framework | `references/setup.md` |
| Layering, injection, naming | `references/structure.md` |
| Types, DTOs, error handling | `references/code.md` |
| Data access, configuration, logging | `references/config-data.md` |
| Writing or reviewing unit tests (PHPUnit / Pest) | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
