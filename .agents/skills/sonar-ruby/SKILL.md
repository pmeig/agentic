---
name: sonar-ruby
description: "Only when asked: Sonar setup, coverage, exclusions of a Ruby / Rails module."
---

# Sonar for Ruby (on request only)

## Properties

- `sonar.projectKey`, `sonar.sourceEncoding=UTF-8`, `sonar.sources=app,lib`, `sonar.tests=spec`, `sonar.test.inclusions=spec/**/*_spec.rb`.
- Coverage: SimpleCov with the JSON formatter and `sonar.ruby.coverage.reportPaths=coverage/.resultset.json`; availability and
  report format are to be re-checked on the Ruby page of the Sonar docs at the monthly refresh.

## Out of the analysis

- Tests: `spec/**` in `sonar.coverage.exclusions` and `sonar.cpd.exclusions`.
- Without behavior (`sonar.coverage.exclusions`): `config/**`, `db/migrate/**`, `db/schema.rb`, `app/models/application_record.rb`,
  `app/jobs/application_job.rb`, `app/mailers/application_mailer.rb`, `bin/**`, serializers without logic.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/ruby/ , https://github.com/simplecov-ruby/simplecov
