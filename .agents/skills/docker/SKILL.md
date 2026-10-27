---
name: docker
description: "Use for Dockerfiles, images, builds, registries, runtime security, Docker Compose, and container deployment."
---

# Docker (router)

Use this skill for Docker-based development and deployment. Choose Docker Compose for local or suitable single-host workloads;
recommend an orchestrator only when scale, availability, or multi-host requirements justify the additional operations burden.
Project rules win. Load only the row(s) that match the task; never load every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Writing or changing a Dockerfile / image, build-time secrets | `references/dockerfile.md` |
| Buildx, labels, registry login, promotion, scanning, SBOM | `references/build-registry.md` |
| Running containers: non-root, ports, health, volumes, ask-first actions | `references/runtime-security.md` |
| Compose files, profiles, env files, single-host deployment | `references/compose.md` |
| Helping the user in Docker Desktop / registry / cloud UI | `references/user-assistance.md` |
| Monthly refresh, official sources | `references/maintenance.md` |
