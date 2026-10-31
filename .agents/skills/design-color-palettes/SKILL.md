---
name: design-color-palettes
description: "designer: build and check accessible palettes, light/dark themes, WCAG contrast, tokens."
---

# Color palettes

## Build

1. **Start from the project**: its tokens and brand color first (conservative proposal). For a free palette, pick one **brand hue**,
   one **accent** if useful, a **neutral scale** (8-10 steps, slightly tinted by the brand hue), and **semantic colors** (success,
   warning, error, info).
2. Generate tone scales in a perceptual space (HCT as in Material 3, or OKLCH) so that steps have predictable contrast; name them as
   **tokens by role** (`surface`, `on-surface`, `primary`, `on-primary`, `outline`, `error`...), never by hue name.
3. **Light and dark themes**: dark is not an inverted light: lower the chroma, use elevated surfaces lighter than the base, no pure
   black on pure white contrast glare.
4. Use color for **meaning and emphasis**, sparingly: one primary color for the main action, neutrals for the rest.

## Check (WCAG 2.2 AA, every pair in both themes)

- Text 4.5:1 against its background; large text (18.66 px bold / 24 px) 3:1; UI components, icons and control borders, focus
  indicators 3:1 against adjacent colors; text over images or gradients on the worst spot.
- Information never carried by color alone (icon, text, pattern or shape too); check with a color-blindness simulation
  (deuteranopia, protanopia, tritanopia) and in grayscale.
- States distinguishable: hover, focus (visible, 2 px, 3:1), pressed, disabled (still readable when it carries information),
  selected, error.
- Write the palette in `design/README.md`: hex, role, contrast ratio of each used pair (compute it, do not eyeball it).

## One tone per proposal

When proposals differ in tone (`design-mockup-variants`): calm and neutral, bold and saturated, editorial monochrome, warm and
friendly, dense professional. The palettes must differ visibly, not only by a few percent of lightness.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://www.w3.org/TR/WCAG22/#contrast-minimum , https://m3.material.io/styles/color/overview , https://oklch.com/ ,
https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
