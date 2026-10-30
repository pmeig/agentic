# C / C++ best practices: tests

- GoogleTest (or Catch2): **one fixture/test suite per public method**, test names `should_<result>_when_<condition>`:
  ```cpp
  class ExpenseServiceCreate : public ::testing::Test {
  protected:
      FakeExpenseRepository repository;
      ExpenseService service{repository};
  };

  TEST_F(ExpenseServiceCreate, should_save_expense_when_input_is_valid) {
      const auto result = service.create(validInput());

      ASSERT_TRUE(result.has_value());
      EXPECT_EQ(repository.saved().size(), 1);
  }
  ```
  (Catch2: `TEST_CASE("ExpenseService")` with one `SECTION("create")` per method.)
- Hand-written fakes behind interfaces (gMock when needed), sanitizers on in test runs, coverage with gcov/llvm-cov for Sonar; Qt Test (`QTest`, `QSignalSpy`) for Qt classes.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with value-parameterized tests (`TEST_P` + `INSTANTIATE_TEST_SUITE_P`) or Catch2 `GENERATE` inside the suite of the method. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.
