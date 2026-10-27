# C# / .NET best practices: tests (xUnit)

- One `<Class>Tests` per class; **one nested class per public method**, test names `Should_<result>_When_<condition>`:
  ```csharp
  public sealed class ExpenseServiceTests
  {
      private readonly IExpenseRepository _repository = Substitute.For<IExpenseRepository>();
      private readonly ExpenseService _service;

      public ExpenseServiceTests() => _service = new ExpenseService(_repository, new FakeTimeProvider());

      public sealed class Create : ExpenseServiceTests
      {
          [Fact]
          public async Task Should_save_expense_When_input_is_valid()
          {
              var result = await _service.CreateAsync(ValidInput(), CancellationToken.None);

              result.Id.Should().NotBeEmpty();
              await _repository.Received(1).SaveAsync(Arg.Any<Expense>(), Arg.Any<CancellationToken>());
          }
      }
  }
  ```
- NSubstitute (or Moq) built by hand, AwesomeAssertions/FluentAssertions or xUnit asserts consistently, `[Theory]` + `[InlineData]` for tables, `FakeTimeProvider` for time; `WebApplicationFactory` + Testcontainers for integration tests.
- Cover every branch and error path; coverage via `coverlet` (Cobertura/OpenCover for Sonar).

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `[Theory]` with `[InlineData]`, `[MemberData]` or `TheoryData<...>` inside the nested class of the method. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.
