# SQL and NoSQL best practices: NoSQL, pick the store from the access patterns

| Store | Use for | Key rules |
|---|---|---|
| MongoDB | aggregates read/written as a whole, flexible documents | embed what is read together, reference what grows unbounded; schema validation; indexes on every query filter; transactions only when unavoidable |
| Redis | cache, sessions, rate limits, queues, pub/sub | TTL on every key, namespaced keys (`app:entity:id`), cache-aside with invalidation on write, never the only copy of business data |
| DynamoDB / Cassandra | huge write throughput, known queries | model tables from the queries (partition key spreads load, sort key orders), no scans, denormalize per query |
| Elasticsearch / OpenSearch | full-text search, analytics | derived index fed from the source of truth, explicit mappings |
| Neo4j | relationship-heavy queries | model relationships as first-class, index lookup properties |

- Default to PostgreSQL (relational + JSONB + full-text) unless an access pattern clearly needs another store; document the choice in the contract or the README.
