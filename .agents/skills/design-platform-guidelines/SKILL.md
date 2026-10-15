---
name: design-platform-guidelines
description: designer: native design language of the platform concerned (Material 3, iOS HIG, Fluent, web); load only that platform.
---

# Platform design guidelines (load only the platform concerned)

The project's own design system always comes first; this skill says what to follow when there is none or when a new screen needs
the platform's native pattern. Several platforms in one project: each proposal follows its platform, the journey stays the same.

## Android: Material 3 and Material 3 Expressive

- Dynamic color and tonal palettes (HCT), roles `primary` / `on-primary`, surface containers, shape scale; type scale roles.
- Window size classes (compact, medium, expanded) with navigation bar → rail → drawer; edge-to-edge with insets; predictive back.
- Components: top app bar, FAB, bottom sheet, snackbar, dialogs, chips, cards, segmented buttons, search bar. Expressive adds
  spring-based motion, shape morphing, emphasized type and color, and new components: use at the "excellent" level, not everywhere.
- Touch targets 48 dp; Compose component names help `front` (`android-compose-architecture`).

## iOS / macOS: Human Interface Guidelines

- Liquid Glass (OS 26): translucent material for navigation and controls **floating above content**, never on the content itself;
  keep contrast (check the system opacity setting), use the standard bars and controls so they adopt it.
- Navigation: tab bar for top-level areas, navigation stack with large titles, sheets with detents; SF Symbols; Dynamic Type; safe areas.
- Gestures follow the platform (swipe back, pull to refresh), always with a visible alternative; Dark Mode, Reduce Motion and
  Reduce Transparency respected; targets 44 pt.

## Windows desktop: Fluent / WinUI

- NavigationView (left or top), command bar, acrylic / mica sparingly, keyboard and pointer first, resizable windows, high contrast themes
  respected, targets at least 24 px with pointer precision.

## Web

- Responsive and progressive: semantic landmarks, the project's CSS framework (Bootstrap 5: grid, utilities, components; the
  `@pmeig/ngb-*` libraries when used, `pmeig-ngb-libs`), system font stack, `prefers-color-scheme` and `prefers-reduced-motion`,
  hover is never the only way to reveal an action, URLs for states.
- Keyboard, focus order and visible focus; forms with native inputs first.

## Desktop cross-platform (Qt, Electron, Tauri)

Follow the guidelines of the OS it runs on for window chrome, menus and shortcuts; consistent app-level design inside the window.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://m3.material.io/ , https://developer.android.com/design , https://developer.apple.com/design/human-interface-guidelines/ ,
https://learn.microsoft.com/windows/apps/design/ , https://getbootstrap.com/docs/5.3/
