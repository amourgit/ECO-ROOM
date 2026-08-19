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
- **Le gestionnaire de modèles neutre** (`models/`) — le moteur de parole (Gemini Live par
  défaut, OpenAI Realtime en alternative) et le modèle de raisonnement (Gemini/OpenAI/
  Anthropic, optionnel) sont sélectionnés par variables d'environnement
  (`SPEECH_MODEL_PROVIDER`/`REASONING_MODEL_PROVIDER`, cf. `.env.example`), jamais figés dans
  le code — cf. [`docs/architecture/05-gestionnaire-de-modeles.md`](../../docs/architecture/05-gestionnaire-de-modeles.md).

Reste à faire avant mise en production (Phase 1 du plan de migration) : tests d'intégration
contre un vrai cluster Jitsi + Gemini, durcissement des cas limites déjà connus et documentés
dans l'ancien `peer` (reconnexion, prejoin bypass, timing du `replaceTrack`) — repris tels quels
mais à revalider dans ce nouveau contexte d'exécution (un container par room).

## Tests

```bash
pip install -r requirements-dev.txt --break-system-packages
python -m pytest -q
```

47 tests, tous verts à ce jour (`tests/`) :
- `test_state.py`, `test_response_policy.py`, `test_context_store.py`,
  `test_speaker_tracker.py` — logique pure portée depuis `services/peer`.
- `test_registry.py` — gating de permissions du catalogue d'outils (doc 01 §9) : outil
  inconnu, outil non implémenté, capacité refusée, liste blanche `tools_allowed`, exception
  interceptée — jamais un faux succès silencieux.
- `test_graph_smoke.py` — **exécute réellement** le graphe LangGraph assemblé
  (`app/graph/build.py`) avec navigateur/moteur de parole/Kafka **simulés** (`MemorySaver` en
  lieu et place du `AsyncPostgresSaver` de production) : vérifie le routage d'entrée
  conditionnel, l'arête conditionnelle `route`, le déclenchement d'un outil (`vision_tools`),
  et surtout l'**isolation entre deux graphes indépendants** (aucune fuite d'état entre deux
  `room_id`).
- `test_models_reasoning_base.py`, `test_models_reasoning_factory.py`,
  `test_models_speech_factory.py` — gestionnaire de modèles neutre (doc 05) : construction de
  prompt et parsing JSON défensif, sélection de fournisseur, **dégradation gracieuse réelle**
  quand un SDK de fournisseur n'est pas installé (exécuté dans un environnement où aucun des 3
  SDK de raisonnement n'est présent — le test valide donc un vrai chemin de repli, pas une
  simulation).

Ce que ces tests NE couvrent PAS (nécessite un environnement de déploiement réel, absent de
l'environnement où ce squelette a été écrit) : navigateur headless contre un vrai Jitsi,
session Gemini Live réelle, vrai broker Kafka, vrai `AsyncPostgresSaver` Postgres. C'est le
critère de bascule vers la Phase 2 du plan de migration (doc 04).

## Démarrage local (développement)

```bash
cp .env.example .env
# éditer .env : GEMINI_API_KEY, ROOM_ID (obligatoire), ROOM_CONFIG_URL/TOKEN, KAFKA_BOOTSTRAP
pip install -r requirements.txt --break-system-packages
python -m app.main
```

En production, ce service n'est **jamais** lancé à la main : `civitas-orchestrator` le spawn
via `docker run` avec `ROOM_ID` positionné dynamiquement (cf. doc 03 §4.3).
