---
name: doc-database-schema
description: Use to document a database for humans and AIs (SQL, NoSQL, Room/SQLite): extract the real schema from the database or migrations, write DBML + a Mermaid ER diagram + a table dictionary, generate browsable docs with tbls or SchemaSpy, and keep it in sync with migrations.
---

# Database schema documentation

An AI fixing a bug needs: tables and columns, keys, indexes, relations, enums and which feature owns each table. Source of
truth order: **live database > migrations > ORM models > guesses** (mark guesses `(unverified)`).

## Outputs (`.agents/docs/data/`)

1. `schema.dbml`: full structure in DBML (compact, diffable, one read). Tables, column types, `pk`, `not null`, `unique`, `default`,
   `note:`, `Ref:` for every foreign key, `Enum`, `indexes { }`, `Note:` on each table saying the owning feature.
2. `schema.md`: relations as edge lists, no diagram (AI doc): `FK: a.col -> b.col (cascade rule) | ...` and `Logical, no FK: a.col = b.col`, then a dictionary table (table | meaning | owner feature | lifecycle: created by, deleted by | soft delete? | sensitive data?). A Mermaid `erDiagram` belongs only in the human README (`documentation-human`).
   (table | meaning | owner feature | lifecycle: created by, deleted by | soft delete? | sensitive data?).
3. `migrations.md`: tool (Flyway, Liquibase, Prisma, Drizzle, Alembic, EF, Room `schemas/`), folder, naming, how to add one, rollback rule,
   how migrations run in each environment.

## Extract the schema

| Source | How |
|---|---|
| PostgreSQL | `pg_dump --schema-only --no-owner`, or `tbls doc postgres://...`, `SELECT` on `information_schema` |
| MySQL/MariaDB | `mysqldump --no-data`, `tbls`, `information_schema` |
| SQLite / Room | `.schema` in `sqlite3`, Room exported JSON in `schemas/<db>/<version>.json` |
| SQL Server | `sqlcmd` + `INFORMATION_SCHEMA`, `tbls` |
| MongoDB | sample documents (`$sample`) + validators + ORM schemas (Mongoose, Spring Data classes); document shape per collection, index list |
| Redis / key-value | key patterns, types, TTLs, owner code path |
| ORM only (no DB reachable) | read entity/model files and migrations; say it is derived |

Local databases: use the project's own way to start local services (its README/AGENTS.md); never connect to production without the owner's go,
use a copy; never print credentials.

## Convert and generate

- **DBML from SQL**: the package ships several binaries, so name the binary: `npx -y -p @dbml/cli sql2dbml schema.sql --postgres -o schema.dbml` (also `--mysql`, `--mssql`; `dbml2sql` for the reverse). Seen on Windows: the CLI crashed on Windows paths; run it in WSL, or validate/convert with the `@dbml/core` API (`Parser.parse(sql, "postgres")` then `ModelExporter`). Always parse the final file to check it.
- **Browsable docs**: `tbls doc <dsn> .agents/docs/data/tbls` (Markdown + Mermaid ER per table, checks with `tbls lint`, `tbls diff`);
  SchemaSpy (Java, JDBC, 12+ databases) for interactive HTML; dbdocs.io for a shared web view of DBML. Pick one generator per project
  and put the command in `commands.md`.
- **Prisma/Drizzle/TypeORM**: use the tool's own export (`prisma-dbml-generator`, `drizzle-kit`) rather than rewriting by hand.

## What to write for each table (the AI value)

- Business meaning in one line, in the project's domain words (glossary link).
- Columns that are not obvious: units (cents vs euros), time zones, enums and their meaning, nullable-by-design, JSON columns' shape.
- Relations in words: "an `entry` belongs to one `shop` and one `category`; deleting a shop is blocked while entries exist".
- Invariants enforced by the DB (constraints, triggers) versus by the service (say which file).
- Access pattern: the repository file and the main queries; the indexes that make them fast.

## Mermaid ER pitfalls

Types are one token; relation syntax `A ||--o{ B : "has"`; quote labels; split big schemas by area; do not draw every column
of every table (key columns only in the diagram, full list in DBML).

## Procedure

1. Identify engines and tools (`doc-code-analysis`), pick the best source above, extract.
2. Write `schema.dbml`, then `schema.md` and `migrations.md`; add the owner feature to each table.
3. Cross-check: every table in the schema is referenced by a repository or migration, and vice versa; list orphans.
4. Link each feature file (`documentation-ai`) to its tables.

## Sources

- https://dbml.dbdiagram.io/docs · https://github.com/k1LoW/tbls · https://schemaspy.org · https://dbdocs.io

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: check DBML CLI, tbls and SchemaSpy releases and supported databases,
Room/Prisma/Drizzle export changes; update, set the date, report changes.
