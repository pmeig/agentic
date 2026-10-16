# Budget app translations

Translations of the 414 texts of `pmeig/budget` (Android `strings.xml` keys + the 7 web-only keys of `web/src/app/core/i18n/messages/web.ts`),
made by the `translator` agent as a native speaker of each target language, informal register (`tu` / `du` / `tú`).

- `en-to-<lang>.json`: from English (`values/strings.xml`) to `fr`, `ro`, `it`, `es`, `de`.
- `fr-to-<lang>.json`: from French (`values-fr/strings.xml`) to `en`, `ro`, `it`, `es`, `de`.
- Same keys and order as the source; placeholders `{1}`, `{2}`… kept (`%1$s` in Android). `translatable="false"` strings are left out.
- These are independent translations, not a replacement of the files in `pmeig/budget`: compare them with the existing ones
  (`web/src/app/core/i18n/messages/`) before adopting a wording.
