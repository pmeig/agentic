---
name: docker
description: Use for Dockerfiles, images, builds, registries, runtime security, Docker Compose, and container deployment.
---

# Docker

Use this skill for Docker-based development and deployment. Choose Docker Compose for local or suitable single-host workloads;
recommend an orchestrator only when scale, availability, or multi-host requirements justify the additional operations burden.

## Dockerfiles and images

- Inspect existing Dockerfiles, base images, build arguments, and architecture requirements before changing the image.
- Prefer multi-stage builds, minimal trusted base images, an explicit non-root user, a `.dockerignore`, and reproducible build
  inputs. Pin production base images by a reviewed immutable digest when the project can maintain those updates.
- Never pass secrets through Dockerfile `ARG`, `ENV`, image layers, build logs, or labels. Use a supported BuildKit secret mount
  for build-only credentials.
- Keep runtime configuration outside the image. Use environment-specific config/secrets at runtime, not by rebuilding an image
  with secrets embedded.

## Build, registry, and promotion

- Use Buildx for multi-platform builds when target architectures require it. Verify target platforms and builder availability
  before building.
- Label images with source and version metadata. Publish immutable version/digest references and retain the digest for
  verification and rollback.
- Authenticate to registries with short-lived credentials or workload identity where supported. Never place registry passwords
  in command arguments, logs, or repository files.
- Promote the same image digest between environments. Moving a release or environment tag is acceptable only when it points to
  the already-built digest; do not rebuild production artifacts.
- Configure image vulnerability scanning and provenance/SBOM according to the project's security requirements; verify the
  selected tool and current Docker features before adding flags or policies.

## Container runtime and operations

- Run as non-root; drop unnecessary capabilities, avoid privileged mode and host mounts, and use a read-only root filesystem
  where compatible.
- Expose only required ports. Define health checks, resource limits, graceful shutdown, log/metrics handling, and restart
  behavior appropriate to the platform.
- Persist data in explicitly managed volumes or external services. Document backup, restore, migration, and rollback before
  using containers for stateful production services.
- Ask before exposing services publicly, deleting persistent volumes, changing production, or enabling billable resources.

## Docker Compose

- Follow the repository's Compose Specification and current CLI. Use service DNS for internal communication, named volumes for
  persistent state, and health checks for dependencies.
- Use profiles only for optional services or tasks. Separate local development settings from production overrides when needed.
- Protect environment files with `.gitignore`; never commit secret values. Review the fully rendered Compose configuration
  before applying it because Compose files can request broad host access.
- `docker compose config` can validate and render the model. Compose deployments target a single Docker host; do not present
  Compose as a multi-node scheduler.
- For public single-host use, document TLS/reverse proxy, host firewall, OS updates, log and disk monitoring, backups, and
  recovery. Explain when a managed container platform or Kubernetes is more appropriate.

## User assistance

Use Docker CLI/API operations when authenticated and authorized. For Docker Desktop, registry UI or cloud console steps, explain
current navigation (authorized screenshots, redacting account IDs, private endpoints, personal data and credentials); if UI access
is unavailable, say so and give official links and exact steps.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, recheck official Docker Engine, Dockerfile, Buildx, Compose, registry, security, and licensing
sources. Verify syntax, flags, attestations, Compose, and terms; preserve user rules, update sources/date, and report changes.

## Official sources

- Docker documentation: https://docs.docker.com/
- Dockerfile reference: https://docs.docker.com/reference/dockerfile/
- Buildx: https://docs.docker.com/build/buildx/
- Compose: https://docs.docker.com/compose/
- Docker Engine security: https://docs.docker.com/engine/security/
