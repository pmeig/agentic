# Database schema documentation: extract the schema

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
