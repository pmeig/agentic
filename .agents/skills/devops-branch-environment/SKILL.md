---
name: devops-branch-environment
description: Use after the lead confirms branch-per-environment CI/CD to configure develop, optional release/prep, and main promotion flows.
---

# Branch-Per-Environment CI/CD

Apply this skill only when the lead has selected branch = environment. Before implementation, confirm the deployment environment
names and order, and ask whether a `prep` environment with a `release` branch exists. Do not also apply
`devops-trunk-based`.

## Workflow organization and quality

- Keep `quality.yml`, `build.yml`, and `deploy.yml` separate. Put unit, quality, and E2E jobs in `quality.yml`; do not create a
  separate E2E workflow for the normal quality gate.
- Run independent jobs in parallel. Use `needs` only when a job consumes a real output or artifact from another job.
- In the prep model, the `release` build on merge skips quality tests and builds the RC artifact. Do not run the quality workflow
  for that release merge.

## With prep: `develop` → `release` → `main`

1. A push to `develop` builds the application with `-SNAPSHOT` embedded in its version and tags the Docker image with
   `-SNAPSHOT`.
2. A merge to `release` does not run quality tests. Build the application with the clean release version, and tag its Docker
   image with `-RC`.
3. A merge to `main` promotes the existing RC image by adding the clean release tag (without `-RC`). Do not rebuild the image.

## Without prep: `develop` → `main`

1. A push to `develop` builds the application with the clean version embedded in its code (no suffix) and tags the Docker image
   with `-SNAPSHOT`.
2. A merge to `main` promotes that existing image by adding the clean release tag (without `-SNAPSHOT`). Do not rebuild the
   image.

Keep the embedded application version separate from the image tag. A clean application version can be carried by an image whose
Docker tag is suffixed; promotion changes the image tag, not the application binary.

## Version management and shared actions

- Follow the project's existing per-module or repository-wide version ownership. Ask the lead for the SemVer bump policy and
  bump timing when they are not documented.
- Prefer the shared composites in `pmeig/github-actions`, including `actions/context/version/semver/bump`,
  `actions/context/version/suffix`, and `actions/github/push`, rather than hand-written suffix, bump, or commit logic.
- Use `pmeig/budget` as the no-prep model reference; keep the explicit version and tag rules above authoritative if the example differs.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, recheck official Actions, shared-action, registry, and provider sources. Verify suffix/version,
triggers, and tag promotion; preserve user rules, update sources/date, and report changes. For UI help, capture authorized current
screens with sensitive data redacted, or disclose unavailable access and provide official links/navigation.

## Official sources

- GitHub Actions workflow syntax: https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions
- GitHub Actions environments: https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment
- Shared versioning actions: https://github.com/pmeig/github-actions
- Team CI/CD example: https://github.com/pmeig/budget
