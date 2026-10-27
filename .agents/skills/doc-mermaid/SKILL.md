---
name: doc-mermaid
description: "Use to draw diagrams as text in Markdown (HUMAN docs): type per question, syntax pitfalls, size limits, mermaid-cli validation."
---
# Mermaid diagrams (router)
Default diagram technology, HUMAN docs only. Load only the row(s) that match the file being written or the question; never load every reference.
## Always (every use)
> AI-facing docs (`.agents/docs/`, `AGENTS.md`) use no diagrams: maps and edge lists are cheaper and easier for an AI to parse (`documentation-ai`). Use Mermaid in READMEs, architecture overviews and guides for people.
## Need -> file
| Need (which document / action) | Load |
|---|---|
| Which diagram type for the question | `references/diagram-choice.md` |
| Writing rules (size, names, direction, accessibility) | `references/diagram-rules.md` |
| Render failures, syntax pitfalls, size limits | `references/syntax-pitfalls.md` |
| Validate / render with mermaid-cli | `references/validate-render.md` |
| Alternatives (D2, PlantUML, Excalidraw, Graphviz) | `references/when-not-mermaid.md` |
| Monthly refresh, sources | `references/maintenance.md` |
