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