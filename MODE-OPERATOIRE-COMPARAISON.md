# Mode opératoire — comparer la consommation des workflows d'agents

Ce guide explique comment comparer `main` et `chore/optimisation` avec **la même tâche**, d'abord avec Claude Code, puis avec GitHub Copilot CLI. Le but est de comparer la consommation observée tout en vérifiant que la qualité du résultat reste équivalente.

> Les scripts déclenchent de vrais appels à des modèles. Vérifie ton accès, tes limites et les éventuels coûts avant de les lancer. Les scripts ne poussent pas de changements sur GitHub, mais les agents peuvent créer/modifier des fichiers dans leurs worktrees temporaires.

## 1. Prérequis

Sur ton PC Windows, ouvre PowerShell et vérifie que tu as :
- Git ;
- Python 3 ;
- Claude Code CLI (`claude`) si tu testes Claude ;
- GitHub Copilot CLI (`copilot`) si tu testes Copilot ;
- une authentification active pour l'outil testé.

Depuis un terminal, place-toi dans ton clone local du dépôt :

```powershell
cd C:\chemin\vers\agentic
git status --short
git fetch origin
git branch --list
```

Le dépôt de départ doit être propre : sauvegarde ou committe tes propres modifications avant le test. Les deux références doivent être présentes localement. Si nécessaire, vérifie avec :

```powershell
git rev-parse main
git rev-parse chore/optimisation
```

Les scripts comparent les commits référencés localement par ces noms de branches. Note les SHA affichés dans les rapports pour savoir précisément quelles versions ont été mesurées.

## 2. Comprendre les prompts et le périmètre

Les prompts de benchmark sont versionnés dans les deux branches :
- Claude Code : [`prompts/token-test-claude.md`](prompts/token-test-claude.md)
- Copilot : [`prompts/token-test-copilot.md`](prompts/token-test-copilot.md)

Ils demandent la même mini-application de gestion de tâches et couvrent les rôles Lead, Designer, Frontend, Backend/Data, QA, Traducteur, Sales/Product et Documentaliste. Le prompt demande de distinguer les vrais sous-agents des rôles simulés. Les livrables de l'application doivent rester dans `sandbox/token-ab-demo/`.

Pour une comparaison valide, utilise **un seul et même fichier de prompt pour les deux variantes**. Lance les scripts depuis un clone où les fichiers de prompt sont présents ; le script lit le prompt avant de lancer les deux essais. N'édite pas le prompt entre les essais.

## 3. Test Claude Code (automatisé)

Dans PowerShell, depuis la racine du dépôt :

```powershell
python scripts/compare-claude-tokens.py --prompt-file .\prompts\token-test-claude.md
```

Le script lance une exécution Claude Code sur `main` puis une sur `chore/optimisation`, dans des worktrees détachés temporaires. Par défaut, il limite chaque exécution à 20 tours. Pour fixer explicitement le modèle et limiter le nombre de tours :

```powershell
python scripts/compare-claude-tokens.py --prompt-file .\prompts\token-test-claude.md --model NOM_DU_MODELE --max-turns 20
```

Pour comparer d'autres références :

```powershell
python scripts/compare-claude-tokens.py --branches main chore/optimisation --prompt-file .\prompts\token-test-claude.md --output-dir .\mesures
```

Le script enregistre `comparison.json`, un JSON par variante et les sorties brutes dans `token-comparison-results/` (ou le dossier indiqué). Il rapporte les métriques présentes dans la réponse JSON de Claude Code, par exemple usage, durée, nombre de tours et coût en USD si disponibles.

## 4. Test GitHub Copilot CLI (automatisé)

Depuis la racine du dépôt :

```powershell
python scripts/compare-copilot-tokens.py --prompt .\prompts\token-test-copilot.md --base main --compare chore/optimisation
```

Pour vérifier la préparation sans lancer de modèle :

```powershell
python scripts/compare-copilot-tokens.py --prompt .\prompts\token-test-copilot.md --base main --compare chore/optimisation --dry-run
```

