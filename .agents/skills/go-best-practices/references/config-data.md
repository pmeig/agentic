# Go best practices: configuration, logging and SQL

- Config from the environment loaded once into a typed struct at startup (secrets from Vault/env, never in code); `log/slog` structured logging with request ids, no personal data.
- SQL: `database/sql` + pgx or sqlc-generated queries, parameters only, migrations numbered (`sql-best-practices`).
