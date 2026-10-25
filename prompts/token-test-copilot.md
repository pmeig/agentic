# Benchmark prompt — GitHub Copilot

Construis la même application de tâches en exerçant tous les agents, skills et mécanismes de délégation réellement disponibles. Ne pose aucune question ; choisis des valeurs par défaut raisonnables.

## Inspecter d’abord
Lis `AGENTS.md`, `.github/copilot-instructions.md` si présent, `.agents/agents/`, `.agents/skills/` et les autres consignes. Énumère les agents/outils disponibles. N’affirme pas qu’un agent a été exécuté sans invocation réelle et résultat. Si délégation impossible, fais la phase toi-même et note « rôle simulé — sans sous-agent ».

## Limites
Tous les livrables et modifications dans `sandbox/token-ab-demo/` uniquement. Aucune installation de dépendance, accès aux secrets, réseau, déploiement, push, commit, changement de branche ou modification des consignes. Pas de worktree créé depuis l’agent. HTML/CSS/JS natifs, sans dépendances externes ni build.

## Rôles
- Lead/Architecte : exigences, plan, risques, intégration.
- Designer : trois directions UX et compromis, puis choix autonome.
- Frontend : HTML sémantique, CSS responsive, interactions accessibles.
- Backend/Data : contrat, persistance locale, erreurs ; ne simule pas de serveur.
- QA : cas d’acceptation, cas limites, tests, corrections et retests.
- Traducteur : `i18n/strings.json` français/anglais, sélecteur fonctionnel, toutes les chaînes UI traduites.
- Sales/Product : `promotion/brief.md` avec audience, valeur, différenciation, limites honnêtes.
- Documentaliste : `README.md` avec usage, architecture, accessibilité, tests et limites.
Évite les éditions concurrentes du même fichier. Ordre : inspecter → planifier/déléguer → contrat de données → concevoir → implémenter → QA/corriger → retester → documenter.

## Fonctionnalités
Ajouter tâche (titre requis, description facultative), lister, rechercher, filtrer Toutes/À faire/Terminées, basculer terminé/à faire, supprimer avec confirmation accessible, persister via localStorage, gérer titres vides et stockage corrompu/indisponible. États vides, clavier, libellés, focus visible, annonces accessibles, contraste, mobile, UI français/anglais avec sélecteur fonctionnel.

## Livrables et rapport
Sous `sandbox/token-ab-demo/` : `index.html`, `styles.css`, `app.js`, `i18n/strings.json`, `promotion/brief.md`, `README.md`. Tests seulement si un runner existant fonctionne sans installer quoi que ce soit ; sinon checklist manuelle. Vérifie ajout, validation, filtres, recherche, bascule, suppression/annulation, persistance, langue, états vides, clavier et erreurs de stockage. Donne commandes/résultats exacts. Rapporte les vrais agents invoqués et leurs résultats, rôles simulés séparément, fichiers, défauts et étapes manuelles. Tokens/coûts/durée uniquement si mesurés et fournis par l’environnement ; jamais d’estimation.
