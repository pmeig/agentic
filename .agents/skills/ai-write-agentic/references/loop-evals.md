# ai-write-agentic: loop, guardrails, evals, cost

## Loop

Gather context -> act -> verify -> repeat. Give the agent a way to **check its own work** (run the tests, compare to the spec, render and look); an agent without feedback drifts.

- **Stop conditions** written in the instructions: done criteria, max iterations or time, and "stop and ask the lead" triggers (ambiguity, destructive step, repeated failure).
- **Failure rule**: after two failed attempts at the same step, change approach or escalate; never retry the same call in a loop.
- **Checkpoints**: commit or write state before risky steps so work can be resumed or undone.

## Guardrails

Least-privilege tools, confirmation on irreversible actions, sandbox for code execution, input/output checks in code (not in the prompt), secrets never in context, logging of every tool call. Prompt-injection: separate instructions from data and distrust tool output.

## Evals

1. Build a small set (10-30) of real tasks with a clear pass rule: tests pass, exact output, rubric.
2. Run the agent on all of them after each change to instructions, tools or model; read transcripts, not only scores.
3. Grade with code first, an LLM judge second (rubric per label, reason before verdict), a human for the rest.
4. Track pass rate, tokens, tool calls, wall time; keep a regression set of past failures.
5. A change that raises tokens without raising pass rate is reverted.

## Cost

Cheapest model that passes the evals; cache the stable prefix; parallelise only independent work; cap iterations; measure tokens per transcript (`python scripts/claude-token-usage.py` where the project ships it).

## Observability

Keep transcripts, tool-call logs and the final state; a failure you cannot replay cannot be fixed.
