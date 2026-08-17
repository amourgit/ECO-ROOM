"""
platform_tools — doc 02 §8 (domaine 4, "CIVITAS Platform"). PAS branché dans
build_default_registry (app/tools/registry.py) pour l'instant : ces APIs métier n'existent pas
encore côté CIVITAS Platform (cf. docs/architecture/04-plan-migration.md Phase 4 — nécessite
une clarification produit avant implémentation, volontairement non anticipée à tort).

Interface posée pour que l'ajout de la Phase 4 n'impacte ni le graphe ni le reste du catalogue
d'outils (doc 01 §10 — point de variabilité anticipé).
"""
import httpx

from app.config import get_settings

settings = get_settings()

# URL de la CIVITAS Platform (domaine 4) — à définir en Phase 4, cf. doc 04.
PLATFORM_URL = "http://civitas-platform:8000"  # placeholder, non résolu tant que non déployé


async def get_user(user_id: str) -> dict:
    raise NotImplementedError("Phase 4 — cf. docs/architecture/04-plan-migration.md")


async def get_meeting(meeting_id: str) -> dict:
    raise NotImplementedError("Phase 4 — cf. docs/architecture/04-plan-migration.md")


async def get_document(document_id: str) -> dict:
    raise NotImplementedError("Phase 4 — cf. docs/architecture/04-plan-migration.md")


async def create_task(payload: dict) -> dict:
    raise NotImplementedError("Phase 4 — cf. docs/architecture/04-plan-migration.md")


async def create_minutes(payload: dict) -> dict:
    raise NotImplementedError("Phase 4 — cf. docs/architecture/04-plan-migration.md")


async def create_vote(payload: dict) -> dict:
    raise NotImplementedError("Phase 4 — cf. docs/architecture/04-plan-migration.md")


def register_tools(registry, browser, speech_engine) -> None:
    """
    NON appelé par build_default_registry aujourd'hui (cf. docstring de module) — laissé ici,
    prêt à être branché en Phase 4, pour que l'ajout futur soit un simple appel supplémentaire
    dans build_default_registry, jamais une réécriture.
    """
    from app.tools.registry import ToolSpec

    for name, func in (
        ("platform_tools.get_user", get_user),
        ("platform_tools.get_meeting", get_meeting),
        ("platform_tools.get_document", get_document),
        ("platform_tools.create_task", create_task),
        ("platform_tools.create_minutes", create_minutes),
        ("platform_tools.create_vote", create_vote),
    ):
        registry.register(ToolSpec(
            name=name, func=func, capability="can_use_tools",
            implemented=False, doc_status="🆕",
        ))
