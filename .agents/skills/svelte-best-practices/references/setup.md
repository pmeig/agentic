# Svelte best practices: setup

- Svelte 5 (runes mode only, no legacy `let`/`$:` reactivity), SvelteKit for apps, TypeScript strict (`lang="ts"`), `svelte-check`, ESLint (`eslint-plugin-svelte`) + Prettier, pnpm.
- Layout: SvelteKit `src/routes/<page>/+page.svelte` (+ `+page.ts`/`+page.server.ts`) for routing, page-only components beside it, shared code in `src/lib/core/<kind of feature>/` (api, auth, i18n, ui, state).
