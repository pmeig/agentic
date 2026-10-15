---
name: e2e-api-best-practices
description: Writing, reviewing or running API e2e/contract tests (REST, GraphQL, gRPC).
---

# API e2e test best practices

- Pick the tool in the language of the module under test: REST Assured (Java/Kotlin), supertest or Playwright `request` (Node), pytest + httpx (Python), Karate, Hurl or Newman for language-neutral suites.
- Derive scenarios from `contract.md` / `openapi.yaml`: status, headers, body schema (validated against the OpenAPI schema), error format (problem details), pagination, auth and permissions, idempotency, concurrency.
- Real stack under test (container or deployed); each test creates its own data through the API with unique identifiers; no shared mutable fixtures; clean up what it created when the environment is shared.
- Auth: tokens from the real login flow or a test client read from Vault, never hardcoded; test the forbidden and unauthenticated paths too.
- Assert the contract fields that matter, not whole responses; no sleeps, poll with a timeout for asynchronous results.
- Run the same suite against the deployed environment after deployment (`qa` step 5).

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `api`, or the runner's name such as `rest-assured`).

Sources:
- https://spec.openapis.org/oas/latest.html , https://rest-assured.io/ , https://hurl.dev/ , https://playwright.dev/docs/api-testing
- https://github.com/karatelabs/karate , https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
