---
name: vue-best-practices
description: "MANDATORY for any Vue code (Vue 3, Nuxt): pages/ and core/, script setup + TypeScript, composables, Pinia, typed API layer, Vitest, Vue 3.5+."
---

# Vue best practices (router)

The user has no Vue project yet: these rules transpose the team's Angular conventions (`angular-best-practices`,
`typescript-best-practices`, `ui-responsive-accessible-modular`) to Vue 3.

Load only the row(s) that match the task; never every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Creating a module / tooling, versions, layout | `references/setup.md` |
| Writing or reviewing code | `references/code.md` |
| Writing or reviewing unit tests | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
