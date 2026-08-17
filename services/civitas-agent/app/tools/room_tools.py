"""
room_tools — doc 02 §4. Réglages de la réunion — requièrent can_moderate.
"""
from app.tools.registry import ToolRegistry, ToolSpec


def register_tools(registry: ToolRegistry, browser, speech_engine) -> None:
    registry.register(ToolSpec(
        name="room_tools.set_subject",
        func=lambda subject: browser.set_subject(subject),
        capability="can_moderate", doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="room_tools.lock_room",
        func=lambda password: browser.lock_room(password),
        capability="can_moderate", doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="room_tools.unlock_room",
        func=lambda: browser.unlock_room(),
        capability="can_moderate", doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="room_tools.end_meeting",
        func=lambda: browser.end_meeting(),
        capability="can_moderate", doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="room_tools.get_breakout_rooms",
        func=lambda: browser.get_breakout_rooms(),
        capability=None, doc_status="📖",
    ))

    async def _not_implemented(**_kwargs):
        raise NotImplementedError("cf. doc 02 §4 — format XMPP à valider avant implémentation")

    registry.register(ToolSpec(
        name="room_tools.manage_breakout_rooms", func=_not_implemented,
        capability="can_moderate", implemented=False, doc_status="🔧",
    ))
    registry.register(ToolSpec(
        name="room_tools.toggle_e2ee", func=_not_implemented,
        capability="can_moderate", implemented=False, doc_status="🔧",
    ))
    registry.register(ToolSpec(
        name="room_tools.dial", func=_not_implemented,
        capability="can_moderate", implemented=False, doc_status="🔧",
    ))
