# Room Config

Source de vérité de la configuration agent par room (Postgres) + mémoire de réunion
persistante (`room_history_entries`). Service **inchangé dans son rôle** par la refonte
CIVITAS Agent (cf. [`docs/architecture/`](../../docs/architecture/README.md)) — seul son
schéma évolue légèrement pour accompagner le remplacement du `peer` par le CIVITAS Agent
Runtime : voir [`docs/architecture/04-plan-migration.md`](../../docs/architecture/04-plan-migration.md#migration-du-schéma-room_configs--colonne-peer_enabled--agent_enabled).

## Migration `0002_add_agent_enabled`

Ajoute la colonne `agent_enabled`, successeur de `peer_enabled` (colonne conservée pendant
toute la période de coexistence de `services/room-spawner`, déprécié, et
`services/civitas-orchestrator`). Les deux colonnes sont synchronisées applicativement à
chaque écriture (`app/services/room_config_service.py::_sync_agent_peer_enabled`) — jamais par
trigger SQL, pour rester lisible et traçable dans les logs applicatifs.

## Tests

```bash
pip install -r requirements.txt pytest --break-system-packages
# nécessite un Postgres accessible localement (rôle civitas / civitas2024) :
#   apt-get install -y postgresql && service postgresql start
#   sudo -u postgres psql -c "CREATE ROLE civitas WITH LOGIN PASSWORD 'civitas2024';"
#   sudo -u postgres psql -c "CREATE DATABASE room_config_test OWNER civitas;"
python -m pytest tests/ -v
```

10 tests, tous verts à ce jour, exécutés contre une **vraie base Postgres** (pas une
simulation SQLite — cf. `tests/conftest.py` pour la justification) :

- `test_agent_enabled_sync.py` (9 tests) — synchronisation bidirectionnelle
  `agent_enabled`/`peer_enabled` sur `create`/`update`/`reserve`, y compris les cas limites
  (aucun des deux flags fourni, les deux fournis explicitement, un champ non lié mis à jour
  sans toucher aux flags).
- `test_migration_0002.py` (1 test) — reconstruit un schéma pré-migration fidèle (SQL brut,
  pas `Base.metadata.create_all()` avec les modèles actuels — sans quoi le test ne testerait
  rien de réel), insère des lignes avec des `peer_enabled` hétérogènes, applique la migration,
  vérifie le backfill ligne par ligne, puis la réversibilité complète (downgrade/re-upgrade).

Piège rencontré et corrigé pendant l'écriture de ces tests, documenté dans
`tests/test_migration_0002.py` : `app/config.py::get_settings()` est `@lru_cache` — une fois
appelé une première fois dans le process de test, il reste figé sur la même `DATABASE_URL`
même après modification de `os.environ`, alors que `migrations/env.py` relit délibérément
`get_settings().DATABASE_URL` à chaque commande Alembic (jamais l'URL passée via
`Config.set_main_option`). Sans `get_settings.cache_clear()` explicite autour du changement
d'URL, les tests de migration s'exécutaient silencieusement contre la mauvaise base.
