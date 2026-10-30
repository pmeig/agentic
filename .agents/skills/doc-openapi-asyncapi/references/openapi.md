# API documentation: OpenAPI and AsyncAPI: openapi

## OpenAPI (REST)

- Version: **OpenAPI 3.2.0** (September 2025, backward compatible with 3.1: new tag `summary`/`parent`/`kind`, streaming media types,
  new HTTP methods, updated OAuth flows). Use the newest version the project's tooling supports; 3.1 is the safe default for
  JSON Schema 2020-12 alignment. State the version in `openapi:`.
- **Generate from the code first** (keeps it true), then complete by hand:

| Stack | Generation |
|---|---|
| Fastify | `@fastify/swagger` (schemas on routes) |
| NestJS | `@nestjs/swagger` (decorators, `SwaggerModule.createDocument`) |
| Express | `swagger-jsdoc` or `tsoa` |
| Spring Boot | `springdoc-openapi` (`/v3/api-docs.yaml`) |
| FastAPI | built in (`/openapi.json`) |
| ASP.NET Core | `Microsoft.AspNetCore.OpenApi` / Swashbuckle |
| Go | `swaggo/swag`, `oapi-codegen` (spec first) |
| No framework support | write it by hand from the controllers, mark `(derived by hand)` |

- Content that matters: `operationId` unique and equal to the handler name, `tags` = feature names, `summary` one line,
  request/response `$ref` schemas in `components/schemas`, **every error response** (400, 401, 403, 404, 409, 422, 5xx) with the
  error schema, `security` schemes, pagination and filtering parameters, examples for non-obvious payloads, `x-` extensions
  only for project facts (`x-feature`, `x-handler: server/src/x/x.controller.ts`).
- Spec-first projects: the spec is the source; document where the generated code goes and "do not edit generated files".
- Lint before delivering: `npx -y @redocly/cli lint openapi.yaml` or Spectral (`npx -y @stoplight/spectral-cli lint openapi.yaml`).
- Human rendering: Redoc (`npx -y @redocly/cli build-docs`), Swagger UI, Scalar; the human README links to it.
