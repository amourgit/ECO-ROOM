# CIVITAS Agent Runtime

> Remplace `services/peer`. Voir la documentation complète :
> [`docs/architecture/`](../../docs/architecture/README.md).

Un process = **une seule room** (`ROOM_ID`, obligatoire, fixé à la création du process — jamais
réassignable, cf. [`docs/architecture/03-isolation-et-orchestration.md`](../../docs/architecture/03-isolation-et-orchestration.md)).
Ce service n'est **jamais** démarré directement pour piloter plusieurs rooms : il est spawné
dynamiquement, une instance par room, par `services/civitas-orchestrator`.

## Statut de ce squelette (Phase 0 du plan de migration)

Ce répertoire pose l'arborescence modulaire complète et l'assemblage du graphe LangGraph
(cf. [`docs/architecture/01-architecture-cible-civitas-agent.md`](../../docs/architecture/01-architecture-cible-civitas-agent.md#8-architecture-interne-du-civitas-agent--arborescence-modulaire)),
avec :

- **Les modules déjà portés depuis `services/peer`** (marqués `# PORTÉ DE services/peer/...`
  dans leur docstring) : `perception/audio_pipe.py`, `perception/speaker_tracker.py`,
  `speech/gemini_live.py`, `speech/response_policy.py`, `context/store.py`,
  `events/bus.py`, `events/handlers.py`, `kafka/producer.py`, `room/config_client.py`,
  `browser/driver.py`.
- **Le catalogue d'outils** (`tools/`) — cf.
  [`docs/architecture/02-catalogue-outils-agent.md`](../../docs/architecture/02-catalogue-outils-agent.md) —
  avec les outils déjà présents dans `peer` portés tels quels (✅), les nouveaux outils P0
  implémentés contre l'API `lib-jitsi-meet` réelle (🆕), et les outils P1/avancés déclarés dans
  le registre mais volontairement non implémentés (`NotImplementedError` explicite, jamais un
  faux succès silencieux) en attendant la Phase correspondante du plan de migration.
- **Le graphe LangGraph** (`graph/`) assemblé et fonctionnel pour le flux nominal
  (ingestion → mise à jour d'état → routage → raisonnement → action → parole → persistance),
  cf. [`docs/architecture/01-architecture-cible-civitas-agent.md`](../../docs/architecture/01-architecture-cible-civitas-agent.md#6-le-graphe-langgraph--nœuds-explicites).

Reste à faire avant mise en production (Phase 1 du plan de migration) : tests d'intégration
contre un vrai cluster Jitsi + Gemini, durcissement des cas limites déjà connus et documentés
dans l'ancien `peer` (reconnexion, prejoin bypass, timing du `replaceTrack`) — repris tels quels
mais à revalider dans ce nouveau contexte d'exécution (un container par room).

## Démarrage local (développement)

```bash
cp .env.example .env
# éditer .env : GEMINI_API_KEY, ROOM_ID (obligatoire), ROOM_CONFIG_URL/TOKEN, KAFKA_BOOTSTRAP
pip install -r requirements.txt --break-system-packages
python -m app.main
```

En production, ce service n'est **jamais** lancé à la main : `civitas-orchestrator` le spawn
via `docker run` avec `ROOM_ID` positionné dynamiquement (cf. doc 03 §4.3).
