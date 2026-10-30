# Context handoff: the lead launches the next agent (every gate)

1. The lead updates `state.md` (1-2 lines), then starts the next agent with a prompt of **at most 10 lines**: role, `state.md` path, brief path, done criteria. No pasted content, no recap.
2. The lead clears its own context at every gate (user choice made, contract agreed, qa go, docs done, PR opened): `/clear`, then reads `state.md` only. Long step with no gate: `/compact` with the focus "state.md + open decisions".
3. After a merge: `state.md` is archived (deleted) with the feature folder when the lead closes the feature.

## Check before starting an agent

Prompt <= 10 lines? Brief <= 40 lines? Read list explicit? Do-not-read list explicit? Old agent ended? If one answer is no, fix it before launching.

