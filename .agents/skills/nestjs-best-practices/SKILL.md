---
name: nestjs-best-practices
description: MANDATORY when writing, reviewing or testing NestJS code: the team's Node conventions transposed to NestJS - one module per feature with controller/service/repository, constructor DI, DTOs validated with class-validator or zod, typed ConfigModule with Vault values, exception filters returning problem details, Jest/Vitest with one describe per public method and should ... when ... names.
---

# NestJS best practices

NestJS is the decorator-based way of doing what `node-api-architecture` describes; follow that skill's layering and data rules,
and `typescript-best-practices` for the language. These rules adapt them to Nest.

## 1. Structure

- One Nest module per feature (`expenses/expenses.module.ts`, `expenses.controller.ts`, `expenses.service.ts`, `repository/expense.repository.ts`, `dto/`), shared infrastructure in `core/` modules (database, config, auth, logging) imported where needed; no circular modules (`forwardRef` is a smell).
- Controller: routes, DTO validation, status codes, calls **one** service method; service: business rules and transactions; repository: data access only (TypeORM/Prisma/Drizzle/pg). A controller never injects a repository.
- Constructor injection with `private readonly`; custom providers (`useFactory`) for clients; request-scoped providers only when unavoidable (cost).

## 2. Rules

- Global `ValidationPipe({ whitelist: true, forbidNonWhitelisted: true, transform: true })` with `class-validator` DTOs, or a zod pipe; response DTOs distinct from entities (`ClassSerializerInterceptor` / explicit mapping).
- Configuration: `ConfigModule` with a validated schema, loaded once at startup (Vault values merged like `load<Name>Properties()`), injected as typed config classes; no `process.env` outside config.
- Errors: domain exceptions mapped by one global exception filter to RFC 9457 problem details; never leak stack traces.
- Auth with guards (`@UseGuards`, global JWT guard + `@Public()` decorator), roles with custom decorators + `Reflector`; identity from the request, never the body.
- Cross-cutting concerns with interceptors (logging, correlation id, timing), `nestjs-pino` structured logs; health checks with `@nestjs/terminus`; OpenAPI with `@nestjs/swagger` decorators kept in sync with the contract.
- Fastify adapter for performance when the project allows; graceful shutdown hooks enabled.

## 3. Tests

- `Test.createTestingModule` with the dependencies replaced by mocks (`useValue`), or plain instantiation for services; `*.spec.ts` beside the source (or mirrored in `test/`), **one `describe` per public method**, `it('should ... when ...')`.
- e2e with `supertest` on the Nest app and a Testcontainers database; cover validation errors, guards and error filters, not only 200.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `it.each` (table of objects, `$name` in the title) inside the `describe` of the method. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

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
