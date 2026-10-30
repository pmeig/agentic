# Vue best practices: code

- **Composition API with `<script setup lang="ts">`** only (no Options API in new code), `defineProps<Props>()` with reactive props destructure and defaults, `defineEmits<{...}>()`, `defineModel()` for v-model.
- Reactivity: `ref` for state, `computed` for derived values (never a method called from the template for derivation), `watch`/`watchEffect` only for side effects; replace or mutate consistently, `shallowRef` for large immutable data.
- Logic reused in composables (`useExpenses()` in `core/` or the page folder), returning refs and functions; Pinia setup stores for shared state (`defineStore('expenses', () => {...})`), exposed state read-only where possible.
- API layer in `core/api` with typed functions per endpoint, one place for auth and error mapping; TanStack Query for Vue or Pinia actions for caching.
- Templates: `v-for` with `:key` on stable ids, never `v-if` with `v-for` on the same element, `v-bind` shorthand, components `PascalCase` in SFCs, multi-word component names.
- Forms: VeeValidate + zod (or native validation with computed errors), a label per field, errors linked with `aria-describedby`; i18n with `vue-i18n`.
- Nuxt: `useFetch`/`useAsyncData` for data, server routes in `server/api`, runtime config for environment values, no secrets in public config.
- Styling: scoped styles or CSS Modules, design tokens as CSS variables.
