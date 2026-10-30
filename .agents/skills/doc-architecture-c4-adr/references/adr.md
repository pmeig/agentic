# Architecture documentation: C4, arc42, ADR: adr

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
