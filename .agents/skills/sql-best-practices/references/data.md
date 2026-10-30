# SQL and NoSQL best practices: schema (DDL)

- Uppercase keywords and types, singular lower_snake tables (`expense`, `tutorial_video`), lower_snake columns, booleans `is_xxx`/`active`, columns aligned, `NOT NULL` explicit.
- Types: `UUID DEFAULT gen_random_uuid()` (or identity `BIGINT GENERATED ALWAYS AS IDENTITY`), sized `VARCHAR(n)` for bounded text, `TEXT` for free/encrypted text, `NUMERIC(p,s)` for money (never float), `DATE`, `TIMESTAMPTZ` (never naive timestamps), `BOOLEAN` with default, `JSONB` for truly schemaless parts only, `BYTEA` for small binaries.
- Audit columns on every table: `created_at TIMESTAMPTZ NOT NULL DEFAULT now()`, `created_by VARCHAR(100) NOT NULL`, `updated_at TIMESTAMPTZ`, `updated_by VARCHAR(100)` (NULL until the first update); seeds use `created_by = 'migration'`.
- Named constraints: `<table>_pk`, `<table>_<cols>_uk`, `<table>_<col>_fk`, `chk_<table>_<rule>`, indexes `idx_<table>_<cols>`; `ON DELETE CASCADE` only for owned children.
- Partial unique indexes for nullable keys (`WHERE subscriber IS NULL`), expression indexes for case-insensitive uniqueness (`lower(alias)`), generated columns for derived keys (`GENERATED ALWAYS AS (...) STORED`), soft delete with `active BOOLEAN NOT NULL DEFAULT true`.
- `COMMENT ON COLUMN` for non-obvious meanings (what true/false/NULL mean). Normalize to 3NF, denormalize only with a measured reason.
- Personal data: encrypted columns (deterministic encryption when it must be a key or searched), no secrets in plain text, least-privilege roles (app role owns no superuser rights).
