---
name: language-ro
description: "Use when reading, writing, translating or reviewing Romanian text: grammar, spelling, register, UI conventions."
---

# Romanian (ro)

Reference for a native Romanian speaker's judgement. Standard Romanian (Romania); Moldova uses the same standard.

## Spelling and grammar essentials

- Diacritics: `ă â î ș ț`. Use comma-below `ș ț`, never cedilla `ş ţ`. Since the 1993 reform `î` is written at the start and end of a word and in compounds (`înscrie`, `a coborî`, `neînțeles`), and `â` inside a word (`cuvânt`, `român`); `sunt`, `suntem` are written with `u`.
- The definite article is enclitic: `session` → `sesiune` / `sesiunea`, `luna` (the month), `lunile`. Indefinite article is a separate word (`o sesiune`, `un buton`).
- Three genders: masculine, feminine and neuter (masculine singular, feminine plural: `un cont, două conturi`).
- Cases: nominative/accusative, genitive/dative (often marked with the article, `numele sesiunii`), vocative. Genitive/dative of feminine nouns often changes the stem.
- Verbs: infinitive `a salva`; the subjunctive `să salvezi` replaces most infinitives (`vreau să plec`); future `o să salvez` (colloquial) or `voi salva`; reflexive clitics are frequent (`Înscrie-te`, `conectează-te`).
- Pronoun subject is usually dropped. Double negation is correct (`nu am nimic`). Possessive and demonstrative agreement with the noun (`acest e-mail`, `această sesiune`, `contul tău`).
- Numbers 2 to 19 take `de` after 20: `două sesiuni`, `20 de sesiuni`, `100 de lei`. Prices: `25 de euro`.

## Typography

- Quotes `„…”` (low-high); nested `«…»`. Numbers `1.234,56` (dot thousands, comma decimal), currency after the figure with a space (`25 €`, `25 lei`); space before `%` is common.
- Dates `16 octombrie 2026`, months and days lowercase; only the first word of a UI label is capitalised. `e-mail` (hyphenated); `link` is `linkul`.

## Register and address

- `tu` (informal, apps for friends and peers) and `dumneavoastră` (formal; `dvs.`). Pick one per product; informal apps use `tu` forms with `-ți`, `-te`.
- Buttons: imperative second person (`Salvează`) or infinitive (`Salvare` as noun); keep one style. Menus often use nouns (`Setări`, `Cont`).
- Polite requests: `te rog` / `vă rog`; error messages state the fix.

## How people really talk

- Fillers and interjections: `păi`, `deci`, `na`, `hai`, `bă` (very informal), `mișto`, `faină`, `ok`, `gata`, `ia`, `măi`.
- Heavy English borrowing in tech (`link`, `app`, `like`, `login`) alongside official terms (`conectare`, `aplicație`, `parolă`). Match the audience.
- Texting often drops diacritics (`ca sa`); formal text never does.

## Regional notes

- Moldova (Republic of Moldova) uses the same norm with some Russian-origin vocabulary; Aromanian and Istro-Romanian are separate.

- Variants (locale code, e.g. `ro-MD`): load `references/variants.md` when the project locale has a region or is unknown.

## Monthly refresh

Last refreshed: 2026-10 (initial writing; confirm sources at the first use of a later month)

At the first use in a later month, recheck the sources below (DOOM updates, Academy decisions), update this file, keep the user's own rules, set the date, and report what changed.

## Sources

- Academia Română, DOOM 3 (2021) and DEX online: https://dexonline.ro
- Gramatica limbii române (GALR), Institutul de Lingvistică „Iorgu Iordan”: https://www.iliiordan.ro
- Microsoft Style Guide, Romanian: https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides
- Unicode CLDR (ro formats): https://cldr.unicode.org
