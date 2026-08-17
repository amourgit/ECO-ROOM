"""
persist — doc 01 §6. Dernier nœud du graphe pour chaque invocation. Publie sur Kafka
(`room.transcriptions`, topics inchangés doc 00 §7) toute nouvelle entrée de conversation
produite par CETTE invocation — le checkpoint LangGraph lui-même (doc 01 §7 niveau 3) est géré
par le compileur du graphe (`app/graph/checkpoint.py`), pas par ce nœud : LangGraph persiste
automatiquement l'état complet après chaque `ainvoke` lorsqu'un checkpointer est configuré.

Ce nœud ne republie que la conversation ajoutée à CETTE invocation (pas tout l'historique
accumulé) — il compare la taille de `conversation` avant/après n'étant pas possible ici (le
nœud ne voit que l'état déjà fusionné), la sous-liste ajoutée est donc reconstituée à partir de
`normalized_event`/`actions_to_execute` de la même façon que `update_state`/`act` l'ont
construite — cf. note d'implémentation dans le corps de la fonction.
"""
from __future__ import annotations

import logging
from typing import Awaitable, Callable

from app.graph.deps import GraphDeps
from app.state import ConferenceAgentState

log = logging.getLogger(__name__)

NodeFunc = Callable[[ConferenceAgentState], Awaitable[dict]]

_CONVERSATION_KINDS = {"chat_message", "speech_transcript", "agent_speech"}


def build_persist(deps: GraphDeps) -> NodeFunc:
    async def persist(state: ConferenceAgentState) -> dict:
        norm = state.get("normalized_event")
        if norm and norm["kind"] in _CONVERSATION_KINDS:
            data = norm.get("data", {})
            media = state["media"]
            if norm["kind"] == "agent_speech":
                speaker = deps.room_config.get("agent_name", "CIVITAS")
                entry_type = "agent"
            elif norm["kind"] == "chat_message":
                speaker = data.get("name", "Participant")
                entry_type = "chat"
            else:
                speaker = media.get("current_speaker_name", "Participant")
                entry_type = "participant"

            await deps.kafka.publish_transcription(
                deps.room_id, speaker, data.get("text", ""), entry_type,
                speaker_id=data.get("participantId"),
                extra={"turn_id": data.get("turn_id")},
            )
            # Miroir local (mémoire niveau 1, doc 01 §7) — déjà tenu à jour en parallèle par
            # les callbacks du moteur de parole/EventBus dans app/main.py ; republié ici aussi
            # pour les cas où l'entrée provient du Control Plane sans passer par ces callbacks.
            deps.context_store.add(
                data.get("participantId") or "", speaker, data.get("text", ""),
                entry_type=entry_type, turn_id=data.get("turn_id"),
            )

        return {}

    return persist
