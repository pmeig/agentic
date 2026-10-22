---
name: doc-openapi-asyncapi
description: Use to document an API contract: OpenAPI 3.x (REST), AsyncAPI (events), compact endpoints table, linting and rendering.
---

# API documentation: OpenAPI and AsyncAPI

The contract is a file (`.agents/docs/api/openapi.yaml`), not prose. An AI reads one YAML and knows every route, input, output and error.
Alongside it, `.agents/docs/api/endpoints.md` is the compact index (`METHOD path | handler file:line | auth | tables touched | feature`).

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

## AsyncAPI (events, queues, WebSocket, MQTT, Kafka)

- Use AsyncAPI **3.x** when the project has messages: one `channels` entry per topic/queue/socket event, `operations` (`send`/`receive`),
  `messages` with payload schemas, `servers` for brokers. Same rules: names = identifiers in code, one file, validate with
  `npx -y @asyncapi/cli validate asyncapi.yaml`.
- No messaging in the project: do not create the file.

## Other API styles

- **GraphQL**: the SDL schema (`schema.graphql`) is the contract; export with the server tooling, add a table of queries/mutations
  with resolver file paths.
- **gRPC**: the `.proto` files are the contract; link them, add the service/method table with the implementing file.
- **tRPC / RPC-style**: list procedures with input/output types and file paths in `endpoints.md`.

## Procedure

1. Find the routes: framework generation if present, else `doc-code-analysis` route grep (decorators, router registrations).
2. Produce or update the spec; diff against the code for undocumented routes.
3. Build `endpoints.md` from the spec (script or by hand) with the **handler path and line**.
4. Lint, fix, report routes you could not verify.

## Sources

- https://spec.openapis.org/oas/latest.html (versions, 3.2 changes) · https://learn.openapis.org
- https://www.asyncapi.com/docs · https://redocly.com/docs/cli · https://docs.stoplight.io/docs/spectral

## Monthly refresh

Last refreshed: 2026-10 (OpenAPI 3.2.0 current). At first use in a later month: check the OpenAPI and AsyncAPI latest versions,
framework generator changes, linter rule updates; update this file, set the date, report changes.
