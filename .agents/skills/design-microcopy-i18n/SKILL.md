---
name: design-microcopy-i18n
description: designer: texts of a mockup (labels, errors, empty states, tone) and design for translation.
---

# Microcopy and internationalization

## Write

- **Product language** in the mockup (the project's), instructions in English elsewhere. Plain words, the user's vocabulary, no jargon,
  active voice, one idea per sentence.
- **Buttons** say the result (`Save invoice`, not `OK`/`Submit`); the same action has the same name everywhere; destructive actions name
  what is destroyed (`Delete 3 expenses`).
- **Labels** visible and short; helper text only when needed; placeholders never replace labels.
- **Errors**: say what happened, why if useful, and how to fix it; next to the field; never blame the user; no codes alone
  (`Password must have at least 12 characters`, not `Invalid input`).
- **Empty states**: explain what will appear here and offer the first action. **Success**: confirm what changed, with an undo when possible.
  **Loading**: say what is loading when longer than a second. **Permissions / offline**: what is limited and what still works.
- **Tone** set per product (calm and clear by default); one proposal may try another tone (`design-mockup-variants`) without
  changing the meaning.

## Design for translation

- Text expands 30-40 % (German, French), CJK is denser and taller: no fixed widths on text containers, test long labels.
- No concatenated sentences; placeholders with full-sentence strings; plurals and gender by ICU message format; numbers, dates,
  currencies and units by locale (`Intl`); names and addresses with flexible formats.
- Right-to-left: mirror layout (logical start / end), keep numbers and media controls as the platform does; icons that imply
  direction flip.
- Keep texts in one catalog per page (`front` implements); the mockup lists the keys in `design/spec.md`.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://m3.material.io/foundations/content-design/overview , https://developer.apple.com/design/human-interface-guidelines/writing ,
https://www.w3.org/International/questions/qa-i18n , https://unicode-org.github.io/icu/userguide/format_parse/messages/
