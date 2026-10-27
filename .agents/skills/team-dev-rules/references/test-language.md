# Team development rules: tests always run in English

- **Tests always run in English** (every type: unit, e2e web and Android, API, Sonar runs): language `en` / `en-US` set explicitly by the test (locale of the browser context, `I18nService.select('en')`, emulator language, `LANG`/`LC_ALL=C.UTF-8` with `TZ`), never read from the machine or the runner; assertions use the English texts or, better, stable test ids. Text-specific tests of another language (translations) set that language explicitly and reset it after.
