---
name: sonar-kotlin
description: Only when asked: Sonar setup, coverage, exclusions of a Kotlin module (JVM, Spring, Android).
---

# Sonar for Kotlin (on request only)

Used by `qa` to answer `front` / `back` (Android `front`, Spring `back`) and to write the Sonar configuration of a Kotlin module.

## Properties

Model: `pmeig/github-actions/actions/java/sonar/properties` (it sets `sonar.language=kotlin` when `*.kt` files exist).

- `sonar.projectKey=<repository>`, `sonar.sourceEncoding=UTF-8`, `sonar.qualitygate.wait=true`.
- `sonar.sources=src/main/kotlin` (Android: `src/main`), `sonar.tests=src/test/kotlin` (Android: `src/test`; `src/androidTest` is
  instrumented code, kept out of coverage).
- Compiled classes: `sonar.java.binaries` (Maven `target/classes`; Gradle `build/classes/kotlin/main`, Android
  `build/tmp/kotlin-classes/debug`) and `sonar.java.libraries` when needed.
- Coverage: Jacoco XML in `sonar.coverage.jacoco.xmlReportPaths` (Maven `target/site/jacoco/jacoco.xml`; Gradle
  `build/reports/jacoco/test/jacocoTestReport.xml`; Android: a `JacocoReport` task on `testDebugUnitTest` with `xml.required = true`).
- Jacoco `excludes` for generated Kotlin bytecode, as the action does: `**/*$WhenMappings.class`, `**/*$DefaultImpls.class`, `**/*Kt$*.class`.

## Out of the analysis

- Tests: `sonar.test.inclusions=**/*Test.kt,**/*Tests.kt,**/*IT.kt`; `**/src/test/**` and `**/src/androidTest/**` in
  `sonar.coverage.exclusions` and `sonar.cpd.exclusions`.
- Without behavior (`sonar.coverage.exclusions`): `**/configuration/**`, `**/*Configuration.*`, `**/properties/**`, `**/*Properties.*`,
  data classes in `**/model/**`, `**/dto/**`, `**/entity/**`, `**/repository/**` (interfaces), `**/exception/**`, `**/*Application.*`.
- Android: `R.class`, `BuildConfig.*`, `**/*_Hilt*`, `**/*_Factory*`, `**/*_MembersInjector*`, `**/di/**` modules, Compose `@Preview`
  functions, `**/theme/**` (colors, typography, shapes), `MainActivity` without logic, navigation graph declarations.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/kotlin/ ,
https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/java-test-coverage/ , https://github.com/pmeig/github-actions
