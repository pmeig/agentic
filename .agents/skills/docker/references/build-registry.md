# Docker: build, registry and promotion

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
