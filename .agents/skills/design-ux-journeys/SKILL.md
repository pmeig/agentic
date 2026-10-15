---
name: design-ux-journeys
description: designer: model users, goals, business gestures, journeys, screen states and heuristics before drawing.
---

# UX journeys and business gestures

## Model first

1. **User and goal**: who, what they want to achieve, how often, in which context (one hand on a phone, desk, in a hurry, offline,
   interrupted), with which expertise. Missing information goes to the lead, grouped.
2. **Task flow**: the happy path in the fewest steps, then the branches: each business rule, each error, each permission,
   cancel / back / undo, interruption and resume, empty first use, offline and sync conflict.
3. **Screens and states**: list the screens and, for each, the states to draw: empty, loading, partial, error (with recovery),
   success, long content, disabled / not allowed, offline.
4. **Gesture hand-over**: the step-by-step description (data, rules, errors, expected result of each step) is what `front` turns
   into `gesture.md` for `qa`; keep your journey numbering stable.

## Heuristics to check every proposal

Nielsen's 10 heuristics: system status visible, real-world language, user control and undo, consistency, error prevention, recognition
over recall, flexibility for experts, minimal design, helpful error messages, help when needed. Plus: one primary action per screen,
frequent actions within thumb reach on mobile, defaults that fit most cases, no data re-entry (WCAG 2.2 3.3.7), confirmations only
for destructive or irreversible actions (and undo instead when possible).

## Typical flows and their pitfalls

| Flow | Watch for |
|---|---|
| Sign-up / sign-in | few fields, show password, passkeys / password managers allowed, no cognitive test (3.3.8), clear error per field |
| Onboarding | value in the first screen, skippable, teach in context, not a tour of every feature |
| Search and filters | search first when the catalog is large, visible active filters, empty result with a way out |
| Entry forms | one column, visible labels, right input type and keyboard, inline validation after leaving the field, save progress |
| List and detail | scan-friendly rows, sort / filter, bulk actions, swipe actions with a visible alternative |
| Checkout / payment | summary always visible, guest option, errors that keep the data |
| Approval | the decision and its context on one screen, reason field, audit trail |
| Dashboard | answer the question first, few indicators, drill-down, no decoration (`dataviz` skill for charts) |
| Settings | grouped by task, immediate effect or one clear save, reset |

## Output

`design/README.md` holds the user, the goal, the journey of each proposal (numbered steps with the number of taps / clicks) and the
state list; `design/spec.md` (final) holds the full states and interactions.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://www.nngroup.com/articles/ten-usability-heuristics/ , https://www.w3.org/WAI/WCAG22/Understanding/ , https://baymard.com/blog
