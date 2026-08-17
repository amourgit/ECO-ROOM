"""
Vision — orchestration de la capture d'écran + description, cf.
docs/architecture/02-catalogue-outils-agent.md §7 (vision_tools).

ADAPTÉ DE PeerInstance._handle_vision (services/peer/app/peer/instance.py) : la logique était
auparavant câblée en dur dans PeerInstance et déclenchée uniquement par mot-clé. Ici, c'est une
fonction autonome, appelable aussi bien par le nœud `acting` (déclenchement décidé par le
raisonnement LLM) que par un déclenchement par mot-clé détecté dans le nœud `routing` — les
deux chemins convergent vers la même fonction, cf. doc 01 §4.3.
"""
import base64
import logging

log = logging.getLogger(__name__)

DEFAULT_VISION_PROMPT = "Décris ce que tu vois dans cette réunion Jitsi en français."


async def capture_frame(browser) -> str | None:
    """PORTÉ DE CivitasBrowser.capture_frame (services/peer/app/browser/browser.py)."""
    try:
        png = await browser.page.screenshot(
            type="jpeg", quality=80,
            clip={"x": 0, "y": 0, "width": 1280, "height": 720},
        )
        return base64.b64encode(png).decode()
    except Exception as e:
        log.warning(f"[Vision] capture_frame: {e}")
        return None


async def describe_screen(browser, speech_engine, prompt: str = DEFAULT_VISION_PROMPT) -> bool:
    """
    Capture puis envoie au moteur de parole (Gemini vision) pour description. Le résultat
    textuel arrive de façon asynchrone via le callback on_speech du moteur de parole (comme
    pour toute réponse), pas en valeur de retour directe — cette fonction retourne seulement
    si la capture + l'envoi ont réussi.
    """
    frame = await capture_frame(browser)
    if not frame:
        return False
    await speech_engine.send_image(frame, prompt)
    return True
