---
name: java-best-practices
description: "MANDATORY for any .java file, pom.xml or Java unit test: Lombok always, JUnit 5 @Nested per public method, final, records, streams, Java 25+."
---
# Java best practices (router)
Current Java practice; the project's own `CLAUDE.md` / skills win. Load only the row(s) that match the task; never load every reference.
## Need -> file
| Need (what the agent is doing) | Load |
|---|---|
| Creating a module, pom.xml, JDK, dependencies, Lombok build config | `references/setup.md` |
| Writing or reviewing Java code (style, null, exceptions, modern Java) | `references/code.md` |
| Lombok annotations, records, value classes | `references/lombok.md` |
| Naming, layering | `references/structure.md` |
| Writing or reviewing unit tests | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
| Spring code | skill `spring-boot-best-practices` |
