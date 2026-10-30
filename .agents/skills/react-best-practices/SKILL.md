---
name: react-best-practices
description: MANDATORY for any React code (Vite, Next.js, React Native): pages/ and core/, function components, React Compiler, server components, TanStack Query, Vitest, React 19.
---

# React best practices (router)

The user has no React project yet: these rules transpose the team's Angular conventions (`angular-best-practices`,
`typescript-best-practices`, `ui-responsive-accessible-modular`) to React 19.

Load only the row(s) that match the task; never every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Creating a module / tooling, versions, layout | `references/setup.md` |
| Writing or reviewing code | `references/code.md` |
| Writing or reviewing unit tests | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
