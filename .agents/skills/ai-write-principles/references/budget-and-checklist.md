# ai-write-principles: size budget and review checklist

## Size budget

| File | Target |
|---|---|
| `AGENTS.md` / `CLAUDE.md` | read in full every session: as short as possible (`doc-ai-context-files`) |
| Agent definition | body <= ~100 lines; procedures live in skills |
| Skill router (`SKILL.md`) | ~1-1.5 KB |
| Skill reference | ~1-4 KB, one need |
| Slash command | <= ~40 lines |
| Memory file | one fact, <= ~15 lines |

Over budget: split by need or delete the least useful lines. Do not go so telegraphic that a cold reader cannot parse it.

## Review checklist (before delivering)

- English, valid frontmatter, every path and command exists or is marked `(not run)`.
- No duplicate of another file's rule; no contradiction with `AGENTS.md`.
- Description says **when**, never **what is inside**.
- Cold-agent test done, result noted in the report.
- No secrets, tokens or personal data.

