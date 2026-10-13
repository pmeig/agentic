---
name: swift-best-practices
description: MANDATORY when writing, reviewing or testing Swift code (iOS/macOS apps with SwiftUI, server Swift, packages): the team's conventions transposed to Swift - MVVM with @Observable view models, pages/ and core/ modules, repositories behind protocols, offline-first, Swift 6 strict concurrency, Swift Testing with one @Suite per public method and should_..._when_... names - plus current Swift 6.x practices.
---

# Swift best practices

The user has no Swift project yet (the iPhone client is the web PWA): these rules transpose the team's Android conventions
(`android-compose-architecture`, `kotlin-best-practices`) to SwiftUI. Layout and accessibility: `ui-responsive-accessible-modular`.

## 1. Setup

- Latest Xcode / Swift 6.x, **Swift 6 language mode** (complete data-race checking), Swift Package Manager for dependencies and for local modules (`Packages/Core`), `swift-format` or SwiftLint in CI.
- App layout: `App/` (entry, DI container), `Pages/<Name>/<Name>Page.swift` + its view model and sub-views, `Core/<kind of feature>/` (Networking, Storage, Auth, UI, I18n).

## 2. Code

- MVVM: SwiftUI views stay dumb; `@Observable @MainActor final class XxxViewModel` holds state and actions; views read it with `@State`/`@Bindable`; navigation with `NavigationStack` + typed routes.
- Repositories behind protocols (`protocol ExpenseRepository: Sendable`), implemented with `URLSession` async/await and a local store (SwiftData/GRDB) for **offline-first** (queue writes, push when the network is back, as the Android app does); injected through initializers from a small container, never singletons reached from views.
- Concurrency: `async/await`, actors for shared mutable state, `Sendable` types across isolation, `@MainActor` for UI, `Task` cancellation honoured, no `DispatchQueue` in new code.
- Value types (`struct`, `enum` with associated values) by default, `final class` when identity is needed, `let` over `var`, typed throws (`throws(ExpenseError)`) for domain errors, `Result` at boundaries.
- No force unwrap/`try!` outside tests; `guard let` early exits; `Codable` DTOs mapped to domain models.
- Money with `Decimal`, dates with `Date` + `FormatStyle`, user-facing strings in String Catalogs (`Localizable.xcstrings`).
- Accessibility: Dynamic Type, `accessibilityLabel`/`Hint`, 44 pt targets, VoiceOver order, dark mode; responsive with size classes and `ViewThatFits`.
- Secrets never in the app bundle (Keychain for tokens); logging with `Logger` (OSLog), no personal data.
- Naming per the Swift API Design Guidelines; `///` doc comments on public API.

## 3. Tests (Swift Testing)

- One test file per type; **one `@Suite` per public method**, nested in the type's suite, test names `should_<result>_when_<condition>`:
  ```swift
  @Suite struct ExpenseViewModelTests {
      @Suite struct Save {
          @Test func should_add_pending_expense_when_offline() async throws {
              let repository = FakeExpenseRepository(online: false)
              let viewModel = await ExpenseViewModel(repository: repository)

              try await viewModel.save(.valid)

              #expect(repository.pending.count == 1)
          }
      }
  }
  ```
- Hand-written fakes conforming to the protocols, parameterized `@Test(arguments:)`, `#expect(throws:)` for errors, injected clocks; XCUITest or Maestro for e2e (`e2e-android-then-web` logic: same flows on every client).

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `@Test(arguments:)` (zipped or combined collections) inside the `@Suite` of the method. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

## Monthly refresh

Last refreshed: 2026-10

- On the **first use of this skill in a calendar month after the date above**, refresh it before applying it: search the web for
  what changed since that month (new stable versions, newly recommended practices, deprecated or removed APIs and tools).
- Update **only the parts that come from the internet**: add the new practices, change outdated versions, remove what is
  deprecated or removed. Keep it short, prefer official sources (release notes, official docs).
- **Never remove or weaken the user's rules**: everything taken from the user's projects (`D:\projects\...`) or explicit
  instructions and the team conventions (layered controller/service/repository, pages/ + core/ modules, one test group per public
  method with parameterized tests favored, `should_..._when_...` names, mocks built by hand, Lombok always for Java, every branch covered...). When the internet
  contradicts one of them, keep the rule and tell the user about the conflict.
- Then set "Last refreshed" to the current month and tell the user in a few bullets what was added, changed or removed (with sources).
