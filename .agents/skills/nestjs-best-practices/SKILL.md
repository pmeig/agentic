---
name: nestjs-best-practices
description: MANDATORY for any NestJS code: module per feature, DTO validation, typed ConfigModule with Vault, exception filters.
---

# NestJS best practices (router)

NestJS is the decorator-based way of building layered MVC: controller → service → repository → infrastructure client, no repository access in a controller, no framework object in a service. Follow that layering and `typescript-best-practices` for the language. These rules adapt it to Nest.

Load only the row(s) that match the task; never every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Creating a module / tooling, versions, layout | `references/setup.md` |
| Writing or reviewing code | `references/code.md` |
| Writing or reviewing unit tests | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
