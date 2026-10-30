# Database schema documentation: table dictionary and ER diagram

## What to write for each table (the AI value)

- Business meaning in one line, in the project's domain words (glossary link).
- Columns that are not obvious: units (cents vs euros), time zones, enums and their meaning, nullable-by-design, JSON columns' shape.
- Relations in words: "an `entry` belongs to one `shop` and one `category`; deleting a shop is blocked while entries exist".
- Invariants enforced by the DB (constraints, triggers) versus by the service (say which file).
- Access pattern: the repository file and the main queries; the indexes that make them fast.

## Mermaid ER pitfalls

Types are one token; relation syntax `A ||--o{ B : "has"`; quote labels; split big schemas by area; do not draw every column
of every table (key columns only in the diagram, full list in DBML).
