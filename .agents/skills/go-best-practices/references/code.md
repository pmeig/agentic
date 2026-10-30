# Go best practices: code (errors, context, concurrency, HTTP)

- Errors: return them, never panic for expected failures; wrap with context `fmt.Errorf("find expense %s: %w", id, err)`; sentinel errors (`var ErrNotFound = errors.New(...)`) and typed errors checked with `errors.Is`/`errors.As`; map to HTTP status in one place.
- `context.Context` first parameter of every I/O function, honoured for cancellation and deadlines; never stored in a struct.
- Concurrency: goroutines owned by a parent with `errgroup`/`sync.WaitGroup.Go`, channels for ownership transfer, mutexes for shared state, no goroutine leak (always a way to stop); run tests with `-race`.
- HTTP: `net/http` `ServeMux` patterns (`GET /expenses/{id}`) or chi; timeouts on server and clients; `http.CrossOriginProtection` for CSRF; JSON with explicit structs and `json:"snake_case"` tags.
