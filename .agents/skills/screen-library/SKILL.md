---
name: screen-library
description: "front (and designer, sales as readers): capture or read the real screens of the app kept in .agents/docs/screens/; load only when a page is added or changed, or when a missing screen is requested."
---

# Screen library (`front` writes, `designer` and `sales` read)

Real captures of the app pages, `.agents/docs/screens/<platform>/<page>[-<state>]-<theme>.png` + `INDEX.md` (page, route, state, file, date, commit).

## Writing (`front`)

`front` re-captures **only the pages it touches** (new, changed, or one of their dialogs/states), on each client (phone and desktop/tablet; light and dark when the theme differs), from the running app (never a mockup), in the same change and before the `qa` handover. Untouched pages are not recaptured. A page the designer asks for and the library lacks is captured on request.

## Reading (`designer`, `sales`)

Open `INDEX.md` first, then only the PNGs of the pages concerned; ask `front` for a missing or outdated screen instead of capturing it yourself.
