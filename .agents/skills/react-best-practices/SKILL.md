---
name: react-best-practices
description: MANDATORY when writing, reviewing or testing React code (Vite SPAs, Next.js, React Native): the team's conventions transposed to React - pages/ and core/ modules, function components only, React Compiler instead of manual memo, server components by default in Next.js, data through a typed API layer and TanStack Query, Vitest + Testing Library with one describe per public function - plus React 19 practices.
---

# React best practices

The user has no React project yet: these rules transpose the team's Angular conventions (`angular-best-practices`,
`typescript-best-practices`, `ui-responsive-accessible-modular`) to React 19.

## 1. Setup

- React 19 + TypeScript strict, Vite for SPAs or Next.js (App Router) when SSR/SEO matters, React Native + Expo for mobile; pnpm; ESLint with `eslint-plugin-react-hooks` and the React Compiler plugin, Prettier.
- **React Compiler on**: no manual `useMemo`/`useCallback`/`memo` unless profiling proves a need; write pure components (no side effects during render, no mutation of props/state).
- Layout: `src/pages/<name>/<Name>Page.tsx` (or Next `app/<route>/page.tsx`) with what only that page uses, `src/core/<kind of feature>/` (api, auth, i18n, ui, storage), no page importing another page.

## 2. Code

- Function components only, one component per file, `PascalCase` names, props typed with an interface, `children` pattern for composition.
- State: local `useState`/`useReducer`; derived values computed during render (never synced with `useEffect`); server data with TanStack Query (or the framework fetcher), global client state minimal (context per concern or Zustand).
- `useEffect` only to synchronize with external systems (subscriptions, DOM APIs), with cleanup; never for data derivation or event handling.
- Server Components (Next.js): server by default, `'use client'` as low in the tree as possible, Server Actions for mutations with validation (zod) on the server, `server-only` for server modules, serializable props only, parallel fetches with `Promise.all`, a `Suspense` + error boundary per independent area.
- Forms: React 19 actions (`useActionState`, `useFormStatus`, `useOptimistic`) or React Hook Form + zod; label per field, errors linked with `aria-describedby`.
- API layer in `core/api`: typed functions per endpoint (contract from `back`), one place for auth headers and error mapping; never `fetch` scattered in components.
- Styling: CSS Modules, Tailwind or a zero-runtime library; design tokens as CSS variables; no runtime CSS-in-JS with server components.
- Accessibility: semantic elements first, `aria-*` only when needed, keyboard support, focus management on route change and dialogs; i18n with `react-i18next`/`next-intl`.
- Lists keyed by stable ids, lazy routes (`React.lazy`/route splitting), images optimized.

## 3. Tests

- Vitest + Testing Library (+ `user-event`), files `*.test.tsx` beside the source: **one `describe` per component or public function**, nested `describe` per behavior group, `it('should ... when ...')`.
- Query by role/label (`getByRole('button', { name: 'Save' })`), never by class or test internals; `data-testid` only for e2e anchors; MSW to mock the API at the network level; fake timers for time.
- Hooks and helpers tested as functions; pages covered by Playwright e2e with axe checks.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `it.each` (table of objects, `$name` in the title) inside the `describe` of the component or function. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, check official sources for version, practice, and deprecation changes. Update only internet-derived
guidance; preserve user/project rules. Add source URLs, update this date, and briefly report changes.
