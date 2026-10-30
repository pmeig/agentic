# Translation skill factory: language

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
