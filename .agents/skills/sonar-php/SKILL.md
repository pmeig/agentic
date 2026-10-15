---
name: sonar-php
description: Only when asked (qa, back): SonarQube setup, coverage and exclusions of a PHP module. Never load on your own.
---

# Sonar for PHP (on request only)

## Properties

- `sonar.projectKey`, `sonar.sourceEncoding=UTF-8`, `sonar.sources=src` (Laravel: `app`), `sonar.tests=tests`, `sonar.exclusions=vendor/**`.
- Coverage: `phpunit --coverage-clover=coverage.xml` (Xdebug or PCOV) and `sonar.php.coverage.reportPaths=coverage.xml`;
  tests report `phpunit --log-junit=phpunit.xml` with `sonar.php.tests.reportPath=phpunit.xml`.

## Out of the analysis

- Tests: `tests/**` in `sonar.coverage.exclusions` and `sonar.cpd.exclusions`.
- Without behavior (`sonar.coverage.exclusions`): `**/Kernel.php`, `bootstrap/**`, `config/**`, `database/migrations/**`,
  `**/Entity/**`, `**/Dto/**`, `**/Model/**` without logic, `**/Exception/**`, service providers, generated code.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/php/ ,
https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/php-test-coverage/
