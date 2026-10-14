---
name: create-project
description: Use before scaffolding a new project to ask where it belongs and whether to create a remote repository or a local-only Git repository.
---

# Creating a Project and Its Repository

Use this skill before creating project files, scaffolding modules, or setting up project CI.

## Questions to ask first

Ask the user one question at a time:

1. Where should the project live, and what should it be called?
2. Should it use an existing repository, create a new remote repository, or create a local-only Git repository?
3. If creating a remote repository, ask for the owner/name and visibility. Confirm before creating it.

Do not assume that a new project belongs in the current repository. Inspect the requested destination before writing and preserve
any existing files.

## Repository behavior

- If the user chooses an existing repository, work inside it and follow its current Git remotes and instructions.
- If the user explicitly requests a remote GitHub repository, verify `gh` authentication and repository availability, then create
  it with `gh` only after the owner, name, visibility, and creation are confirmed.
- If the user declines a remote repository, initialize a local Git repository in the new project directory with `git init`.
  Keep it local and do not add a remote.
- Never create, replace, rename, or change the visibility of a remote repository without explicit user approval.
- Never run `git init` inside a non-empty unrelated directory or overwrite an existing `.git` directory.

## Handover

Record the selected project path and repository choice in the project README or shared feature need. Then hand off the chosen
stack, repository location, and Git setup to the relevant agents.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, recheck the official GitHub CLI, repository API, and UI sources above. Verify syntax, scopes, and
permissions; preserve user/project rules, update source URLs and date, and report changes. For UI help, capture current screens
with an authorized tool and redact sensitive data, or disclose the limitation and provide official links and exact navigation.

## Official sources

- GitHub CLI `repo create`: https://cli.github.com/manual/gh_repo_create
- GitHub REST API repository creation: https://docs.github.com/en/rest/repos/repos#create-a-repository-for-the-authenticated-user
- GitHub new repository UI: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
