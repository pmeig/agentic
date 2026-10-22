---
name: translation-craft
description: Use for any translation: native target-language rendering, ask tone and sentence type, faithful yet natural, several renderings.
---

# Translation craft

Translate **into your native language**: the target language is the one you grew up in. English → French means you are a native
French speaker reading a foreign text and writing what a French person would naturally say. Italian → German means you are a
native German speaker. Read the source as a foreigner would have to, write the target as a local.

## Before translating

1. Load `language-<target>` (you speak it natively), `language-<source>` (to understand it precisely) and, if it exists,
   `translation-<source>-<target>`. If a language or pair skill is missing, create it first with `translation-skill-factory`.
2. At the first use in a month, run the monthly refresh of each skill you loaded (see their "Monthly refresh").
3. Get the context. Ask the user in one grouped message only what is missing and matters:
   - **Tone**: neutral, friendly, formal, playful, technical, marketing, poetic. `tu`/`vous` (or the equivalent) for the target.
   - **Sentence type**: UI label, button, error, tooltip, notification, dialogue, headline, slogan, email, legal text, subtitle.
   - **Audience and place**: age, country/variant (fr-CA, es-MX, pt-BR…), where the text appears, length limits.
   - **Terminology**: glossary, fixed names, text that must not be translated.
   If the user already gave a project's conventions (existing translations, register), infer them and say so; do not re-ask.

## How to translate

- Translate the **meaning, intent and effect**, not the words (dynamic equivalence, Nida; purpose of the translation, Skopos).
- Choose the technique the sentence needs (Vinay & Darbelnet): literal translation when it sounds natural; **transposition**
  (change the part of speech), **modulation** (change the viewpoint: `Do not forget` → `Pense à`), **equivalence** (replace an
  idiom by the target idiom), **adaptation** (replace a cultural reference), **borrowing** only when natives really say it.
- Rebuild the sentence in the target's order; split long sentences or join short ones; avoid translationese and false friends.
- **Be as close as possible to what people actually say** in that context: everyday words, natural contractions, the tone of the
  product. A friendly app does not speak like a contract. A legal text does not speak like a text message.
- **Be creative when the context needs it**: slogans, jokes, wordplay, titles and microcopy may leave the source wording to keep
  the same effect, rhythm and humour. State when you departed from the literal text and why.
- Keep fidelity on facts: numbers, names, negations, conditions, order of steps, who does what. Never add or drop information
  without telling.
- Localise formats (numbers, dates, currency, units, quotes, punctuation spacing) to the target's rules.
- Keep placeholders (`{1}`, `%1$s`), markup, keys, punctuation that is code, and glossary terms exactly; reorder them when the
  target grammar needs it.
- Mind length: German and Romanian often grow 20–35 %, French and Spanish 15–25 % over English. For UI, shorten with verbs and
  drop filler words rather than truncate.
- Consistency: one term per concept across the whole text; reuse the project's existing terms.

## Propose alternatives

- When a sentence can be turned in clearly different ways, give **2 to 4 proposals** that differ for real (not synonyms):
  e.g. *faithful*, *natural/colloquial*, *short*, *creative*, each with a one-line reason and the situation it fits. Recommend one.
- For whole files or long texts, give one version (the recommended one) and list the sentences where you see a real alternative.
- If the user asks for "several ways", always give them without being asked twice.

## Check

- Read the target aloud as a native: does it sound written by a person? Does it fit the context and tone?
- Back-translate mentally to catch meaning drift; check false friends of the pair and that every placeholder and number survived.
- Report briefly: choices made, doubts, anything left untranslated on purpose.

## Monthly refresh

Last refreshed: 2026-10 (initial writing; confirm sources at the first use of a later month)

At the first use in a later month, recheck the sources below, update this file with any new practice, keep the user's own rules,
set the date, and report what changed.

## Sources

- Vinay & Darbelnet, *Stylistique comparée du français et de l'anglais* (translation procedures); Nida, *Toward a Science of Translating*
- Skopos theory (Reiß & Vermeer); ISO 17100 (translation services); ATA Code of Professional Conduct: https://www.atanet.org
- EU DGT Translation Quality Guidelines and Interinstitutional Style Guide: https://style-guide.europa.eu
- Microsoft, Google and Apple localization/style guides; Unicode CLDR: https://cldr.unicode.org
