# UX journeys: user model, task flow, states and heuristics

## Model first

1. **User and goal**: who, what they want to achieve, how often, in which context (one hand on a phone, desk, in a hurry, offline, interrupted), with which expertise. Missing information goes to the lead, grouped.
2. **Task flow**: the happy path in the fewest steps, then the branches: each business rule, each error, each permission, cancel / back / undo, interruption and resume, empty first use, offline and sync conflict.
3. **Screens and states**: list the screens and, for each, the states to draw: empty, loading, partial, error (with recovery), success, long content, disabled / not allowed, offline.
4. **Gesture hand-over**: the step-by-step description (data, rules, errors, expected result of each step) is what `front` turns into `gesture.md` for `qa`; keep your journey numbering stable.

## Heuristics (check every proposal)

Nielsen's 10: system status visible, real-world language, user control and undo, consistency, error prevention, recognition over recall, flexibility for experts, minimal design, helpful errors, help when needed. Plus: one primary action per screen, frequent actions within thumb reach, defaults that fit most cases, no data re-entry (WCAG 3.3.7), confirmations only for destructive/irreversible actions.

## Output

`design/README.md`: user, goal, journey of each proposal (steps + tap/click count), state list. `design/spec.md` (final): full states and interactions.

## Monthly refresh

Last refreshed: 2026-10. Sources: https://www.nngroup.com/articles/ten-usability-heuristics/ · https://www.w3.org/WAI/WCAG22/Understanding/ · https://baymard.com/blog
