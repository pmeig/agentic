---
feature: stats-web-tour-sample
project: budget (D:\projects\typescript\budget, repo pmeig/budget)
status: need (not started)
date: 2026-10-23
---
# Need: web stats tour must work on an empty period

## Problem
Tour `stats` (25 steps, shipped in PR #144): the step on the table toggle of the first widget card ("see the figures as a table") has **no spotlight on web** when the selected period has no data. An empty period renders no chart, so the toggle does not exist and the bubble explains a control the user cannot see.
Android does not have the problem: `WidgetInput.forTour` (`A/stats/StatsTourPreviews.kt`, wired in `StatsScreen.kt`) draws made-up monthly figures during the tour, so the sample card is a chart card with the toggle. Nothing is stored.
Hits mostly new users who start the tour before entering any expense. Not caught by e2e (they run with data).

## Goal
On web, during the `stats` tour, the step on the table toggle always has a spotlight, with the same behavior as Android: sample figures shown only while the tour runs, never saved, gone when the tour ends, is skipped or is left.

## Scope
- Web only: `web/src/app/pages/stats/` (existing `helpers/tour-sample.helper.ts`, `stats.page`, `widgets/widget-card`), tour catalog `web/src/app/core/tour/helpers/tour-catalog.helper.ts` (step key stays, **tour keys never change**).
- Android is the reference, no change.

## Options (front recommends, lead decides)
1. **Same sample figures as Android** (recommended): parity, the step stays useful. Reuse the golden figures of Android `tourSampleRows` so both clients show the same example.
2. Skip the step when the toggle is absent: cheaper, but the explanation is lost for exactly the users who need it.

## Acceptance
- Empty period + tour: the toggle step spotlights the toggle; the card shows sample figures; nothing is written to the server or local storage.
- Tour end / skip / back / page leave: sample gone, real empty state back.
- Period with data: unchanged (real figures).
- Unit tests 100 % on new code, every condition (empty period, data period, tour on/off, tour left mid-step), parameterized.
- E2E: web spec of tour `stats` (`23-tours-toutes-pages`) extended with an empty-period account, Android twin checked for parity; `qa` runs the impacted web e2e.
- Skill `feature-tutorial` of the project checked (tour goes everywhere, temporary sample removed). No new text expected; if one is needed, `translator` for the 6 languages.
- Release note only if the user sees a change (probably none); docs: `features/tutorial-tours.md` gap line removed.

## Agents
`front` (build), `qa` (e2e + go), `documentalist` (remove the known-gap line). No designer, no back.
