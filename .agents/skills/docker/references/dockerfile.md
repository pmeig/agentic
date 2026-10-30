# Docker: Dockerfiles and images

- Inspect existing Dockerfiles, base images, build arguments, and architecture requirements before changing the image.
- Prefer multi-stage builds, minimal trusted base images, an explicit non-root user, a `.dockerignore`, and reproducible build
  inputs. Pin production base images by a reviewed immutable digest when the project can maintain those updates.
- Never pass secrets through Dockerfile `ARG`, `ENV`, image layers, build logs, or labels. Use a supported BuildKit secret mount
  for build-only credentials.
- Keep runtime configuration outside the image. Use environment-specific config/secrets at runtime, not by rebuilding an image
  with secrets embedded.
