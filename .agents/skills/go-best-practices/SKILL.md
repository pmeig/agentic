---
name: go-best-practices
description: "MANDATORY for any Go code (HTTP APIs, CLIs, workers): layered by feature, small interfaces, wrapped errors, context, table-driven tests, Go 1.25+."
---
# Go best practices (router)
Idiomatic Go transposing the team's layering conventions; the project's own rules win. Load only the row(s) that match the task; never load every reference.

## Need -> file
| Need (what the agent is doing) | Load |
|---|---|
| Creating a module / go.mod, layout, tooling, containers | `references/setup.md` |
| Layering, injection, interfaces, naming | `references/structure.md` |
| Errors, context, concurrency, HTTP handlers | `references/code.md` |
| Configuration, logging, SQL | `references/config-data.md` |
| Writing or reviewing unit tests | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
