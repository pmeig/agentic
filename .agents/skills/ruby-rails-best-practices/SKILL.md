---
name: ruby-rails-best-practices
description: "MANDATORY for any Ruby or Rails code: thin controllers, service and query objects, strong params, RuboCop, RSpec, Rails 8."
---

# Ruby / Rails best practices (router)

The user has no Ruby project yet: these rules transpose the team's conventions to idiomatic Rails.

Load only the row(s) that match the task; never every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Creating a module / tooling, versions, layout | `references/setup.md` |
| Writing or reviewing code | `references/code.md` |
| Writing or reviewing unit tests | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
