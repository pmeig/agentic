# Dart / Flutter best practices: unit tests

- `flutter_test` + `mocktail`: **one `group` per public method**, test names `should <result> when <condition>`:
  ```dart
  void main() {
    late FakeExpenseRepository repository;
    late ExpenseViewModel viewModel;

    setUp(() {
      repository = FakeExpenseRepository();
      viewModel = ExpenseViewModel(repository);
    });

    group('save', () {
      test('should queue the expense when offline', () async {
        repository.online = false;

        await viewModel.save(validExpense);

        expect(repository.pending, hasLength(1));
      });
    });
  }
  ```
- Widget tests with `pumpWidget` + `find.bySemanticsLabel`, golden tests for key screens, `integration_test`/Patrol or Maestro for e2e; fake clocks (`clock` package); coverage `flutter test --coverage` (lcov for Sonar).

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with a list of cases iterated inside the `group` of the method (`for (final c in cases) test("should ... when ${c.name}", ...)`). Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.
