---
name: design-mockup-variants
description: "designer: propose 3 to 5 mockups that really differ, checked with a difference matrix, with a recommendation."
---

# Mockup variants (3 to 5 truly different proposals)

The lead wants **real choices**, not three versions of the same screen. Minimum 3 proposals, up to 5 when the need leaves room
(several plausible mental models, a new screen, a redesign). A simple change of a known screen can stay at 3.

## 1. Find the axes before drawing

Read the need, the user, the frequency and the context of the gesture, the current screens (asked to `front`), and write the
**decisions the design must take**. Each decision is an axis; every proposal picks a different position on at least **two axes**,
and no two proposals share the same position on more than half of them:

| Axis | Examples of positions |
|---|---|
| Layout paradigm | list + detail, cards, table, dashboard of tiles, single focused step, canvas / map / timeline, split view |
| Navigation | bottom bar, drawer, tabs, top bar + search first, command palette, wizard, single page with sections |
| Information hierarchy | action first, data first, summary first, search first, status first |
| Interaction model | forms, inline editing, direct manipulation (drag, swipe), conversational / assistant, bulk actions, keyboard-first |
| Flow shape | one step, progressive disclosure, wizard, guided with defaults, expert shortcut |
| Density | spacious touch-first, balanced, compact data-dense |
| Visual tone | calm and neutral, bold and colorful, editorial / typographic, playful, dense professional, system-native |
| Feedback | optimistic with undo, confirmation steps, live preview, toasts vs inline |

At least one proposal is **conservative** (closest to the current app and its design system), at least one **bold** (another mental
model of the same goal). Name each with a short idea ("Inbox", "Timeline", "Wizard"), not "Proposal 2".

## 2. Difference matrix (mandatory, in `design/README.md`)

A table with the proposals as columns and the axes as rows. Two proposals that look alike on the matrix are merged or one is
redrawn. Add the one-line **intent** of each, its journey step by step (taps / clicks count), strengths, weaknesses, who it suits
best, the cost for `front` and `back` (new components, new data), and the accessibility risk.

## 3. Draw them

- Same real content and data in every proposal, so the comparison is about design; every state shown (empty, loading, error,
  success, long text, offline when relevant).
- Each proposal self-contained (`design/proposal-<n>-<idea>.html`), rendered to desktop and mobile PNG (`design-mockup-render`).
- Palette, type and spacing may differ by proposal when the tone is an axis (`design-color-palettes`,
  `design-typography-spacing`); the project's design system and tokens stay the base for the conservative one.
- Do not pad: a proposal that breaks a hard constraint (accessibility, platform guideline, data the back end cannot give) is
  dropped, not shown.

## 4. Present and recommend

Show every rendered screenshot inline, then the matrix, then **one recommendation with the reason**. The lead (or the user) picks;
a mix of two proposals is allowed and becomes a new refinement round, not a sixth proposal.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://www.nngroup.com/articles/ , https://m3.material.io/ , https://developer.apple.com/design/human-interface-guidelines/
