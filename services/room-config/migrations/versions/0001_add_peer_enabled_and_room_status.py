"""add_peer_enabled_and_room_status_tracking

Ajoute à room_configs :
  - peer_enabled (bool, défaut true) : contrôle modérateur manuel
    inject/eject, colonne dédiée. AVANT : bricolé dans extra_config (écrit)
    vs permissions (lu, jamais rempli) — l'éjection manuelle ne "tenait"
    jamais. Cf. §2.3/§7.5 PLAN_SYNCHRONISATION_ROOMS_JITSI.md.
  - status (varchar(20), défaut 'confirmed') : 'pending' | 'confirmed' —
    traçabilité room réelle Jitsi. Cf. §1-4 du même document.
  - source (varchar(50), défaut 'manager_api_legacy') : origine de la ligne.
  - jitsi_confirmed_at (timestamp, nullable) : horodatage de la confirmation
    réelle (événement Jitsi reçu), NULL si jamais confirmée autrement que
    par défaut historique.

Idempotente (IF NOT EXISTS / IF EXISTS) à dessein : sur une base FRAÎCHE,
`Base.metadata.create_all()` (appelé au démarrage de l'app, cf.
app/database.py::init_db) crée déjà la table avec ces colonnes incluses —
cette migration s'applique alors sans effet (colonnes déjà présentes). Sur
une base EXISTANTE (déploiement antérieur à ce changement), c'est elle qui
fait le travail réel. Les deux chemins convergent vers le même schéma sans
jamais échouer selon l'ordre de passage.

Revision ID: 0001
Revises:
Create Date: 2026-08-13
"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '0001'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "ALTER TABLE room_configs "
        "ADD COLUMN IF NOT EXISTS peer_enabled BOOLEAN NOT NULL DEFAULT TRUE"
    )
    op.execute(
        "ALTER TABLE room_configs "
        "ADD COLUMN IF NOT EXISTS status VARCHAR(20) NOT NULL DEFAULT 'confirmed'"
    )
    op.execute(
        "ALTER TABLE room_configs "
        "ADD COLUMN IF NOT EXISTS source VARCHAR(50) NOT NULL DEFAULT 'manager_api_legacy'"
    )
    op.execute(
        "ALTER TABLE room_configs "
        "ADD COLUMN IF NOT EXISTS jitsi_confirmed_at TIMESTAMP NULL"
    )


def downgrade() -> None:
    op.execute("ALTER TABLE room_configs DROP COLUMN IF EXISTS jitsi_confirmed_at")
    op.execute("ALTER TABLE room_configs DROP COLUMN IF EXISTS source")
    op.execute("ALTER TABLE room_configs DROP COLUMN IF EXISTS status")
    op.execute("ALTER TABLE room_configs DROP COLUMN IF EXISTS peer_enabled")
