---
name: doc-database-schema
description: "Use to document a database: extract the real schema, DBML + ER diagram + table dictionary, tbls/SchemaSpy, keep in sync with migrations."
---
# Database schema documentation (router)
An AI fixing a bug needs: tables and columns, keys, indexes, relations, enums and which feature owns each table. Source of
truth order: **live database > migrations > ORM models > guesses** (mark guesses `(unverified)`).
Load only the row(s) that match the file being written or the question; never load every reference.
## Need -> file
| Need (which document / action) | Load |
|---|---|
| Which files to produce in `.agents/docs/data/` | `references/outputs.md` |
| Extract the real schema (per engine) | `references/extract-schema.md` |
| SQL -> DBML, tbls, SchemaSpy, ORM exports | `references/dbml-convert.md` |
| What to write per table, Mermaid ER pitfalls | `references/table-dictionary.md` |
| Procedure and cross-check | `references/procedure.md` |
| Monthly refresh, sources | `references/maintenance.md` |
