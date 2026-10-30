# ai-write-agentic: patterns

Rule zero: use the simplest design that works. Add a layer only when a measured failure demands it.

## Workflow or agent

| Choose | When | Cost |
|---|---|---|
| Single LLM call (+ retrieval, examples) | task fits one prompt | lowest |
| **Workflow**: code fixes the steps | steps known in advance, predictability matters | low, testable |
| **Agent**: the model decides the steps and tools in a loop | open-ended, unknown number of steps, needs feedback from the environment | highest, least predictable |

## Workflow patterns

- **Prompt chaining**: fixed sequence, a gate between steps (validate, then continue).
- **Routing**: classify the input, send it to a specialised prompt or model (cheap model for easy cases).
- **Parallelization**: independent subtasks at once (sectioning) or the same task several times (voting).
- **Orchestrator-workers**: a lead splits a task whose subtasks are not known upfront, workers run them, the lead merges.
- **Evaluator-optimizer**: one produces, one critiques against clear criteria, loop until accepted or a cap.

## Multi-agent

Split into several agents only for: a context that would not fit or would drown the task, truly parallel independent work, or distinct tool/permission sets. Each agent owns disjoint files or outputs; two agents never write the same file. Pass **paths and short briefs**, not content; each worker returns a small structured result. A subagent is a fresh context: brief it fully (goal, files, done criteria), since it sees nothing else.

Costs to price before splitting: tokens (every agent reloads its instructions), coordination errors, merge effort. Start with one agent; add a second only for a stated gain.

## Roles

One role = one reason to exist, one owner of outputs, explicit questions it may ask peers. Avoid roles that only relay. Name an owner for each shared file or contract.
