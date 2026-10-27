---
name: kotlin-best-practices
description: "MANDATORY for any .kt file or Kotlin unit test (Spring, Android): val and data classes, constructor injection, JUnit 5 @Nested per public method, mockito-kotlin."
---
# Kotlin best practices (router)
Current Kotlin practice; the project's own rules win. Load only the row(s) that match the task; never load every reference.
## Need -> file
| Need (what the agent is doing) | Load |
|---|---|
| Creating a module, Kotlin build, plugins, test libs | `references/setup.md` |
| Writing or reviewing Kotlin code (style, nullability, scope functions) | `references/code.md` |
| Error handling (exceptions, `runCatching`, `Result`) | `references/errors-logging.md` |
| Coroutines, Flow, Spring injection | `references/async-spring.md` |
| Writing or reviewing unit tests | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
| Spring code | skill `spring-boot-best-practices` |
