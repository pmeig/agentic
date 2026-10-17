---
name: doc-mermaid
description: Use to draw any diagram as text in Markdown (flowchart, sequenceDiagram, erDiagram, classDiagram, stateDiagram-v2, architecture-beta, C4, gantt): which type for which question, syntax pitfalls, size limits, rendering and validation with mermaid-cli, and when to use another tool.
---

# Mermaid diagrams (default diagram technology, HUMAN docs only)

> AI-facing docs (`docs/ai/`, `AGENTS.md`) use no diagrams: maps and edge lists are cheaper and easier for an AI to parse (`documentation-ai`). Use Mermaid in READMEs, architecture overviews and guides for people.

Mermaid is text: an AI reads and edits it directly, git diffs it, GitHub, GitLab, Docusaurus, VitePress, Starlight and MkDocs render
it. It is the default; mermaid v11 supports 20+ diagram types. Fenced block with the `mermaid` language tag.

## Which type answers which question

| Question | Type | Notes |
|---|---|---|
| What are the parts and how do they connect | `flowchart LR` / `TD` | subgraphs for layers or modules |
| Who calls whom, in what order, for one journey | `sequenceDiagram` | `autonumber`, `alt/opt/loop`, `participant X as Label` |
| Which tables and relations | `erDiagram` | cardinality `\|\|--o{`; generate from the schema (`doc-database-schema`) |
| Classes, interfaces, inheritance | `classDiagram` | only the types that matter, never the whole codebase |
| Lifecycle of an entity | `stateDiagram-v2` | states, transitions, guards in labels |
| Cloud/infrastructure icons and groups | `architecture-beta` | beta: check the renderer supports it, else flowchart |
| System context / containers (C4) | `C4Context`, `C4Container` (experimental) or flowchart styled as C4 | see `doc-architecture-c4-adr` |
| Plan, milestones | `gantt`, `timeline` | |
| User journey, mind map, git graph, quadrant, sankey | `journey`, `mindmap`, `gitGraph`, `quadrantChart`, `sankey-beta` | rarely needed |

## Rules that keep diagrams useful

1. **One diagram = one question**, 5 to 15 nodes. More: split by layer or feature and link the pieces.
2. **Real names**: use the identifiers of the code (class, route, table) so an AI can grep them; label arrows with the verb or payload.
3. **Direction**: `LR` for flows and pipelines, `TD` for hierarchies; sequence diagrams read top to bottom in time order.
4. **Stable ids, readable labels**: `svc[OrderService]`; quote labels with punctuation `A["POST /orders (auth)"]`.
5. **Source of truth in text**: put a one-line caption above the block saying what it shows and its commit/date.
6. Do not rely on colors alone (accessibility): use shapes or labels too; keep styling minimal (`classDef` only for 2 to 3 groups).
7. For an AI, a table next to the diagram (node | path) is worth more than extra styling.

## Pitfalls (common render failures)

- Reserved word `end` in a flowchart label: wrap in quotes or write `End`.
- Parentheses, brackets, `#`, `;` or `:` inside labels: quote the label.
- `erDiagram` attribute types are single tokens (`varchar` not `varchar(255)`: write it in a comment or alias).
- In `sequenceDiagram` use `participant` aliases; semicolons end statements.
- Very large graphs make GitHub time out: cap the size, split.
- `architecture-beta` and some C4 syntax depend on the Mermaid version of the viewer; fall back to `flowchart` when unsure.

## Validate and render

```bash
# validate / render one block or file (Node; run through the project's node-version rules)
npx -y @mermaid-js/mermaid-cli -i diagram.mmd -o diagram.svg      # also .png / .pdf
npx -y @mermaid-js/mermaid-cli -i README.md -o out.md             # renders every mermaid block of a Markdown file
```

A parse error exits non-zero: use it as the check before delivering. Where Node is unavailable, state `(render not checked)`.
Keep the `.mmd` source; commit images only when a viewer cannot render Mermaid.

## When not Mermaid

| Need | Alternative |
|---|---|
| Very large or precisely laid-out architecture, many nested boxes | D2 or PlantUML + C4-PlantUML, Structurizr DSL (model once, many views) |
| Hand-drawn whiteboard feel, workshops | Excalidraw (`.excalidraw` JSON, exports SVG) |
| Pure graph analysis (dependencies) | Graphviz `dot`, or tool output (`doc-code-analysis`) |
Check that the viewer of the readers renders the chosen tool; otherwise export SVG and keep the source beside it.

## Sources

- https://mermaid.js.org (syntax per diagram type, release notes)
- https://github.com/mermaid-js/mermaid-cli (mmdc)
- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams

## Monthly refresh

Last refreshed: 2026-10 (Mermaid v11 line, `architecture-beta` still beta). At first use in a later month: check the Mermaid
release notes and the mermaid-cli version, new diagram types, GitHub's supported Mermaid version; update, set the date, report.
