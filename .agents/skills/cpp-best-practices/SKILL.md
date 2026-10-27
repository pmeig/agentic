---
name: cpp-best-practices
description: "MANDATORY for any C or C++ code (apps, libraries, Qt, Unreal): RAII, value semantics, const by default, CMake presets, GoogleTest/Catch2, C++23/26."
---

# C / C++ best practices (router)

The user has Qt (`D:\projects\Qt\certification`: signing scripts only) and Unreal Engine (`D:\projects\UE\tuto`: Blueprint project)
folders but no C++ sources: these rules transpose the team's conventions to modern C++ and follow the C++ Core Guidelines.
Project rules win. Load only the row(s) that match the task; never load every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Project, CMake, dependencies, warnings, CI tooling, layout | `references/setup.md` |
| Writing C/C++ code: RAII, errors, types, concurrency, C | `references/code.md` |
| Layering, dependency injection, naming, headers | `references/structure.md` |
| Qt 6 / QML code | `references/qt.md` |
| Unreal Engine 5 code | `references/unreal.md` |
| Unit tests (GoogleTest/Catch2, parameterized, coverage) | `references/tests.md` |
| Monthly refresh | `references/maintenance.md` |
