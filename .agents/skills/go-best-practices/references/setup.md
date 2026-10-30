# Go best practices: setup (module, layout, tooling)

- Latest Go from `go.mod` (`go 1.25+`, `toolchain` line), modules only, `go mod tidy` clean; tools pinned with `tool` directives.
- Layout: `cmd/<app>/main.go` (wiring only), `internal/<feature>/` (handler, service, repository, model), `internal/platform/` (db, http, config, logging), `pkg/` only for code meant to be imported by other repos.
- `gofmt`/`goimports`, `go vet`, `staticcheck` or `golangci-lint` in CI; `govulncheck` for dependencies.
- Containers: Go 1.25 sets `GOMAXPROCS` from the cgroup CPU limit; build static binaries (`CGO_ENABLED=0`) into distroless/scratch images.
