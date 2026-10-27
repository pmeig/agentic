# Java best practices: module and build setup (Maven)

- Latest JDK the project targets (25 LTS or 26): `<java.version>` driving `maven.compiler.release`; UTF-8 encoding.
- groupId `io.github.pmeig`, root package `pmeig.<project>.<module>` (no `io.github`), module folder names with dashes become package segments.
- Multi-module: parent pom `packaging pom`, one artifact per module, versions as properties (`pmeig-<module>.version`, `<lib>.version`), never hard-coded inline in child poms. Library poms carry the Maven Central metadata (name, description, url, license, developers, scm).
- Spring apps inherit `spring-boot-starter-parent` (or import `spring-boot-dependencies`), library versions from the BOM.
- **Lombok always**: dependency `org.projectlombok:lombok` (`optional`/`provided`), declared in `maven-compiler-plugin > annotationProcessorPaths`
  (with `spring-boot-configuration-processor` when used) and excluded from the `spring-boot-maven-plugin` jar. Add a root `lombok.config`:
  ```
  config.stopBubbling = true
  lombok.addLombokGeneratedAnnotation = true
  lombok.anyConstructor.addConstructorProperties = true
  lombok.log.fieldName = log
  ```
  (`addLombokGeneratedAnnotation` keeps generated code out of JaCoCo/Sonar coverage.)
- Tests: JUnit Jupiter (5/6), Mockito (+ `-javaagent` for inline mocking on recent JDKs), AssertJ. Never JUnit 4.
- Publishing goes through the project's CI (artifact repository, secrets from its secret store); no credentials in poms.

Spring: `spring-boot-best-practices`.
