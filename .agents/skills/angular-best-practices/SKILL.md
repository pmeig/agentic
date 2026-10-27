---
name: angular-best-practices
description: "MANDATORY for any Angular code (apps, PWAs, libraries): standalone, zoneless, signals, inject(), lazy pages, t pipe i18n, Vitest helpers, Angular 21/22 practices."
---
# Angular best practices (router)
Angular 21/22 conventions; the project's own rules win. Load only the row(s) that match the task; never load every reference.
Related: `ui-responsive-accessible-modular` (layout, a11y), `typescript-best-practices` (language).

## Need -> file
| Need (what the agent is doing) | Load |
|---|---|
| Creating an app / build, app config, budgets | `references/setup.md` |
| Writing a component, page or template (signals, inputs, DI) | `references/components.md` |
| Services, HTTP, interceptors, guards, error mapping | `references/data.md` |
| Routing, forms, i18n | `references/routing-forms-i18n.md` |
| Building an ng-packagr library | `references/libraries.md` |
| Writing or reviewing unit tests (Vitest) | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
