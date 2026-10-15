---
name: java-best-practices
description: MANDATORY for any .java file, pom.xml or Java unit test: Lombok always, JUnit 5 @Nested per public method, final, records, streams, Java 25+.
---

# Java best practices

Based on the user's projects (`pmeig-core`, `MyController`, `spring-libraries`) and current Java practice. A project's own
`CLAUDE.md` / skills win; otherwise apply everything below. Spring: `spring-boot-best-practices`. Commands: `java-version`.

## 1. Build (Maven)

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
- Publishing goes through the shared CI (`github-actions-cicd` skill: Sonatype/JFrog, secrets from Vault); no credentials in poms.

## 2. Lombok: never write boilerplate by hand

| Need | Annotation |
|---|---|
| Spring bean / service with dependencies | `@RequiredArgsConstructor` + `private final` fields (constructor injection, no `@Autowired`) |
| Logger | `@Slf4j` (`log.info("Found {} classes", count)` with placeholders, never string concatenation) |
| Immutable value class | `@Value` (all fields `private final`, getters, equals/hashCode/toString) + `@Builder` when > 3 fields or optional ones; `@With` for copies |
| Mutable class (JPA entity, `@ConfigurationProperties`) | `@Getter` `@Setter` `@NoArgsConstructor`; never `@Data` on a JPA entity (equals/hashCode on lazy relations, `toString` loops): write equals/hashCode on the id, `@ToString(onlyExplicitlyIncluded = true)` |
| Utility holder | `@UtilityClass` (or prefer instance beans) |
| Builder for a record or a class with many args | `@Builder(toBuilder = true)` |
| Checked exception rethrow | avoid `@SneakyThrows`: wrap in a domain exception with the cause |

- `@EqualsAndHashCode(callSuper = ...)` explicit on subclasses. `@NonNull` only where JSpecify/`Objects.requireNonNull` is not enough.
- Records are fine for small immutable DTOs (API payloads, events, query results); add `@Builder` on the record when it has many fields. Use a Lombok `@Value` class when you need inheritance-free immutability with custom methods, builders and validation together.

## 3. Code style

- 2-space indentation, K&R braces, **braces always** (no braceless `if`), max ~140 columns, explicit imports (no wildcard, no unused).
- `final` on fields, parameters and locals; **no `var`**: explicit types.
- Immutability first: `List.of`/`Map.of`/`List.copyOf` for returned collections (defensive copies), `Stream.toList()`, no setters on value types.
- Streams and method references for transformations (`map`, `flatMap(Collection::stream)`, `Collectors.partitioningBy/groupingBy`); a plain loop when it reads better or needs early exit.
- Null: constant-first comparisons (`null != value`, `"x".equals(input)`, `Boolean.TRUE.equals(flag)`). Prefer `Optional` as a **return type** for "may be absent" (never as a field or parameter); mark packages `@NullMarked` (JSpecify) and use `@Nullable` for the exceptions.
- Modern Java (25+): records, sealed interfaces + pattern matching `switch` (exhaustive, no `default` on sealed types), text blocks for SQL/JSON, `instanceof` patterns, flexible constructor bodies (validate before `super(...)`), virtual threads for blocking I/O, `ScopedValue` instead of `ThreadLocal` for request context. Preview features only when the project enables them.
- Exceptions: unchecked domain exceptions (`BusinessException`, `TechnicalException`) carrying a code; wrap checked ones with message + cause (`throw new XxxException("Failed to create file: " + name, e)`); try-with-resources; never swallow.
- Naming: classes by role (`AnnotationScanner`, `MojoService`, `OrderController`), verb-first methods, `UPPER_SNAKE` `private static final` constants, enum constants UPPER_SNAKE (PascalCase only when mirroring external names), no placeholder names (`MyMojo`, `toto`).
- Concurrency: use concurrent collections only when shared between threads; `synchronized` sparingly, prefer `java.util.concurrent` locks/atomics.
- Javadoc on public API (what and why, one or two sentences); no commented-out code.
- Layering for applications: controller → service → repository (`node-api-architecture` principles apply): no repository in a controller, no web objects in a service.

## 4. Unit tests (JUnit 5)

- One test class `<Class>Test` per production class, same package under `src/test/java`.
- **One `@Nested` class per public method**, named after the method in PascalCase, holding every test of that method:
  ```java
  class CryptoServiceTest {

    private final KeyProvider keyProvider = mock(KeyProvider.class);
    private final CryptoService service = new CryptoService(keyProvider);

    @Nested
    class Encrypt {

      @Test
      void should_return_cipher_text_when_value_is_present() {
        when(keyProvider.key()).thenReturn(KEY);

        final String result = service.encrypt("secret");

        assertThat(result).isNotEqualTo("secret");
      }

      @Test
      void should_throw_when_value_is_null() {
        assertThatThrownBy(() -> service.encrypt(null)).isInstanceOf(BusinessException.class);
      }
    }

    @Nested
    class Decrypt { /* ... */ }
  }
  ```
- Names `should_<expected result>_when_<condition>` in snake_case; package-private classes and methods; `// given` / `// when` / `// then` as blank-line separated blocks.
- Mocks built by hand as fields (`mock(X.class)`), SUT constructed explicitly; no `@Mock`/`@InjectMocks`/`@ExtendWith(MockitoExtension.class)` unless genuinely needed. Static imports for Mockito and AssertJ (`import static org.mockito.Mockito.when;`), never `Mockito.when(...)` inline.
- AssertJ for assertions (`assertThat`, `assertThatThrownBy`). **Favor parameterized tests** inside the nested group: tests of a method that differ only by inputs and expected results become one `@ParameterizedTest` (`@MethodSource` with a `static Stream<Arguments>` in the nested class, `@CsvSource`, `@EnumSource`, `name = "should_..._when_{0}"`); separate tests stay for genuinely different arrange or verify steps.
- Cover every branch (`if`/`else`, `switch`, `catch`, null paths), force every lambda/callback to run (`doAnswer(inv -> inv.<Runnable>getArgument(0).run())`), await async results (`join()`, `StepVerifier`), and `verify` side effects. Re-read the method and list its paths before calling it covered.
- Never test getters/setters generated by Lombok, records without logic, or interfaces.
- Spring: unit tests without a context by default; slices (`@WebMvcTest`, `@DataJpaTest`) or `@SpringBootTest` + Testcontainers only for integration tests (`*IT`, failsafe).

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the official sources, update only internet-derived guidance, keep user/project rules, add source URLs, update this date, report changes.
