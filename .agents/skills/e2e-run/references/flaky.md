# E2E run: flaky tests, fix them, never hide them

**A test that passes only on rerun, or only sometimes, is flaky, not a pass.** No automatic retries to hide it (a retry setting only detects flakiness; the run is reported flaky). `qa` fixes the cause, with the owner (`front`/`back`) when the cause is in the code:
1. **Reproduce**: rerun the single test several times (10) alone, then in parallel with the others, then under load; note the failing step and the trace/screenshot of failures only.
2. **Find the cause**, most frequent first: a fixed sleep instead of waiting for a state; a transient element (toast, snackbar, animation) the test cannot catch; shared data or order dependency between tests (one account/dataset per test); port, folder or resource conflict between workers; a race (request not finished, element not yet interactive); machine load (try fewer workers); time zone, locale or date at midnight; an external service. A real race in the application is a bug: send it to the owner.
3. **Fix the cause**: wait for the state (never a long fixed sleep), isolate the data, give each worker its own ports and outputs, assert on the final state, stabilize the clock; do not weaken the assertion or widen a timeout without a cause.
4. **Prove it**: the test passes repeatedly (the 10 alone, then the whole selection several times, then in the CI), and the result is stated in the report.
5. **Record the case** (symptom, cause, fix) for `documentalist` to add to the project's gotchas, so it is not rediscovered.
Two failed fixes on the same flaky test: report to the lead with what was tried instead of looping.
