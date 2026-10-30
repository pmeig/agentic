# Lead playbook: step 8, documentation

8. **Documentation, last step of every development (mandatory)**: after the `qa` go and **before** any push, `front` and `back` brief `documentalist` (files, routes, tables, screens, keys, tours, e2e touched). It always updates the AI docs (`.agents/docs/`). Human docs (README, guides, changelog) stay light: touched only when the public API, architecture, an install/run command or a user-visible journey changed, and then only the touched section. It verifies, commits on the same branch, reports "docs done" (and "human docs: unchanged" when skipped) to `qa` and the lead. Docs-only commits do not rerun the e2e. No AI docs, not done.

Gate: "docs done" received -> lead updates `state.md`, clears its context, then `references/step-pr.md`.
