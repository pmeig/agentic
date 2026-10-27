# SQL and NoSQL best practices: queries

- One `UPPER_SNAKE` constant per query, named `<VERB>_BY_<CRITERIA>_<ENTITY>` (`FIND_BY_MONTH_EXPENSE`), multi-line, one clause per line, uppercase keywords.
- **Parameters only** (`$1`, `?`, `:name`), never concatenated input; optional filters through a placeholder replaced by a constant fragment or `''` (never `$n IS NULL OR ...`).
- Explicit column lists (no `SELECT *` in application queries), camelCase aliases double-quoted (`is_expense AS "isExpense"`), `jsonb_build_object` for nested shapes, `= ANY($n)` for lists, `RETURNING` instead of a second read.
- Upsert: `INSERT ... ON CONFLICT ON CONSTRAINT <table>_pk DO UPDATE SET col = EXCLUDED.col` (or the partial-index target), audit columns set in the same statement.
- `LIKE/ILIKE` input escaped (`\`, `%`, `_`), ranking prefix matches first (`ORDER BY (name ILIKE $2) DESC, name`); full-text (`tsvector` + GIN) or trigram (`pg_trgm`) indexes for real search.
- Pagination by keyset (`WHERE (date, id) < ($1, $2) ORDER BY date DESC, id DESC LIMIT n`) for large lists; `OFFSET` only for small ones.
- Check plans with `EXPLAIN (ANALYZE, BUFFERS)` for any query on a growing table; index the columns of `WHERE`, `JOIN` and `ORDER BY` in that order of selectivity, and drop unused indexes.
