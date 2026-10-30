# ai-write-principles: token optimization

Goal: the file changes the reader's behaviour for the fewest tokens, at creation time and at every later load. Tokens ~ characters / 4; measure with `wc -c`.

## Where tokens go

| Cost | Paid | Lever |
|---|---|---|
| `description` of every skill and agent | every session | 1-2 sentences, trigger words only, no content summary |
| `AGENTS.md`, memory index | every session | link out; one line per item |
| Router `SKILL.md` | each time the skill triggers | table only, no procedure |
| Reference file | when its need arises | one need per file, ~1-4 KB |
| Maintenance, sources, history | only at refresh | separate `references/maintenance.md`, never in the router |
| Cold-agent test | once per file | `haiku` model, one task, quiet output |

## Techniques

1. **Delete before compressing**: a line that does not change behaviour goes. Then merge duplicates (one rule, one file). Only then shorten wording.
2. **Tables and `key: value` over prose** for lookups; sentences only where a reason must be carried.
3. **Pointers over copies**: cite `references/<file>.md`; never paste another file's rule.
4. **Do not teach what the model knows**: skip generic programming or writing advice; keep only project facts, traps and exact formats.
5. **Lazy by default**: nothing is loaded "just in case"; every reference has a trigger row. Rarely used detail lives one hop away.
6. **Examples**: one minimal example per non-obvious rule, not three; trim it to the lines that teach.
7. **Output of work**: when creating files, write each once (no write-read-rewrite loops); read siblings with a header-only look (`head -20`, `grep -n '^#'`) before reading in full; quiet commands (`| tail`).
8. **Cheapest model that works**: `haiku` for mechanical transformation and cold tests, `sonnet` for judgement.
9. **Measure**: report size before and after (`wc -c`) for any file revised for brevity; a revision that grows a file needs a reason.

## Do not over-compress

Telegraphic text that a cold reader misreads costs more in retries than it saves. Keep articles and verbs where meaning depends on them; cut filler words, hedges, recaps and politeness.
