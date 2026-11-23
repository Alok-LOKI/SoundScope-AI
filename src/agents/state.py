"""
SoundScope-AI: LangGraph State Definition
Defines the shared typed dictionary passed between the multi-agent critique nodes.
"""

from typing import TypedDict, Optional, List, Dict, Any


class TrackState(TypedDict):
    """Shared state for the multi-agent music critique workflow."""
    # Metadata
    track_id: str
    track_title: str
    artist_name: Optional[str]
    file_path: Optional[str]

    # Signal & NLP Features
    audio_metrics: Optional[Dict[str, Any]]
    lyric_metrics: Optional[Dict[str, Any]]
    transcribed_lyrics: Optional[str]

    # Agent Critique Outputs
    signal_critique: Optional[str]
    lyric_critique: Optional[str]
    mastering_recommendations: Optional[List[str]]
    overall_score: Optional[float]

    # Guardrails & Verification
    guardrail_passed: bool
    guardrail_warnings: List[str]

    # History & Logs
    agent_logs: List[str]
