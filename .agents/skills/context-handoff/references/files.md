# Context handoff: files and formats

| File | Owner | Max | Content |
|---|---|---|---|
| `state.md` | lead | 15 lines | step done / current / next, decisions taken (1 line each), open questions, ids of live agents, branch |
| `brief-<from>-<to>.md` | the agent that finishes | 40 lines | what was decided, what to do, **Read** (paths, in order), **Do not read** (paths/topics out of scope), done criteria |
| `gesture.md` | front | 2 KB | user steps table, edge cases, offline/permissions — machine-first |
| `contract.md` | front + back | 3 KB | endpoints table, schemas, pagination, versioning — machine-first |
| `qa.md` | qa | 2 KB | test plan table: scenario, path, gesture steps, expected — machine-first |
| `brief-<dev>-documentalist.md` | front / back | 20 lines | changed files, routes, schemas, keys, e2e — machine-first table |

All in `.agents/docs/team/<feature>/`, local only (gitignored).

A brief never copies a deliverable: it links the path and the lines that matter. No history, no rejected options.
Templates and section budgets: `references/brief-formats.md`. SendMessage rules: `references/sendmessage-rules.md`.
