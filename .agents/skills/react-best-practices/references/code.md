# React best practices: code

- Function components only, one component per file, `PascalCase` names, props typed with an interface, `children` pattern for composition.
- State: local `useState`/`useReducer`; derived values computed during render (never synced with `useEffect`); server data with TanStack Query (or the framework fetcher), global client state minimal (context per concern or Zustand).
- `useEffect` only to synchronize with external systems (subscriptions, DOM APIs), with cleanup; never for data derivation or event handling.
- Server Components (Next.js): server by default, `'use client'` as low in the tree as possible, Server Actions for mutations with validation (zod) on the server, `server-only` for server modules, serializable props only, parallel fetches with `Promise.all`, a `Suspense` + error boundary per independent area.
- Forms: React 19 actions (`useActionState`, `useFormStatus`, `useOptimistic`) or React Hook Form + zod; label per field, errors linked with `aria-describedby`.
- API layer in `core/api`: typed functions per endpoint (contract from `back`), one place for auth headers and error mapping; never `fetch` scattered in components.
- Styling: CSS Modules, Tailwind or a zero-runtime library; design tokens as CSS variables; no runtime CSS-in-JS with server components.
- Accessibility: semantic elements first, `aria-*` only when needed, keyboard support, focus management on route change and dialogs; i18n with `react-i18next`/`next-intl`.
- Lists keyed by stable ids, lazy routes (`React.lazy`/route splitting), images optimized.
