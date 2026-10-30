# NestJS best practices: setup

- One Nest module per feature (`expenses/expenses.module.ts`, `expenses.controller.ts`, `expenses.service.ts`, `repository/expense.repository.ts`, `dto/`), shared infrastructure in `core/` modules (database, config, auth, logging) imported where needed; no circular modules (`forwardRef` is a smell).
- Controller: routes, DTO validation, status codes, calls **one** service method; service: business rules and transactions; repository: data access only (TypeORM/Prisma/Drizzle/pg). A controller never injects a repository.
- Constructor injection with `private readonly`; custom providers (`useFactory`) for clients; request-scoped providers only when unavoidable (cost).
