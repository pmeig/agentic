# Swift best practices: code

- MVVM: SwiftUI views stay dumb; `@Observable @MainActor final class XxxViewModel` holds state and actions; views read it with `@State`/`@Bindable`; navigation with `NavigationStack` + typed routes.
- Repositories behind protocols (`protocol ExpenseRepository: Sendable`), implemented with `URLSession` async/await and a local store (SwiftData/GRDB) for **offline-first** (queue writes, push when the network is back, as the Android app does); injected through initializers from a small container, never singletons reached from views.
- Concurrency: `async/await`, actors for shared mutable state, `Sendable` types across isolation, `@MainActor` for UI, `Task` cancellation honoured, no `DispatchQueue` in new code.
- Value types (`struct`, `enum` with associated values) by default, `final class` when identity is needed, `let` over `var`, typed throws (`throws(ExpenseError)`) for domain errors, `Result` at boundaries.
- No force unwrap/`try!` outside tests; `guard let` early exits; `Codable` DTOs mapped to domain models.
- Money with `Decimal`, dates with `Date` + `FormatStyle`, user-facing strings in String Catalogs (`Localizable.xcstrings`).
- Accessibility: Dynamic Type, `accessibilityLabel`/`Hint`, 44 pt targets, VoiceOver order, dark mode; responsive with size classes and `ViewThatFits`.
- Secrets never in the app bundle (Keychain for tokens); logging with `Logger` (OSLog), no personal data.
- Naming per the Swift API Design Guidelines; `///` doc comments on public API.
