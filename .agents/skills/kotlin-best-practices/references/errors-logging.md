# Kotlin best practices: errors

- Errors: domain exceptions with a code; `runCatching` only at boundaries and never swallowing `CancellationException`; `Result`/sealed types for expected failures in app code.

Logging rule (no `println`, logger, no secrets): `references/code.md`.
