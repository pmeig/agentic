# Kotlin best practices: unit tests

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
