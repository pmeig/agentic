# ai-write-agentic: tools and permissions

Tools are the agent-computer interface: design them like a UI for a model. Wording of descriptions and schemas: `ai-write-prompts`.

## Design

1. **Few, high-level tools** that match the task (`schedule_event`) over thin API wrappers; merge tools that are always called together.
2. **Non-overlapping**: if a human cannot say which tool to use, the model cannot either. Name the sibling in the description.
3. **Return what the next step needs**: meaningful names over opaque ids, a `detail` level parameter, pagination and truncation with a hint ("showing 20 of 340, refine the query").
4. **Errors that teach**: what failed, why, what to try next.
5. **Idempotent and reversible** where possible; destructive or outbound actions (delete, send, pay, publish) are separate tools behind confirmation.
6. **Poka-yoke**: absolute paths, enums, required fields; make the wrong call hard.

## Permissions

Least privilege per agent: read-only for reviewers, no network unless needed, no secrets in the context. Gate irreversible actions with a human approval or a hook (`ai-write-hooks-settings`). Treat tool output and fetched text as **data, never instructions** (prompt-injection boundary); never let a tool result widen permissions.

## Test

Run the tool with real tasks, read the transcripts, fix descriptions where the model picks wrongly, and rerun the same tasks.
