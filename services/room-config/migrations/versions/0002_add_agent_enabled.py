"""add_agent_enabled

Ajoute à room_configs :
  - agent_enabled (bool, défaut true) : successeur de `peer_enabled`, lu/écrit par
    services/civitas-orchestrator (remplace services/room-spawner, déprécié) — cf.
    docs/architecture/03-isolation-et-orchestration.md et
    docs/architecture/04-plan-migration.md, Phase 2 "Migration du schéma room_configs".

Additive et réversible, en 3 étapes espacées dans le temps (doc 04) :
  Migration A (CETTE migration, début Phase 2) : ADD COLUMN + backfill depuis peer_enabled.
    Les deux colonnes coexistent ensuite, synchronisées applicativement (JAMAIS par trigger
    SQL) à chaque écriture par app/services/room_config_service.py::_sync_agent_peer_enabled,
    tant que room-spawner (lit/écrit peer_enabled) et civitas-orchestrator (lit/écrit
    agent_enabled) tournent en parallèle pendant la bascule progressive.
  Migration B (Phase 6, PAS écrite ici, volontairement — ne pas anticiper) : suppression de
    la synchronisation applicative + DROP COLUMN peer_enabled, une fois room-spawner
    définitivement désactivé.

Idempotente (IF NOT EXISTS), même convention que 0001 : sur une base FRAÎCHE,
`Base.metadata.create_all()` (app/database.py::init_db, appelé avant run_migrations() au
démarrage) a déjà créé la colonne via le modèle SQLAlchemy à jour (app/models/room_config.py)
— cette migration s'applique alors sans effet sur la structure. Le backfill
(`UPDATE ... SET agent_enabled = peer_enabled`) est en revanche TOUJOURS exécuté, y compris
sur une base fraîche où il est un no-op inoffensif (chaque ligne venant d'être créée avec
`agent_enabled` déjà égal à son défaut `TRUE`, identique au défaut de `peer_enabled`) — sur
une base EXISTANTE remontée depuis avant ce changement, c'est ce backfill qui fait le travail
réel : reprendre la valeur RÉELLE de peer_enabled déjà en place, ligne par ligne, jamais une
simple valeur par défaut uniforme.

Validé manuellement contre une base Postgres réelle avant ce commit (3 lignes de test avec
des valeurs peer_enabled hétérogènes True/False/True → backfill vérifié ligne par ligne après
migration, cf. commit associé) — pas seulement une relecture du SQL.

Revision ID: 0002
Revises: 0001
Create Date: 2026-08-21
"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '0002'
down_revision: Union[str, Sequence[str], None] = '0001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "ALTER TABLE room_configs "
        "ADD COLUMN IF NOT EXISTS agent_enabled BOOLEAN NOT NULL DEFAULT TRUE"
    )
    # Backfill — reprend la valeur réelle de peer_enabled déjà en place pour CHAQUE ligne
    # existante, pas un simple défaut uniforme (cf. docstring de module).
    op.execute(
        "UPDATE room_configs SET agent_enabled = peer_enabled"
    )


def downgrade() -> None:
    op.execute("ALTER TABLE room_configs DROP COLUMN IF EXISTS agent_enabled")
