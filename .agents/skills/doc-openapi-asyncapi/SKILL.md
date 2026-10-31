---
name: doc-openapi-asyncapi
description: "Use to document an API contract: OpenAPI 3.x (REST), AsyncAPI (events), compact endpoints table, linting and rendering."
---

# API documentation: OpenAPI and AsyncAPI (router)

The contract is a file (`.agents/docs/api/openapi.yaml`), not prose. An AI reads one YAML and knows every route, input, output and error.
Alongside it, `.agents/docs/api/endpoints.md` is the compact index (`METHOD path | handler file:line | auth | tables touched | feature`).

Load only the row(s) that match the task; never every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Documenting a REST API (OpenAPI) | `references/openapi.md` |
| Documenting events, queues, WebSocket, MQTT, Kafka (AsyncAPI) | `references/asyncapi.md` |
| GraphQL, gRPC, tRPC / RPC-style | `references/other-styles.md` |
| Order of work, endpoints.md, linting | `references/procedure.md` |
| Monthly refresh, sources | `references/maintenance.md` |
