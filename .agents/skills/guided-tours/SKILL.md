---
name: guided-tours
description: front, qa, lead: ONLY when the project already has guided tours (then every new feature gets its tutorial page and full tour, windows included, and screen changes re-check the tours); on a new project front asks the lead whether to add tours.
---

# Guided tours and first-launch tutorial (any app with a tour system)

## When to use
- **Project has guided tours** (tour catalog, overlay, help button, tutorial pages): always apply this skill to every new feature, in full, and on every screen change. The project skill (`.agents/skills/feature-tutorial` or similar) wins over this one.
- **Project has none**: do not add any. On a **new project**, `front` asks the lead (grouped with the other business choices) whether the app gets guided tours; only on a yes, propose a tour system (catalog of features, overlay on real elements, help button per page, "seen" state stored per user) and create the project skill.
- **Existing project without tours**: do nothing unless the lead asks.

## Definition of done of any user-facing feature
1. A **catalog entry with a tutorial page** shown at the next launch to every user who has not seen it (and to a new user). No page = invisible feature.
2. A **guided tour** on the real screen reaching **every control** of the feature, **windows included**.
3. Texts in every supported language (via `translator`), bubbles readable at 200 % font on a small screen.
4. Both clients (web + mobile) when the app has twins; same keys, same steps.
5. Tour e2e extended (`qa`), release notes bullet if the project has them, docs updated (`documentalist`).
`qa` refuses the PR go when one of these is missing.

## The tour goes everywhere
- Never stop at "the button is here": a control that opens something (gear, menu, import, export, picker, dialog, sheet) is **entered** and each control inside gets a step.
- If the window cannot open by itself (needs data, a file, a selection, a permission), **create a temporary sample element** (sample widget, made-up session, sample file, fake result) and **delete it** when the tour ends, is skipped or left, and at next launch if the app was killed. A sample never writes to the server or user data.
- Draw the window inline under the dimmed screen when the overlay cannot light a real system window (stateless window content shared by the screen and the preview).
- Checklist: list every control of the screen -> every window each opens -> every control of those windows; each has a step; an exception needs a written reason in the PR.

## Rules
- Tour keys never change (seen state is stored by key); a new key shows the page again to everybody, so a detail gets `inTutorial = false` (help list only).
- Any change of a screen (element moved/renamed/removed, text, gesture) means checking the tours it touches in the same PR and saying which were checked.
- A tour that needs data makes it and puts everything back.
- Mark the novelty (badge) until the user uses the feature.

## Check before handing off
Catalog entry present with tutorial page? Every control and window has a step? Sample elements removed? Texts in all languages? Tour e2e passes to the last step on every client?
