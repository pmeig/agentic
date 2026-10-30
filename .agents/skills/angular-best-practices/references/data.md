# Angular best practices: services, HTTP, interceptors, guards, errors

- `@Injectable({ providedIn: 'root' })` signal stores: private writable `signal`, exposed with `asReadonly()` and `computed`. Logic that deserves tests lives in plain classes (constructor DI) or pure functions in `*.helper.ts`, wrapped by the thin service.
- HTTP: an `ApiService` returning `firstValueFrom(this.http.get<T>(...))` (Promises + async/await); RxJS only for real streams (router events via `toSignal`, debounce, websockets); `resource`/`httpResource` for read-only data bound to signals once stable in the project's version.
- Functional interceptors (`HttpInterceptorFn`, `request.clone({ setHeaders })`, rethrow with `throwError(() => error)`) and guards (`CanActivateFn` returning `true` or a `UrlTree` with `returnUrl`).
- Errors: helpers taking `unknown` and mapping `HttpErrorResponse` status to translated messages, shown in an `error` signal and a snackbar service.
- SSR-safe code: guard browser APIs (`isPlatformBrowser`, `typeof window === 'undefined'`).
