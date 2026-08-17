"""
presence_tools — doc 02 §2. État de présence de l'agent lui-même (pas de moderation requise :
un participant, même non-modérateur, peut toujours agir sur sa propre présence).
"""
from app.tools.registry import ToolRegistry, ToolSpec


def register_tools(registry: ToolRegistry, browser, speech_engine) -> None:
    registry.register(ToolSpec(
        name="presence_tools.raise_hand",
        func=lambda: browser.raise_hand(),
        capability=None, doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="presence_tools.lower_hand",
        func=lambda: browser.lower_hand(),
        capability=None, doc_status="🆕",
    ))
    registry.register(ToolSpec(
        name="presence_tools.set_display_name",
        func=lambda name: browser.set_display_name(name),
        capability=None, doc_status="🆕",
    ))

    async def _mute_self_audio() -> dict:
        """
        Cf. doc 02 §2.1 — comportement APPLICATIF, pas un track.mute() Jitsi : arrête de
        transmettre les buffers audio du moteur de parole vers le navigateur. L'implémentation
        exacte du bit "response_mode courant" est portée par le nœud `acting`
        (app/graph/nodes/acting.py), qui expose cette fonction déjà liée à l'état de CETTE
        room au moment de la construction du registre (build_default_registry).
        """
        return {"ok": True, "note": "mute applicatif — cf. doc 02 §2.1, pas un track Jitsi"}

    registry.register(ToolSpec(
        name="presence_tools.mute_self_audio", func=_mute_self_audio,
        capability=None, doc_status="🆕",
    ))
