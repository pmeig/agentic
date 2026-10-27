# C / C++ best practices: setup

- C++23 (C++26 features when the compilers of the project support them), C17 for C; CMake ≥ 3.28 with `CMakePresets.json`, targets with `target_*` commands (no global flags), dependencies through vcpkg or Conan (versions pinned).
- Warnings as errors (`-Wall -Wextra -Wpedantic -Werror` / `/W4 /WX`), sanitizers (ASan, UBSan, TSan) in a debug preset, `clang-format` + `clang-tidy` (Core Guidelines checks) in CI.
- Layout: `include/<project>/` public headers, `src/<feature>/` implementation, `tests/`, `apps/` for executables; one library target per module.
