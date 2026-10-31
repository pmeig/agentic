---
name: design-accessibility-review
description: "designer: check a mockup against WCAG 2.2 AA before presenting it."
---

# Accessibility review of a mockup (WCAG 2.2 AA)

Run it on **every proposal** before showing it and on the final design; list the result in `design/README.md` (checked / issue / not
applicable). A proposal with an open AA issue is fixed or dropped.

## Checklist

- **Perceivable**: text contrast 4.5:1 (3:1 large), UI components and focus 3:1 (1.4.3, 1.4.11); no information by color alone (1.4.1);
  text resizes to 200 % and reflows at 320 px without two-way scrolling (1.4.4, 1.4.10); text spacing tolerated (1.4.12); alt text
  or names for meaningful images and icons (1.1.1); captions for media.
- **Operable**: everything reachable and usable by keyboard with a logical order and a visible focus that is not hidden by sticky
  bars (2.1.1, 2.4.3, 2.4.7, **2.4.11**); **target size at least 24 x 24 CSS px** (**2.5.8**), 44-48 for touch; **any dragging has a
  single-pointer alternative** (**2.5.7**); gestures with a simple alternative (2.5.1); no keyboard trap; skip link; page / screen titles.
- **Understandable**: language set; a visible label per field, instructions before the field (3.3.2); errors identified in text next to
  the field with how to fix them (3.3.1, 3.3.3); **no re-entry of data already given** (**3.3.7**); **authentication without cognitive
  test**, paste and password managers allowed (**3.3.8**); **help in the same place** on every screen (**3.2.6**); consistent
  navigation and naming (3.2.3, 3.2.4); confirm or undo irreversible actions (3.3.4).
- **Robust**: semantic roles, accessible names that match the visible labels (2.5.3), status messages announced without moving focus (4.1.3).
- **Motion**: nothing flashes more than 3 times a second; animations respect reduced motion; auto-moving content can be paused (2.2.2).
- **Mobile equivalents**: Dynamic Type / font scale, TalkBack and VoiceOver reading order and labels, orientation not locked
  (1.3.4), Reduce Transparency and increased contrast respected.

## In the spec

`design/spec.md` gives, per screen: accessible names, roles, reading and tab order, focus management (dialogs, errors, route
changes), announcements, keyboard shortcuts, breakpoints. This is what `front` implements and `qa` checks with
`e2e-accessibility-best-practices`.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://www.w3.org/TR/WCAG22/ , https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/ , https://www.w3.org/WAI/WCAG22/quickref/
