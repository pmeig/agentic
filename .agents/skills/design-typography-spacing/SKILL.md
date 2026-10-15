---
name: design-typography-spacing
description: designer: type scale, spacing, grid, density, breakpoints, touch targets.
---

# Typography, spacing and layout

## Type

- A **modular scale** (ratio 1.2-1.25 for apps, up to 1.333 for editorial), 5-7 sizes at most, with roles (display, title, body,
  label, caption). Body at least 16 px (web) / 16 sp (Android) / 17 pt (iOS); never below 12 for secondary text.
- Line height 1.4-1.6 for body, 1.1-1.3 for titles; line length 45-75 characters; left aligned text; no all-caps paragraphs.
- Fonts: the system font stack or the project font first; a second family only for a distinct tone (editorial proposal). Load a
  variable font with `font-display: swap` in the mockup, with a fallback.
- Everything in relative units (`rem`/`sp`/Dynamic Type): the layout survives 200 % text size (WCAG 1.4.4) and 320 px reflow (1.4.10).

## Spacing and grid

- One **spacing scale** on a 4 px base (4, 8, 12, 16, 24, 32, 48, 64), applied by role (gap, padding, section); related items closer
  than unrelated ones (proximity), consistent alignment on a 4-column (phone) / 8 (tablet) / 12-column (desktop) grid.
- **Touch targets**: 44 x 44 pt (iOS), 48 x 48 dp (Android), at least 24 x 24 CSS px with spacing for pointer inputs (WCAG 2.5.8 AA),
  aim for 44 on touch; space between neighbouring targets.
- **Density as an axis** (`design-mockup-variants`): spacious touch-first, balanced, compact data-dense (rows 32-40 px, only for
  expert desktop use, still 24 px targets).

## Responsive

- Mobile first, then breakpoints driven by content: about 360 / 600 / 840-900 / 1200 / 1600 px; a layout per class (compact,
  medium, expanded, as in Material window size classes), not a scaled phone.
- Navigation adapts: bottom bar on phone, rail or sidebar on larger screens; tables become cards or scroll with a fixed first column;
  modals become full screens or bottom sheets on phone.
- Safe areas (notch, home indicator), landscape, foldables, keyboard open on forms, long translated text (+30-40 %).
- Mockups are rendered at least at **390 x 844 (phone)** and **1440 x 900 (desktop)**, plus **768 x 1024** when the tablet layout
  differs (`design-mockup-render`).

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://m3.material.io/foundations/layout/applying-layout/window-size-classes , https://m3.material.io/styles/typography/overview ,
https://developer.apple.com/design/human-interface-guidelines/typography , https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
