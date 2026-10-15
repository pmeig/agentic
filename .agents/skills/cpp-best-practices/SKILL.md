---
name: cpp-best-practices
description: MANDATORY for any C or C++ code (apps, libraries, Qt, Unreal): RAII, value semantics, const by default, CMake presets, GoogleTest/Catch2, C++23/26.
---

# C / C++ best practices

The user has Qt (`D:\projects\Qt\certification`: signing scripts only) and Unreal Engine (`D:\projects\UE\tuto`: Blueprint project)
folders but no C++ sources: these rules transpose the team's conventions to modern C++ and follow the C++ Core Guidelines.

## 1. Setup

- C++23 (C++26 features when the compilers of the project support them), C17 for C; CMake ≥ 3.28 with `CMakePresets.json`, targets with `target_*` commands (no global flags), dependencies through vcpkg or Conan (versions pinned).
- Warnings as errors (`-Wall -Wextra -Wpedantic -Werror` / `/W4 /WX`), sanitizers (ASan, UBSan, TSan) in a debug preset, `clang-format` + `clang-tidy` (Core Guidelines checks) in CI.
- Layout: `include/<project>/` public headers, `src/<feature>/` implementation, `tests/`, `apps/` for executables; one library target per module.

## 2. Code

- **RAII for every resource**; no raw owning pointers or `new`/`delete`: `std::unique_ptr` (default), `std::shared_ptr` only for real shared ownership, references or `std::span`/`std::string_view` for non-owning access.
- Value semantics and `const` by default (`const` locals, `const&` parameters for big types, `constexpr`/`consteval` where possible), rule of zero; `[[nodiscard]]` on functions whose result matters.
- Errors: exceptions for exceptional failures, `std::expected<T, Error>` for expected ones (parsing, I/O, validation); never error codes ignored; `noexcept` on moves and destructors.
- Types: `enum class`, strong types for ids/units, `std::optional` for absence, `std::variant` + `std::visit` for closed sets, concepts to constrain templates, ranges/views for transformations, `std::format`/`std::print` instead of iostream formatting.
- Concurrency: `std::jthread` + `std::stop_token`, `std::mutex` with `std::scoped_lock`, atomics only with a clear memory-order reason; no data shared without synchronization.
- Layering stays: UI/controller → service (business rules) → repository/infrastructure, dependencies injected through constructors (interfaces as abstract classes or concepts) for testability; no singletons with hidden state.
- Naming per project style (Qt: `camelCase` methods, `m_member`; Unreal: its prefixes), headers with `#pragma once`, minimal includes (forward declarations), no `using namespace` in headers.
- C: `const` correctness, sized types (`<stdint.h>`), bounds-checked APIs, every allocation paired with its free in the same module.

## 3. Qt 6

- Qt 6 + CMake (`qt_add_executable`, `qt_add_qml_module`), QML for UI with C++ models (`QAbstractListModel`, `Q_PROPERTY` with `NOTIFY`, `QML_ELEMENT`), logic out of QML; parent-child ownership for `QObject`s, `connect` with the function-pointer syntax, no blocking work on the GUI thread (`QtConcurrent`, worker `QThread`).
- Accessibility (`Accessible.name`), high-DPI and layouts that resize (`ui-responsive-accessible-modular`); code signing scripts in the CI.

## 4. Unreal Engine 5

- Gameplay logic in C++ classes exposed to Blueprints (`UCLASS`, `UPROPERTY(EditAnywhere, BlueprintReadOnly)`, `UFUNCTION(BlueprintCallable)`), Blueprints for content and tuning; UE naming (`A` actors, `U` objects, `F` structs, `E` enums, `b` booleans), `TObjectPtr` for UObject members, never raw `new` for UObjects.
- Modules declared in `*.Build.cs`, Gameplay Ability System / Enhanced Input for new projects, data in Data Assets/Data Tables, automation tests (`IMPLEMENT_SIMPLE_AUTOMATION_TEST`) for logic.

## 5. Tests

- GoogleTest (or Catch2): **one fixture/test suite per public method**, test names `should_<result>_when_<condition>`:
  ```cpp
  class ExpenseServiceCreate : public ::testing::Test {
  protected:
      FakeExpenseRepository repository;
      ExpenseService service{repository};
  };

  TEST_F(ExpenseServiceCreate, should_save_expense_when_input_is_valid) {
      const auto result = service.create(validInput());

      ASSERT_TRUE(result.has_value());
      EXPECT_EQ(repository.saved().size(), 1);
  }
  ```
  (Catch2: `TEST_CASE("ExpenseService")` with one `SECTION("create")` per method.)
- Hand-written fakes behind interfaces (gMock when needed), sanitizers on in test runs, coverage with gcov/llvm-cov for Sonar; Qt Test (`QTest`, `QSignalSpy`) for Qt classes.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with value-parameterized tests (`TEST_P` + `INSTANTIATE_TEST_SUITE_P`) or Catch2 `GENERATE` inside the suite of the method. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the official sources, update only internet-derived guidance, keep user/project rules, add source URLs, update this date, report changes.
