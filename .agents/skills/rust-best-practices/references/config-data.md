# Rust best practices: configuration, logging and SQL

- Config: typed struct from env/files (`serde` + `config`/`figment`) loaded once; secrets never in code; `tracing` for structured logs.
- SQL: `sqlx` with compile-time checked queries, parameters only, migrations in `migrations/` (`sql-best-practices`).
