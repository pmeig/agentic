# Angular best practices: routing, forms, i18n

- Routing: every page lazy (`loadComponent: () => import('./pages/x/x.page').then(m => m.XPage)`), protected parent with `canActivate`, a `title` per route, `**` redirect; route/query params bound to `input()`s (`withComponentInputBinding`).
- i18n: custom `I18nService` (language signal, `t(key, ...args)` falling back to English then the key) + impure `t` pipe, message bundles per language in `core/i18n/messages/*.ts`; keys for route titles.
- Forms: template-driven with signals (`[ngModel]="email()" (ngModelChange)="email.set($event)"`) and `computed` field errors from pure validators, or Signal Forms when stable in the version used; reactive typed forms for large/dynamic forms.
