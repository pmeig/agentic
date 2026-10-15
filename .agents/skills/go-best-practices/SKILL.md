---
name: go-best-practices
description: MANDATORY for any Go code (HTTP APIs, CLIs, workers): layered by feature, small interfaces, wrapped errors, context, table-driven tests, Go 1.25+.
---

# Go best practices

The user has no Go project yet: these rules transpose the team's conventions (`java-best-practices`, `typescript-best-practices`,
`node-api-architecture`) to idiomatic Go. A project's own rules win.

## 1. Setup

- Latest Go from `go.mod` (`go 1.25+`, `toolchain` line), modules only, `go mod tidy` clean; tools pinned with `tool` directives.
- Layout: `cmd/<app>/main.go` (wiring only), `internal/<feature>/` (handler, service, repository, model), `internal/platform/` (db, http, config, logging), `pkg/` only for code meant to be imported by other repos.
- `gofmt`/`goimports`, `go vet`, `staticcheck` or `golangci-lint` in CI; `govulncheck` for dependencies.
- Containers: Go 1.25 sets `GOMAXPROCS` from the cgroup CPU limit; build static binaries (`CGO_ENABLED=0`) into distroless/scratch images.

## 2. Code

- Layering: handler (decode, validate, encode, status) → service (business rules, transactions) → repository (SQL) → infrastructure. A handler never runs SQL; a service never sees `http.Request`.
- Dependencies injected through constructors (`NewService(repo Repository, clock Clock) *Service`), wired in `main`; no package-level mutable state, no `init()` side effects.
- **Interfaces small and defined where they are used** (the consumer), return concrete types; accept interfaces, return structs.
- Errors: return them, never panic for expected failures; wrap with context `fmt.Errorf("find expense %s: %w", id, err)`; sentinel errors (`var ErrNotFound = errors.New(...)`) and typed errors checked with `errors.Is`/`errors.As`; map to HTTP status in one place.
- `context.Context` first parameter of every I/O function, honoured for cancellation and deadlines; never stored in a struct.
- Concurrency: goroutines owned by a parent with `errgroup`/`sync.WaitGroup.Go`, channels for ownership transfer, mutexes for shared state, no goroutine leak (always a way to stop); run tests with `-race`.
- HTTP: `net/http` `ServeMux` patterns (`GET /expenses/{id}`) or chi; timeouts on server and clients; `http.CrossOriginProtection` for CSRF; JSON with explicit structs and `json:"snake_case"` tags.
- Config from the environment loaded once into a typed struct at startup (secrets from Vault/env, never in code); `log/slog` structured logging with request ids, no personal data.
- SQL: `database/sql` + pgx or sqlc-generated queries, parameters only, migrations numbered (`sql-best-practices`).
- Naming: short package names (no `util`), `MixedCaps`, exported only what other packages need, doc comment starting with the name on every exported identifier.

## 3. Tests

- `<file>_test.go` beside the code (package `x_test` for black-box tests).
- **One `Test<Type>_<Method>` (or `Test<Function>`) per public function**, table-driven with `t.Run` sub-tests named `should_<result>_when_<condition>`:
  ```go
  func TestService_Create(t *testing.T) {
      tests := []struct {
          name    string
          input   CreateExpense
          wantErr error
      }{
          {name: "should_save_expense_when_input_is_valid", input: validInput()},
          {name: "should_fail_when_amount_is_negative", input: negativeAmount(), wantErr: ErrInvalidAmount},
      }
      for _, tt := range tests {
          t.Run(tt.name, func(t *testing.T) {
              service := NewService(&fakeRepository{}, fixedClock)

              _, err := service.Create(context.Background(), tt.input)

              if !errors.Is(err, tt.wantErr) {
                  t.Fatalf("got %v, want %v", err, tt.wantErr)
              }
          })
      }
  }
  ```
- Hand-written fakes for interfaces (no mocking framework needed), `testing/synctest` for time and concurrency, `httptest` for handlers, Testcontainers for repository integration tests; `t.Parallel()` when independent.
- Cover every branch and error path; `go test -race -cover ./...` in CI with the coverage profile sent to Sonar.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with the table-driven test of the function (`[]struct{name ...}` + `t.Run(tt.name, ...)`). Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the official sources, update only internet-derived guidance, keep user/project rules, add source URLs, update this date, report changes.
