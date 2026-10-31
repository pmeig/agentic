---
name: e2e-live-progress
description: "On every e2e run: live step preview in the prompt (green, red, blinking grey dots)."
---

# E2E live progress

An e2e run is never silent: the user sees the steps while they run (`qa`, with `e2e-run`, any e2e tool).

## Events

The run appends one tab-separated line per event to `<e2e root>/work/e2e-progress.tsv` (next to `e2e.pid`, unique per worker group,
removed at the end of the run, even on failure):

```
<state>\t<index>\t<total>\t<title>
```

`state` = `start`, `pass` or `fail`; `index` starts at 1 (order of completion with several workers); `total` = tests of the run
(0 while unknown); `title` = `<feature> > <scenario>`, plus the step on failure. Feed it from the tool's reporter: Playwright custom
reporter (`onTestBegin` / `onTestEnd`), Cypress `before:spec` / `after:spec` events, JUnit XML or console of Maestro, `xcodebuild` and
Gradle logs, Cucumber `--format message`.

## In the prompt (terminal)

`scripts/render.sh <progress-file>` (this skill's folder) prints one line per event:

| State | Dot |
|---|---|
| running | grey `●` blinking (ANSI blink, or alternating `●` / `○` every 500 ms if the terminal ignores blink) |
| `pass` | green `●` |
| `fail` | red `●`, with the failing step and the path of the trace or screenshot |

Launch the run in the background and follow it with the renderer (e.g. the `Monitor` tool) so steps appear as they happen. End with
`● 18/20 passed, 2 failed, <duration>` (green if all pass, red otherwise).

## Remote control

When the session is followed through remote control (small screen, no redraw), send **one short status per change**, never a
redrawn list. Numbers are `passed/total`; update on each failure and every few tests:
- `🟢 12/20` (all good so far) · `⚪ 0/20` (running, no result) · `🔴 12/20 - <title of the first failing test>`
- end: `🟢 20/20` or `🔴 18/20 - <title>`

## Rules

- The preview never replaces the report: results, failures with traces and the not-covered list still go to the lead.
- No secrets in titles or steps (tokens, passwords, personal data).
