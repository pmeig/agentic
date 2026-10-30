# Lead playbook: steps 6-7, handover and e2e gate

6. **Handover**: `front` writes `gesture.md` (steps, implied data/rules/errors/edge cases/offline, expected result per step, stable test ids or accessible names); `front` and `back` confirm unit tests are ready.
7. **E2E gate**: `qa` writes the e2e from `gesture.md` and runs locally **only the impacted e2e** (`e2e-run`; the CI runs all on the PR). A failure goes to its owner with the steps; loop. **Only `qa` gives the PR go**, when the impacted e2e are green; nobody pushes before that go and the docs of step 8. **Several platforms: twin e2e** (same scenarios, numbers, names, steps, values, element ids), aligned by `qa`; no go while a twin is missing.

- **One `qa` per feature until the merge**: keep the same `qa` agent (resume it, brief it on `git log` and the contract if its context grows) through red CIs instead of a fresh agent per red; before each push it applies skill `ci-parity-before-push` (CI locale/encoding/screen), and at a red CI all failed and skipped jobs are read and fixed in one push.
- Red locally during a feature: no mode switch; routing in `team-bugfix-mode` -> `references/feature-red-locally.md`.
- Guided tours: when the project has them, `qa` and `front` complete them for the new feature (`guided-tours`).
