---
name: rust-best-practices
description: MANDATORY for any Rust code (CLIs, axum/tokio services, libraries): modules by feature, traits, thiserror/anyhow, no unwrap, tests per function, edition 2024.
---

# Rust best practices

The user has no Rust project yet: these rules transpose the team's conventions to idiomatic Rust. A project's own rules win.

## 1. Setup

- Edition 2024, `rust-version` in `Cargo.toml` (Cargo resolves dependencies against it), `Cargo.lock` committed for binaries; workspace (`[workspace]`, shared `[workspace.dependencies]`) for several crates.
- `cargo fmt`, `cargo clippy -- -D warnings` (pedantic where reasonable), `cargo deny`/`cargo audit` in CI.
- Layout: `src/main.rs` (wiring), `src/lib.rs` (public API), one module folder per feature (`expense/{mod.rs, handler.rs, service.rs, repository.rs, model.rs}`), shared `core/`.

## 2. Code

- Layering: handler (axum extractors, status) → service (business rules) → repository (sqlx queries) → infrastructure; dependencies passed as structs holding trait objects or generics (`Arc<dyn ExpenseRepository>`), built in `main`.
- Errors: libraries define typed errors with `thiserror`, binaries use `anyhow` with `.context("...")`; `?` to propagate; **no `unwrap`/`expect` in production paths** (only in tests or with an invariant comment); map domain errors to HTTP responses in one `IntoResponse` impl.
- Ownership: borrow (`&str`, `&[T]`) in parameters, own (`String`, `Vec<T>`) in structs; clone deliberately; `Arc` for shared read-only state, `Mutex`/`RwLock` (tokio versions in async) only when needed.
- Types make invalid states unrepresentable: newtypes for ids and money (`struct ExpenseId(Uuid)`), enums for states, `#[non_exhaustive]` on public enums of libraries, builders for many optional fields.
- Async: tokio runtime, no blocking calls in async code (`spawn_blocking`), structured tasks (`JoinSet`), cancellation-safe `select!`; async closures (2024) where they simplify.
- `unsafe` only with a `// SAFETY:` comment explaining the invariant; `unsafe extern` blocks (2024).
- Config: typed struct from env/files (`serde` + `config`/`figment`) loaded once; secrets never in code; `tracing` for structured logs.
- SQL: `sqlx` with compile-time checked queries, parameters only, migrations in `migrations/` (`sql-best-practices`).
- Naming: `snake_case` functions/modules, `PascalCase` types, `SCREAMING_SNAKE_CASE` constants; `///` doc comments with examples on every public item.

## 3. Tests

- Unit tests in a `#[cfg(test)] mod tests` at the bottom of the file, **one sub-module per public function**, test names `should_<result>_when_<condition>`:
  ```rust
  #[cfg(test)]
  mod tests {
      use super::*;

      mod create {
          use super::*;

          #[test]
          fn should_save_expense_when_input_is_valid() {
              let service = Service::new(FakeRepository::default());

              let result = service.create(valid_input());

              assert!(result.is_ok());
          }

          #[test]
          fn should_fail_when_amount_is_negative() {
              let service = Service::new(FakeRepository::default());

              assert!(matches!(service.create(negative_amount()), Err(ExpenseError::InvalidAmount)));
          }
      }
  }
  ```
- Integration tests in `tests/`, `#[tokio::test]` for async, fakes implementing the traits (or `mockall` when needed), `proptest` for invariants, `insta` for snapshot outputs; cover every `match` arm and error path (`cargo llvm-cov` for coverage).

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `rstest` `#[case]` / `#[values]` (or a table iterated in the test) inside the module of the function. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the official sources, update only internet-derived guidance, keep user/project rules, add source URLs, update this date, report changes.
