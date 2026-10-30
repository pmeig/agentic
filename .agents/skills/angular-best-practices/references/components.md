# Angular best practices: components (signals, templates, inputs, DI)

- **Signals for all state**: `protected readonly x = signal(...)`, `computed` for derived values (never a getter called from the template), replace instead of mutate (`update(list => [...list, item])`); `effect()` only for real side effects (storage, DOM, logging), with `untracked` around writes.
- `input()` / `input.required()` / `output()` / `model()`, `viewChild()`/`contentChild()` signal queries, `booleanAttribute` transforms; never `@Input`/`@Output`/`@ViewChild` in new code.
- `inject()` in fields (`private readonly` for internals, `protected readonly` for what the template uses); no constructor DI in components and services.
- `changeDetection: OnPush` (default in v22) and zoneless: anything shown must be a signal (or `async` pipe).
- Templates: built-in control flow (`@if (x(); as value)`, `@for (... ; track item.id)`, `@switch`, `@defer` for heavy below-the-fold parts), self-closing tags, `type="button"` on non-submit buttons, `data-testid` on interactive elements for e2e. Separate `templateUrl` + `styleUrl` (`.scss`), no file when there is no style.
- Host bindings in the `host: {}` metadata (not `@HostListener`/`@HostBinding`); cleanup with `inject(DestroyRef).onDestroy` or `takeUntilDestroyed`.
- Handlers `protected async ...(): Promise<void>` guarded by a `busy` signal, `try/catch/finally` setting an `error` signal; floating promises marked `void`.
- Selectors: kebab-case elements without prefix in apps, camelCase attribute directives; classes `XxxPage`, `XxxComponent`, `XxxDirective`, root `App`.
