# Svelte best practices: code

- Runes: `$state` for state, `$derived` for derived values (never `$effect` to sync state), `$effect` only for side effects with cleanup, `$props()` with a typed destructure and defaults, `$bindable` for two-way props.
- Shared state in classes or functions inside `.svelte.ts` modules (fine-grained, no stores needed); context (`setContext`/`getContext`) for request-scoped state in SSR to avoid leaking between users.
- Snippets (`{#snippet}` / `{@render}`) instead of slots, standard event attributes (`onclick`) instead of `on:` directives, callback props instead of `createEventDispatcher`.
- Data: SvelteKit `load` functions (server load for secrets and DB access), form actions with progressive enhancement (`use:enhance`) and server-side validation (zod/valibot); typed API layer in `lib/core/api`; `$env/static/private` for secrets, never in client code.
- `{#each items as item (item.id)}` with keys, `{#await}` for async UI, transitions respecting `prefers-reduced-motion`.
- Accessibility: Svelte's a11y warnings treated as errors, semantic elements, labels and focus management; i18n with `paraglide`/`svelte-i18n`.
- Styling: component-scoped `<style>`, design tokens as CSS variables.
