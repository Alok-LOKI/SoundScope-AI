"""
Unit tests for SoundScope-AI baseline feature extraction.
"""

import numpy as np
from src.lyric_nlp.analyzer import LyricAnalyzer
from src.agents.state import TrackState


def test_lyric_analyzer_basic():
    analyzer = LyricAnalyzer()
    sample_lyrics = """
    I see the flashing light tonight
    It makes the future look so bright
    We keep on dancing through the pain
    Until the sunshine meets the rain
    """
    metrics = analyzer.analyze_text(sample_lyrics)
    assert metrics.total_words > 0
    assert metrics.unique_words > 0
    assert metrics.type_token_ratio > 0
    assert metrics.rhyme_density_score > 0
    assert -1.0 <= metrics.valence_score <= 1.0


def test_track_state_structure():
    state: TrackState = {
        "track_id": "track_001",
        "track_title": "Neon Horizons",
        "artist_name": "SoundScope Demo",
        "file_path": None,
        "audio_metrics": None,
        "lyric_metrics": None,
        "transcribed_lyrics": "Sample test lyrics",
        "signal_critique": None,
        "lyric_critique": None,
        "mastering_recommendations": None,
        "overall_score": None,
        "guardrail_passed": True,
        "guardrail_warnings": [],
        "agent_logs": ["Initialized track state"],
    }
    assert state["track_id"] == "track_001"
    assert state["guardrail_passed"] is True
