"""
Comprehensive End-to-End System Verification for SoundScope-AI.
Tests DSP feature extraction, NLP lyric analysis, Multi-Agent LangGraph pipeline,
FastAPI REST endpoints, and all 6 multi-genre catalog tracks.
"""

import os
import sys

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from fastapi.testclient import TestClient

from src.audio_dsp.features import AudioFeatureExtractor
from src.lyric_nlp.analyzer import LyricAnalyzer
from src.agents.pipeline import MultiAgentPipeline
from src.api.main import app, TRACK_CATALOG


def run_full_system_verification():
    print("=" * 65)
    print("SOUNDSCOPE-AI: FULL SYSTEM VERIFICATION SUITE")
    print("=" * 65)

    # 1. Test DSP Feature Extractor
    print("\n[Step 1/5] Testing Audio DSP Engine...")
    extractor = AudioFeatureExtractor()
    sr = 22050
    t = np.linspace(0, 2.0, int(sr * 2.0), endpoint=False)
    synthetic_signal = 0.5 * np.sin(2 * np.pi * 440 * t)
    audio_metrics = extractor.extract_from_array(synthetic_signal, sr)
    assert audio_metrics.tempo_bpm > 0, "DSP tempo failed"
    assert audio_metrics.spectral_centroid_mean > 0, "DSP centroid failed"
    assert len(audio_metrics.mfcc_means) == 20, "MFCC band count mismatch"
    print(f"  [OK] DSP Engine (Tempo: {audio_metrics.tempo_bpm} BPM, Centroid: {audio_metrics.spectral_centroid_mean} Hz, 20 MFCCs)")

    # 2. Test Lyric NLP Analyzer
    print("\n[Step 2/5] Testing Lyric & Poetic NLP Engine...")
    analyzer = LyricAnalyzer()
    sample_lyrics = """
    Riding high into the neon night
    Chasing after the burning light
    Never looking back again
    Dancing away the silent pain
    """
    lyric_metrics = analyzer.analyze_text(sample_lyrics)
    assert lyric_metrics.total_words > 0, "Word count zero"
    assert lyric_metrics.rhyme_density_score > 0, "Rhyme density failed"
    assert lyric_metrics.primary_theme != "", "Theme missing"
    print(f"  [OK] NLP Engine (Theme: {lyric_metrics.primary_theme}, Rhyme: {lyric_metrics.rhyme_density_score * 100:.1f}%, Valence: {lyric_metrics.valence_score})")

    # 3. Test Multi-Agent Pipeline
    print("\n[Step 3/5] Testing Multi-Agent Orchestration & Guardrails...")
    pipeline = MultiAgentPipeline()
    state = pipeline.run(audio_metrics.to_dict(), lyric_metrics.to_dict(), "Test Track", "SoundScope")
    assert state["overall_score"] is not None and state["overall_score"] > 50, "Invalid score"
    assert len(state["signal_critique"]) > 20, "Signal critique empty"
    assert len(state["lyric_critique"]) > 20, "Lyric critique empty"
    assert len(state["mastering_recommendations"]) > 0, "Recommendations missing"
    assert state["guardrail_passed"] is True, "Guardrail failure"
    print(f"  [OK] Multi-Agent Pipeline (Production Score: {state['overall_score']}/100, Guardrails: PASSED)")

    # 4. Test FastAPI Server & Web App
    print("\n[Step 4/5] Testing FastAPI Endpoints & Static Dashboard...")
    client = TestClient(app)

    # Health check
    res_health = client.get("/api/health")
    assert res_health.status_code == 200, "Health check failed"
    print("  [OK] /api/health -> 200 OK")

    # Static HTML root
    res_root = client.get("/")
    assert res_root.status_code == 200, "Web dashboard root failed"
    assert "SoundScope-AI" in res_root.text, "Dashboard HTML missing brand"
    print("  [OK] GET / (Dashboard UI) -> 200 OK")

    # Track catalog list
    res_tracks = client.get("/api/tracks")
    assert res_tracks.status_code == 200
    track_list = res_tracks.json()
    assert len(track_list) == 6, f"Expected 6 tracks, found {len(track_list)}"
    print(f"  [OK] GET /api/tracks -> 200 OK ({len(track_list)} demo tracks available)")

    # 5. Test All 6 Genre Demo Tracks (Data & Audio Streams)
    print("\n[Step 5/5] Testing All 6 Genre Catalog Tracks (Audio & Data)...")
    for track in track_list:
        tid = track["id"]
        # Data & metrics endpoint
        res_data = client.get(f"/api/tracks/{tid}/data")
        assert res_data.status_code == 200, f"Failed getting data for {tid}"
        tdata = res_data.json()
        assert "audio_metrics" in tdata
        assert "lyric_metrics" in tdata
        assert "critique" in tdata

        # Audio stream endpoint
        res_audio = client.get(f"/api/tracks/{tid}/audio")
        assert res_audio.status_code == 200, f"Failed streaming audio for {tid}"
        assert len(res_audio.content) > 10000, f"Audio content too small for {tid}"

        tempo = tdata["audio_metrics"]["tempo_bpm"]
        score = tdata["critique"]["overall_score"]
        print(f"  [OK] Track '{track['title']}' ({track['genre']}) -> Tempo: {tempo} BPM, Score: {score}/100, Audio: {len(res_audio.content):,} bytes")

    print("\n" + "=" * 65)
    print("ALL SYSTEMS PASSING! 100% OPERATIONAL & READY TO RUN!")
    print("=" * 65)


if __name__ == "__main__":
    run_full_system_verification()
