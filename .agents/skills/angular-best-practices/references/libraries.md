# Angular best practices: libraries (ng-packagr)

- One project per library (`@pmeig/ngb-<name>`), `src/public-api.ts` → `public.*.ts` barrels, peer deps `@angular/* >= <major>`, `sideEffects: false`, `compilationMode: partial`; a `XxxMaterial` NgModule only bundles standalone directives for import.
- Directive base classes (`TagDirective`) for shared behavior, DOM changes through `Renderer2`, `override` on lifecycle hooks, typed signal inputs with transforms; README per library with API table, "Fixed in", "Known issues".
