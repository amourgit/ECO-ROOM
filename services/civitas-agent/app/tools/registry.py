"""
Registre d'outils — NOUVEAU, cœur de la modularité demandée (cf.
docs/architecture/01-architecture-cible-civitas-agent.md §9 et
docs/architecture/02-catalogue-outils-agent.md).

Relie enfin `room_configs.permissions`/`tools_allowed` (existants dans le schéma Postgres
depuis le début, jamais exploités par l'ancien peer, cf. doc 00 §6.1) à un mécanisme réel :
chaque outil déclare la capacité dont il dépend, et le registre refuse tout appel non autorisé
AVANT d'atteindre le navigateur/Jitsi — jamais un faux succès silencieux.

Le nœud `act` (app/graph/nodes/acting.py) est l'unique point d'entrée qui appelle
`ToolRegistry.invoke(...)` — aucun autre code n'appelle directement une fonction de
`chat_tools`/`moderation_tools`/etc., pour garantir que la vérification de permission ne peut
jamais être contournée par erreur.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Awaitable, Callable

log = logging.getLogger(__name__)

Capability = str  # "can_speak" | "can_write_chat" | "can_use_tools" | "can_use_rag" | "can_moderate"

ToolFunc = Callable[..., Awaitable[dict]]


@dataclass
class ToolSpec:
    name: str                      # "moderation_tools.kick_participant" — nom qualifié, doc 02
    func: ToolFunc
    capability: Capability | None  # None = toujours autorisé si can_use_tools (outils de base)
    implemented: bool = True       # False pour les outils P1 déclarés mais non codés (doc 02)
    doc_status: str = "✅"          # "✅" | "🆕" | "🔧" — reflète doc 02, pour l'observabilité


class ToolRegistry:
    """Un registre par process (donc par room, cf. app/config.py) — pas de partage entre agents."""

    def __init__(self):
        self._tools: dict[str, ToolSpec] = {}

    def register(self, spec: ToolSpec) -> None:
        if spec.name in self._tools:
            raise ValueError(f"Outil déjà enregistré: {spec.name}")
        self._tools[spec.name] = spec

    def list_tools(self) -> list[str]:
        return sorted(self._tools.keys())

    def describe(self) -> list[dict]:
        """Pour /admin/state (doc 01 §8.1) et pour construire le prompt du nœud `reason`
        (quels outils sont réellement disponibles pour cette room, avec quel statut)."""
        return [
            {"name": s.name, "capability": s.capability,
             "implemented": s.implemented, "doc_status": s.doc_status}
            for s in self._tools.values()
        ]

    async def invoke(self, tool_name: str, args: dict, permissions: dict,
                      tools_allowed: list[str], reason: str = "") -> dict:
        """
        Point d'entrée unique (cf. docstring de module). Contrat de sortie stable, sur le
        modèle déjà en place pour kick_participant/mute_participant dans l'ancien peer
        (doc 00 §5.4), généralisé ici à TOUS les outils :

            {"ok": bool, "allowed": bool, "implemented": bool, "result": ..., "error": str|None}
        """
        requested_at = datetime.now(timezone.utc).isoformat()
        spec = self._tools.get(tool_name)

        if spec is None:
            log.warning(f"[ToolRegistry] Outil inconnu demandé: {tool_name}")
            return {"ok": False, "allowed": False, "implemented": False,
                    "result": None, "error": f"outil inconnu: {tool_name}"}

        if not spec.implemented:
            log.info(f"[ToolRegistry] Outil non implémenté (P1, cf. doc 02): {tool_name}")
            return {"ok": False, "allowed": True, "implemented": False, "result": None,
                     "error": f"'{tool_name}' est planifié mais pas encore implémenté (voir "
                              f"docs/architecture/02-catalogue-outils-agent.md)"}

        allowed, deny_reason = self._check_permission(spec, permissions, tools_allowed)
        if not allowed:
            log.info(f"[ToolRegistry] Refusé ({deny_reason}): {tool_name} args={args}")
            return {"ok": False, "allowed": False, "implemented": True,
                    "result": None, "error": deny_reason}

        try:
            result = await spec.func(**args)
            log.info(f"[ToolRegistry] {tool_name}({args}) → ok — raison: {reason!r}")
            return {"ok": True, "allowed": True, "implemented": True,
                    "result": result, "error": None}
        except Exception as e:
            log.error(f"[ToolRegistry] {tool_name}({args}) exception: {e}", exc_info=True)
            return {"ok": False, "allowed": True, "implemented": True,
                    "result": None, "error": str(e)}

    @staticmethod
    def _check_permission(spec: ToolSpec, permissions: dict,
                           tools_allowed: list[str]) -> tuple[bool, str | None]:
        # 1. Liste blanche explicite (room_configs.tools_allowed), si non vide — la plus
        #    restrictive, elle prime sur les capacités générales.
        if tools_allowed and spec.name not in tools_allowed:
            return False, (
                f"'{spec.name}' n'est pas dans tools_allowed pour cette room"
            )

        # 2. Capacité générale requise (room_configs.permissions.*)
        if spec.capability and not permissions.get(spec.capability, False):
            return False, f"capacité '{spec.capability}' non accordée à cette room"

        # 3. can_use_tools : garde-fou global, cohérent avec le schéma existant (doc 00 §6.1) —
        #    un outil qui ne requiert aucune capacité spécifique (spec.capability is None)
        #    reste soumis à ce garde-fou général.
        if spec.capability is None and not permissions.get("can_use_tools", False):
            return False, "can_use_tools non accordé à cette room"

        return True, None


def build_default_registry(browser, speech_engine) -> ToolRegistry:
    """
    Construit le registre pour CETTE room, à partir du CivitasBrowser et du SpeechEngine déjà
    démarrés pour ce process (cf. app/main.py). Rassemble tous les modules `tools/*.py` — c'est
    le SEUL endroit du code où l'arborescence "un fichier par catégorie" (doc 01 §8) est
    aplatie en un registre unique consommé par le graphe.
    """
    from app.tools import (
        chat_tools, media_tools, moderation_tools, presence_tools,
        room_tools, vision_tools,
    )

    registry = ToolRegistry()
    for module in (chat_tools, presence_tools, moderation_tools,
                   room_tools, media_tools, vision_tools):
        module.register_tools(registry, browser, speech_engine)
    return registry
