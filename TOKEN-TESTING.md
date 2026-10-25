# Tester et comparer la consommation de tokens Claude Code

Ce guide permet de comparer **deux exécutions réelles** (par exemple agents en série vs agents en parallèle) à partir des transcriptions locales Claude Code. Le script mesure les champs d'usage présents dans les fichiers JSONL ; il ne mesure pas le temps et ne garantit pas le montant facturé.

## 1. Préparer un test A/B comparable

1. Mets le dépôt dans un état connu et note le commit avec `git rev-parse HEAD`.
2. Choisis une tâche représentative, avec un résultat vérifiable et un périmètre limité.
3. Lance deux sessions neuves avec le même modèle, les mêmes réglages, le même prompt et le même état initial :
   - **A — référence** : demande explicitement une exécution séquentielle, sans agents parallèles.
   - **B — parallèle** : demande d'appliquer la règle de parallélisme piloté par le coût et de lancer les agents indépendants utiles.
4. Ne réutilise pas la même session entre A et B. Note pour chaque essai le commit, le prompt, le modèle, les réglages, le résultat, la durée et les éventuels échecs/reprises.

Les résultats ne sont comparables que si le travail livré et les critères de qualité sont équivalents. Pour une comparaison plus fiable, répète chaque variante plusieurs fois et compare la médiane ; une seule exécution peut être influencée par le cache, la variabilité du modèle ou des différences de travail.

## 2. Trouver les transcriptions

Claude Code conserve normalement ses transcriptions dans le dossier utilisateur Claude. Sur Windows, commence par :

```powershell
Get-ChildItem "$HOME\.claude\projects" -Recurse -Filter *.jsonl |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 30 LastWriteTime, Length, FullName
```

Repère les fichiers modifiés pendant chaque session. Les transcriptions des sous-agents peuvent être rangées dans des sous-dossiers (par exemple `subagents`) : inclus-les aussi, car elles comptent pour le travail parallèle.

## 3. Isoler les fichiers de chaque essai

Le rapport additionne tous les JSONL trouvés sous `--root`. **Ne lance donc pas le rapport sur tout l'historique pour comparer une seule exécution** : copie les transcriptions de A dans un dossier dédié, et celles de B dans un autre. Préserve les sous-dossiers et noms de fichiers, notamment ceux des sous-agents.

Exemple PowerShell (remplace les chemins par les fichiers/dossiers repérés à l'étape précédente) :

```powershell
New-Item -ItemType Directory -Force .\token-test\A, .\token-test\B
# Copie les fichiers JSONL de la session A et ses transcriptions de sous-agents dans token-test\A
# Copie ceux de la session B et ses transcriptions de sous-agents dans token-test\B
```

Évite de copier des transcriptions d'autres sessions dans ces dossiers. Les transcriptions peuvent contenir du code, des chemins et des échanges privés : garde les copies localement et ne les publie pas.

## 4. Générer les rapports

Depuis la racine du dépôt :

```powershell
python scripts/claude-token-usage.py --root .\token-test\A
python scripts/claude-token-usage.py --root .\token-test\B
python scripts/claude-token-usage.py --root .\token-test\A --json
python scripts/claude-token-usage.py --root .\token-test\B --json
```

Le tableau donne, par fichier de transcription, les tokens d'entrée, de sortie, de création de cache et de lecture de cache, ainsi qu'un total calculé à partir de ces quatre colonnes. La ligne `-TOTAL-` additionne les fichiers du dossier ; veille à ne pas compter deux fois les transcriptions parent/sous-agent.

## 5. Calculer et interpréter l'écart

Pour chaque variante, relève le total et les colonnes séparées. Calcule :

- **Écart absolu** = total B − total A.
- **Écart relatif (%)** = (total B − total A) / total A × 100.
- Fais aussi la comparaison séparément pour entrée, sortie, cache créé et cache lu.
- Compare la durée et la qualité : tests passés, critères d'acceptation, défauts, reprises et travail réellement livré.

Un écart relatif négatif signifie que B a consommé moins de tokens rapportés que A ; positif signifie plus. Le parallélisme peut accélérer le travail tout en consommant davantage de tokens à cause des contextes séparés et du travail de coordination. Décide sur le compromis qualité/durée/coût, pas sur le seul total.

## Limites à connaître

- Le script additionne les champs `usage` présents sur les enregistrements assistant et ignore les lignes JSON invalides ou les fichiers illisibles.
- Les colonnes de cache sont affichées séparément et sont également incluses dans `total_reported_tokens` ; ne les ajoute pas une deuxième fois.
- Les compteurs observés dans les transcriptions ne sont pas une garantie de facturation exacte. Selon le format des transcriptions et le fournisseur, certains compteurs peuvent se recouvrir ou représenter des notions différentes.
- Si aucun résultat n'apparaît, vérifie le chemin `--root`, le format JSONL et la présence de champs `usage`.
- Le script ne lance pas Claude Code et ne crée pas les transcriptions : exécute les tests dans Claude Code d'abord.