Le script crée un worktree par référence, appelle la commande Copilot CLI en mode prompt, enregistre les journaux stdout/stderr et un `comparison.json`, puis retire les worktrees temporaires. Les résultats sont placés dans `token-comparison-results/copilot-<horodatage>/`.

**Limite importante :** selon la version et la configuration de Copilot CLI, la sortie peut ne pas exposer de champs d'utilisation. Dans ce cas, le rapport indique `usage: null`. Cela ne veut pas dire zéro token ; cela veut dire que le script n'a pas trouvé de métrique exploitable. Utilise les informations d'utilisation/facturation disponibles dans ton compte Copilot pour les chiffres officiels. Le temps d'exécution reste mesuré.

## 5. Lire les résultats

Pour chaque variante, relève au minimum :

| Mesure | À quoi elle sert |
|---|---|
| Branche et SHA du commit | Identifier exactement le code testé |
| Statut / code retour | Vérifier que l'exécution s'est terminée correctement |
| Tokens d'entrée et de sortie | Comparer les métriques disponibles, sans inventer celles qui manquent |
| Tokens de cache | Les garder séparés ; ne pas les additionner deux fois |
| Coût rapporté | Comparer seulement si l'outil le fournit réellement |
| Durée / nombre de tours | Mesurer le temps et l'effort observés |
| Qualité | Vérifier les mêmes critères d'acceptation et les mêmes défauts |

Pour une mesure numérique, calcule :

- **Écart absolu** = valeur `chore/optimisation` − valeur `main`.
- **Écart en %** = (valeur candidate − valeur de référence) / valeur de référence × 100.
- Un résultat négatif signifie une baisse de cette mesure ; un résultat positif, une hausse.

Ne compare pas uniquement le total de tokens : une variante peut consommer moins parce qu'elle a échoué, fait moins de travail ou omis des agents. Compare aussi les fichiers produits, les tests réellement exécutés, les défauts et les rôles qui ont effectivement été mobilisés.

## 6. Rendre la comparaison plus fiable

1. Fais d'abord un essai de validation, puis idéalement **3 essais par variante**.
2. Garde le même prompt, le même modèle, les mêmes options/limites et le même état initial.
3. Utilise des sessions neuves ; ne réutilise pas une conversation déjà chargée de contexte.
4. Exécute les deux variantes dans une période rapprochée et note les changements de modèle ou de configuration.
5. Compare la médiane des mesures sur plusieurs essais, pas uniquement le meilleur résultat.
6. Vérifie les transcriptions des sous-agents lorsque l'outil les expose. Ne suppose pas que le résumé principal inclut toute leur consommation.
7. Conserve les rapports JSON et les SHA des commits pour pouvoir refaire la comparaison.

## 7. Dépannage

- **Branche introuvable** : exécute `git fetch origin`, vérifie `git branch -a`, puis crée/actualise les branches locales si nécessaire.
- **CLI introuvable** : vérifie que `claude` ou `copilot` est installé et présent dans le `PATH`.
- **Authentification refusée** : authentifie la CLI manuellement avant de lancer le benchmark.
- **Aucun coût ou token affiché pour Copilot** : ce n'est pas zéro ; la CLI n'a probablement pas exposé ces champs. Consulte l'interface d'utilisation Copilot.
- **Résultat invalide ou trop tôt terminé** : examine les logs bruts, le code retour et les fichiers produits avant de tirer une conclusion.
- **Worktree déjà utilisé / dépôt sale** : termine ou sauvegarde les modifications locales, vérifie `git worktree list`, puis relance.

## 8. Fichiers utiles

- [Prompt Claude](prompts/token-test-claude.md)
- [Prompt Copilot](prompts/token-test-copilot.md)
- [Script de comparaison Claude](scripts/compare-claude-tokens.py)
- [Script de comparaison Copilot](scripts/compare-copilot-tokens.py)
- [Guide détaillé de mesure des transcriptions Claude](TOKEN-TESTING.md)
