# Mockup render: PNG screenshots

Save to `design/screenshots/<proposal>-<state>-<viewport>-<theme>.png`.

| Viewport | Size |
|---|---|
| phone | 390 x 844 (and 360 x 740 for a small phone when the layout is tight) |
| tablet | 768 x 1024, only if its layout differs from phone |
| desktop | 1440 x 900 |

Light and dark when the proposal supports both (at least the main state in dark).

Render in this order:
1. **Playwright**: `page.setViewportSize`, `page.goto('file://...')`, `page.screenshot({ path, fullPage: true })`, `colorScheme: 'dark'` for dark, `reducedMotion: 'reduce'`. Install once: `npx playwright install chromium`.
2. Built-in browser (desktop app or Claude in Chrome) when Playwright is not installed.
3. If no rendering is possible: say so to the lead; do not ask for a choice on unseen mockups.

## Monthly refresh

Last refreshed: 2026-10. Sources: https://playwright.dev/docs/screenshots · https://gs.statcounter.com/screen-resolution-stats
