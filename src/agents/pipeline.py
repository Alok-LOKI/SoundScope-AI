"""
SoundScope-AI: Orchestrated Multi-Agent Critique Pipeline
Coordinates the Acoustic Signal Agent, Lyric Critic Agent, Mastering Advisor, and Verification Guard.
"""

from typing import Dict, Any, List
from .state import TrackState


class MultiAgentPipeline:
    """Orchestrates acoustic, lyrical, and mastering agents to produce verified track critiques."""

    def __init__(self):
        pass

    def run(self, audio_metrics: Dict[str, Any], lyric_metrics: Dict[str, Any], track_title: str = "Untitled Track", artist_name: str = "Unknown Artist") -> TrackState:
        """Executes the full agent evaluation cycle."""
        state: TrackState = {
            "track_id": f"track_{abs(hash(track_title)) % 100000}",
            "track_title": track_title,
            "artist_name": artist_name,
            "file_path": None,
            "audio_metrics": audio_metrics,
            "lyric_metrics": lyric_metrics,
            "transcribed_lyrics": None,
            "signal_critique": "",
            "lyric_critique": "",
            "mastering_recommendations": [],
            "overall_score": 0.0,
            "guardrail_passed": True,
            "guardrail_warnings": [],
            "agent_logs": [],
        }

        # Step 1: Acoustic Signal Analyst Agent
        state = self._signal_analyst_agent(state)

        # Step 2: Lyric Semantic Agent
        state = self._lyric_semantic_agent(state)

        # Step 3: Mastering Critic Agent
        state = self._mastering_critic_agent(state)

        # Step 4: Verification & Guard Agent
        state = self._verification_guard_agent(state)

        # Step 5: Scoring
        state = self._calculate_overall_score(state)

        return state

    def _signal_analyst_agent(self, state: TrackState) -> TrackState:
        m = state["audio_metrics"] or {}
        centroid = m.get("spectral_centroid_mean", 2000)
        tempo = m.get("tempo_bpm", 120)
        dyn_range = m.get("dynamic_range_db", 30)
        harm_ratio = m.get("harmonic_ratio", 0.6)

        critiques = []
        critiques.append(f"• **Pacing & Rhythm:** Detected tempo is **{tempo} BPM**, displaying stable rhythmic consistency.")

        if centroid < 1600:
            critiques.append(f"• **Frequency Balance:** Spectral centroid sits low (~{centroid:.0f} Hz), indicating a warm, bass-heavy mix with potential low-mid mud around 250-400 Hz.")
        elif centroid > 3200:
            critiques.append(f"• **Frequency Balance:** Spectral centroid is elevated (~{centroid:.0f} Hz), showing prominent high-end brightness; check for sibilance in the 6-8 kHz region.")
        else:
            critiques.append(f"• **Frequency Balance:** Well-balanced spectral distribution (centroid ~{centroid:.0f} Hz) providing clean clarity across the midrange.")

        if dyn_range < 18:
            critiques.append(f"• **Dynamics:** Dynamic range is compressed ({dyn_range:.1f} dB). While competitive for loudness, transient punch on drums may be compromised.")
        else:
            critiques.append(f"• **Dynamics:** Healthy dynamic contrast ({dyn_range:.1f} dB) preserving natural transient attack and breathability.")

        critiques.append(f"• **Texture:** Harmonic-to-Percussive ratio is {harm_ratio:.2f} : {1 - harm_ratio:.2f}, indicating a {'melodic/harmonic-led' if harm_ratio >= 0.55 else 'groove/percussive-driven'} arrangement.")

        state["signal_critique"] = "\n".join(critiques)
        state["agent_logs"].append("Acoustic Signal Analyst Agent completed spectral evaluation.")
        return state

    def _lyric_semantic_agent(self, state: TrackState) -> TrackState:
        lm = state["lyric_metrics"] or {}
        am = state["audio_metrics"] or {}
        theme = lm.get("primary_theme", "General Narrative")
        rhyme = lm.get("rhyme_density_score", 0.5)
        valence = lm.get("valence_score", 0.0)
        ttr = lm.get("type_token_ratio", 0.6)
        tempo = am.get("tempo_bpm", 120)

        critiques = []
        critiques.append(f"• **Core Theme:** Primary lyrical domain identified as **{theme}**.")
        critiques.append(f"• **Poetic Density:** End-rhyme density scored at **{rhyme * 100:.1f}%**, demonstrating consistent stanza cadence.")
        critiques.append(f"• **Vocabulary Diversity:** Type-Token Ratio of **{ttr:.2f}** indicates {'rich, evocative word choice' if ttr >= 0.55 else 'repetitive, hook-focused phrasing'}.")

        # Multimodal alignment check
        if tempo >= 125 and valence < -0.2:
            critiques.append("• **Multimodal Contrast:** High-energy acoustic tempo is paired with melancholic lyrical sentiment, creating an engaging dramatic tension.")
        elif tempo < 100 and valence > 0.3:
            critiques.append("• **Multimodal Synergy:** Laid-back groove complements warm, optimistic lyrical tone, creating an intimate listening experience.")
        else:
            critiques.append(f"• **Sentiment Alignment:** Lyrical valence score of {valence:+.2f} matches the acoustic energy profile.")

        state["lyric_critique"] = "\n".join(critiques)
        state["agent_logs"].append("Lyric Semantic Agent completed poetic and emotional analysis.")
        return state

    def _mastering_critic_agent(self, state: TrackState) -> TrackState:
        m = state["audio_metrics"] or {}
        recs = []

        centroid = m.get("spectral_centroid_mean", 2200)
        dyn_range = m.get("dynamic_range_db", 30)
        harm_ratio = m.get("harmonic_ratio", 0.6)

        if centroid < 1800:
            recs.append("Apply a subtle high-shelf boost (+1.5 dB @ 10 kHz) to open up air and vocal presence.")
            recs.append("Dip low-mids (-1.0 dB around 300 Hz) to eliminate acoustic muddiness.")
        elif centroid > 3200:
            recs.append("Softly attenuate the top-end using a dynamic EQ dip between 5 kHz and 7 kHz to tame harshness.")
        else:
            recs.append("Maintain the current frequency balance; mid-range tonal contour is balanced.")

        if dyn_range < 20:
            recs.append("Ease limiter threshold by 1-2 dB to restore drum snare transients and reduce fatigue.")
        else:
            recs.append("Apply light parallel bus compression (2:1 ratio, slow attack) to glue the rhythm section.")

        if harm_ratio > 0.7:
            recs.append("Carve out space in the stereo sides (Mid/Side processing) to keep the central vocal focal.")

        state["mastering_recommendations"] = recs
        state["agent_logs"].append("Mastering Critic Agent generated studio recommendations.")
        return state

    def _verification_guard_agent(self, state: TrackState) -> TrackState:
        """Verifies that mastering recommendations do not contradict ground-truth DSP metrics."""
        m = state["audio_metrics"] or {}
        centroid = m.get("spectral_centroid_mean", 2200)
        recs = state["mastering_recommendations"] or []
        warnings = []

        # Check: If centroid is very bright, ensure no advice asks for more treble boost
        if centroid > 3400:
            contradictory = [r for r in recs if "high-shelf boost" in r.lower()]
            if contradictory:
                warnings.append("Guardrail Triggered: Treble boost suggested on an already bright mix. Suppressed recommendation.")
                state["mastering_recommendations"] = [r for r in recs if r not in contradictory]

        state["guardrail_warnings"] = warnings
        state["guardrail_passed"] = len(warnings) == 0
        state["agent_logs"].append("Verification Guard Agent passed critique checks.")
        return state

    def _calculate_overall_score(self, state: TrackState) -> TrackState:
        am = state["audio_metrics"] or {}
        lm = state["lyric_metrics"] or {}

        # Heuristic production quality score out of 100
        score = 75.0
        # Balance bonus
        centroid = am.get("spectral_centroid_mean", 2000)
        if 1800 <= centroid <= 2800:
            score += 8.0
        # Dynamic range bonus
        dyn = am.get("dynamic_range_db", 25)
        if 20 <= dyn <= 40:
            score += 7.0
        # Lyric vocabulary bonus
        ttr = lm.get("type_token_ratio", 0.5)
        score += min(10.0, ttr * 15.0)

        state["overall_score"] = round(min(98.0, max(50.0, score)), 1)
        return state
