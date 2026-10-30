# Ruby / Rails best practices: code

- Layering: controller (params, authorization, render/status) → service object (`app/services/expenses/create.rb`, one public `call`) → model/query object (scopes, `app/queries`) → database. Models keep validations, associations and simple domain methods; no business workflow in callbacks.
- Strong parameters (`params.expect(expense: [:amount, :date])`), authorization with Pundit/Action Policy, identity from the session/token, never params.
- Data: migrations never edited once applied, constraints in the database (null, foreign keys, unique indexes) as well as validations, `includes`/`preload` against N+1 (Bullet in development), `find_each` for batches, parameters only in raw SQL (`sql-best-practices`).
- Errors: domain error classes, `rescue_from` in a base controller rendering problem details for APIs; never rescue `Exception`.
- Config and secrets from credentials/environment (Vault in deployment), never committed in clear; structured logging with request ids, `filter_parameters` for personal data.
- Ruby style: `frozen_string_literal: true`, small methods, keyword arguments, `snake_case` methods/files, `CamelCase` classes, `SCREAMING_SNAKE_CASE` constants; YARD comments on public service APIs.
- Front end: Hotwire (Turbo + Stimulus) by default; accessibility and responsiveness per `ui-responsive-accessible-modular`.
