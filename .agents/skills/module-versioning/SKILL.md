---
name: module-versioning
description: Use for CI/CD in a monorepo with independently versioned modules to manage change detection, SemVer bumps, builds, tags, and releases per module.
---

# Per-Module Versioning

Use this skill when a repository contains modules that can be built or released independently. Follow the module-versioning
pattern used by `pmeig/budget`.

## Discover the version model

- Identify the independently releasable modules, each module's authoritative version file, dependency relationships, image or
  package name, and release tag format.
- Keep each module's version and release lifecycle independent. A change to one module must not bump, build, or publish an
  unrelated module.
- Ask the lead when module boundaries, shared-module impact, version ownership, or the SemVer bump policy is unclear.
- Record the version file, artifact name, and release-tag format for each module in the shared feature docs.

## CI and release behavior

- Determine changed modules from the pull request diff and run the relevant quality checks and builds. Changes to shared modules
  must also validate their dependents.
- Build, publish, promote, and release modules independently. Use module-qualified release tags where the repository convention
  requires them.
- Never infer a release from a version-file-only change; follow the repository's existing change-detection rules.
- Keep source/application versions separate from container image tags when the selected branch strategy defines different
  suffixes.

## Shared version actions

Prefer the user's `pmeig/github-actions` composites, especially `actions/context/version/semver/bump`,
`actions/context/version/suffix`, and `actions/github/push`. Use them for SemVer calculation, environment suffixes, and version
commits rather than creating duplicate shell logic. Follow the selected branch-strategy skill for suffixes and promotion; do not
mix the trunk-based and branch-per-environment models.

After a successful release, prepare the next module version only according to the documented bump policy. Do not guess whether the
next version should be patch, minor, or major.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, recheck official GitHub Actions and `pmeig/github-actions` sources for versioning and workflow
changes. Verify action inputs, outputs, and permissions; preserve user/project rules, update sources/date, and report changes.
For GitHub UI help, capture authorized current screens with sensitive data redacted, or disclose unavailable access and provide
official links and exact navigation.

## Official sources

- Semantic Versioning specification: https://semver.org/
- GitHub Actions workflow syntax: https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions
- Shared versioning actions: https://github.com/pmeig/github-actions
- Example module-versioned project: https://github.com/pmeig/budget
