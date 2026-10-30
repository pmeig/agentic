# Spring Boot best practices: tests

- Unit tests without Spring (language skills: `@Nested` per public method, `should_..._when_...`).
- Slices: `@WebMvcTest` + `MockMvcTester`/`RestTestClient`, `@DataJpaTest` with Testcontainers (`@ServiceConnection`), `@SpringBootTest` only for end-to-end wiring (`*IT`, failsafe). `@MockitoBean` instead of the removed `@MockBean`.
- Test error and validation paths, not only 200, and one test of the security rules per endpoint family.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `@ParameterizedTest` (`@MethodSource`, `@CsvSource`, `@EnumSource`), also for controller validation cases with `MockMvcTester`. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.
