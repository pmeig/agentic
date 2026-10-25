# Benchmark prompt — Claude Code

Construis une application de gestion de tâches soignée, responsive et accessible, en mobilisant tous les agents et rôles pertinents réellement disponibles dans ce dépôt. Ne pose aucune question : prends des décisions raisonnables et documente-les.

## Règles
- Tous les livrables/modifications doivent rester dans `sandbox/token-ab-demo/`.
- N’installe aucune dépendance. Aucun réseau, secret, déploiement, push, commit, changement de branche ou modification des instructions du dépôt.
- Inspecte `AGENTS.md`, les agents, skills et conventions. N’affirme jamais qu’un sous-agent a tourné sans invocation et résultat réels. Si délégation impossible, note « rôle simulé — sans sous-agent ».
- Pas d’éditions concurrentes du même fichier.

## Rôles à couvrir
1. Lead/Architecte : exigences, décomposition, séquencement, risques et intégration.
2. Designer : trois directions UX, compromis accessibilité/ergonomie, puis choix autonome.
3. Frontend : HTML sémantique, CSS responsive, interactions accessibles.
4. Backend/Data : contrat de données, persistance et erreurs ; pas de faux serveur.
5. QA : cas d’acceptation, cas limites, vérifications, corrections et retests.
6. Traducteur : dictionnaire `i18n/strings.json` français/anglais, sélecteur fonctionnel, toutes les chaînes UI traduites.
7. Sales/Product : `promotion/brief.md` avec audience, proposition de valeur, différenciation et limites honnêtes.
8. Documentaliste : `README.md` sur usage, architecture, accessibilité, tests et limites.

## Application
- Ajouter une tâche (titre obligatoire, description facultative), lister, rechercher par titre, filtrer Toutes/À faire/Terminées.
- Basculer l’état terminé ; supprimer avec confirmation accessible.
- Persistance localStorage après rechargement ; gérer stockage corrompu/indisponible et titres vides.
- États vides utiles, navigation clavier, libellés sémantiques, focus visible, annonces accessibles, contraste et mobile.
- Interface française/anglaise avec sélecteur fonctionnel.
- HTML/CSS/JS natifs, sans réseau, ressources externes, build ni dépendances.

## Livrables et séquence
Sous `sandbox/token-ab-demo/` : `index.html`, `styles.css`, `app.js`, `i18n/strings.json`, `promotion/brief.md`, `README.md`. Tests uniquement si un runner existant fonctionne sans installation ; sinon checklist manuelle reproductible. Ordre : inspecter → planifier/déléguer → contrat de données → concevoir → implémenter → QA/corriger → retester → documenter.

Vérifie ajout, validation, filtres, recherche, bascule, suppression/annulation, persistance, langue, états vides, clavier et erreurs de stockage. Rapporte commandes et résultats exacts ; ne prétends pas avoir testé ce qui ne l’a pas été. Compte rendu : agents réellement invoqués et résultats, rôles simulés séparément, fichiers modifiés, défauts restants et étapes manuelles. Durée/coût/tokens uniquement si mesurés et exposés par l’environnement ; aucune estimation.
