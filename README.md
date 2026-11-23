# SoundScope-AI: Multi-Agent Acoustic & Lyric Intelligence Platform

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green.svg)](https://fastapi.tiangolo.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-orange.svg)](https://langchain-ai.github.io/langgraph/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Author:** [Alok Sali](https://github.com/aloksali)  

---

## 📌 Overview

**SoundScope-AI** is a multimodal music intelligence platform uniting **Digital Signal Processing (DSP)**, **Natural Language Processing (NLP)**, and **Multi-Agent Orchestration (LangGraph)**.

Existing music analytics tools operate in silos: DSP tools output raw numbers without artistic context, while recommendation systems rely on shallow metadata. SoundScope-AI bridges this gap by evaluating audio mix balance, tempo, frequency spectrum, genre, emotional mood, and lyrical themes to provide explainable, studio-grade production and mastering reviews.

```
                              ┌────────────────────────┐
                              │ User Audio (MP3 / WAV) │
                              └───────────┬────────────┘
                                          │
                    ┌─────────────────────┴─────────────────────┐
                    ▼                                           ▼
      ┌───────────────────────────┐               ┌───────────────────────────┐
      │  Acoustic Signal (DSP)    │               │    Lyric & NLP Branch     │
      │  - 20-band MFCCs          │               │  - Whisper Speech-to-Text │
      │  - Spectral Moments       │               │  - Sentiment Valence/Arc  │
      │  - HPSS & Tempogram (BPM) │               │  - Rhyme & Meter Analysis │
      │  - UMAP 3D Cluster Map    │               │  - BERTopic Thematic Mod. │
      └─────────────┬─────────────┘               └─────────────┬─────────────┘
                    │                                           │
                    └─────────────────────┬─────────────────────┘
                                          ▼
                      ┌───────────────────────────────────────┐
                      │    LangGraph Multi-Agent Pipeline     │
                      │  - Signal Analyst Agent               │
                      │  - Lyric Semantic Agent               │
                      │  - Mastering Critic Agent (LoRA LLM)  │
                      │  - Verification & Guard Agent         │
                      └───────────────────┬───────────────────┘
                                          ▼
                      ┌───────────────────────────────────────┐
                      │ Fullstack Dashboard & Visual Insights │
                      │  - Wavesurfer.js Audio Player         │
                      │  - 3D UMAP Genre & Mood Explorer      │
                      │  - Explainable Mastering Report       │
                      └───────────────────────────────────────┘
```

---

## ✨ Key Features

- **Dual-Branch Processing:** Simultaneous acoustic signal analysis via Librosa/Essentia and lyric intelligence via Whisper and NLP models.
- **20-Band Acoustic Fingerprinting:** Computes MFCCs, spectral centroid, rolloff, flux, flatness, dynamic range (dB), and harmonic-percussive separation (HPSS).
- **Poetic & Sentiment Analysis:** Evaluates rhyme density, vocabulary richness (type-token ratio), and valence-arousal emotional trajectories across song sections.
- **Orchestrated Multi-Agent Architecture:** Powered by LangGraph with specialized domain agents providing structured production critiques.
- **Hallucination Guardrails:** Verification agent mathematically checks LLM recommendations against measured DSP physics to eliminate factual hallucinations.
- **High-Dimensional Manifold Learning:** 2D and 3D UMAP / PCA projections for acoustic clustering and song similarity mapping.

---

## 🛠️ Architecture & Tech Stack

| Domain | Frameworks & Technologies |
|---|---|
| **Audio DSP & MIR** | `librosa`, `essentia`, `scipy`, `soundfile`, `numpy` |
| **NLP & Speech-to-Text** | `openai-whisper`, `transformers` (RoBERTa), `bertopic`, `nltk` |
| **Agent Pipelines** | `langgraph`, `langchain-core` |
| **LLM & Fine-Tuning** | `qwen2.5` / `llama-3`, `unsloth`, `peft`, `bitsandbytes` |
| **Machine Learning** | `scikit-learn`, `xgboost`, `umap-learn`, `pytorch` |
| **Backend & API** | `fastapi`, `uvicorn`, `pydantic`, `celery`, `redis` |
| **Frontend UI** | `react`, `vite`, `wavesurfer.js`, `plotly.js` |

---

## 📂 Repository Layout

```
├── src/
│   ├── audio_dsp/       # Acoustic feature extraction (MFCC, HPSS, spectral moments)
│   ├── lyric_nlp/       # Whisper transcription, sentiment arcs, rhyme density
│   ├── models/          # Genre/mood classifiers & UMAP embedding pipelines
│   ├── agents/          # LangGraph multi-agent orchestration & state definitions
│   ├── api/             # FastAPI asynchronous backend endpoints
│   └── web/             # Fullstack web interface
├── data/
│   ├── raw/             # Raw audio & lyric datasets (FMA, GTZAN, Genius)
│   ├── processed/       # Extracted acoustic features & embeddings
│   └── samples/         # Test audio tracks
├── notebooks/           # Exploratory signal analysis and model experimentation
├── tests/               # Unit and integration test suites
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🚀 Quickstart

### 1. Clone & Set Up Environment
```bash
git clone https://github.com/aloksali/SoundScope-AI.git
cd SoundScope-AI

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run Baseline Extraction
```python
from src.audio_dsp import AudioFeatureExtractor
from src.lyric_nlp import LyricAnalyzer

# Extract acoustic features
extractor = AudioFeatureExtractor()
metrics = extractor.extract_from_file("path/to/song.mp3")
print(metrics.to_dict())

# Analyze lyrics
analyzer = LyricAnalyzer()
lyrics_data = analyzer.analyze_text("Your song lyric text here...")
print(lyrics_data.to_dict())
```

### 3. Run Unit Tests
```bash
pytest tests/
```

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
