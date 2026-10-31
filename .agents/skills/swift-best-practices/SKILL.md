---
name: swift-best-practices
description: "MANDATORY for any Swift code (SwiftUI, server Swift, packages): MVVM with @Observable, repositories behind protocols, Swift 6 concurrency, Swift Testing."
---

# Swift best practices (router)

The user has no Swift project yet (the iPhone client is the web PWA): these rules transpose the team's Android conventions
(`kotlin-best-practices`) to SwiftUI. Layout and accessibility: `ui-responsive-accessible-modular`.

Load only the row(s) that match the task; never every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Creating a module / tooling, versions, layout | `references/setup.md` |
| Writing or reviewing code | `references/code.md` |
| Writing or reviewing unit tests | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
