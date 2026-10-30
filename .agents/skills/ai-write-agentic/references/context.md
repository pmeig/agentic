# ai-write-agentic: context engineering

The context window is a budget: give the smallest set of high-signal tokens that makes the next step correct.

## Rules

1. **Just-in-time retrieval**: keep paths, queries and identifiers; load the content when needed (lazy skills, header-only reads, `grep` before `read`).
2. **Progressive disclosure**: description -> router -> one reference -> linked file. Never pre-load.
3. **Right altitude** in instructions: specific enough to act on, flexible enough not to break on variation; no brittle if-else lists, no vague slogans.
4. **Structured notes outside the window**: a `state.md` (step, decisions, open questions, next) or progress file lets a fresh agent resume; keep it short.
5. **Compaction**: summarise a long history keeping decisions, open issues and file paths; drop raw tool output.
6. **Sub-agent isolation**: send exploration or noisy work to a fresh agent and take back a summary (<= ~40 lines); the lead's context stays clean.
7. **Handoff between steps**: one brief per hop (goal, decisions, Read list, Do-not-read list, done criteria), then the sender stops (`context-handoff`).
8. **Prefix stability**: fixed instructions first, variable data last, so prompt caching applies; do not edit the prefix mid-session.
9. **Quiet tools**: summaries and failures, never full logs or lockfiles.

## Memory

Short-term = the window; long-term = files (`ai-write-memory`, `.agents/docs`). Store decisions and reasons, not transcripts. Verify a remembered fact before acting on it.

## Failure signs

Agent repeats work, forgets a decision, rereads the same files, or contradicts the brief: shrink and sharpen the context, move state to a file, or replace the agent with a fresh one.
