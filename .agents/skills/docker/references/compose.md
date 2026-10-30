# Docker: Compose and single-host deployment

- Follow the repository's Compose Specification and current CLI. Use service DNS for internal communication, named volumes for
  persistent state, and health checks for dependencies.
- Use profiles only for optional services or tasks. Separate local development settings from production overrides when needed.
- Protect environment files with `.gitignore`; never commit secret values. Review the fully rendered Compose configuration
  before applying it because Compose files can request broad host access.
- `docker compose config` can validate and render the model. Compose deployments target a single Docker host; do not present
  Compose as a multi-node scheduler.
- For public single-host use, document TLS/reverse proxy, host firewall, OS updates, log and disk monitoring, backups, and
  recovery. Explain when a managed container platform or Kubernetes is more appropriate.
