"""
GraphDeps — regroupe tout ce dont les nœuds ont besoin en dehors de ConferenceAgentState
lui-même : le state porte "ce qui est vrai", GraphDeps porte "avec quoi agir" (navigateur,
moteur de parole, registre d'outils, config de room, mémoire, Kafka).

Un seul GraphDeps par process (donc par room, cf. app/config.py) — jamais partagé entre deux
instances de graphe, ce qui serait de toute façon impossible ici puisqu'un seul process ne
construit jamais qu'un seul graphe (doc 03 §2).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class GraphDeps:
    room_id: str
    room_config: dict                 # chargé une fois au démarrage (app/room/config_client.py)
    browser: Any                      # app.browser.driver.CivitasBrowser
    speech_engine: Any                # app.speech.engine.SpeechEngine (GeminiSession par défaut)
    tool_registry: Any                # app.tools.registry.ToolRegistry
    context_store: Any                # app.context.store.ContextStore (mémoire niveau 1)
    kafka: Any                        # app.kafka.producer (module)
