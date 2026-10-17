---
name: doc-architecture-c4-adr
description: Use to document the architecture of a project: C4 model levels (context, containers, components), deployment view, arc42 section map, and Architecture Decision Records (ADR) with the Markdown template; drawn as Mermaid text.
---

# Architecture documentation: C4, arc42, ADR

## C4 model (what to draw, in order)

| Level | Question | Audience | Draw it when |
|---|---|---|---|
| 1 Context | Who uses the system, which external systems does it touch? | everyone | always |
| 2 Containers | Which deployable/runnable parts (web app, API, mobile app, database, queue, runner) and how do they talk (protocol)? | developers, ops | always |
| 3 Components | Inside one container, which modules/layers and their dependencies? | developers | per complex container only |
| 4 Code | classes | rarely | never by hand; generated if needed |

Plus a **deployment view** (environments, hosts, images, network, secrets store) and a **dynamic view** (a numbered journey, as a
`sequenceDiagram`, see `documentation-ai` flows).

- Draw with Mermaid (`doc-mermaid`) in the HUMAN architecture doc; the AI version (`.agents/docs/architecture.md`) is an edge list `a -> b (protocol)` plus a table, no diagram.
  experimental, check the viewer. Use Structurizr DSL when the model is large and needs several views from one source.
- Each box: name (as in the repository), technology, one-line responsibility; each arrow: protocol and payload.
- Put the folder next to each container (`web/`, `server/`, `android/`) so the diagram maps to the tree.

## arc42 as the checklist of a full architecture document

1 Goals and constraints · 2 Constraints · 3 Context and scope · 4 Solution strategy · 5 Building blocks (= C4 containers/components) ·
6 Runtime view (journeys) · 7 Deployment · 8 Cross-cutting concepts (auth, errors, i18n, offline, logging) ·
9 Decisions (ADRs) · 10 Quality requirements · 11 Risks and debt · 12 Glossary.
Use only the sections the project needs; the human doc is `docs/architecture.md`, the AI doc is `.agents/docs/architecture.md` (same
diagrams, shorter prose, more paths).

## ADR (Architecture Decision Record)

One file per decision in `docs/decisions/NNNN-short-title.md` (append-only: a changed decision gets a new ADR that supersedes the old
one, whose status becomes `superseded by NNNN`). Write one when a choice is hard to reverse, surprising, or debated; recover old ones
from `git log`, PR descriptions and `need.md`/`contract.md` of the team (`.agents/docs/team/`).

```markdown
# NNNN. Title in the form of the decision
- Status: proposed | accepted | superseded by NNNN | deprecated
- Date: YYYY-MM-DD
- Deciders: roles (lead, back, front...)

## Context
Forces at play: need, constraints, existing stack, cost, deadline.

## Options considered
1. Option A: pros, cons.
2. Option B: pros, cons.

## Decision
We choose X because ... (one paragraph).

## Consequences
Good, bad, what we must now do or watch; how to revisit.
```

Index: `docs/decisions/README.md` table (number | title | status | date). Keep ADRs short (one screen).

## Procedure

1. Read build files, compose/CI files, deployment folders, `README.md`, existing diagrams.
2. Draw context, then containers, then deployment; components only for the container the task touches.
3. List cross-cutting concepts with the file that implements each (auth middleware, error handler, i18n loader, offline queue).
4. Recover or write ADRs for the decisions that shape the code; link them from the architecture file.
5. Verify every box maps to a folder or image and every arrow to real code or config; mark gaps `(unverified)`.

## Sources

- https://c4model.com · https://arc42.org · https://adr.github.io · https://structurizr.com

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: check c4model.com, arc42 template version, ADR tooling (adr-tools, log4brains),
Structurizr and Mermaid C4 support; update, set the date, report changes.
