---
name: e2e-bdd-best-practices
description: Writing e2e scenarios in Gherkin (Cucumber, Playwright-BDD, Behave, Reqnroll) or Robot Framework.
---

# BDD / Cucumber / Robot Framework e2e best practices

- Use BDD only when the business reads the scenarios; otherwise plain Playwright or Cypress tests are lighter. One `.feature` per business gesture of `gesture.md`, in `features/<feature>/`.
- Declarative steps in business language ("Given a customer with an overdue invoice"), not UI steps ("click button 3"); the UI detail lives in step definitions and page objects.
- `Background` for shared context only; `Scenario Outline` + `Examples` for the same rule with different data; tags (`@smoke`, `@regression`) for suites.
- Small step definitions, one per sentence, shared in `steps/` only when several features reuse them; no logic or assertion hidden in hooks; hooks create and clean data.
- Robot Framework: keywords in resource files, `Browser` (Playwright) or `SeleniumLibrary`, variables from the environment; same isolation rules.
- Runner parallelism: Cucumber `--parallel`, `pabot` for Robot, at the count of `e2e-parallelism-init`.

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `cucumber`, `robot`...).

Sources:
- https://cucumber.io/docs/bdd/better-gherkin/ , https://cucumber.io/docs/guides/
- https://vitalets.github.io/playwright-bdd/ , https://robotframework.org/ , https://docs.reqnroll.net/

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
