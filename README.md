# agentic

Une équipe de sept agents IA (designer, front, back, qa, sales, translator, documentalist ; l'agent devops est désactivé) qui produit une feature de bout en
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
        documentalist : doc IA + doc humaine (dernière étape de tout développement)
                               ▼
        pull request ─▶ déploiement ─▶ qa : toute la feature ─▶ sales (optionnel)
```

- **designer** : UX, gestes métier, parcours, couleurs ; 3 à 5 maquettes HTML vraiment différentes avec screenshots PNG desktop et
  mobile affichés avant le choix ; demande à `front` les écrans existants.
- **front** : reproduit la maquette, établit le contrat avec `back`, écrit ses tests unitaires, remet à `qa` le geste métier (`gesture.md`).
- **back** : API, règles métier, SQL/NoSQL derrière le contrat ; écrit ses tests unitaires.
- **qa** : écrit et lance les e2e, exécute les TU et le rapport Sonar (100 % de couverture, 0 issue, les corrections reviennent au
  propriétaire du code) ; **lui seul donne le feu vert de la PR** ; reteste toute la feature après déploiement. Si le projet a des e2e sur plusieurs plateformes, ils doivent être **jumeaux** (mêmes scénarios, numéros, noms, étapes, résultats attendus et identifiants d'éléments) ; pas de feu vert tant qu'un scénario n'a pas son jumeau.
- **sales** : positionnement, idées de promotion, canaux de diffusion, scripts, textes et vidéos promotionnelles (montage) ; demande
  maquettes et visuels au `designer`, écrans de démo à `front` ; ne publie rien, le lead valide.
- Les agents se posent leurs questions par `SendMessage` et partagent leur travail dans `docs/team/<feature>/` du projet.
- **translator** : traduit comme un natif de la langue cible (anglais → français : un Français ; italien → allemand : un Allemand),
  demande le ton et le type de phrase, propose plusieurs tournures quand elles diffèrent vraiment, reste proche de ce que disent les
  gens et créatif quand le contexte l'exige. Un skill par langue (`language-<code>`) et par paire (`translation-<source>-<cible>`),
  mis à jour une fois par mois ; pour une nouvelle langue ou paire il génère lui-même le skill (`translation-skill-factory`).
- **documentalist** : rend un projet compréhensible, d'abord pour une IA (`docs/ai/` : arborescence annotée, features par couche, API,
  schéma de base de données, flux, conventions, commandes, glossaire, pièges, avec le format adapté : Mermaid, OpenAPI, DBML, C4,
  `AGENTS.md`, graphe de connaissances Graphify pour les gros codes), puis pour les humains (`README.md` avec l'architecture, guides
  selon Diátaxis, ADR, site de documentation). Les autres agents lui demandent « comment marche X, où est Y » par `SendMessage` ; il
  écrit la doc IA pour une machine (aucun souci de lisibilité humaine : cartes, listes de liens, pas de diagrammes) avec une **carte d'impact** `docs/ai/graph.yaml` (chemin modifié → features → tests et e2e impactés : en local on ne lance que les e2e impactés, la CI lance tous les e2e) ; il met la doc à jour **en dernière étape de tout développement : après le feu vert de `qa` et avant le push ou la PR** (la PR embarque la doc ; un commit de documentation seule ne relance pas les e2e). Optimisation des tokens réservée à la doc IA (budget de lecture, un fait à un seul endroit, fichiers lus par section) ; la doc humaine n'est pas raccourcie. Les « Change set » des fiches nomment les tests à mettre à jour (flows e2e et jumeaux web, doubles de test, stores persistés) et `conventions.md` porte la liste « terminé quand… » du projet. Deux skills principaux (`documentation-ai`, `documentation-human`) et des skills
  de technologie mis à jour une fois par mois : `doc-code-analysis`, `doc-mermaid`, `doc-openapi-asyncapi`, `doc-database-schema`,
  `doc-architecture-c4-adr`, `doc-ai-context-files`, `doc-sites-markdown`, `doc-graphify` (licence à vérifier avant usage).
- Chaque agent ne charge que les skills de la stack du module où il travaille (« Skill selection » de `AGENTS.md`) ; les règles
  propres à un projet passent avant.

## Arborescence

```
agentic/
├── AGENTS.md                 instructions de l'équipe (lues par tous les outils IA)
├── CLAUDE.md                 importe AGENTS.md pour Claude Code
├── setup.ps1                 recrée les jonctions .claude/ -> .agents/ après un clone
├── .agents/
│   ├── agents/               designer, front, back, qa, sales, translator, documentalist (devops.md.disabled)
│   └── skills/<nom>/SKILL.md
│       langages et frameworks   <langage>-best-practices (java, kotlin, typescript, python, go, rust, csharp-dotnet, php, cpp,
│                               swift, dart-flutter, ruby-rails, shell-bash, sql), angular, react, vue, svelte, nestjs, spring-boot
│       CI/CD et déploiement      git-branch-sync, devops-*, deployment-*, terraform, docker, create-project, module-versioning, github-actions-*
│       design                    ui-responsive-accessible-modular, design-*
│       qualité                   e2e-run, e2e-live-progress, e2e-parallelism-init, e2e-<outil>-best-practices (17 outils),
│                                 sonar-report, sonar-<langage>
│       communication             promo-communication, promo-video
│       langues et traduction     language-<code> (en, fr, ro, it, es, de), translation-<source>-<cible>, translation-craft,
│                                 translation-skill-factory
│       documentation             documentation-ai, documentation-human, doc-code-analysis, doc-mermaid, doc-openapi-asyncapi,
│                                 doc-database-schema, doc-architecture-c4-adr, doc-ai-context-files, doc-sites-markdown, doc-graphify
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
- `git-branch-sync` (géré par `front`) : après le merge d'une PR, retour sur la branche cible mise à jour et suppression de la branche
  locale (sauf `develop`/`release`/`main`) ; avant toute nouvelle feature, mise à jour de la branche par défaut puis création de la branche.
- Les skills `sonar-<langage>` ne sont chargés que sur demande.

## Démarrage

```powershell
git clone https://github.com/pmeig/agentic.git
cd agentic
./setup.ps1        # recrée .claude/agents et .claude/skills
```

Pour utiliser l'équipe dans un autre projet : lier (jonction) `.agents/agents` et `.agents/skills` dans le `.agents/` du projet
(ou de `~/.agents/` pour tous les projets), puis leurs liens `.claude/`.
