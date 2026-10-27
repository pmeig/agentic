# Context handoff: files and formats

| File | Owner | Max | Content |
|---|---|---|---|
| `state.md` | lead | 15 lines | step done / current / next, decisions taken (1 line each), open questions, ids of live agents, branch |
| `brief-<from>-<to>.md` | the agent that finishes | 40 lines | what was decided, what to do, **Read** (paths, in order), **Do not read** (paths/topics out of scope), done criteria |
| existing deliverables | owner | | `need.md`, `design/spec.md`, `contract.md`, `gesture.md` stay the source; briefs only point to them |

All in `.agents/docs/team/<feature>/`, local only.

A brief never copies a deliverable: it links the path and the 3-10 lines that matter. No history, no rejected options (they stay in `design/` or `decisions.md`, not in the brief).
