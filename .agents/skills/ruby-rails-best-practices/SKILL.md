---
name: ruby-rails-best-practices
description: MANDATORY when writing, reviewing or testing Ruby or Ruby on Rails code: the team's conventions transposed to Rails - thin controllers, service objects for business rules, query objects/scopes for data access, strong parameters, migrations never edited, RuboCop, RSpec with one describe per public method and context/it should ... when ... - plus current Rails 8 practices.
---

# Ruby / Rails best practices

The user has no Ruby project yet: these rules transpose the team's conventions to idiomatic Rails.

## 1. Setup

- Latest Ruby (`.ruby-version`) and Rails 8, Bundler with a committed `Gemfile.lock`, RuboCop (`rubocop-rails`, `rubocop-rspec`) and Brakeman in CI, `bundler-audit` for dependencies.
- Rails 8 defaults where they fit: Solid Queue/Cache/Cable, Propshaft, Kamal for deployment, built-in authentication generator.

## 2. Code

- Layering: controller (params, authorization, render/status) → service object (`app/services/expenses/create.rb`, one public `call`) → model/query object (scopes, `app/queries`) → database. Models keep validations, associations and simple domain methods; no business workflow in callbacks.
- Strong parameters (`params.expect(expense: [:amount, :date])`), authorization with Pundit/Action Policy, identity from the session/token, never params.
- Data: migrations never edited once applied, constraints in the database (null, foreign keys, unique indexes) as well as validations, `includes`/`preload` against N+1 (Bullet in development), `find_each` for batches, parameters only in raw SQL (`sql-best-practices`).
- Errors: domain error classes, `rescue_from` in a base controller rendering problem details for APIs; never rescue `Exception`.
- Config and secrets from credentials/environment (Vault in deployment), never committed in clear; structured logging with request ids, `filter_parameters` for personal data.
- Ruby style: `frozen_string_literal: true`, small methods, keyword arguments, `snake_case` methods/files, `CamelCase` classes, `SCREAMING_SNAKE_CASE` constants; YARD comments on public service APIs.
- Front end: Hotwire (Turbo + Stimulus) by default; accessibility and responsiveness per `ui-responsive-accessible-modular`.

## 3. Tests (RSpec)

- `spec/` mirroring `app/`; **one `describe '#method'` (or `'.method'`) per public method**, `context 'when ...'`, `it 'should ...'` style descriptions (`it 'saves the expense'` under `context 'when the input is valid'`).
- `let`/`subject` for setup, FactoryBot factories (no fixtures sprawl), `instance_double` for collaborators, `travel_to` for time, request specs for APIs, system specs (Capybara) or Playwright for e2e.
- Cover every branch and error path; SimpleCov coverage for Sonar.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with a table of cases iterated inside the `describe` of the method (`[...].each { |input, expected| it "..." }`) or shared examples. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, check official sources for version, practice, and deprecation changes. Update only internet-derived
guidance; preserve user/project rules. Add source URLs, update this date, and briefly report changes.
