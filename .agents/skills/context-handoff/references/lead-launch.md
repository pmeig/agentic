# Context handoff: the lead launches the next agent (every gate)

1. The lead updates `state.md` (1-2 lines), then starts the next agent with a prompt of **at most 10 lines**: role, `state.md` path, brief path, done criteria. No pasted content, no recap.
2. The lead clears its own context at every gate (user choice made, contract agreed, qa go, docs done, PR opened): `/clear`, then reads `state.md` only. Long step with no gate: `/compact` with the focus "state.md + open decisions".
3. After a merge: `state.md` is archived (deleted) with the feature folder when the lead closes the feature.

## Check before starting an agent

Prompt <= 10 lines? Brief <= 40 lines? Read list explicit? Do-not-read list explicit? Old agent ended? If one answer is no, fix it before launching.

## Context hygiene (images, long-lived builders and resumed agents cost the most; everything in a context is paid again at each turn)

- **Each step ends with a brief and a stop**: the finishing agent writes `team/<feature>/brief-<from>-<to>.md` (<= 40 lines: decisions, tasks, Read list, Do-not-read list, done criteria), deletes its scratch and ends; it is not resumed. The next agent starts cold with its agent file, its brief and the listed paths, nothing else.
- **The lead clears its context at every gate** (mockup chosen, contract agreed, qa go, docs done, PR opened): `team/<feature>/state.md` (<= 15 lines: step, decisions, open questions, next) is the only memory carried; launch prompts <= 10 lines with paths, never pasted content.
- Strict minimum per agent (`references/read-minimum.md`): designer never reads code; front never reads proposals or back code; back never reads mockups; qa never reads source.
