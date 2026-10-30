# Angular best practices: setup (project, build, app config)

- Latest Angular, **standalone** (never write `standalone: true`, never an NgModule except a library's import bundle), **zoneless** (no zone.js, no `provideZoneChangeDetection`), `@angular/build:application` (esbuild), strict TS + `strictTemplates`, `strictInjectionParameters`, `strictInputAccessModifiers`.
- `app.config.ts`: `provideBrowserGlobalErrorListeners()`, `provideRouter(routes, withComponentInputBinding())`, `provideHttpClient(withFetch(), withInterceptors([...]))`, service worker for PWAs (`registerWhenStable:30000`), custom `TitleStrategy` when titles are translated.
- Schematics defaults: OnPush, `style: scss`, functional guards/interceptors/resolvers, `typeSeparator: "."`, no selector prefix in apps.
- Budgets in production (initial 750 kB warning / 1 MB error, component style 4/8 kB), `outputHashing: all`.
