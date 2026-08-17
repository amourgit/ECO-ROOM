"""
rag_tools — doc 02 §9 (domaine 4, Qdrant). PAS branché dans build_default_registry pour
l'instant — nécessite le pipeline d'ingestion documentaire (doc 01 §7, doc 04 Phase 4).

Soumis à `permissions.can_use_rag` (déjà présent dans le schéma room_configs, doc 00 §6.1).
"""
from app.config import get_settings

settings = get_settings()

# Collection Qdrant scoping par knowledge_base_id (room_configs.extra_config), pas par
# room_id — une base de connaissances peut être partagée entre plusieurs rooms d'une même
# organisation (cf. docs/architecture/01-architecture-cible-civitas-agent.md §7).
QDRANT_URL = "http://civitas-qdrant:6333"  # placeholder, non résolu tant que non déployé


async def query_knowledge_base(query: str, knowledge_base_id: str, top_k: int = 5) -> dict:
    raise NotImplementedError(
        "Phase 4 — pipeline d'ingestion Qdrant non déployé, "
        "cf. docs/architecture/04-plan-migration.md"
    )


def register_tools(registry, browser, speech_engine) -> None:
    """NON appelé par build_default_registry aujourd'hui — cf. docstring de module."""
    from app.tools.registry import ToolSpec

    registry.register(ToolSpec(
        name="rag_tools.query_knowledge_base", func=query_knowledge_base,
        capability="can_use_rag", implemented=False, doc_status="🆕",
    ))
