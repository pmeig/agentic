# PHP best practices: structure (layering, injection, naming)

- Layering: controller (request mapping, validation, response) → service (business rules, transactions) → repository (Doctrine/Eloquent queries) → infrastructure. No query in a controller, no `Request` in a service.
- Constructor injection with promoted properties (`public function __construct(private readonly ExpenseRepository $repository) {}`), autowiring, no static facades in domain code, no `new` of services inside services.
- Naming: `PascalCase` classes, `camelCase` methods/properties, `UPPER_SNAKE` constants, one class per file; PHPDoc only where types cannot say it (generics `@param list<Expense>`).
