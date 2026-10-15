---
name: sql-best-practices
description: MANDATORY for any schema, migration or query (PostgreSQL first, also MySQL/SQL Server/Oracle) and SQL vs NoSQL choices: numbered immutable migrations, naming, constraints, indexes, transactions.
---

# SQL and NoSQL best practices

Based on `D:\projects\typescript\budget\server\src\db\migrations` and its repositories (PostgreSQL), `rpg` (node-pg-migrate TS),
`spring-libraries` (JPA), plus current practice. Data access layering: `node-api-architecture` / `spring-boot-best-practices`.

## 1. Migrations

- Numbered files `NNN_snake_case_topic.sql` (or the tool's format: Flyway `V<n>__topic.sql`, node-pg-migrate), applied in order with a lock (`advisoryLockMode: 'wait'`) so several instances can start together; history table in a `config` schema.
- **An applied migration is never edited**: add a new one. Forward-only in production; a destructive change is split (add, back-fill, switch code, drop later).
- Header on every file: `-- NNN_name: one-line purpose`, then `--` lines on the design choices (why no FK, what NULL means, how existing rows are back-filled).
- Test a migration on a copy of the production data before merging when it rewrites rows or adds constraints; large tables: `CREATE INDEX CONCURRENTLY`, batched updates.

## 2. Schema (DDL)

- Uppercase keywords and types, singular lower_snake tables (`expense`, `tutorial_video`), lower_snake columns, booleans `is_xxx`/`active`, columns aligned, `NOT NULL` explicit.
- Types: `UUID DEFAULT gen_random_uuid()` (or identity `BIGINT GENERATED ALWAYS AS IDENTITY`), sized `VARCHAR(n)` for bounded text, `TEXT` for free/encrypted text, `NUMERIC(p,s)` for money (never float), `DATE`, `TIMESTAMPTZ` (never naive timestamps), `BOOLEAN` with default, `JSONB` for truly schemaless parts only, `BYTEA` for small binaries.
- Audit columns on every table: `created_at TIMESTAMPTZ NOT NULL DEFAULT now()`, `created_by VARCHAR(100) NOT NULL`, `updated_at TIMESTAMPTZ`, `updated_by VARCHAR(100)` (NULL until the first update); seeds use `created_by = 'migration'`.
- Named constraints: `<table>_pk`, `<table>_<cols>_uk`, `<table>_<col>_fk`, `chk_<table>_<rule>`, indexes `idx_<table>_<cols>`; `ON DELETE CASCADE` only for owned children.
- Partial unique indexes for nullable keys (`WHERE subscriber IS NULL`), expression indexes for case-insensitive uniqueness (`lower(alias)`), generated columns for derived keys (`GENERATED ALWAYS AS (...) STORED`), soft delete with `active BOOLEAN NOT NULL DEFAULT true`.
- `COMMENT ON COLUMN` for non-obvious meanings (what true/false/NULL mean). Normalize to 3NF, denormalize only with a measured reason.
- Personal data: encrypted columns (deterministic encryption when it must be a key or searched), no secrets in plain text, least-privilege roles (app role owns no superuser rights).

## 3. Queries

- One `UPPER_SNAKE` constant per query, named `<VERB>_BY_<CRITERIA>_<ENTITY>` (`FIND_BY_MONTH_EXPENSE`), multi-line, one clause per line, uppercase keywords.
- **Parameters only** (`$1`, `?`, `:name`), never concatenated input; optional filters through a placeholder replaced by a constant fragment or `''` (never `$n IS NULL OR ...`).
- Explicit column lists (no `SELECT *` in application queries), camelCase aliases double-quoted (`is_expense AS "isExpense"`), `jsonb_build_object` for nested shapes, `= ANY($n)` for lists, `RETURNING` instead of a second read.
- Upsert: `INSERT ... ON CONFLICT ON CONSTRAINT <table>_pk DO UPDATE SET col = EXCLUDED.col` (or the partial-index target), audit columns set in the same statement.
- `LIKE/ILIKE` input escaped (`\`, `%`, `_`), ranking prefix matches first (`ORDER BY (name ILIKE $2) DESC, name`); full-text (`tsvector` + GIN) or trigram (`pg_trgm`) indexes for real search.
- Pagination by keyset (`WHERE (date, id) < ($1, $2) ORDER BY date DESC, id DESC LIMIT n`) for large lists; `OFFSET` only for small ones.
- Check plans with `EXPLAIN (ANALYZE, BUFFERS)` for any query on a growing table; index the columns of `WHERE`, `JOIN` and `ORDER BY` in that order of selectivity, and drop unused indexes.

## 4. Transactions

- Read-only transactions for reads, read-write with the default `READ COMMITTED`; `SERIALIZABLE` or `SELECT ... FOR UPDATE` only for real races (counters, balances), with retry on serialization failure.
- Short transactions, no network call inside; nested calls reuse the same connection (AsyncLocalStorage / Spring propagation); a client is destroyed after a failed rollback.
- Idempotent writes (natural keys, upserts, idempotency keys) for anything retried by clients or queues.

## 5. NoSQL: pick the store from the access patterns

| Store | Use for | Key rules |
|---|---|---|
| MongoDB | aggregates read/written as a whole, flexible documents | embed what is read together, reference what grows unbounded; schema validation; indexes on every query filter; transactions only when unavoidable |
| Redis | cache, sessions, rate limits, queues, pub/sub | TTL on every key, namespaced keys (`app:entity:id`), cache-aside with invalidation on write, never the only copy of business data |
| DynamoDB / Cassandra | huge write throughput, known queries | model tables from the queries (partition key spreads load, sort key orders), no scans, denormalize per query |
| Elasticsearch / OpenSearch | full-text search, analytics | derived index fed from the source of truth, explicit mappings |
| Neo4j | relationship-heavy queries | model relationships as first-class, index lookup properties |

- Default to PostgreSQL (relational + JSONB + full-text) unless an access pattern clearly needs another store; document the choice in the contract or the README.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the official sources, update only internet-derived guidance, keep user/project rules, add source URLs, update this date, report changes.
