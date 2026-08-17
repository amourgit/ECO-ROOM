"""
moderation_tools — doc 02 §3. Actions sur les autres participants — toutes requièrent
can_moderate, et requièrent en pratique que l'agent soit lui-même modérateur côté Jitsi (vérifié
au niveau navigateur, get_moderator_status, cf. doc 00 §5.4 — pattern conservé).
"""
from app.tools.registry import ToolRegistry, ToolSpec


def register_tools(registry: ToolRegistry, browser, speech_engine) -> None:
    registry.register(ToolSpec(
        name="moderation_tools.kick_participant",
        func=lambda participant_id, reason=None: browser.kick_participant(participant_id, reason),
        capability="can_moderate", doc_status="✅",
    ))
    registry.register(ToolSpec(
        name="moderation_tools.mute_participant",
        func=lambda participant_id: browser.mute_participant(participant_id),
        capability="can_moderate", doc_status="✅",
    ))
    registry.register(ToolSpec(
        name="moderation_tools.get_moderator_status",
        func=lambda: browser.get_moderator_status(),
        capability=None, doc_status="✅",
    ))
    registry.register(ToolSpec(
        name="moderation_tools.grant_moderator",
        func=lambda participant_id: browser.grant_moderator(participant_id),
        capability="can_moderate", doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="moderation_tools.enable_av_moderation",
        func=lambda media_type="audio": browser.enable_av_moderation(media_type),
        capability="can_moderate", doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="moderation_tools.disable_av_moderation",
        func=lambda media_type="audio": browser.disable_av_moderation(media_type),
        capability="can_moderate", doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="moderation_tools.approve_unmute_request",
        func=lambda participant_id, media_type="audio": browser.approve_unmute_request(participant_id, media_type),
        capability="can_moderate", doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="moderation_tools.reject_unmute_request",
        func=lambda participant_id, media_type="audio": browser.reject_unmute_request(participant_id, media_type),
        capability="can_moderate", doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="moderation_tools.enable_lobby",
        func=lambda: browser.enable_lobby(),
        capability="can_moderate", doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="moderation_tools.disable_lobby",
        func=lambda: browser.disable_lobby(),
        capability="can_moderate", doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="moderation_tools.lobby_approve_access",
        func=lambda participant_id: browser.lobby_approve_access(participant_id),
        capability="can_moderate", doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="moderation_tools.lobby_deny_access",
        func=lambda participant_id: browser.lobby_deny_access(participant_id),
        capability="can_moderate", doc_status="🆕",
    ))
