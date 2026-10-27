# Sonar report: is there a Sonar for this language?

1. SonarQube up (`/api/system/status` answers `UP`), project existing (`api/components/search`), module language analysed
   (`api/languages/list`, `ncloc_language_distribution` measure).
2. Language without analyser or plugin: **no Sonar check**; say so in the report, keep the local coverage figures, fall back to the
   linter and coverage tool of the language skill.
3. Sonar missing or down: never skip silently; report "Sonar not available" with the reason and ask the lead whether to start it.
