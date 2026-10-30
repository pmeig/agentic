# Mermaid diagrams: syntax pitfalls and size limits

## Pitfalls (common render failures)

- Reserved word `end` in a flowchart label: wrap in quotes or write `End`.
- Parentheses, brackets, `#`, `;` or `:` inside labels: quote the label.
- `erDiagram` attribute types are single tokens (`varchar` not `varchar(255)`: write it in a comment or alias).
- In `sequenceDiagram` use `participant` aliases; semicolons end statements.
- Very large graphs make GitHub time out: cap the size, split.
- `architecture-beta` and some C4 syntax depend on the Mermaid version of the viewer; fall back to `flowchart` when unsure.
