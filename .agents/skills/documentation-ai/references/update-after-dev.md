# AI documentation: update after a development

## Update after a development (last step of every dev)
After the `qa` go, before the push or PR: `git diff <base>...HEAD --stat` and read the diff; update `graph.yaml`, touched feature files (Change set, rules, traps), `api/*`, `data/*`, `structure.md` if a folder moved, glossary, the `commit` stamp of each touched file and INDEX counts; keep the token budget; verify; commit docs only on the same branch.

Also load `references/token-budget.md` (caps) and, for `graph.yaml`, `references/impact-graph.md`.
