# Push, pull request and CI: flaky tests are not green

A check that fails then passes on a rerun, or a test that only passes sometimes, is **not** a pass and is never just rerun. `qa` fixes the cause (procedure in `e2e-run`, `references/flaky.md`), with the owner when the cause is in the code, and shows it stable (several consecutive green runs, in the CI too) before the PR counts as green.
