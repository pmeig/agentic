# SQL and NoSQL best practices: transactions

- Read-only transactions for reads, read-write with the default `READ COMMITTED`; `SERIALIZABLE` or `SELECT ... FOR UPDATE` only for real races (counters, balances), with retry on serialization failure.
- Short transactions, no network call inside; nested calls reuse the same connection (AsyncLocalStorage / Spring propagation); a client is destroyed after a failed rollback.
- Idempotent writes (natural keys, upserts, idempotency keys) for anything retried by clients or queues.
