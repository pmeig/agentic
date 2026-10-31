---
name: design-motion-feedback
description: "designer: transitions, loading, feedback, optimistic updates, reduced motion."
---

# Motion and feedback

## Purpose first

Motion explains **where something comes from or goes**, confirms an action, or shows progress; it never decorates a frequent
action. Each animation in the spec states its purpose, trigger, duration, easing and reduced-motion alternative.

## Values

- Durations: 100-150 ms micro feedback, 200-300 ms element transitions, 300-500 ms large or full-screen; exits shorter than entrances.
  Ease-out for entering, ease-in for leaving, standard ease-in-out for moving; springs on platforms that use them (Material 3
  Expressive, iOS); no linear except progress.
- Animate `transform` and `opacity`; avoid layout-triggering properties; 60 fps target.
- Frequent actions (typing, scrolling, toggling) get almost no motion.

## Feedback

- **Response within 100 ms** to any input (pressed state), **loading indicator after 1 s**, a skeleton for content with a known shape,
  a determinate progress bar when the duration is known, and a way to cancel long actions.
- **Optimistic update with undo** for reversible actions; a confirmation step only for irreversible ones.
- Success and errors: inline near the cause; toasts / snackbars only for passive confirmations (not for errors that need action),
  announced to assistive tech (status messages) and visible long enough (not auto-dismissed while focused).
- Haptics on mobile for confirmations and errors, never alone.

## Reduced motion and safety

`prefers-reduced-motion` / Reduce Motion: replace movement by a fade or an instant change; no parallax, no auto-playing carousel
without pause; nothing flashes more than 3 times a second (WCAG 2.3.1, 2.2.2).

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://m3.material.io/styles/motion/overview , https://developer.apple.com/design/human-interface-guidelines/motion ,
https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
