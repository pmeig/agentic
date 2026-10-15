# agentic

Une équipe de cinq agents IA (designer, front, back, qa, sales ; l'agent devops est désactivé) qui produit une feature de bout en
bout en autonomie, en se questionnant entre eux, avec des skills de bonnes pratiques par langage et framework. Les instructions
des agents sont en anglais (`AGENTS.md`, `.agents/`), cette page est la documentation humaine.

| Élément | Rôle |
|---|---|
| [`AGENTS.md`](AGENTS.md) | rôles, déroulé d'une feature, règles communes, sélection des skills par stack |
| [`.agents/agents/`](.agents/agents) | définition de chaque agent |
| [`.agents/skills/`](.agents/skills) | skills de bonnes pratiques, de stratégies CI/CD et de déploiement |

## Architecture

```
            besoin (lead)
                 │
                 ▼
  designer ⇄ front ──(contrat d'interface)──⇄ back
  (maquettes)  │  code + TU                     │  code + TU
               └───────────────┬────────────────┘
                               ▼
        qa : TU + Sonar + tous les e2e verts = feu vert
                               ▼
        pull request ─▶ déploiement ─▶ qa : toute la feature ─▶ sales (optionnel)
```

- **designer** : UX, gestes métier, parcours, couleurs ; 3 à 5 maquettes HTML vraiment différentes avec screenshots PNG desktop et
  mobile affichés avant le choix ; demande à `front` les écrans existants.
- **front** : reproduit la maquette, établit le contrat avec `back`, écrit ses tests unitaires, remet à `qa` le geste métier (`gesture.md`).
- **back** : API, règles métier, SQL/NoSQL derrière le contrat ; écrit ses tests unitaires.
- **qa** : écrit et lance les e2e, exécute les TU et le rapport Sonar (100 % de couverture, 0 issue, les corrections reviennent au
  propriétaire du code) ; **lui seul donne le feu vert de la PR** ; reteste toute la feature après déploiement.
- **sales** : positionnement, idées de promotion, canaux de diffusion, scripts, textes et vidéos promotionnelles (montage) ; demande
  maquettes et visuels au `designer`, écrans de démo à `front` ; ne publie rien, le lead valide.
- Les agents se posent leurs questions par `SendMessage` et partagent leur travail dans `docs/team/<feature>/` du projet.
- Chaque agent ne charge que les skills de la stack du module où il travaille (« Skill selection » de `AGENTS.md`) ; les règles
  propres à un projet passent avant.

## Arborescence

```
agentic/
├── AGENTS.md                 instructions de l'équipe (lues par tous les outils IA)
├── CLAUDE.md                 importe AGENTS.md pour Claude Code
├── setup.ps1                 recrée les jonctions .claude/ -> .agents/ après un clone
├── .agents/
│   ├── agents/               designer, front, back, qa, sales (devops.md.disabled)
│   └── skills/<nom>/SKILL.md
│       langages et frameworks   <langage>-best-practices (java, kotlin, typescript, python, go, rust, csharp-dotnet, php, cpp,
│                               swift, dart-flutter, ruby-rails, shell-bash, sql), angular, react, vue, svelte, nestjs, spring-boot
│       CI/CD et déploiement      devops-*, deployment-*, terraform, docker, create-project, module-versioning, github-actions-*
│       design                    ui-responsive-accessible-modular, design-*
│       qualité                   e2e-run, e2e-live-progress, e2e-parallelism-init, e2e-<outil>-best-practices (17 outils),
│                                 sonar-report, sonar-<langage>
│       communication             promo-communication, promo-video
└── .claude/                  jonctions (non versionnées) vers .agents/agents et .agents/skills
```

## Skills

- Basés sur les projets de `D:\projects` (conventions réelles : Lombok toujours en Java, un groupe de tests `@Nested` par méthode
  publique avec tests paramétrés privilégiés, noms `should_..._when_...`, couches controller → service → repository...),
  complétés par les bonnes pratiques actuelles trouvées sur internet.
- **Mise à jour mensuelle** : au premier usage d'un mois, le skill vérifie les sources officielles pertinentes (documentation,
  API/CLI, tarifs, notes de version et interface), conserve les liens des sources et note la date dans « Last refreshed », sans
  jamais retirer les règles de l'utilisateur. Pour les parcours console, il capture les écrans courants avec un outil autorisé,
  masque les données sensibles et guide l'utilisateur étape par étape ; sans capture possible, il le signale et donne les liens
  officiels et la navigation exacte.
- Les skills `sonar-<langage>` ne sont chargés que sur demande.

## Démarrage

```powershell
git clone https://github.com/pmeig/agentic.git
cd agentic
./setup.ps1        # recrée .claude/agents et .claude/skills
```

Pour utiliser l'équipe dans un autre projet : lier (jonction) `.agents/agents` et `.agents/skills` dans le `.agents/` du projet
(ou de `~/.agents/` pour tous les projets), puis leurs liens `.claude/`.
