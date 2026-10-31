---
name: svelte-best-practices
description: "MANDATORY for any Svelte or SvelteKit code: Svelte 5 runes, .svelte.ts state, snippets, load functions and form actions, Vitest."
---

# Svelte best practices (router)

The user has no Svelte project yet: these rules transpose the team's front-end conventions (`typescript-best-practices`,
`ui-responsive-accessible-modular`) to Svelte 5 / SvelteKit.

Load only the row(s) that match the task; never every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Creating a module / tooling, versions, layout | `references/setup.md` |
| Writing or reviewing code | `references/code.md` |
| Writing or reviewing unit tests | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
