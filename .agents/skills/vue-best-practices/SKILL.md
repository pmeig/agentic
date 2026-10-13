---
name: vue-best-practices
description: MANDATORY when writing, reviewing or testing Vue code (Vue 3 SPAs, Nuxt): the team's conventions transposed to Vue - pages/ and core/ modules, Composition API with script setup and TypeScript, composables, Pinia stores, typed API layer, Vitest + Vue Test Utils with one describe per public function - plus Vue 3.5+/Nuxt practices.
---

# Vue best practices

The user has no Vue project yet: these rules transpose the team's Angular conventions (`angular-best-practices`,
`typescript-best-practices`, `ui-responsive-accessible-modular`) to Vue 3.

## 1. Setup

- Vue 3.5+ with TypeScript strict and `vue-tsc`, Vite (or Nuxt when SSR/SEO matters), pnpm, ESLint (`eslint-plugin-vue` recommended) + Prettier; Vapor mode only once stable in the version used.
- Layout: `src/pages/<name>/<Name>Page.vue` + its components and composables, `src/core/<kind of feature>/` (api, auth, i18n, ui, storage, stores), router with lazy routes (`component: () => import(...)`).

## 2. Code

- **Composition API with `<script setup lang="ts">`** only (no Options API in new code), `defineProps<Props>()` with reactive props destructure and defaults, `defineEmits<{...}>()`, `defineModel()` for v-model.
- Reactivity: `ref` for state, `computed` for derived values (never a method called from the template for derivation), `watch`/`watchEffect` only for side effects; replace or mutate consistently, `shallowRef` for large immutable data.
- Logic reused in composables (`useExpenses()` in `core/` or the page folder), returning refs and functions; Pinia setup stores for shared state (`defineStore('expenses', () => {...})`), exposed state read-only where possible.
- API layer in `core/api` with typed functions per endpoint, one place for auth and error mapping; TanStack Query for Vue or Pinia actions for caching.
- Templates: `v-for` with `:key` on stable ids, never `v-if` with `v-for` on the same element, `v-bind` shorthand, components `PascalCase` in SFCs, multi-word component names.
- Forms: VeeValidate + zod (or native validation with computed errors), a label per field, errors linked with `aria-describedby`; i18n with `vue-i18n`.
- Nuxt: `useFetch`/`useAsyncData` for data, server routes in `server/api`, runtime config for environment values, no secrets in public config.
- Styling: scoped styles or CSS Modules, design tokens as CSS variables.

## 3. Tests

- Vitest + Vue Test Utils (`mount`) + Testing Library queries: **one `describe` per component or composable/public function**, `it('should ... when ...')`.
- Test composables and stores as functions (`setActivePinia(createPinia())`), components through their rendered output and emitted events; MSW for the API; Playwright e2e with axe for pages.

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
