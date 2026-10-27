# PHP best practices: unit tests (PHPUnit / Pest)

- `tests/` mirroring `src/`, one `<Class>Test` per class. **Group the tests per public method**: with Pest, one `describe('<method>')` per method (real nesting, preferred); with PHPUnit (no nested classes), prefix every test with its method, `test_<method>_should_<result>_when_<condition>`, kept together in the file:
  ```php
  final class ExpenseServiceTest extends TestCase
  {
      private ExpenseRepository&MockObject $repository;
      private ExpenseService $service;

      protected function setUp(): void
      {
          $this->repository = $this->createMock(ExpenseRepository::class);
          $this->service = new ExpenseService($this->repository, new MockClock('2026-01-01'));
      }

      public function test_create_should_save_expense_when_input_is_valid(): void
      {
          $this->repository->expects(self::once())->method('save');

          $this->service->create(ExpenseFixture::valid());
      }
  }
  ```
  (Pest: `describe('create', fn () => it('should save expense when input is valid', ...))` gives real nesting.)
- Attributes (`#[Test]`, `#[DataProvider]`), mocks built in `setUp`, clocks injected (`symfony/clock`), `KernelTestCase`/`WebTestCase` or Laravel feature tests with a test database for integration.
- Cover every branch and error path; coverage via PCOV/Xdebug in Clover format for Sonar.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `#[DataProvider]` (PHPUnit) or `->with([...])` datasets (Pest) for the tests of the method. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.
