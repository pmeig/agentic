# API documentation: OpenAPI and AsyncAPI: asyncapi

## AsyncAPI (events, queues, WebSocket, MQTT, Kafka)

- Use AsyncAPI **3.x** when the project has messages: one `channels` entry per topic/queue/socket event, `operations` (`send`/`receive`),
  `messages` with payload schemas, `servers` for brokers. Same rules: names = identifiers in code, one file, validate with
  `npx -y @asyncapi/cli validate asyncapi.yaml`.
- No messaging in the project: do not create the file.
