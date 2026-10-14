---
name: devops-trunk-based
description: Use after the lead confirms trunk-based development to design CI/CD, versioning, and artifact promotion for a single integration trunk.
---

# Trunk-Based CI/CD

Apply this skill only when the lead has selected trunk-based development. Do not import the branch-per-environment suffix or
promotion rules from `devops-branch-environment`.

## Branch and workflow model

- Use one shared trunk, normally `main`, with short-lived feature branches merged through pull requests.
- Do not create long-lived `develop`, `release`, or environment-named branches unless the lead explicitly requests them.
- Keep `quality.yml`, `build.yml`, and `deploy.yml` responsibilities separate. Put required unit, quality, and E2E jobs in
  `quality.yml`; run independent checks in parallel and add `needs` only for genuine dependencies.
- Run the pull-request quality gate before merge. After merge to trunk, build the release artifact and deploy according to the
  user-confirmed environment sequence.

## Decisions to confirm

The branch model does not define release or deployment policy. Ask the lead and record the answers before implementing when the
project does not already specify:

- how many deployment environments exist, their names, promotion order, and approval gates;
- when versions are assigned or bumped, the version scheme, and whether versions belong to the whole repository or individual
  modules;
- which event creates a release artifact, how it is tagged, whether the same immutable artifact is promoted or rebuilt per
  environment, and whether promotion to production requires an approval.

Do not apply `-SNAPSHOT` or `-RC` naming from the branch-per-environment strategy unless the lead explicitly chooses it.
Prefer promoting the same immutable artifact through environments once the lead confirms that release policy.

## Shared version actions

Prefer the user's `pmeig/github-actions` composites for semantic version bumps and commits, including
`actions/context/version/semver/bump` and `actions/github/push`. Follow the project's existing version files and do not duplicate
shared version logic in shell scripts.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, recheck official Git, Actions, release, and deployment sources. Verify triggers, action inputs, and
environment APIs; preserve user rules, update sources/date, and report changes. For UI help, capture authorized current screens
with sensitive data redacted, or disclose unavailable access and provide official links/navigation.

## Official sources

- GitHub Actions workflow syntax: https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions
- GitHub protected branches: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches
- Shared versioning actions: https://github.com/pmeig/github-actions
- Team example: https://github.com/pmeig/budget
