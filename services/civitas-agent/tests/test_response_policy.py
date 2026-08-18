"""
Tests app/speech/response_policy.py — fonction pure portée telle quelle depuis
services/peer/app/peer/response_policy.py (cf. docs/architecture/00-etat-des-lieux.md §5.6).
"""
from app.speech.response_policy import ResponseMode, decide_chat_response_mode, parse_keywords


def test_parse_keywords_strips_and_lowercases():
    assert parse_keywords(" Oral, VOIX ,parle") == ["oral", "voix", "parle"]


def test_parse_keywords_empty_string():
    assert parse_keywords("") == []


def test_decide_response_mode_defaults_to_text():
    mode = decide_chat_response_mode("Peux-tu résumer la réunion ?", ["oral", "voix"])
    assert mode == ResponseMode.TEXT


def test_decide_response_mode_oral_keyword_triggers_audio():
    mode = decide_chat_response_mode("Réponds-moi à voix haute stp", ["à voix haute"])
    assert mode == ResponseMode.AUDIO


def test_decide_response_mode_case_insensitive():
    mode = decide_chat_response_mode("Dis-le en VOCAL", ["vocal"])
    assert mode == ResponseMode.AUDIO
