# API documentation: OpenAPI and AsyncAPI: procedure

## Procedure

1. Find the routes: framework generation if present, else `doc-code-analysis` route grep (decorators, router registrations).
2. Produce or update the spec; diff against the code for undocumented routes.
3. Build `endpoints.md` from the spec (script or by hand) with the **handler path and line**.
4. Lint, fix, report routes you could not verify.
