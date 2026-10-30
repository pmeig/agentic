# E2E run: selecting the e2e to run (local gate)

Locally run **only the scenarios the change impacts**; once they are green the push or the PR may happen, and the CI then runs **every** e2e. This skill is self-contained: the selection input is the project's impact graph, `.agents/docs/graph.yaml`, kept by `documentalist`.
1. Changed files: `git diff --name-only <base>...HEAD` plus uncommitted files.
2. For each file, take the longest matching prefix in `paths` of the graph -> features -> their `e2e` scenario numbers. Add the scenarios created or edited in this change, and the cross-screen scenarios (`tours` key: guided tours, every-page walks) when a screen, an element id/anchor or a text changed.
3. **Run all instead** when: a file is under `shared`, no prefix matches, the graph is missing or older than the code (its `commit` stamp against `git log`), the change is a merge bringing unknown content, or you doubt. A selection is never a guess.
4. No graph: read the diff and the test names, select the same way, say it in the report and lean towards running more; ask `documentalist` to build the graph.
5. Several platforms: select by scenario number on every platform; run the reference platform first, then its twins (twin rule in `references/twin-e2e.md`).
6. A red scenario outside the selection, or a regression only the CI finds, means the graph is wrong: report it to `documentalist` to fix `graph.yaml`, and rerun with the corrected selection.
7. Report which scenarios ran and why.
