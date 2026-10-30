# Mermaid diagrams: choosing the diagram type

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

Also load `references/diagram-rules.md` to write the diagram and `references/when-not-mermaid.md` if Mermaid does not fit.
