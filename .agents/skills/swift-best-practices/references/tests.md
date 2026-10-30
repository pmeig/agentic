# Swift best practices: unit tests

- One test file per type; **one `@Suite` per public method**, nested in the type's suite, test names `should_<result>_when_<condition>`:
  ```swift
  @Suite struct ExpenseViewModelTests {
      @Suite struct Save {
          @Test func should_add_pending_expense_when_offline() async throws {
              let repository = FakeExpenseRepository(online: false)
              let viewModel = await ExpenseViewModel(repository: repository)

              try await viewModel.save(.valid)

              #expect(repository.pending.count == 1)
          }
      }
  }
  ```
- Hand-written fakes conforming to the protocols, parameterized `@Test(arguments:)`, `#expect(throws:)` for errors, injected clocks; XCUITest or Maestro for e2e (twin e2e: the same flows on every client, see `e2e-run`).

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `@Test(arguments:)` (zipped or combined collections) inside the `@Suite` of the method. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.
