---
name: translation-skill-factory
description: Use to create a missing language-<code> or translation-<source>-<target> skill in the existing format.
---

# Translation skill factory (router)

The translator creates its own skills. Never translate with a language or pair that has no skill: generate it first, then use it.

Load only the row(s) that match the task; never every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Creating a missing language-<code> skill | `references/language.md` |
| Creating a missing translation-<source>-<target> skill | `references/pair.md` |
| Monthly refresh, sources | `references/maintenance.md` |
