# ai-write-memory: write and test
# memory: Memory files (write)

Memory carries what a future session cannot derive from the code, git history or `AGENTS.md`. If the repo already records it, store only the non-obvious part (the reason, the preference, the constraint).

## Layout

`memory/<kebab-slug>.md`, one fact per file, plus one line in `MEMORY.md` (`- [Title](file.md) — hook`). The index is loaded every session: one line per memory, no content, no frontmatter.

```markdown
---
name: slug
description: one line, used to decide relevance during recall
metadata:
  type: user | feedback | project | reference
---
<the fact>
**Why:** the reason or incident behind it.
**How to apply:** when and how it changes behaviour.
```

- `user`: role, expertise, preferences. `feedback`: corrections and confirmed approaches (what to avoid and what worked). `project`: goals, deadlines, constraints not in the repo (absolute dates, never "next week"). `reference`: pointers to external systems (URL, dashboard, ticket).
- Link related memories with `[[slug]]`.

## Rules

- Search for an existing memory first; update it rather than duplicate; delete one proven wrong.
- A memory that names a file, function or flag was true when written: verify before acting on it.
- No secrets, credentials or customer data; refer to people by role when the memory may be shared.
- Never store a task transcript, a snippet the repo holds, or a to-do list.
- The description must let a cold session decide relevance without opening the file.

## Test

Read the index alone: can a new session tell which files matter for a given task? If not, rewrite the descriptions.

