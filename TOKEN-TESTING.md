# Mesurer les tokens consommés par mes tests d'agents

## But

Ce guide sert à choisir la variante de workflow qui consomme le moins de tokens **pour un même travail et un résultat de qualité équivalente**. Il mesure l'usage observé dans les transcriptions Claude Code. Il ne lance pas les tests à ta place et ne fournit pas automatiquement le coût en euros.

## 1. Définir les variantes à comparer

Pour comparer deux versions du workflow (par exemple `main` et `chore/optimisation`, ou séquentiel et parallèle) :

1. Utilise la même tâche de test, le même prompt, le même modèle et les mêmes réglages.
2. Pars d'un état de code équivalent et utilise une **nouvelle session Claude Code** pour chaque essai.
3. Note la branche et le commit testé, puis lance exactement le même scénario.
4. Vérifie que le résultat satisfait les mêmes tests/critères d'acceptation.
5. Répète si possible chaque variante au moins trois fois : le cache et la variabilité des réponses peuvent modifier les chiffres.

Ne compare pas seulement le total de tokens si une variante a fait moins de travail ou échoué plus tôt.

## 2. Repérer les transcriptions de chaque exécution (Windows / PowerShell)

Claude Code enregistre normalement ses transcriptions JSONL sous `$HOME\.claude\projects`. Liste les fichiers récemment modifiés :

```powershell
Get-ChildItem "$HOME\.claude\projects" -Recurse -Filter *.jsonl |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 40 LastWriteTime, Length, FullName
```

Repère les fichiers correspondant à la session que tu viens de terminer. Identifie aussi les transcriptions des sous-agents, souvent dans un sous-dossier `subagents`. Pour mesurer le workflow complet, inclus les transcriptions des agents lancés par cette session.

## 3. Séparer les données de chaque variante

Le script traite tous les fichiers `*.jsonl` sous le dossier fourni avec `--root`. Crée donc un dossier isolé par essai et copie-y **uniquement** les transcriptions de cette exécution, avec celles de ses sous-agents.

```powershell
New-Item -ItemType Directory -Force .\token-tests\main-run1, .\token-tests\optimisation-run1
# Copie les JSONL de la session testée sur main et ses sous-agents dans main-run1
# Copie les JSONL de la session testée sur chore/optimisation et ses sous-agents dans optimisation-run1
```

Ne mets pas dans ces dossiers les transcriptions d'autres sessions. Les transcriptions peuvent contenir du code et des échanges privés : garde-les localement.

## 4. Calculer les tokens pour chaque essai

Depuis la racine du dépôt, exécute le script de la branche que tu testes :

```powershell
python scripts/claude-token-usage.py --root .\token-tests\main-run1
python scripts/claude-token-usage.py --root .\token-tests\optimisation-run1
```

Pour conserver les résultats en JSON :

```powershell
python scripts/claude-token-usage.py --root .\token-tests\main-run1 --json > .\token-tests\main-run1-report.json
python scripts/claude-token-usage.py --root .\token-tests\optimisation-run1 --json > .\token-tests\optimisation-run1-report.json
```

Le rapport affiche, par transcription et en total, `input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens` et `total_reported_tokens`. Vérifie que le dossier ne contient que les fichiers de l'essai visé.

## 5. Comparer et décider

Reporte les totaux dans ce tableau (une ligne par essai) :

| Variante | Commit | Total tokens rapportés | Entrée | Sortie | Cache créé | Cache lu | Durée | Tests/qualité |
|---|---|---:|---:|---:|---:|---:|---|---|
| `main` — essai 1 | à renseigner | à mesurer | à mesurer | à mesurer | à mesurer | à mesurer | à mesurer | à vérifier |
| `chore/optimisation` — essai 1 | à renseigner | à mesurer | à mesurer | à mesurer | à mesurer | à mesurer | à mesurer | à vérifier |

Calculs :

- **Écart de tokens** = total de la variante candidate − total de référence.
- **Écart en %** = (total candidat − total référence) / total référence × 100.
- Un pourcentage négatif signifie moins de tokens rapportés ; un pourcentage positif signifie plus.
- Si tu fais plusieurs essais, compare aussi la médiane de chaque variante plutôt qu'un seul résultat.

Choisis la variante la moins consommatrice seulement si elle passe les mêmes tests et produit un résultat équivalent. Prends en compte le temps gagné : le parallélisme peut utiliser plus de tokens mais terminer plus vite.

## Limites et interprétation

- Le script additionne les champs `usage` disponibles sur les enregistrements assistant dans les fichiers JSONL. Il n'infère pas les tokens absents.
- Les tokens des sous-agents ne seront inclus que si leurs transcriptions sont présentes dans le dossier fourni.
- `total_reported_tokens` est la somme des quatre colonnes affichées. Ne rajoute pas les colonnes de cache une seconde fois.
- Ces compteurs sont des mesures de transcription, pas une garantie de facturation exacte. Le coût monétaire dépend aussi du modèle et de la tarification applicable.
- Des tests unitaires classiques qui n'appellent pas un modèle ne consomment pas de tokens Claude. Pour mesurer le coût du workflow d'agents, lance réellement chaque scénario dans Claude Code, puis analyse ses transcriptions.
- Si le rapport dit `No usage records found`, vérifie le chemin, les fichiers JSONL et qu'ils contiennent des enregistrements assistant avec `usage`.

## 6. Lancer automatiquement le même scénario sur deux branches

