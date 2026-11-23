"""
SoundScope-AI: Audio Digital Signal Processing (DSP) Feature Extractor
Extracts high-dimensional acoustic fingerprints from raw audio signals.
"""

from dataclasses import dataclass, asdict
from typing import Dict, Any, Optional
import numpy as np


@dataclass
class AudioMetrics:
    """Dataclass holding extracted mathematical acoustic features."""
    sample_rate: int
    duration_seconds: float
    tempo_bpm: float
    spectral_centroid_mean: float
    spectral_centroid_std: float
    spectral_rolloff_mean: float
    spectral_rolloff_std: float
    spectral_flux_mean: float
    spectral_flatness_mean: float
    zero_crossing_rate_mean: float
    rms_energy_mean: float
    rms_energy_std: float
    dynamic_range_db: float
    harmonic_ratio: float
    percussive_ratio: float
    mfcc_means: list[float]
    chroma_means: list[float]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class AudioFeatureExtractor:
    """Extracts DSP features from audio waveforms."""

    def __init__(self, sample_rate: int = 22050, n_mfcc: int = 20):
        self.sample_rate = sample_rate
        self.n_mfcc = n_mfcc

    def extract_from_array(self, y: np.ndarray, sr: Optional[int] = None) -> AudioMetrics:
        """
        Extracts comprehensive acoustic metrics from a loaded audio array.
        Uses lazy import of librosa to allow lightweight imports.
        """
        import librosa

        sr = sr or self.sample_rate
        duration = float(len(y) / sr)

        # 1. Rhythm & Tempo
        onset_env = librosa.onset.onset_strength(y=y, sr=sr)
        tempo = float(librosa.feature.tempo(onset_envelope=onset_env, sr=sr)[0])

        # 2. Spectral Features
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
        spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr, roll_percent=0.85)
        spectral_flatness = librosa.feature.spectral_flatness(y=y)
        zcr = librosa.feature.zero_crossing_rate(y=y)

        # Spectral flux approximated via onset envelope
        spectral_flux_mean = float(np.mean(onset_env))

        # 3. Energy & Dynamics
        rms = librosa.feature.rms(y=y)[0]
        rms_mean = float(np.mean(rms))
        rms_std = float(np.std(rms))
        # Approximate dynamic range in decibels
        min_rms = max(float(np.min(rms[rms > 0])), 1e-6)
        max_rms = max(float(np.max(rms)), 1e-6)
        dynamic_range_db = float(20 * np.log10(max_rms / min_rms))

        # 4. Harmonic-Percussive Source Separation (HPSS)
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        harm_energy = float(np.sum(y_harmonic ** 2))
        perc_energy = float(np.sum(y_percussive ** 2))
        total_energy = max(harm_energy + perc_energy, 1e-6)
        harmonic_ratio = float(harm_energy / total_energy)
        percussive_ratio = float(perc_energy / total_energy)

        # 5. Timbre: 20-band MFCCs
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=self.n_mfcc)
        mfcc_means = [float(val) for val in np.mean(mfcc, axis=1)]

        # 6. Harmony: 12-pitch Chroma Energy
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_means = [float(val) for val in np.mean(chroma, axis=1)]

        return AudioMetrics(
            sample_rate=sr,
            duration_seconds=round(duration, 2),
            tempo_bpm=round(tempo, 1),
            spectral_centroid_mean=round(float(np.mean(spectral_centroid)), 2),
            spectral_centroid_std=round(float(np.std(spectral_centroid)), 2),
            spectral_rolloff_mean=round(float(np.mean(spectral_rolloff)), 2),
            spectral_rolloff_std=round(float(np.std(spectral_rolloff)), 2),
            spectral_flux_mean=round(spectral_flux_mean, 4),
            spectral_flatness_mean=round(float(np.mean(spectral_flatness)), 4),
            zero_crossing_rate_mean=round(float(np.mean(zcr)), 4),
            rms_energy_mean=round(rms_mean, 4),
            rms_energy_std=round(rms_std, 4),
            dynamic_range_db=round(dynamic_range_db, 2),
            harmonic_ratio=round(harmonic_ratio, 3),
            percussive_ratio=round(percussive_ratio, 3),
            mfcc_means=[round(x, 3) for x in mfcc_means],
            chroma_means=[round(x, 3) for x in chroma_means],
        )

    def extract_from_file(self, audio_path: str, max_duration: Optional[float] = 120.0) -> AudioMetrics:
        """Loads an audio file and extracts its acoustic feature metrics."""
        import librosa

        y, sr = librosa.load(audio_path, sr=self.sample_rate, duration=max_duration, mono=True)
        return self.extract_from_array(y, sr)
