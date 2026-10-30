# Database schema documentation: DBML conversion and generators

## Convert and generate

- **DBML from SQL**: the package ships several binaries, so name the binary: `npx -y -p @dbml/cli sql2dbml schema.sql --postgres -o schema.dbml` (also `--mysql`, `--mssql`; `dbml2sql` for the reverse). Seen on Windows: the CLI crashed on Windows paths; run it in WSL, or validate/convert with the `@dbml/core` API (`Parser.parse(sql, "postgres")` then `ModelExporter`). Always parse the final file to check it.
- **Browsable docs**: `tbls doc <dsn> .agents/docs/data/tbls` (Markdown + Mermaid ER per table, checks with `tbls lint`, `tbls diff`);
  SchemaSpy (Java, JDBC, 12+ databases) for interactive HTML; dbdocs.io for a shared web view of DBML. Pick one generator per project
  and put the command in `commands.md`.
- **Prisma/Drizzle/TypeORM**: use the tool's own export (`prisma-dbml-generator`, `drizzle-kit`) rather than rewriting by hand.
