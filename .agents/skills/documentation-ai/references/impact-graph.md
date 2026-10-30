# AI documentation: impact graph (`graph.yaml`)

## Impact graph (`graph.yaml`, required)
One YAML (~2k tokens for a mid-size monorepo) so the AI knows what a change touches:
- `roots`: aliases for long prefixes. `shared`: paths whose change can break any scenario (app shell, HTTP client, auth, DB layer, test ids, proxy, compose): a hit means "run all".
- `paths`: prefix -> feature ids (longest prefix wins; shared widgets list every feature using them). `tours`: cross-screen scenarios to run when a screen, an id/anchor or a string changes.
- `features.<id>`: `routes`, `tables`, `unit` (test folders), `e2e` (scenario numbers), `note`. `e2e`: scenario number -> features.
- Header comment = usage. **It defines the local gate**: only the selected scenarios run locally before a push or PR (`qa`, `e2e-run`), the CI runs all. Never a guess: shared path, no matching prefix, stale graph (`commit` older than the code) or doubt = run all. A red outside the selection, or a regression only the CI finds, means the graph is wrong: fix it the same day.
- Build from imports/call chains, controllers, repositories/migrations, test contents; verify every prefix exists (script); in the end-of-development update add new prefixes, routes, tables, scenarios.
