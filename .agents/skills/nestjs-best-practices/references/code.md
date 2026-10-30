# NestJS best practices: code

- Global `ValidationPipe({ whitelist: true, forbidNonWhitelisted: true, transform: true })` with `class-validator` DTOs, or a zod pipe; response DTOs distinct from entities (`ClassSerializerInterceptor` / explicit mapping).
- Configuration: `ConfigModule` with a validated schema, loaded once at startup (Vault values merged like `load<Name>Properties()`), injected as typed config classes; no `process.env` outside config.
- Errors: domain exceptions mapped by one global exception filter to RFC 9457 problem details; never leak stack traces.
- Auth with guards (`@UseGuards`, global JWT guard + `@Public()` decorator), roles with custom decorators + `Reflector`; identity from the request, never the body.
- Cross-cutting concerns with interceptors (logging, correlation id, timing), `nestjs-pino` structured logs; health checks with `@nestjs/terminus`; OpenAPI with `@nestjs/swagger` decorators kept in sync with the contract.
- Fastify adapter for performance when the project allows; graceful shutdown hooks enabled.
