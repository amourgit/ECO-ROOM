"""
vision_tools — doc 02 §7. Perception visuelle. Ne requiert aucune capacité de modération —
gardée sous can_use_tools (garde-fou général du registre, cf. app/tools/registry.py).
"""
from app.perception.vision import DEFAULT_VISION_PROMPT, capture_frame, describe_screen
from app.tools.registry import ToolRegistry, ToolSpec


def register_tools(registry: ToolRegistry, browser, speech_engine) -> None:
    registry.register(ToolSpec(
        name="vision_tools.capture_frame",
        func=lambda: capture_frame(browser),
        capability=None, doc_status="✅",
    ))
    registry.register(ToolSpec(
        name="vision_tools.describe_screen",
        func=lambda prompt=DEFAULT_VISION_PROMPT: describe_screen(browser, speech_engine, prompt),
        capability=None, doc_status="✅",
    ))
    registry.register(ToolSpec(
        name="vision_tools.read_shared_content",
        func=lambda prompt="Lis et extrais le contenu affiché à l'écran, précisément.":
            describe_screen(browser, speech_engine, prompt),
        capability=None, doc_status="🆕",
    ))
