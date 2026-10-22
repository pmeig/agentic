---
name: context-handoff
description: Lead and every agent at each step change of a feature: write a handoff brief, end the agent, start the next one cold with only its brief; /clear the lead between steps.
---

# Context handoff: every step starts with a near-empty context

Principle: a decision is paid once (written in a brief), never carried. The context of a finished step is discarded; the next agent reads **its brief, not the history**.

## Files (`.agents/docs/team/<feature>/`, local only)

| File | Owner | Max | Content |
|---|---|---|---|
| `state.md` | lead | 15 lines | step done / current / next, decisions taken (1 line each), open questions, ids of live agents, branch |
| `brief-<from>-<to>.md` | the agent that finishes | 40 lines | what was decided, what to do, **Read** (paths, in order), **Do not read** (paths/topics out of scope), done criteria |
| existing deliverables | owner | | `need.md`, `design/spec.md`, `contract.md`, `gesture.md` stay the source; briefs only point to them |

A brief never copies a deliverable: it links the path and the 3-10 lines that matter. No history, no rejected options (they stay in `design/` or `decisions.md`, not in the brief).

## Procedure at each step end

1. The finishing agent writes `brief-<from>-<to>.md`, deletes its scratch (review boards, unchosen proposals go to `design/archive/`, never read again), reports in 3 lines to the lead with the brief path, and **stops**. It is not resumed (at most once, for a fix of its own deliverable).
2. The lead updates `state.md` (1-2 lines), then starts the next agent with a prompt of **at most 10 lines**: role, `state.md` path, brief path, done criteria. No pasted content, no recap.
3. The lead clears its own context at every gate (user choice made, contract agreed, qa go, docs done, PR opened): `/clear`, then reads `state.md` only. Long step with no gate: `/compact` with the focus "state.md + open decisions".
4. The next agent reads: its agent file, the brief, the paths in **Read**. Nothing else unless the brief is insufficient: then it asks the previous owner by `SendMessage` (answer one line, written to the brief) instead of exploring.

## Strict minimum per agent (Read / never read)

| Agent | Reads | Never reads |
|---|---|---|
| `designer` | `need.md`, screens `INDEX.md` + the PNGs of the pages concerned, design-system tokens | code, contract, tests, other features |
| `front` | `brief-designer-front.md`, `design/spec.md` + final PNG of the page, `contract.md`, the page's directory, `core` APIs it names | proposals, archived boards, back code, other pages |
| `back` | `contract.md`, `brief-front-back.md`, the module and tables it names | mockups, front code, e2e |
| `qa` | `gesture.md`, impacted e2e files, runner output tail | mockups, source code except ids named in `gesture.md` |
| `documentalist` | `brief-*-documentalist.md` (files/routes/tables touched), INDEX, `graph.yaml`, the feature file | the whole repo; it updates only what the brief lists |
| `translator` | key list with screen, tone, sentence type, length limit, target language | code, design |
| `sales` | `need.md`, final spec summary, store/brand facts | code |

## Cuts inside a step

- Split work larger than ~30 min or ~40 files read into packages, one fresh agent each, each with its own brief (paths owned, checklist).
- Images: only the designer opens them; later agents get the final PNG path, opened at most once, at half scale. The lead never views images except the 3-4 key boards for the user.
- Command output: quiet mode, `tail -n 30`, grep for failures; never paste logs into a brief or message.
- Questions between agents: one line each way, written to the brief if the answer is lasting.
- After a merge: `state.md` is archived (deleted) with the feature folder when the lead closes the feature.

## Check before starting an agent

Prompt <= 10 lines? Brief <= 40 lines? Read list explicit? Do-not-read list explicit? Old agent ended? If one answer is no, fix it before launching.
