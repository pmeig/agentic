# Mockup render: HTML mockup file

One **self-contained** file per proposal: `.agents/docs/team/<feature>/design/proposal-<n>-<idea>.html`, inline CSS (custom properties as tokens: colors, type, spacing), no build, no network except an optional system-safe font; relative units; mobile first with media queries; `prefers-color-scheme` and `prefers-reduced-motion` handled.

Real labels and realistic data (the product language), all states reachable: a small state switcher (`?state=empty|loading|error|success|long`) or one section per state; semantic HTML (landmarks, headings, buttons, labels) so the mockup can be tested for accessibility.

Charts follow the `dataviz` skill when the harness has it. The final design: `design/final.html` + `design/spec.md`.
