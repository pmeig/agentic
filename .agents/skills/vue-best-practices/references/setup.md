# Vue best practices: setup

- Vue 3.5+ with TypeScript strict and `vue-tsc`, Vite (or Nuxt when SSR/SEO matters), pnpm, ESLint (`eslint-plugin-vue` recommended) + Prettier; Vapor mode only once stable in the version used.
- Layout: `src/pages/<name>/<Name>Page.vue` + its components and composables, `src/core/<kind of feature>/` (api, auth, i18n, ui, storage, stores), router with lazy routes (`component: () => import(...)`).
