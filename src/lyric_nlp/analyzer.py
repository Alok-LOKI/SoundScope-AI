"""
SoundScope-AI: Lyric & Natural Language Processing (NLP) Analyzer
Evaluates lyrical features: rhyme density, vocabulary richness, and emotional polarity.
"""

from dataclasses import dataclass, asdict
from typing import Dict, Any, List
import re


@dataclass
class LyricMetrics:
    """Dataclass holding extracted linguistic and poetic metrics."""
    total_words: int
    unique_words: int
    type_token_ratio: float  # Vocabulary richness
    verse_count: int
    avg_line_length_words: float
    rhyme_density_score: float
    valence_score: float     # Positivity (-1.0 to +1.0)
    arousal_score: float     # Emotional intensity (0.0 to 1.0)
    primary_theme: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class LyricAnalyzer:
    """Analyzes poetic meter, vocabulary diversity, and emotional tone of song lyrics."""

    def __init__(self):
        pass

    def analyze_text(self, text: str) -> LyricMetrics:
        """Computes linguistic metrics on lyric text."""
        lines = [line.strip() for line in text.strip().split("\n") if line.strip()]
        words = re.findall(r"\b[a-zA-Z']+\b", text.lower())

        total_words = len(words)
        unique_words = len(set(words))
        type_token_ratio = round(unique_words / max(total_words, 1), 3)

        avg_line_len = round(total_words / max(len(lines), 1), 1)

        # Baseline rhyme density (comparing terminal end-rhymes)
        rhyme_density = self._calculate_rhyme_density(lines)

        # Sentiment heuristics (baseline prior to RoBERTa model inference)
        valence, arousal = self._estimate_sentiment(words)

        # Topic detection baseline
        theme = self._detect_theme(words)

        return LyricMetrics(
            total_words=total_words,
            unique_words=unique_words,
            type_token_ratio=type_token_ratio,
            verse_count=max(len(lines) // 4, 1),
            avg_line_length_words=avg_line_len,
            rhyme_density_score=round(rhyme_density, 3),
            valence_score=round(valence, 2),
            arousal_score=round(arousal, 2),
            primary_theme=theme,
        )

    def _calculate_rhyme_density(self, lines: List[str]) -> float:
        """Approximates end-rhyme similarity between adjacent lines."""
        if len(lines) < 2:
            return 0.0

        end_words = []
        for line in lines:
            matches = re.findall(r"\b[a-zA-Z]+\b", line.lower())
            if matches:
                end_words.append(matches[-1])

        rhyme_matches = 0
        for i in range(len(end_words) - 1):
            w1, w2 = end_words[i], end_words[i + 1]
            if len(w1) >= 2 and len(w2) >= 2 and w1[-2:] == w2[-2:]:
                rhyme_matches += 1

        return float(rhyme_matches / max(len(end_words) - 1, 1))

    def _estimate_sentiment(self, words: List[str]) -> tuple[float, float]:
        """Domain-calibrated Valence-Arousal lexical scoring across musical stanzas."""
        positive_seed = {
            "love", "happy", "joy", "shine", "light", "dream", "dance", "bright", "good", "alive",
            "peaceful", "gleam", "sunny", "gentle", "breeze", "rising", "grace", "passion", "magic",
            "sparkle", "sweet", "crystal", "fairy", "warm", "free", "golden", "smile"
        }
        negative_seed = {
            "pain", "sorrow", "tear", "cry", "dark", "die", "alone", "lost", "broken", "hate",
            "shadows", "fade", "fading", "heartbreak", "silent", "underground", "static", "haze",
            "smoke", "lonely", "midnight", "velvet", "weeping", "cold", "empty"
        }
        high_arousal = {
            "fire", "run", "running", "scream", "fight", "shout", "wild", "fast", "crash", "boom",
            "speeding", "rumbling", "rattling", "electric", "rising", "allegro", "fiery", "passion",
            "crescendo", "dramatic", "sync", "tempo", "neon", "flame", "dancing"
        }
        low_arousal = {
            "quiet", "gentle", "peaceful", "floating", "dream", "drifting", "calm", "soft", "slow",
            "whisper", "velvet", "late", "smooth", "brass", "breeze", "morning", "sleep"
        }

        pos_count = sum(1 for w in words if w in positive_seed)
        neg_count = sum(1 for w in words if w in negative_seed)
        hi_arousal = sum(1 for w in words if w in high_arousal)
        lo_arousal = sum(1 for w in words if w in low_arousal)

        total_sentiment_words = pos_count + neg_count
        if total_sentiment_words == 0:
            valence = 0.0
        else:
            valence = (pos_count - neg_count) / (total_sentiment_words + 1.5)

        arousal_raw = 0.50 + (hi_arousal - lo_arousal) / max(len(words) * 0.22, 1.0)
        arousal = max(0.12, min(0.92, arousal_raw))
        return valence, arousal

    def _detect_theme(self, words: List[str]) -> str:
        """Multi-domain lyrical theme classifier."""
        themes = {
            "Nocturnal Synth & Struggle": {"shadows", "neon", "heartbreak", "underground", "midnight", "flame"},
            "High-Octane Kinetic Energy": {"speeding", "static", "electric", "tempo", "signal", "beat"},
            "Pastoral Serenity & Nature": {"lake", "breeze", "pine", "peaceful", "sunny", "clouds", "water"},
            "Dramatic Orchestral Grandeur": {"allegro", "orchestra", "crescendo", "classical", "embrace", "fiery"},
            "Late-Night Noir & Brass": {"jazz", "horn", "brass", "smoke", "melody", "blues", "street"},
            "Enchanted Chamber Fantasy": {"sugar", "plum", "fairy", "crystal", "magic", "ballet", "twilight"},
            "Romance & Relationships": {"love", "baby", "heart", "kiss", "together", "miss"},
            "Melancholy & Introspection": {"lonely", "dark", "pain", "crying", "lost", "empty"},
            "Celebration & Energy": {"party", "dance", "night", "club", "music", "drink"},
            "Resilience & Motivation": {"fight", "strong", "rise", "stand", "survive", "never"},
        }
        word_set = set(words)
        best_theme = "General Narrative"
        max_overlap = 0

        for theme_name, keywords in themes.items():
            overlap = len(word_set.intersection(keywords))
            if overlap > max_overlap:
                max_overlap = overlap
                best_theme = theme_name

        return best_theme
