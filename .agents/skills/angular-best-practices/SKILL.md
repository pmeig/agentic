---
name: angular-best-practices
description: MANDATORY when writing, reviewing or testing Angular code (apps, PWAs, component libraries): the user's conventions - standalone, zoneless, signals everywhere, inject(), functional guards/interceptors, lazy loadComponent pages, Promise-based HTTP, custom t pipe i18n, pure helpers tested with Vitest - plus current Angular (21/22) practices. Use for any Angular component, service, template, route or spec.
---

# Angular best practices

Based on `D:\projects\typescript\budget\web` (reference), `D:\projects\angular\angular-material` (library workspace),
`cofee`, plus Angular 21/22 practice. Bootstrap libraries `@pmeig/ngb-*`: `pmeig-ngb-libs`; page/core layout, responsive and
accessibility: `ui-responsive-accessible-modular`; language: `typescript-best-practices`.

## 1. Setup

- Latest Angular, **standalone** (never write `standalone: true`, never an NgModule except a library's import bundle), **zoneless** (no zone.js, no `provideZoneChangeDetection`), `@angular/build:application` (esbuild), strict TS + `strictTemplates`, `strictInjectionParameters`, `strictInputAccessModifiers`.
- `app.config.ts`: `provideBrowserGlobalErrorListeners()`, `provideRouter(routes, withComponentInputBinding())`, `provideHttpClient(withFetch(), withInterceptors([...]))`, service worker for PWAs (`registerWhenStable:30000`), custom `TitleStrategy` when titles are translated.
- Schematics defaults: OnPush, `style: scss`, functional guards/interceptors/resolvers, `typeSeparator: "."`, no selector prefix in apps.
- Budgets in production (initial 750 kB warning / 1 MB error, component style 4/8 kB), `outputHashing: all`.

## 2. Components

- **Signals for all state**: `protected readonly x = signal(...)`, `computed` for derived values (never a getter called from the template), replace instead of mutate (`update(list => [...list, item])`); `effect()` only for real side effects (storage, DOM, logging), with `untracked` around writes.
- `input()` / `input.required()` / `output()` / `model()`, `viewChild()`/`contentChild()` signal queries, `booleanAttribute` transforms; never `@Input`/`@Output`/`@ViewChild` in new code.
- `inject()` in fields (`private readonly` for internals, `protected readonly` for what the template uses); no constructor DI in components and services.
- `changeDetection: OnPush` (default in v22) and zoneless: anything shown must be a signal (or `async` pipe).
- Templates: built-in control flow (`@if (x(); as value)`, `@for (... ; track item.id)`, `@switch`, `@defer` for heavy below-the-fold parts), self-closing tags, `type="button"` on non-submit buttons, `data-testid` on interactive elements for e2e. Separate `templateUrl` + `styleUrl` (`.scss`), no file when there is no style.
- Host bindings in the `host: {}` metadata (not `@HostListener`/`@HostBinding`); cleanup with `inject(DestroyRef).onDestroy` or `takeUntilDestroyed`.
- Handlers `protected async ...(): Promise<void>` guarded by a `busy` signal, `try/catch/finally` setting an `error` signal; floating promises marked `void`.
- Selectors: kebab-case elements without prefix in apps, camelCase attribute directives; classes `XxxPage`, `XxxComponent`, `XxxDirective`, root `App`.

## 3. Services, data, routing, forms

- `@Injectable({ providedIn: 'root' })` signal stores: private writable `signal`, exposed with `asReadonly()` and `computed`. Logic that deserves tests lives in plain classes (constructor DI) or pure functions in `*.helper.ts`, wrapped by the thin service.
- HTTP: an `ApiService` returning `firstValueFrom(this.http.get<T>(...))` (Promises + async/await); RxJS only for real streams (router events via `toSignal`, debounce, websockets); `resource`/`httpResource` for read-only data bound to signals once stable in the project's version.
- Functional interceptors (`HttpInterceptorFn`, `request.clone({ setHeaders })`, rethrow with `throwError(() => error)`) and guards (`CanActivateFn` returning `true` or a `UrlTree` with `returnUrl`).
- Errors: helpers taking `unknown` and mapping `HttpErrorResponse` status to translated messages, shown in an `error` signal and a snackbar service.
- Routing: every page lazy (`loadComponent: () => import('./pages/x/x.page').then(m => m.XPage)`), protected parent with `canActivate`, a `title` per route, `**` redirect; route/query params bound to `input()`s (`withComponentInputBinding`).
- i18n: custom `I18nService` (language signal, `t(key, ...args)` falling back to English then the key) + impure `t` pipe, message bundles per language in `core/i18n/messages/*.ts`; keys for route titles.
- Forms: template-driven with signals (`[ngModel]="email()" (ngModelChange)="email.set($event)"`) and `computed` field errors from pure validators, or Signal Forms when stable in the version used; reactive typed forms for large/dynamic forms.
- SSR-safe code: guard browser APIs (`isPlatformBrowser`, `typeof window === 'undefined'`).

## 4. Libraries (ng-packagr)

- One project per library (`@pmeig/ngb-<name>`), `src/public-api.ts` → `public.*.ts` barrels, peer deps `@angular/* >= <major>`, `sideEffects: false`, `compilationMode: partial`; a `XxxMaterial` NgModule only bundles standalone directives for import.
- Directive base classes (`TagDirective`) for shared behavior, DOM changes through `Renderer2`, `override` on lifecycle hooks, typed signal inputs with transforms; README per library with API table, "Fixed in", "Known issues".

## 5. Tests

- Vitest through `@angular/build:unit-test` (jsdom), explicit `import { describe, expect, it, vi } from 'vitest'`.
- Unit-test pure helpers and service cores (no TestBed needed): one `describe` per function, behavior sentences in `it`, `setup()` factories returning fakes, `vi.useFakeTimers()` + `advanceTimersByTime`. Components and pages are covered by e2e (Playwright) unless they hold logic that cannot move to a helper.
- Library directives: a host component with an inline template per variant, `TestBed.createComponent(Host)`, wait for stability (and the libraries' 50 ms debounce) before asserting.
- Accessibility checked in e2e with axe (0 violation).

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `it.each` (table of objects, `$name` in the title) inside the `describe` of the function. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, check official sources for version, practice, and deprecation changes. Update only internet-derived
guidance; preserve user/project rules. Add source URLs, update this date, and briefly report changes.
