# AI documentation: token budget

## Token budget (AI docs only; human docs are not shortened)
Reference: a 590-file monorepo, whole folder ~50k tokens, a typical task reads 3-6k.
1. `INDEX.md` (<= 1.2k tokens) gives the reading order, the cost of each file and the rule "one feature file, never the whole folder".
2. **One fact, one place** (a route in `endpoints.md`, a table in `data/schema.*`, a feature's layers in `features/<f>.md`); other files link. Module files hold only module specifics, never the per-feature tables.
3. Caps: feature <= 1.8k tokens, module <= 6k, other <= 2.5k; contract files (OpenAPI, DBML) exempt but "read by section only".
4. Big files by section: `grep -n '^## '` then Read with offset/limit. Flag giant or generated files (data-only migrations, lock files, build output) as "never open".
5. Dense: tables, paths, short bullets; no introductions, repeated context or narrative; no copy of source or long lists that `ls`/`grep` gives.
6. Measure: tokens ~ bytes / 3.6; report total, largest files and typical read path before and after. Remove duplication and prose, never facts, paths or traps.
