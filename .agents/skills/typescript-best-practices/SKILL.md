---
name: typescript-best-practices
description: "MANDATORY for any .ts/.js, tsconfig or package.json: strict ESM, no enums, satisfies, undefined over null, Vitest, TypeScript 7."
---
# TypeScript / JavaScript best practices (router)
Strict ESM TypeScript conventions; the project's own rules win. Load only the row(s) that match the task; never load every reference.
Related: Angular `angular-best-practices`; SQL `sql-best-practices`.

## Need -> file
| Need (what the agent is doing) | Load |
|---|---|
| Creating a module / tooling, tsconfig, build and dependencies | `references/setup.md` |
| Writing or reviewing code: types, errors, async, naming | `references/code.md` |
| Publishing a library or monorepo module (exports, versions) | `references/libraries.md` |
| Writing or reviewing unit tests (Vitest) | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
