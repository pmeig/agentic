# Database schema documentation: procedure

## Procedure

1. Identify engines and tools (`doc-code-analysis`), pick the best source above, extract.
2. Write `schema.dbml`, then `schema.md` and `migrations.md`; add the owner feature to each table.
3. Cross-check: every table in the schema is referenced by a repository or migration, and vice versa; list orphans.
4. Link each feature file (`documentation-ai`) to its tables.

Also load `references/extract-schema.md` (step 1), `references/outputs.md` (step 2) and `references/table-dictionary.md`.
