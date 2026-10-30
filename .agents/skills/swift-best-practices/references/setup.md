# Swift best practices: setup

- Latest Xcode / Swift 6.x, **Swift 6 language mode** (complete data-race checking), Swift Package Manager for dependencies and for local modules (`Packages/Core`), `swift-format` or SwiftLint in CI.
- App layout: `App/` (entry, DI container), `Pages/<Name>/<Name>Page.swift` + its view model and sub-views, `Core/<kind of feature>/` (Networking, Storage, Auth, UI, I18n).
