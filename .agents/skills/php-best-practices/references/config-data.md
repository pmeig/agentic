# PHP best practices: data, configuration and logging

- Data: Doctrine ORM or Eloquent with migrations, parameters only (no string-built SQL), eager loading against N+1 (`sql-best-practices`).
- Config and secrets from the environment (`.env.local` not committed, Vault in deployment); PSR-3 logging (Monolog) with context arrays, no personal data.
