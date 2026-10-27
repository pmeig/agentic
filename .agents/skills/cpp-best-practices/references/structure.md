# C / C++ best practices: structure and naming

- Layering stays: UI/controller → service (business rules) → repository/infrastructure, dependencies injected through constructors (interfaces as abstract classes or concepts) for testability; no singletons with hidden state.
- Naming per project style (Qt: `camelCase` methods, `m_member`; Unreal: its prefixes), headers with `#pragma once`, minimal includes (forward declarations), no `using namespace` in headers.
