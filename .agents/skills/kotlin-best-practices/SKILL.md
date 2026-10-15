---
name: kotlin-best-practices
description: MANDATORY for any .kt file or Kotlin unit test (Spring, Android): val and data classes, constructor injection, JUnit 5 @Nested per public method, mockito-kotlin.
---

# Kotlin best practices

Based on `spring-libraries` (its `CLAUDE.md` and `unit-test-conventions` skill) and the `budget` Android app, plus current Kotlin
practice. A project's own rules win. Spring: `spring-boot-best-practices`; Android: `android-compose-architecture`; commands:
`java-version` / `android-tooling`.

## 1. Build

- Kotlin 2.x (K2), JVM target = the project's JDK. Maven: `kotlin-maven-plugin` with compiler plugins `spring` (all-open) and
  `jpa`/`no-arg` when entities exist, args `-Xjsr305=strict` (Spring nullability) and `-Xannotation-default-target=param-property`.
  Gradle (Android): Kotlin DSL, version catalog.
- Sources in `src/main/kotlin`, tests in `src/test/kotlin` mirroring the packages. Package `pmeig.<project>.<module>`.
- Test libs: JUnit Jupiter, `mockito-kotlin` (Mockito agent on surefire), `kotlin-test`, `kotlinx-coroutines-test`; no MockK/kotest unless the project uses them.

## 2. Style

- Follow the project's indentation (spring-libraries 2 spaces, Android 4 spaces + trailing commas); `kotlin.code.style=official`, `class X : Y` with a space.
- `val` by default; `var` only for `@ConfigurationProperties`, JPA columns, or local accumulators. Immutable collections (`List`, `Map`) in APIs, `toList()` copies when exposing internal state.
- `data class` for values, `sealed interface` + data classes/objects for closed results and states (exhaustive `when`, no `else`), `enum class` for fixed sets, `object` for stateless singletons, `fun interface` for single-method strategies, `value class` for typed ids.
- Nullability: no `!!` (only where an API guarantees non-null, with a comment); `?.let`, elvis with early return (`val token = manager.token(request) ?: return null`), `requireNotNull`/`checkNotNull` with a message, `require(...)` for argument validation. Name unused catch variables `_`.
- Expression bodies for one-liners, named arguments for booleans and multiple same-typed parameters, default arguments instead of overloads (`@JvmOverloads` when Java calls them).
- Extension and top-level functions instead of utility classes (`StringHelper.kt`, lowercase file names for files of top-level functions); `private` top-level `const val` constants; `internal` for module-private API.
- Scope functions: `apply` to configure an object, `let` for nullable transforms, `also` for side effects; never nested scope functions.
- Errors: domain exceptions with a code; `runCatching` only at boundaries and never swallowing `CancellationException`; `Result`/sealed types for expected failures in app code.
- Coroutines (apps/Android): `suspend` functions, structured concurrency (`coroutineScope`, viewModelScope), `Dispatchers.IO` injected for testability, `Flow`/`StateFlow` for streams; no `GlobalScope`, no `runBlocking` in production code. Reactive Spring code: Reactor `Mono`/`Flux` or coroutines, not both mixed in one flow.
- Spring injection: primary constructor with `private val` parameters; never `@Autowired lateinit` (only `lateinit` for `*Aware` callbacks).
- KDoc on public API, in English, linking symbols with `[name]`; no commented-out code, no `println` (use the logger, never log secrets).

## 3. Unit tests

- One `<Class>Test` per class; **one `@Nested inner class` per public method**, named after the method in PascalCase.
- Names `should_<expected result>_when_<condition>` in snake_case, **no backtick sentences** (grep-able, consistent).
- Mocks by hand: `private val dependency: Dependency = mock()`, SUT built explicitly; no `@Mock`/`@InjectMocks`/`@ExtendWith`. Import mockito-kotlin functions one by one (`import org.mockito.kotlin.whenever`), never `Mockito.xxx(...)` inline.
- Assertions: `kotlin.test` (`assertEquals`, `assertFailsWith`, `assertIs`) consistently in a file.
- **Favor parameterized tests** inside the nested group: tests of a method that differ only by inputs and expected results become one `@ParameterizedTest` (`@MethodSource` with a `@JvmStatic` function in a `companion object` of the nested class or `@TestInstance(PER_CLASS)`, `@CsvSource`, `@EnumSource`); separate tests stay for genuinely different arrange or verify steps.
- Coverage of every branch (`if`, `when`, elvis, safe call, `catch`), every lambda forced to run (`doAnswer { it.getArgument<() -> Unit>(0).invoke() }`), async awaited (`runTest`, `StepVerifier`), side effects verified (`verify`).
- Fixtures: private top-level helpers in the test file or `shared/` test packages; named arguments in fixture builders.

```kotlin
class DataContextServiceTest {

  private val cacheManager: DataCacheManager = mock()
  private val service = DataContextService(cacheManager)

  @Nested
  inner class Context {

    @Test
    fun should_name_parameters_positionally_when_no_param_annotation() {
      whenever(cacheManager.getCache(any())).thenReturn(NoOpCache("noOp"))

      val context = service.context(method("queryWithPositional"), String::class.java)

      assertEquals(2, context.parameters.size)
    }
  }
}
```

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the official sources, update only internet-derived guidance, keep user/project rules, add source URLs, update this date, report changes.
