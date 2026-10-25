# Prompt de test exhaustif — GitHub Copilot / équipe agentic

Tu es le lead du dépôt pmeig/agentic. Ce scénario sert à mesurer la qualité et le coût de l'orchestration. Fais intervenir explicitement tous les rôles configurés dans le dépôt. Ne modifie pas les règles générales de l'équipe pour faciliter le test.

## Mission
Crée une petite application autonome de gestion de tâches, isolée dans sandbox/token-ab-demo/ afin de ne pas toucher au produit ou aux instructions du dépôt.

L'application doit fonctionner localement dans un navigateur, sans dépendance externe ni installation de package :
- ajouter une tâche avec titre obligatoire et description facultative ;
- afficher les tâches, filtrer par statut (toutes / à faire / terminées) et rechercher dans le titre ;
- marquer une tâche comme terminée ou à faire ;
- supprimer une tâche avec une confirmation accessible ;
- persister les données dans localStorage ;
- gérer l'état vide, les entrées invalides et les erreurs de stockage ;
- être responsive, accessible au clavier, avec labels, focus visible, messages accessibles et contraste lisible.

Utilise HTML, CSS et JavaScript natifs. N'ajoute aucune dépendance. Utilise les outils de test déjà présents. Si aucun test front automatisable n'est disponible, fournis un plan manuel reproductible et des contrôles simples sans dépendance. N'affirme jamais qu'un test a réussi s'il n'a pas été exécuté.

## Rôles obligatoires et livrables
Commence par inspecter AGENTS.md, .agents/agents/, les instructions Copilot du dépôt et les capacités d'agents disponibles dans cette session.

Fais contribuer les rôles suivants avec des responsabilités séparées. Si Copilot ne permet pas de déléguer à un rôle ou si aucun agent correspondant n'est configuré, réalise son travail toi-même dans une phase distincte, étiquette-le « rôle simulé sans sous-agent » et ne prétends pas qu'un agent séparé a été lancé.

1. Lead / orchestration : besoin, critères d'acceptation et répartition ; écrire sandbox/token-ab-demo/need.md.
2. Designer : trois directions UX distinctes, compromis, choix argumenté d'une variante accessible et simple dans sandbox/token-ab-demo/design-options.md. Pour ce benchmark, prends une décision sans demander de clarification.
3. Front : implémenter l'interface responsive en HTML/CSS/JS natifs et respecter la direction retenue.
4. Back / données : définir la persistance locale, le schéma, la validation et les erreurs dans sandbox/token-ab-demo/data-contract.md. Ne construis pas un serveur artificiel.
5. QA : plan de test dans sandbox/token-ab-demo/qa-plan.md, exécution réelle des tests disponibles, corrections avec les propriétaires et rapport des commandes/résultats. Couvrir parcours heureux, validation, recherche, filtres, persistance, suppression, état vide, clavier et petits écrans.
6. Translator : créer sandbox/token-ab-demo/i18n/strings.json avec les chaînes françaises et anglaises, vérifier les accents, placeholders et clés ; français par défaut, sélecteur de langue si raisonnable.
7. Sales : créer sandbox/token-ab-demo/promotion/brief.md avec audience, proposition de valeur, pitch de 10 secondes, trois idées de lancement et un indicateur par idée. N'invente aucune traction.
8. Documentalist : après le feu vert QA, créer sandbox/token-ab-demo/README.md expliquant lancement, fonctionnalités, architecture, tests réellement exécutés, limites et décisions. Évite de dupliquer la documentation générale du dépôt.

## Critères de réussite
- Chaque rôle a une contribution identifiable. Distingue les sous-agents réellement lancés des phases exécutées par l'agent principal.
- L'application fonctionne hors ligne et les contrôles annoncés sont reproductibles.
- Tous les nouveaux fichiers restent sous sandbox/token-ab-demo/.
- Aucune dépendance, aucun déploiement, aucun push, aucun commit, aucune modification de branche.
- Termine par un rapport : rôles mobilisés, fichiers produits, commandes et résultats des tests, défauts connus, mesures de tokens/coût/durée uniquement si elles sont réellement exposées par Copilot ou ses journaux. N'estime pas les valeurs manquantes.

Travaille jusqu'à l'implémentation vérifiée, pas seulement jusqu'au plan.
