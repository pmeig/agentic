# Database schema documentation: outputs (`.agents/docs/data/`)

## Outputs (`.agents/docs/data/`)

1. `schema.dbml`: full structure in DBML (compact, diffable, one read). Tables, column types, `pk`, `not null`, `unique`, `default`,
   `note:`, `Ref:` for every foreign key, `Enum`, `indexes { }`, `Note:` on each table saying the owning feature.
2. `schema.md`: relations as edge lists, no diagram (AI doc): `FK: a.col -> b.col (cascade rule) | ...` and `Logical, no FK: a.col = b.col`, then a dictionary table (table | meaning | owner feature | lifecycle: created by, deleted by | soft delete? | sensitive data?). A Mermaid `erDiagram` belongs only in the human README (`documentation-human`).
   (table | meaning | owner feature | lifecycle: created by, deleted by | soft delete? | sensitive data?).
3. `migrations.md`: tool (Flyway, Liquibase, Prisma, Drizzle, Alembic, EF, Room `schemas/`), folder, naming, how to add one, rollback rule,
   how migrations run in each environment.

Also load `references/table-dictionary.md` for what to write per table and `references/extract-schema.md` to get the real schema.
