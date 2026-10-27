# Lead playbook: step 8, documentation

8. **Documentation, last step of every development (mandatory)**: after the `qa` go and **before** any push, `front` and `back` brief `documentalist` (files, routes, tables, screens, keys, tours, e2e touched); it updates AI and human docs (READMEs, guides, changelog), verifies, commits on the same branch, reports "docs done" to `qa` and the lead. Docs-only commits do not rerun the e2e. No docs, not done.

Gate: "docs done" received -> lead updates `state.md`, clears its context, then `references/step-pr.md`.
