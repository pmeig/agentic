---
name: ui-responsive-accessible-modular
description: Use to implement responsive, accessible UI from an approved design and keep page features modular.
---

# Responsive, Accessible, Modular UI

## Implement the design

- Treat the approved mockup, design specification, and interface contract as the source of truth. Render the correct loading,
  empty, success, validation, error, and offline states; never present sample data as live.
- Keep each page's components, state, styles, helpers, and tests in its feature. Put code in shared core only when multiple
  pages use the same behavior.
- Use semantic platform controls and native HTML before introducing custom widgets. Keep visual, keyboard, and screen-reader
  states consistent.

## Accessibility and responsiveness

- Target WCAG 2.2 AA for web: semantic landmarks/headings, programmatic labels, accessible names, keyboard operation, visible
  focus, logical focus order, and status/error announcements.
- Preserve information without color alone. Check text and non-text contrast; use `aria-live` for asynchronous updates and
  `aria-invalid`/descriptions for form errors.
- Support narrow phone through desktop widths, zoom/reflow, touch targets, and reduced motion. Do not hide essential actions
  or content at small breakpoints.
- Avoid unnecessary ARIA; verify controls with keyboard and screen-reader semantics.

## Verification

- Test every designed state and user interaction. Run unit tests plus the project's accessibility checks where available.
- Verify at least a narrow mobile and desktop viewport, including keyboard focus, validation, asynchronous updates, and errors.
  Capture screenshots when visual regression or handoff needs evidence.

## Sources

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/
- MDN responsive design: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design

Last refreshed: 2026-10-14

At first use in a later month, verify current accessibility guidance and supported browser/platform behavior. Preserve the
approved product design and report any material constraint.
