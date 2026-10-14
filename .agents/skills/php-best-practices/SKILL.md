---
name: php-best-practices
description: MANDATORY when writing, reviewing or testing PHP code (Symfony, Laravel, plain PHP): the team's conventions transposed to PHP - strict types, layered controller/service/repository by feature, constructor injection, readonly classes and enums, PSR-12/PER, PHPStan max, PHPUnit with one nested group per public method and should_..._when_... names - plus PHP 8.5 practices.
---

# PHP best practices

The user has no PHP project yet: these rules transpose the team's conventions to idiomatic PHP. A project's own rules win.

## 1. Setup

- Latest PHP (8.5) declared in `composer.json` (`"php": ">=8.5"`), Composer with a committed `composer.lock`, PSR-4 autoload (`App\\` → `src/`).
- `declare(strict_types=1);` at the top of every file; PER Coding Style (PSR-12 successor) with PHP-CS-Fixer or ECS; PHPStan (level max) or Psalm in CI; Rector for upgrades.
- Framework: Symfony (preferred for typed, explicit DI) or Laravel when the project uses it; follow the framework's directory conventions.

## 2. Code

- Layering: controller (request mapping, validation, response) → service (business rules, transactions) → repository (Doctrine/Eloquent queries) → infrastructure. No query in a controller, no `Request` in a service.
- Constructor injection with promoted properties (`public function __construct(private readonly ExpenseRepository $repository) {}`), autowiring, no static facades in domain code, no `new` of services inside services.
- `final readonly class` for services and value objects, backed `enum` for fixed sets, typed properties, union/intersection types, `never`, first-class callables; the pipe operator `|>` (8.5) for linear transformations; `#[\NoDiscard]` on functions whose result must be used; property hooks/asymmetric visibility (8.4) instead of getters/setters boilerplate.
- DTOs for input/output mapped and validated at the edge (Symfony Validator / Form Requests), never raw arrays across layers.
- Errors: domain exceptions extending a project base exception, one handler mapping them to RFC 9457 problem responses; never `@` error suppression.
- Data: Doctrine ORM or Eloquent with migrations, parameters only (no string-built SQL), eager loading against N+1 (`sql-best-practices`).
- Config and secrets from the environment (`.env.local` not committed, Vault in deployment); PSR-3 logging (Monolog) with context arrays, no personal data.
- Naming: `PascalCase` classes, `camelCase` methods/properties, `UPPER_SNAKE` constants, one class per file; PHPDoc only where types cannot say it (generics `@param list<Expense>`).

## 3. Tests (PHPUnit)

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

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, check official sources for version, practice, and deprecation changes. Update only internet-derived
guidance; preserve user/project rules. Add source URLs, update this date, and briefly report changes.
