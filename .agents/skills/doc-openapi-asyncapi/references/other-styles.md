# API documentation: OpenAPI and AsyncAPI: other-styles

## Other API styles

- **GraphQL**: the SDL schema (`schema.graphql`) is the contract; export with the server tooling, add a table of queries/mutations
  with resolver file paths.
- **gRPC**: the `.proto` files are the contract; link them, add the service/method table with the implementing file.
- **tRPC / RPC-style**: list procedures with input/output types and file paths in `endpoints.md`.
