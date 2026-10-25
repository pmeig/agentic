# Prompt de test exhaustif — Claude Code / équipe agentic

Tu es le lead du dépôt pmeig/agentic. Ce scénario est un benchmark contrôlé de l'orchestration : il doit faire travailler explicitement tous les rôles configurés et produire un résultat vérifiable. Ne modifie pas les règles générales de l'équipe pour faciliter le test.

## Mission
Crée une petite application autonome de gestion de tâches, isolée dans sandbox/token-ab-demo/ pour ne pas toucher au produit ou aux instructions du dépôt.

L'application doit fonctionner localement dans un navigateur, sans dépendance externe ni installation de package :
- ajouter une tâche avec titre obligatoire et description facultative ;
- afficher les tâches, les filtrer par statut (toutes / à faire / terminées) et rechercher dans le titre ;
- marquer une tâche comme terminée ou à faire ;
- supprimer une tâche avec une confirmation accessible ;
- persister les données dans localStorage ;
- gérer proprement l'état vide, les entrées invalides et les erreurs de stockage ;
- être responsive, utilisable au clavier, avec labels, focus visible, messages accessibles et contraste lisible.

Utilise HTML, CSS et JavaScript natifs. N'ajoute aucune dépendance. Les tests doivent pouvoir être lancés avec les outils déjà présents ; si aucun outil de test front n'existe, écris un plan de test manuel reproductible et, si raisonnable, des tests JavaScript simples sans dépendance. Ne prétends pas avoir exécuté des tests que tu n'as pas pu lancer.

## Participation obligatoire des rôles
Fais intervenir chaque rôle de l'équipe, avec une tâche distincte et une preuve de son apport. Utilise le mécanisme de délégation configuré dans ce dépôt (par exemple les sous-agents Claude Code) lorsque disponible. Les travaux doivent être bornés, sans chevauchement inutile. Les dépendances restent séquentielles : conception choisie avant implémentation, contrat avant code, QA avant documentation finale.

1. Lead : inspecte les règles du dépôt, définit le besoin, les critères d'acceptation, le périmètre et la répartition. Écris sandbox/token-ab-demo/need.md.
2. Designer : propose trois directions UX distinctes et compare brièvement leurs compromis dans sandbox/token-ab-demo/design-options.md. Pour ce benchmark automatisé, choisis ensuite la variante la plus simple, accessible et cohérente avec le besoin sans demander de clarification ; note explicitement le choix et sa justification.
3. Front : implémente l'interface HTML/CSS/JS responsive, les interactions et l'accessibilité, en respectant le choix du designer.
4. Back : même sans serveur requis, définis la couche de données et le contrat de persistance (schéma, validation, erreurs, évolutions possibles) dans sandbox/token-ab-demo/data-contract.md ; travaille avec front sur les comportements et les cas limites. N'ajoute pas de backend artificiel.
5. QA : rédige sandbox/token-ab-demo/qa-plan.md, exécute les tests automatisables disponibles, corrige les défauts avec le propriétaire du code et rapporte exactement les commandes et résultats. Couvre le parcours heureux, validation, recherche, filtres, persistance, suppression, état vide, clavier et petits écrans.
6. Translator : crée sandbox/token-ab-demo/i18n/strings.json avec des libellés français et anglais pour l'interface, et vérifie cohérence, accents, placeholders et clés. L'interface peut être en français par défaut ; ajoute un sélecteur de langue simple si cela reste dans le périmètre.
7. Sales : rédige sandbox/token-ab-demo/promotion/brief.md avec audience, proposition de valeur, pitch de 10 secondes, trois idées de lancement réalistes et un indicateur pour chacune. N'invente pas de traction, clients ou résultats.
8. Documentalist : en dernière étape, après le feu vert QA, écris sandbox/token-ab-demo/README.md avec lancement, fonctionnalités, architecture, tests réellement exécutés, limites et décisions. Mets aussi à jour toute documentation IA locale strictement nécessaire au mini-projet, sans recopier la documentation générale du dépôt.

## Critères de réussite
- Tous les huit rôles ci-dessus ont contribué ou, si une capacité de délégation manque, le rapport le signale explicitement sans inventer de sous-agent.
- Les fichiers demandés existent, l'application fonctionne sans réseau et les tests/contrôles annoncés sont vérifiables.
- Aucun fichier hors de sandbox/token-ab-demo/ ne doit être modifié.
- Pas de dépendance ajoutée, pas de déploiement, pas de push, pas de commit, pas de modification de branche.
- En fin d'exécution, donne un rapport concis avec : rôles réellement mobilisés, fichiers produits, commandes de test et résultats, défauts connus, et coût/usage seulement si le CLI ou les transcriptions donnent des valeurs observées. N'estime pas les tokens.

Commence par lire les règles et vérifier l'état du dépôt. Travaille jusqu'à une implémentation complète et vérifiée, sans t'arrêter après le plan.
