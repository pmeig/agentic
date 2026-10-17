---
name: design-mockup-render
description: designer: self-contained HTML mockups rendered to PNG screenshots (phone, tablet, desktop, light/dark) shown inline.
---

# Mockup files and screenshots

## HTML mockup

- One **self-contained** file per proposal: `.agents/docs/team/<feature>/design/proposal-<n>-<idea>.html`, inline CSS (custom properties as
  tokens: colors, type, spacing), no build, no network except an optional system-safe font; relative units; mobile first with media
  queries; `prefers-color-scheme` and `prefers-reduced-motion` handled.
- Real labels and realistic data (the product language), all states reachable: a small state switcher (`?state=empty|loading|error|success|long`)
  or one section per state; semantic HTML (landmarks, headings, buttons, labels) so the mockup can be tested for accessibility.
- Charts follow the `dataviz` skill when the harness has it.
- The final design: `design/final.html` + `design/spec.md`.

## Screenshots (PNG)

For every proposal and every state worth showing, in `design/screenshots/<proposal>-<state>-<viewport>-<theme>.png`:

| Viewport | Size |
|---|---|
| phone | 390 x 844 (and 360 x 740 for a small phone when the layout is tight) |
| tablet | 768 x 1024, only if its layout differs |
| desktop | 1440 x 900 |

Light and dark when the proposal supports both (at least the main state in dark).

Render with the tool available, in this order:
1. **Playwright** (`e2e-playwright-best-practices` for the API): `page.setViewportSize`, `page.goto('file://...')`,
   `page.screenshot({ path, fullPage: true })`, `colorScheme: 'dark'` for the dark theme, `reducedMotion: 'reduce'`. Node commands run
   as the project runs Node commands; install the browser once (`npx playwright install chromium`).
2. The built-in browser of the desktop app or Claude in Chrome, when Playwright is not installed.
3. If no rendering is possible, say so to the lead: do not ask for a choice on unseen mockups.

## Show them

Display every screenshot **inline** (image-viewing tool or embedding), proposal by proposal, phone and desktop side by side, then the
difference matrix (`design-mockup-variants`). Paths and descriptions alone are not a presentation. Keep the folder tidy: delete
screenshots of dropped proposals once the choice is made, keep the chosen one's.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://playwright.dev/docs/screenshots , https://playwright.dev/docs/emulation , https://gs.statcounter.com/screen-resolution-stats
