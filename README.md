# agentic

Une équipe de cinq agents IA (designer, front, back, devops, qa) qui produit une feature de bout en bout en autonomie, en se
questionnant entre eux, avec des skills de bonnes pratiques par langage et framework. Les instructions des agents sont en anglais
(`AGENTS.md`, `.agents/`), cette page est la documentation humaine.

| Élément | Rôle |
|---|---|
| [`AGENTS.md`](AGENTS.md) | rôles, déroulé d'une feature, règles communes, sélection des skills par stack |
| [`.agents/agents/`](.agents/agents) | définition de chaque agent |
| [`.agents/skills/`](.agents/skills) | 40 skills de bonnes pratiques, de stratégies CI/CD et de déploiement |

## Architecture

```
            besoin (lead)
                 │
                 ▼
  designer ⇄ front ──(contrat d'interface)──⇄ back
  (maquettes)  │  code + TU verts               │  code + TU verts
               └───────────────┬────────────────┘
                               ▼
                 devops (monorepo, CI/CD)
                               ▼
              qa : tous les e2e verts = feu vert
                               ▼
                pull request ─▶ déploiement ─▶ qa : toute la feature
```

- **designer** : UX, gestes métier, parcours, couleurs ; propose au moins 3 maquettes HTML avec screenshots PNG desktop et mobile affichés avant le choix, demande à `front` les écrans existants.
- **front** : reproduit la maquette (ou fait évoluer l'élément bloquant avec `designer`), établit le contrat avec `back`, écrit
  ses tests unitaires, remet à `qa` le geste métier (`gesture.md`).
- **back** : API, règles métier, SQL/NoSQL derrière le contrat ; écrit ses tests unitaires.
- **devops** : monorepo et CI/CD selon les technos choisies.
- **qa** : écrit et lance les e2e ; **lui seul donne le feu vert de la PR**, quand tous les e2e passent ; reteste toute la feature
  après déploiement.
- Les agents se posent leurs questions par `SendMessage`, et partagent leur travail dans `docs/team/<feature>/` du projet
  (`need.md`, `design/`, `contract.md`, `gesture.md`, `qa.md`).
- Chaque agent ne charge que les skills de la stack du module où il travaille (tableau « Skill selection » de `AGENTS.md`) ; les
  règles propres à un projet passent avant.

## Arborescence

```
agentic/
├── AGENTS.md                 instructions de l'équipe (lu par tous les outils IA)
├── CLAUDE.md                 importe AGENTS.md pour Claude Code
├── setup.ps1                 recrée les jonctions .claude/ -> .agents/ après un clone
├── .agents/
│   ├── agents/               designer.md, front.md, back.md, devops.md, qa.md
│   └── skills/<nom>/SKILL.md java, kotlin, spring-boot, typescript, angular, python, sql, go, rust, csharp-dotnet,
│                             php, cpp, swift, dart-flutter, react, vue, svelte, nestjs, ruby-rails, shell-bash,
│                             devops-trunk-based, devops-branch-environment, create-project, module-versioning,
│                             deployment-platform-selection, deployment-gcp, deployment-aws, terraform,
│                             docker, deployment-kubernetes, android-google-play, ios-app-store,
│                             github-actions-deployment, github-actions-cicd, monorepo-layout,
│                             ui-responsive-accessible-modular, node-api-architecture, node-version,
│                             feature-e2e-loop, flaky-tests
└── .claude/                  jonctions (non versionnées) vers .agents/agents et .agents/skills
```

## Skills

- Basés sur les projets de `D:\projects` (conventions réelles : Lombok toujours en Java, un groupe de tests `@Nested` par méthode
  publique avec tests paramétrés privilégiés, noms `should_..._when_...`, couches controller → service → repository...),
  complétés par les bonnes pratiques actuelles trouvées sur internet.
- **Mise à jour mensuelle** : au premier usage d'un mois, le skill vérifie les sources officielles pertinentes (documentation,
  API/CLI, tarifs, notes de version et interface), conserve les liens des sources et note la date dans « Last refreshed », sans
  jamais retirer les règles de l'utilisateur. Pour les parcours console, il capture les écrans courants avec un outil autorisé,
  masque les données sensibles et guide l'utilisateur étape par étape ; si la capture n'est pas possible, il le signale et donne
  les liens officiels et la navigation exacte.

## Démarrage

```powershell
git clone https://github.com/pmeig/agentic.git
cd agentic
./setup.ps1        # recrée .claude/agents et .claude/skills
```

Pour utiliser l'équipe dans un autre projet : lier (jonction) `.agents/agents` et `.agents/skills` dans le `.agents/` du projet
(ou de `~/.agents/` pour tous les projets), puis leurs liens `.claude/`.
