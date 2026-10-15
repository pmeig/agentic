---
name: e2e-accessibility-best-practices
description: Adding automated WCAG 2.2 AA accessibility checks to e2e tests (axe, mobile checks, keyboard scenarios).
---

# Accessibility e2e best practices

- Run **axe-core** on every page state of a gesture (`@axe-core/playwright`, `cypress-axe`, `@axe-core/webdriverio`, `axe-selenium`) with the tags `wcag2a`, `wcag2aa`, `wcag21aa`, `wcag22aa`; fail on violations; every exclusion is listed with a reason.
- Add the scenarios axe cannot cover: keyboard-only journey (Tab order, visible focus, no trap, Escape closes dialogs), focus moved to dialogs and errors, 200 % zoom and 320 px reflow, reduced motion, dark mode and contrast, role-based locators that prove accessible names.
- Mobile: Espresso `AccessibilityChecks`, Compose semantics, XCUITest `performAccessibilityAudit()`, Maestro assertions on labels; touch targets and dynamic type or font scale.
- Automation finds only part of the problems: report what was checked and what needs a manual pass (screen reader, cognitive load). The design rules are in `ui-responsive-accessible-modular`.

Run through `e2e-run`; workers from `e2e-parallelism-init` (key of the e2e tool that hosts the checks).

Sources:
- https://www.w3.org/TR/WCAG22/ , https://github.com/dequelabs/axe-core , https://playwright.dev/docs/accessibility-testing

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
