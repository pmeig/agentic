---
name: documentation-human
description: MANDATORY for the documentalist when writing documentation for HUMANS (README.md, architecture overview, CONTRIBUTING, user guide, changelog, ADR summaries, docs site): structure by reader need (Diátaxis), README skeleton with the architecture, language and tone rules, update rules.
---

# Documentation for humans

AI-facing documentation is `documentation-ai`; this skill is for people: newcomers, contributors, operators, end users. Write it
in **the product's language** (ask when unclear; this team's projects are often French with English code).

## Know the reader first

| Reader | Needs | Where |
|---|---|---|
| New developer | what it is, how to run it in 10 minutes, where code lives | `README.md`, `docs/getting-started.md` |
| Contributor | conventions, branch/PR flow, tests, how to add a feature | `CONTRIBUTING.md`, `docs/contributing/` |
| Operator | deploy, config, secrets, monitoring, runbooks | `docs/operations/` |
| End user | what the app does, how to do each task | `docs/user-guide/` (screenshots allowed) |
| Decision maker | why this architecture, trade-offs | `docs/architecture.md`, `docs/decisions/` |

## Structure by need: Diátaxis

Split any larger documentation into four kinds and never mix them in one page (source: diataxis.fr):
- **Tutorials**: learning by doing, one guaranteed path, a result at the end.
- **How-to guides**: a goal, steps, no theory ("How to add a language").
- **Reference**: exact, complete, neutral, dry (config keys, endpoints, commands). Generate it when possible (`doc-openapi-asyncapi`).
- **Explanation**: why and how it fits together (architecture, trade-offs).

## README skeleton (project and each module)

Every README has the architecture: a diagram, the annotated folder tree and a table of layers.

1. Title, one-sentence purpose, status badges only if they are real and maintained.
2. **What it does**: 3 to 6 lines, the main features.
3. **Architecture**: a Mermaid diagram of the modules and flows (`doc-mermaid`), the annotated folder tree, and a table of layers
   (layer | folder | responsibility). Link to `docs/ai/structure.md` rather than duplicating it.
4. **Quick start**: prerequisites with versions, install, run, test; commands copy-pasteable and checked.
5. **Configuration**: environment variables and secrets by name (never values), where they live.
6. **Features / modules**: table with a link to each module README or feature doc.
7. **Tests and quality**: how to run unit and e2e, coverage and Sonar targets.
8. **Deployment**: how it ships, environments, links to the CI/CD.
9. **Contributing and license**.
A module README repeats only 3, 4 and 7 for that module and links up to the root README.

## Writing rules

- One page = one purpose; headings that say the answer ("Run the tests", not "Testing").
- Short sentences, active voice, second person for instructions, present tense; explain a term the first time or link the glossary.
- Every command in a fenced block with the language tag, run it before publishing; every path in backticks and existing.
- Diagrams as Mermaid text (diffable, rendered by GitHub); screenshots only for UI, with alt text, dated, stored in `docs/assets/`.
- Numbers, versions and ports come from the code or config, not memory; link to the source instead of copying long content.
- No marketing tone in technical pages; no "simply", "just", "obviously".
- Accessibility: alt text, meaningful link text, no color-only meaning, headings in order.
- Translate human docs only when the lead asks (`translator` agent); keep one source language.

## Other documents

- **CHANGELOG.md**: Keep a Changelog style (Added / Changed / Fixed / Removed), newest first, linked to PRs; generated from conventional
  commits when the project uses them (never invent entries).
- **Architecture overview**: C4 context and container diagrams + the five or six decisions that shape the code (`doc-architecture-c4-adr`).
- **Runbooks**: symptom, check, fix, who to call; tested by someone who did not write them.
- **Docs site**: only when the content outgrows a few Markdown files; choice and setup in `doc-sites-markdown`.

## Procedure

1. Read the code, `docs/ai/` (create it first when missing: it is the cheapest source of truth), existing README and docs.
2. Pick the reader and the Diátaxis kind of each page; list the pages to create or update.
3. Write, then **verify**: links resolve, commands run, versions match the build files, Mermaid renders.
4. Report what changed and what could not be verified.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check Diátaxis (diataxis.fr), GitHub Markdown/Mermaid rendering and Keep a
Changelog for changes, update only confirmed guidance, keep the user's rules, update this date, report changes.
