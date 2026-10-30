# Dart / Flutter best practices: code

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
