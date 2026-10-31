# Translation craft: before translating (skills and context)

1. Load `language-<target>` (you speak it natively), `language-<source>` (to understand it precisely) and, if it exists,
   `translation-<source>-<target>`. If a language or pair skill is missing, create it first with `translation-skill-factory`.
2. At the first use in a month, run the monthly refresh of each skill you loaded (see their "Monthly refresh"): refresh when `Last refreshed` is older than 1 month.
   Variant: take it from the project locale code (`language-<target>/references/variants.md`); ask if unknown; one variant per project.
3. Get the context. Ask the user in one grouped message only what is missing and matters:
   - **Tone**: neutral, friendly, formal, playful, technical, marketing, poetic. `tu`/`vous` (or the equivalent) for the target.
   - **Sentence type**: UI label, button, error, tooltip, notification, dialogue, headline, slogan, email, legal text, subtitle.
   - **Audience and place**: age, country/variant (fr-CA, es-MX, pt-BR…), where the text appears, length limits.
   - **Terminology**: glossary, fixed names, text that must not be translated.
   If the user already gave a project's conventions (existing translations, register), infer them and say so; do not re-ask.
