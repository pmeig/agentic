---
name: team-bugfix-mode
description: "Use (lead) for a red test, red CI, flaky test or bug with behavior already specified: triage, owners, flaky repair, stop conditions. Load the reference of the situation only."
---

# Bugfix mode (router)

Behavior already specified and unchanged. New or changed behavior, contract or screen is a feature (skill `team-lead`); doubt: ask the user. Load only the row that matches.

## Need -> file

| Situation | Load |
|---|---|
| Red test, red CI, flaky test or bug on a merged or PR'd change, no feature in progress | `references/triage-and-fix.md` |
| A feature is in progress and its tests are red locally | `references/feature-red-locally.md` |
| Green locally but red in the CI, or red CI that passes locally | `references/ci-red.md` (after `references/triage-and-fix.md`) |
