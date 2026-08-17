"""
Checkpoint LangGraph — doc 01 §7 niveau 3 ("froid").

Garantie d'isolation (doc 03 §2) : `thread_id` est TOUJOURS `Settings.ROOM_ID` — il n'existe
aucune autre valeur possible dans ce process. Un CIVITAS Agent qui redémarre après un crash
(cf. doc 03 §4.4) ne peut donc physiquement recharger que SON PROPRE état de graphe, jamais
celui d'une autre room, même en cas de bug (il n'y a pas de paramètre `thread_id` exposé
ailleurs dans le code qui pourrait être mal renseigné).

Utilise `langgraph-checkpoint-postgres` (PostgresSaver) contre la même base Postgres que
room-config (schéma séparé, table dédiée `civitas_agent_checkpoints`, cf. doc 01 §7) — pas de
nouvelle instance Postgres à déployer.
"""
from __future__ import annotations

import logging
from contextlib import asynccontextmanager

from app.config import get_settings

log = logging.getLogger(__name__)

settings = get_settings()


def thread_config(room_id: str) -> dict:
    """Configuration LangGraph passée à chaque `graph.ainvoke(state, config=...)`."""
    assert room_id == settings.ROOM_ID, (
        "Garantie d'isolation violée : ce process ne doit jamais utiliser un thread_id "
        "différent de son propre ROOM_ID — cf. docs/architecture/03-isolation-et-orchestration.md §2"
    )
    return {"configurable": {"thread_id": room_id}}


@asynccontextmanager
async def build_checkpointer():
    """
    Context manager retournant un checkpointer prêt à l'emploi (`async with build_checkpointer()
    as checkpointer:`), utilisé une seule fois au démarrage du process (app/main.py) pour
    compiler le graphe (app/graph/build.py).

    Dégradation explicite (jamais silencieuse) si Postgres est indisponible au démarrage :
    logge une erreur claire et laisse l'exception remonter — un CIVITAS Agent qui ne peut pas
    persister son état ne doit pas démarrer en faisant croire qu'il le peut (contrairement à
    la dégradation gracieuse acceptée pour la mémoire niveau 2, doc 00 §5.3, qui ne concerne
    que la RÉHYDRATATION, pas la capacité à checkpointer en continu).
    """
    try:
        from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
    except ImportError as e:
        raise RuntimeError(
            "langgraph-checkpoint-postgres non installé — cf. requirements.txt"
        ) from e

    async with AsyncPostgresSaver.from_conn_string(settings.CHECKPOINT_DATABASE_URL) as saver:
        try:
            await saver.setup()  # idempotent — crée les tables si absentes
        except Exception as e:
            log.warning(f"[Checkpoint:{settings.ROOM_ID}] setup(): {e}")
        log.info(f"[Checkpoint:{settings.ROOM_ID}] Prêt (thread_id={settings.ROOM_ID})")
        yield saver
