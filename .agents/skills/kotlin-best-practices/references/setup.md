# Kotlin best practices: module and build setup

- Kotlin 2.x (K2), JVM target = the project's JDK. Maven: `kotlin-maven-plugin` with compiler plugins `spring` (all-open) and
  `jpa`/`no-arg` when entities exist, args `-Xjsr305=strict` (Spring nullability) and `-Xannotation-default-target=param-property`.
  Gradle (Android): Kotlin DSL, version catalog.
- Sources in `src/main/kotlin`, tests in `src/test/kotlin` mirroring the packages. Package `pmeig.<project>.<module>`.
- Test libs: JUnit Jupiter, `mockito-kotlin` (Mockito agent on surefire), `kotlin-test`, `kotlinx-coroutines-test`; no MockK/kotest unless the project uses them.

Spring: `spring-boot-best-practices`.
