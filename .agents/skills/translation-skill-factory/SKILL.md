---
name: translation-skill-factory
description: Use to create a missing language-<code> or translation-<source>-<target> skill in the existing format.
---

# Translation skill factory

The translator creates its own skills. Never translate with a language or pair that has no skill: generate it first, then use it.

## New language (`language-<code>`)

1. Pin the language and the variant: ISO 639-1 code (`pt`, `nl`, `ja`…) and region if it matters (`pt-BR` vs `pt-PT`, `zh-Hans`
   vs `zh-Hant`, `es-MX`). Ask the user in one short question when the variant is not obvious.
2. Research the authoritative sources before writing: the language academy or standards body, a reference dictionary and grammar,
   the Microsoft/Google/Apple style guides for the language, and Unicode CLDR for formats. Prefer official and current sources;
   keep their links.
3. Create `.agents/skills/language-<code>/SKILL.md` with the **same sections as `language-fr`**, in English (AI-facing file),
   examples in the language:
   - frontmatter `name: language-<code>` and a `description` starting with "Use when reading, writing, translating or reviewing …";
   - **Spelling and grammar essentials** (script, diacritics, gender/cases, articles, verb system, word order, particles, politeness);
   - **Typography** (quotes, spacing before punctuation, number/date/currency formats, capitalisation, inclusive-writing stance);
   - **Register and address** (formal/informal pronouns or honorifics, UI conventions for buttons, errors, instructions);
   - **How people really talk** (fillers, contractions, slang levels, loanwords, texting);
   - **Regional notes**;
   - **Monthly refresh** (with `Last refreshed: <YYYY-MM>`) and **Sources**.
4. For non-alphabetic or right-to-left languages, add the sections the language needs (writing direction, mixed-direction
   punctuation, honorific levels, counters, spacing, input forms).
5. Add the language to the language list of `README.md` and tell the user the skill is ready. Do not invent rules: mark anything
   you could not verify.

## New pair (`translation-<source>-<target>`)

1. Create it only after both language skills exist. The pair is **directional**: `translation-en-fr` is for a native French speaker.
2. Write the pair-specific part only; the generic method lives in `translation-craft`:
   - **Structural contrasts** that decide how sentences are rebuilt;
   - **False friends and traps** both ways that matter for this direction;
   - **Idioms and register shifts**, what natives say instead;
   - **Formats and typography** to convert;
   - **Length and UI**: expansion, buttons, titles;
   - **Frequent decisions** (formal/informal choice, terms, borrowings) with the recommended default.
3. End with **Monthly refresh** (`Last refreshed: <YYYY-MM>`) and **Sources** (bilingual dictionaries, parallel corpora, translator
   communities, style guides of the pair, for example Linguee, Reverso, IATE, EU Interinstitutional Style Guide).
4. Keep it short: tips a translator really uses, with 1 to 3 example pairs each.

## Monthly refresh (all generated skills)

Every generated skill carries a "Monthly refresh" section: at the first use in a later month, recheck its sources, update the
file, keep the user's own rules, set the date, and report what changed.

## Monthly refresh of this skill

Last refreshed: 2026-10 (initial writing; confirm sources at the first use of a later month)

Recheck that the sections of `language-fr` and the pair format above still match the existing skills, and update them together.
