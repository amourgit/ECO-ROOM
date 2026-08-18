# CIVITAS Agent Orchestrator

> Remplace `services/room-spawner`. Voir la documentation complète :
> [`docs/architecture/03-isolation-et-orchestration.md`](../../docs/architecture/03-isolation-et-orchestration.md).

Process **unique**, sans état de raisonnement (aucun `ConferenceAgentState`, aucune session
IA, aucun navigateur headless — juste un registre `room_id → container`). Seul consommateur
Kafka de `jitsi.room.events`/`jitsi.participant.events`. Spawn/route/détruit un container
`civitas-agent` isolé par room (cf. `services/civitas-agent/`).

## Statut de ce squelette (Phase 0 du plan de migration)

- `app/registry.py`, `app/forwarder.py` : implémentés, logique complète.
- `app/kafka_consumer.py` : port direct de `services/room-spawner/app/kafka_consumer.py`.
- `app/docker_runtime.py` : implémentation `DockerAgentRuntimeProvider` via le SDK `docker`
  Python — à valider contre un hôte Docker réel (Phase 2 du plan de migration).
- `app/agent_client.py` : client HTTP vers un agent précis (remplace `peer_client.py`).
- `app/main.py` : routes `/moderator/*` reprises à l'identique de `room-spawner` pour
  compatibilité CLI immédiate (cf. `docs/architecture/04-plan-migration.md`).

## Tests

```bash
pip install -r requirements-dev.txt --break-system-packages
python -m pytest -q
```

9 tests, tous verts à ce jour (`tests/`) : `test_registry.py` (le registre `room_id →
container` ne mélange jamais deux rooms) et `test_docker_runtime.py` (`slugify_room_id` est
déterministe, respecte le charset Docker, et ne fait jamais collisionner deux rooms distinctes
même après troncature — cf. doc 03 §3.1). Le spawn/teardown Docker réel
(`DockerAgentRuntimeProvider`) n'est pas testé ici : il nécessite un vrai daemon Docker,
absent de l'environnement où ce squelette a été écrit — critère de bascule vers la Phase 2 du
plan de migration (doc 04).

## Démarrage local (développement)

```bash
cp .env.example .env
pip install -r requirements.txt --break-system-packages
python -m app.main
```

Nécessite un accès au socket Docker (`/var/run/docker.sock`) pour spawn/teardown des agents —
monté en lecture-écriture uniquement dans ce container, jamais dans les agents eux-mêmes.
