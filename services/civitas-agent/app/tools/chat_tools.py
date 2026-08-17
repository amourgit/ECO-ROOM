"""
chat_tools — doc 02 §1. Communication écrite/réaction, vers le groupe ou en privé.
"""
from app.tools.registry import ToolRegistry, ToolSpec


def register_tools(registry: ToolRegistry, browser, speech_engine) -> None:
    registry.register(ToolSpec(
        name="chat_tools.send_chat",
        func=lambda text: browser.send_chat(text),
        capability="can_write_chat",
        doc_status="✅",
    ))
    registry.register(ToolSpec(
        name="chat_tools.send_private_chat",
        func=lambda participant_id, text: browser.send_private_chat(participant_id, text),
        capability="can_write_chat",
        doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="chat_tools.send_reaction",
        func=lambda emoji: browser.send_reaction(emoji),
        capability="can_write_chat",
        doc_status="🆕",
    ))

    # P1 — cf. docs/architecture/02-catalogue-outils-agent.md §11 : format à extraire du
    # bundle JS déployé avant implémentation, volontairement non codé ici.
    async def _not_implemented(**_kwargs):
        raise NotImplementedError("cf. doc 02 §11 — format à valider avant implémentation")

    registry.register(ToolSpec(
        name="chat_tools.create_poll", func=_not_implemented,
        capability="can_write_chat", implemented=False, doc_status="🔧",
    ))
    registry.register(ToolSpec(
        name="chat_tools.answer_poll", func=_not_implemented,
        capability="can_write_chat", implemented=False, doc_status="🔧",
    ))
