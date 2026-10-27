# Docker: container runtime security and operations

- Run as non-root; drop unnecessary capabilities, avoid privileged mode and host mounts, and use a read-only root filesystem
  where compatible.
- Expose only required ports. Define health checks, resource limits, graceful shutdown, log/metrics handling, and restart
  behavior appropriate to the platform.
- Persist data in explicitly managed volumes or external services. Document backup, restore, migration, and rollback before
  using containers for stateful production services.
- Ask before exposing services publicly, deleting persistent volumes, changing production, or enabling billable resources.
