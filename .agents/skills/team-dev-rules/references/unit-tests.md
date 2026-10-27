# Team development rules: unit tests

- **Unit tests** (`front`, `back`): yours, for all code with behavior, in the same change. One nested group per public method, parameterized tests first, **every condition exercised** (branch, `&&`/`||` operand, ternary, optional chaining, null/empty check, error path, boundary). **Every loop** (`for`, `while`, `map`/`forEach`, streams, recursion, retries, pagination) gets at least **3 iterations**, plus the empty case and the exits (`break`, `continue`, limit).
- **Run little while building**: only the impacted specs (`vitest --related`, one Gradle test class); the full suite, build and coverage once at the end. Quiet output: failures and summary only.
- Test language and locale: `references/test-language.md`. Coverage target: `references/coverage.md`.
