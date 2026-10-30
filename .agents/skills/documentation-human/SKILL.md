---
name: documentation-human
description: "MANDATORY for the documentalist writing docs for HUMANS (README, architecture, guides, changelog, ADR): Diátaxis, README skeleton, tone, update rules."
---
# Documentation for humans (router)
AI-facing documentation is `documentation-ai`; this skill is for people: newcomers, contributors, operators, end users. Write it
in **the product's language** (ask when unclear; this team's projects are often French with English code).
Load only the row(s) that match the file being written or the question; never load every reference.
## Need -> file
| Need (which document / action) | Load |
|---|---|
| Who reads it, where it lives, Diátaxis kinds | `references/readers-diataxis.md` |
| README (project or module) | `references/readme.md` |
| Style, commands, diagrams, accessibility | `references/writing-rules.md` |
| CHANGELOG, architecture overview, runbooks, docs site | `references/other-documents.md` |
| Procedure and final report | `references/procedure.md` |
| Monthly refresh | `references/maintenance.md` |
