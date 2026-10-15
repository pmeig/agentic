---
name: dart-flutter-best-practices
description: MANDATORY for any Dart or Flutter code: pages/ and core/ modules, MVVM view models, repositories, offline-first, flutter_test, Dart 3.
---

# Dart / Flutter best practices

The user has no Flutter project yet: these rules transpose the team's Android/Angular conventions to Flutter
(official Flutter architecture guide: UI layer with views + view models, data layer with repositories + services).

## 1. Setup

- Latest stable Flutter/Dart 3 (FVM or `.fvmrc` to pin), `analysis_options.yaml` with `flutter_lints` or `very_good_analysis`, `dart format` + `flutter analyze` in CI, null safety everywhere.
- Layout: `lib/main.dart` (wiring), `lib/pages/<name>/<name>_page.dart` + view model + widgets, `lib/core/<kind of feature>/` (data, network, storage, auth, ui, l10n), `test/` mirroring `lib/`.

## 2. Code

- MVVM: widgets render and forward events; view models (`ChangeNotifier` + `ListenableBuilder`, or Riverpod `Notifier`) hold UI state and commands; repositories (abstract class + implementation) own data and caching; services wrap APIs and local storage.
- **Offline-first**: local store (drift/sqflite/Hive) as source of truth, writes queued and synced when connectivity returns, like the Android app.
- Immutable models (`final` fields, `copyWith`, `freezed` or Dart 3 records/sealed classes), `sealed class` + `switch` pattern matching for states and results; no `dynamic`.
- Dependency injection through constructors (Provider/Riverpod at the root), no global singletons reached from widgets.
- `const` constructors and small widgets for rebuild performance; keys for list items; heavy work in isolates (`compute`).
- Errors: typed exceptions in the data layer mapped to UI states; `Result` sealed types for expected failures; never swallow errors.
- Navigation with `go_router` (typed routes), localization with `flutter_localizations` + ARB files, theming from a single `ThemeData` (Material 3 color scheme).
- Accessibility: `Semantics`, 48 dp targets, text scaling, contrast, screen reader order; responsive with `LayoutBuilder`/breakpoints (`ui-responsive-accessible-modular`).
- Secrets never in the app (flutter_secure_storage for tokens); logging with `package:logging`, no personal data.
- Naming: `lower_snake_case` files, `UpperCamelCase` types, `lowerCamelCase` members and constants; `///` doc comments on public API.

## 3. Tests

- `flutter_test` + `mocktail`: **one `group` per public method**, test names `should <result> when <condition>`:
  ```dart
  void main() {
    late FakeExpenseRepository repository;
    late ExpenseViewModel viewModel;

    setUp(() {
      repository = FakeExpenseRepository();
      viewModel = ExpenseViewModel(repository);
    });

    group('save', () {
      test('should queue the expense when offline', () async {
        repository.online = false;

        await viewModel.save(validExpense);

        expect(repository.pending, hasLength(1));
      });
    });
  }
  ```
- Widget tests with `pumpWidget` + `find.bySemanticsLabel`, golden tests for key screens, `integration_test`/Patrol or Maestro for e2e; fake clocks (`clock` package); coverage `flutter test --coverage` (lcov for Sonar).

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with a list of cases iterated inside the `group` of the method (`for (final c in cases) test("should ... when ${c.name}", ...)`). Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the official sources, update only internet-derived guidance, keep user/project rules, add source URLs, update this date, report changes.
