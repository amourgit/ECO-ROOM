# Documentation d'architecture — CIVITAS Agent Runtime (LangGraph)

> Remplacement complet de `services/peer` par un runtime d'agent IA basé sur **LangGraph**, un
> process **strictement isolé par room**, et un catalogue d'outils couvrant explicitement tout
> ce qu'un participant humain peut faire dans le navigateur Jitsi.
>
> Jitsi lui-même (Prosody/Jicofo/JVB/Web) est acté et hors périmètre de cette refonte.

## Ordre de lecture recommandé

1. **[`00-etat-des-lieux.md`](./00-etat-des-lieux.md)** — analyse exhaustive de l'architecture
   actuelle (control plane, data plane, `peer`, modèle de données, Kafka, CLI) et de ses limites
   — en particulier l'absence d'isolation par room, qui motive toute la refonte.
2. **[`01-architecture-cible-civitas-agent.md`](./01-architecture-cible-civitas-agent.md)** —
   l'architecture cible : les 4 domaines, Control Plane / Data Plane, `ConferenceAgentState`,
   le graphe LangGraph et ses nœuds, la mémoire à 3 niveaux, l'arborescence modulaire complète
   du nouveau service `civitas-agent`.
3. **[`02-catalogue-outils-agent.md`](./02-catalogue-outils-agent.md)** — catalogue exhaustif,
   groundé sur l'API réelle `IJitsiConference`/`lib-jitsi-meet`, de tous les outils que le
   CIVITAS Agent doit exposer pour couvrir les actions d'un participant humain.
4. **[`03-isolation-et-orchestration.md`](./03-isolation-et-orchestration.md)** — le mécanisme
   concret garantissant qu'un crash d'un CIVITAS Agent dans une room n'affecte jamais les
   autres rooms, et l'évolution de `room-spawner` en `civitas-orchestrator`.
5. **[`04-plan-migration.md`](./04-plan-migration.md)** — plan d'exécution phasé, fichier par
   fichier, avec critères de bascule et stratégie de rollback à chaque étape.

## Principes non négociables de cette refonte

- Le concept de `peer` disparaît entièrement — remplacé par le **CIVITAS Agent Runtime**.
- **Un process = une room, toujours.** Isolation garantie à la fois structurellement (état) et
  à l'exécution (container OS dédié).
- Séparation physique stricte Control Plane / Data Plane, consolidées uniquement dans l'état
  unifié de chaque agent (jamais de transport partagé entre les deux plans).
- Rien de ce qui fonctionne déjà en production n'est réécrit sans raison : `EventBus`,
  `SpeakerTracker`, `ContextStore`, `GeminiSession`, `CivitasBrowser`, le schéma Postgres
  existant sont portés, pas recréés.
