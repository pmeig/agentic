---
name: svelte-best-practices
description: MANDATORY when writing, reviewing or testing Svelte or SvelteKit code: the team's conventions transposed to Svelte 5 - runes ($state, $derived, $effect, $props), shared state in .svelte.ts classes, snippets instead of slots, SvelteKit load functions and form actions, typed API layer, Vitest with one describe per public function - plus current Svelte 5 practices.
---

# Svelte best practices

The user has no Svelte project yet: these rules transpose the team's front-end conventions (`typescript-best-practices`,
`ui-responsive-accessible-modular`) to Svelte 5 / SvelteKit.

## 1. Setup

- Svelte 5 (runes mode only, no legacy `let`/`$:` reactivity), SvelteKit for apps, TypeScript strict (`lang="ts"`), `svelte-check`, ESLint (`eslint-plugin-svelte`) + Prettier, pnpm.
- Layout: SvelteKit `src/routes/<page>/+page.svelte` (+ `+page.ts`/`+page.server.ts`) for routing, page-only components beside it, shared code in `src/lib/core/<kind of feature>/` (api, auth, i18n, ui, state).

## 2. Code

- Runes: `$state` for state, `$derived` for derived values (never `$effect` to sync state), `$effect` only for side effects with cleanup, `$props()` with a typed destructure and defaults, `$bindable` for two-way props.
- Shared state in classes or functions inside `.svelte.ts` modules (fine-grained, no stores needed); context (`setContext`/`getContext`) for request-scoped state in SSR to avoid leaking between users.
- Snippets (`{#snippet}` / `{@render}`) instead of slots, standard event attributes (`onclick`) instead of `on:` directives, callback props instead of `createEventDispatcher`.
- Data: SvelteKit `load` functions (server load for secrets and DB access), form actions with progressive enhancement (`use:enhance`) and server-side validation (zod/valibot); typed API layer in `lib/core/api`; `$env/static/private` for secrets, never in client code.
- `{#each items as item (item.id)}` with keys, `{#await}` for async UI, transitions respecting `prefers-reduced-motion`.
- Accessibility: Svelte's a11y warnings treated as errors, semantic elements, labels and focus management; i18n with `paraglide`/`svelte-i18n`.
- Styling: component-scoped `<style>`, design tokens as CSS variables.

## 3. Tests

- Vitest + `@testing-library/svelte`: **one `describe` per component or public function**, `it('should ... when ...')`; test `.svelte.ts` state classes as plain code (`flushSync` after changes), `load` functions and actions as functions with mocked `fetch`.
- Playwright e2e (SvelteKit default) with axe for pages.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `it.each` (table of objects, `$name` in the title) inside the `describe` of the component or function. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

## Monthly refresh

Last refreshed: 2026-10

- On the **first use of this skill in a calendar month after the date above**, refresh it before applying it: search the web for
  what changed since that month (new stable versions, newly recommended practices, deprecated or removed APIs and tools).
- Update **only the parts that come from the internet**: add the new practices, change outdated versions, remove what is
  deprecated or removed. Keep it short, prefer official sources (release notes, official docs).
- **Never remove or weaken the user's rules**: everything taken from the user's projects (`D:\projects\...`) or explicit
  instructions and the team conventions (layered controller/service/repository, pages/ + core/ modules, one test group per public
  method with parameterized tests favored, `should_..._when_...` names, mocks built by hand, Lombok always for Java, every branch covered...). When the internet
  contradicts one of them, keep the rule and tell the user about the conflict.
- Then set "Last refreshed" to the current month and tell the user in a few bullets what was added, changed or removed (with sources).