Le script \`scripts/compare-claude-tokens.py\` lance le même prompt avec Claude Code sur deux worktrees temporaires, par défaut \`main\` et \`chore/optimisation\`, puis sauvegarde les sorties JSON, la durée, le nombre de tours, le coût rapporté par le CLI et les champs d'usage disponibles.

**Attention : cela déclenche de vrais appels potentiellement facturés.** Vérifie le prompt, le modèle et les limites avant de lancer. Il faut avoir \`git\`, Python et Claude Code (\`claude\`) installés, être authentifié, et lancer la commande depuis un clone local du dépôt.

Crée un fichier \`test-prompt.md\` avec une tâche courte, représentative et identique pour les deux variantes, puis lance :

\`\`\`powershell
python scripts/compare-claude-tokens.py --prompt-file .\\test-prompt.md
\`\`\`

Options utiles :

\`\`\`powershell
python scripts/compare-claude-tokens.py --prompt-file .\\test-prompt.md --model <nom-du-modele> --max-turns 10
python scripts/compare-claude-tokens.py --branches main chore/optimisation --prompt-file .\\test-prompt.md --output-dir .\\mesures
\`\`\`

Les résultats sont écrits dans \`token-comparison-results/\` (ou le dossier passé à \`--output-dir\`). Le script ne pousse aucun changement vers GitHub : il crée des worktrees détachés temporaires et les supprime après chaque exécution. Le dépôt de départ doit être propre pour éviter toute confusion sur le code testé.

Le rapport dépend des champs d'usage renvoyés par la version installée de Claude Code. Vérifie les transcriptions des sous-agents si elles sont utilisées : ne conclus pas qu'un total inclut les sous-agents à moins que les compteurs le confirment. Pour une décision solide, répète plusieurs fois chaque variante et vérifie la qualité du résultat.


## Comparaison A/B avec GitHub Copilot CLI

Le script active la télémétrie OpenTelemetry locale pour chaque exécution, dans un fichier JSONL distinct. Il additionne les compteurs des spans `chat` (un span par requête au modèle), sans additionner les totaux des spans parents `invoke_agent`, ce qui évite de compter deux fois les tokens.

```powershell
python scripts/compare-copilot-tokens.py --prompt .\prompts\token-test-copilot.md --base main --compare chore/optimisation
```

Pour vérifier les worktrees sans lancer de modèle :

```powershell
python scripts/compare-copilot-tokens.py --prompt .\prompts\token-test-copilot.md --base main --compare chore/optimisation --dry-run
```

Les résultats se trouvent dans `token-comparison-results/copilot-<horodatage>/` :
- `comparison.json` : commits testés, durée et métriques résumées ;
- `base.otel.jsonl` et `compare.otel.jsonl` : télémétrie brute propre à chaque variante ;
- `base.stdout.log`, `base.stderr.log`, et les équivalents `compare.*` : sorties brutes du CLI.

### Test initial et solution de repli

Avant le benchmark, le script effectue un appel minimal à Copilot (réponse demandée : `OK`) et enregistre `preflight.json`. Ce test vérifie si les tokens sont accessibles par télémétrie OpenTelemetry, par champs structurés de la sortie CLI, ou seulement par interprétation. **Cet appel consomme potentiellement des crédits** ; le test `--dry-run` ne lance aucun appel.

Ordre de priorité :
1. **Mesure directe** : OpenTelemetry local JSONL, avec tokens par appel modèle.
2. **Repli structuré** : champs de consommation JSON explicitement émis par la CLI.
3. **Interprétation estimative** : estimation grossière à partir du nombre de caractères visibles du prompt et de la réponse (environ 4 caractères par token). Le rapport la marque `source: interpretive_estimate` et `is_estimate: true`.

L'estimation interprétative **n'est pas une mesure réelle** : elle ne comprend pas le contexte système caché, les appels intermédiaires, les outils, ni les effets de cache. Ne l'utilise pas pour comparer précisément la facturation ; elle sert uniquement de signal de secours. Les fichiers `preflight.stdout.log` et `preflight.stderr.log` permettent d'examiner la réponse du test initial.

### Métriques disponibles via OpenTelemetry

Quand la version installée de Copilot CLI les émet, le script mesure :
- `gen_ai.usage.input_tokens` : tokens d'entrée par appel modèle ;
- `gen_ai.usage.output_tokens` : tokens de sortie par appel modèle ;
- `gen_ai.usage.cache_read.input_tokens` et `gen_ai.usage.cache_creation.input_tokens` : compteurs de cache séparés ;
- le modèle et le nombre de requêtes ayant fourni des compteurs ;
- `github.copilot.nano_aiu`, si présent, comme unité de consommation IA rapportée par le CLI.

Les totaux d'entrée/sortie sont calculés en sommant les spans `chat`. Les tokens de cache restent des colonnes séparées : ne les additionne pas une seconde fois au total entrée/sortie.

### Limites importantes

- Si une version du CLI ne produit pas ces spans ou attributs, la métrique reste indisponible (`null`), jamais remplacée par zéro. Le script conserve alors les métriques structurées de la sortie CLI comme solution de repli, si elles existent.
- `github.copilot.cost` est un multiplicateur de facturation par modèle, **pas un montant en euros** ; le script ne le traite pas comme un coût monétaire.
- Les rapports d'utilisation GitHub au niveau du compte ou de l'organisation sont utiles comme contrôle global, mais ne permettent pas nécessairement d'attribuer exactement chaque token à un commit ou à un prompt isolé.
- Le script désactive la capture du contenu des prompts et réponses dans OpenTelemetry ; les compteurs de tokens n'exigent pas de conserver ces contenus.
- Cette mesure correspond aux appels réellement observés dans les spans exportés. Vérifie la présence des fichiers `.otel.jsonl` et répète chaque variante au moins trois fois pour réduire les effets de variabilité. Compare aussi les commits, les résultats des tests et la qualité.

Référence officielle : [commande Copilot CLI — OpenTelemetry monitoring](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference#opentelemetry-monitoring).
