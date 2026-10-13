---
name: kotlin-best-practices
description: MANDATORY when writing, reviewing or testing Kotlin code (Spring libraries/apps on Maven, Android): the user's conventions - val and data classes, constructor injection, extension functions, JUnit 5 with one @Nested inner class per public method, should_..._when_... names, mockito-kotlin - plus current Kotlin practices. Use for any .kt file or Kotlin unit test.
---

# Kotlin best practices

Based on `D:\projects\kotlin\spring-libraries` (its `CLAUDE.md` and `unit-test-conventions` skill) and the Android app of
`D:\projects\typescript\budget\android`, plus current Kotlin practice. A project's own rules win. Spring:
`spring-boot-best-practices`; Android architecture: `android-compose-architecture`; commands: `java-version` / `android-tooling`.

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

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `@ParameterizedTest` with `@MethodSource` (a `@JvmStatic` function in a `companion object` of the nested class, or `@TestInstance(PER_CLASS)`), `@CsvSource` or `@EnumSource`. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

## Monthly refresh

Last refreshed: 2026-10

- On the **first use of this skill in a calendar month after the date above**, refresh it before applying it: search the web for
  what changed since that month (new stable versions, newly recommended practices, deprecated or removed APIs and tools).
- Update **only the parts that come from the internet**: add the new practices, change outdated versions, remove what is
  deprecated or removed. Keep it short, prefer official sources (release notes, official docs).
- **Never remove or weaken the user's rules**: everything taken from the user's projects (`D:\projects\...`) or explicit
  instructions and the team conventions (layered controller/service/repository, pages/ + core/ modules, one test group per public
  method with parameterized tests favored, `should_..._when_...` names, mocks built by hand, Lombok always for Java, every branch covered...). When the internet
  contradicts one of them, keep the rule and tell the user about the conflict.
- Then set "Last refreshed" to the current month and tell the user in a few bullets what was added, changed or removed (with sources).
