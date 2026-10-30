# React best practices: setup

- React 19 + TypeScript strict, Vite for SPAs or Next.js (App Router) when SSR/SEO matters, React Native + Expo for mobile; pnpm; ESLint with `eslint-plugin-react-hooks` and the React Compiler plugin, Prettier.
- **React Compiler on**: no manual `useMemo`/`useCallback`/`memo` unless profiling proves a need; write pure components (no side effects during render, no mutation of props/state).
- Layout: `src/pages/<name>/<Name>Page.tsx` (or Next `app/<route>/page.tsx`) with what only that page uses, `src/core/<kind of feature>/` (api, auth, i18n, ui, storage), no page importing another page.
