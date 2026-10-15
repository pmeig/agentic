---
name: e2e-cypress-best-practices
description: Writing, reviewing or running Cypress e2e or component tests.
---

# Cypress e2e best practices

- Select with `data-cy` / `data-testid` attributes, never brittle classes, ids or changing text.
- Each test independent; reset state in `beforeEach` (never `after`/`afterEach`); share login with `cy.session()`; seed data through `cy.request`/`cy.task` on the API, not through the UI.
- No `cy.wait(ms)`: alias requests with `cy.intercept(...).as('x')` and `cy.wait('@x')`, or assert the state; do not assign command results to variables (use aliases and `.then`).
- Test only what you control; stub third-party services. Set `baseUrl`; start the web server before Cypress, not inside a test.
- Prefer integration-style tests with several assertions over one-assertion tests. Secrets with `cy.env()`, only public values in `Cypress.expose()`.
- Config: `retries` only to detect flakiness, video off, screenshots on failure, `e2e.specPattern` by feature folder; component tests for isolated UI, e2e for journeys.
- Parallel: `cypress run --record --parallel` (Cypress Cloud) or split specs across machines yourself, with the count of `e2e-parallelism-init`.
- Accessibility with `cypress-axe`; TypeScript strict and `eslint-plugin-cypress`.

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `cypress`).

Sources:
- https://docs.cypress.io/app/core-concepts/best-practices
- https://docs.cypress.io/app/continuous-integration/overview , https://docs.cypress.io/app/references/changelog

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
