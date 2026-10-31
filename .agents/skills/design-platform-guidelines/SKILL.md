---
name: design-platform-guidelines
description: "designer: native design language of the platform concerned (Material 3, iOS HIG, Fluent, web); load only that platform."
---

# Platform design guidelines (load only the platform concerned) (router)

The project's own design system always comes first; this skill says what to follow when there is none or when a new screen needs
the platform's native pattern. Several platforms in one project: each proposal follows its platform, the journey stays the same.

Load only the row(s) that match the task; never every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Android (Material 3 / Expressive) | `references/android.md` |
| iOS / macOS (Human Interface Guidelines) | `references/ios.md` |
| Windows desktop (Fluent / WinUI) | `references/windows.md` |
| Web | `references/web.md` |
| Cross-platform desktop (Qt, Electron, Tauri) | `references/desktop.md` |
| Monthly refresh, sources | `references/maintenance.md` |
