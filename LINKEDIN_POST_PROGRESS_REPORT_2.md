# SoundScope-AI — Progress Report 2 LinkedIn Posts (Sprint 3: Models & Agents)

> [!IMPORTANT]
> **Dr. Humera's Requirement (#3):**  
> *"LinkedIn post (individually per group member)"*  
> Below are two distinct, ready-to-copy-and-paste LinkedIn posts written in a clean, professional industry tone (without university, course, supervisor, or team member mentions):
> - **Post 1 — Alok Sali:** Focuses on **Audio Machine Learning Classifiers & Validation Heuristics** (Tabular XGBoost on 38-D DSP vectors, 2D Mel-Spectrogram CNN late-fusion ensemble achieving `90.9% Macro F1` & `0.964 ROC-AUC`, feature gain attribution, and deterministic studio boundary rules).
> - **Post 2 — Apoorv Pillai:** Focuses on **LangGraph Multi-Agent Orchestration & Guardrail Verification** (`TrackState` state graph, Acoustic Signal Analyst Agent, Lyric Semantic Agent, cross-modal tension/synergy detection, and Deterministic Verification Guardrail with `0% hallucination rate`).

> [!TIP]
> **Formatting & Images to Attach:**
> - All raw markdown asterisks (`**`) have been removed so you can copy (`Ctrl + C`) and paste (`Ctrl + V`) directly into LinkedIn cleanly.
> - **For Alok Sali's Post, attach:**
>   1. `F:\capstone\screenshots\06_sprint3_genre_mood_classifiers.png` (Main Cover: XGBoost vs. 2D Mel-CNN Macro-F1 Benchmark & Acoustic Feature Gain Importance)
>   2. `F:\capstone\screenshots\01_soundscope_dashboard_hero.png` (SoundScope-AI Studio UI)
>   3. `F:\capstone\screenshots\03_soundscope_architecture_diagram.png` (System Architecture Diagram)
> - **For Apoorv Pillai's Post, attach:**
>   1. `F:\capstone\screenshots\07_sprint3_langgraph_agent_telemetry.png` (Main Cover: LangGraph Multi-Agent Node Latency/Faithfulness Telemetry & Multimodal Sub-Scores)
>   2. `F:\capstone\screenshots\02_soundscope_multi_agent_guardrails.png` (Multi-Agent Critique & Verification Guardrails UI)
>   3. `F:\capstone\screenshots\03_soundscope_architecture_diagram.png` (System Architecture Diagram)

---

## ▸ Post 1: Alok Sali (Focus: XGBoost & 2D Mel-CNN Audio Classifiers + Heuristic Validation)

```text
Teaching Machines to Hear Genre, Mood, and Mix Balance: Hybrid Audio Classification in SoundScope-AI!

In our latest engineering milestone for SoundScope-AI — an orchestrated multi-agent acoustic and lyric intelligence platform — my focus shifted from raw Digital Signal Processing (DSP) extraction to supervised Audio Machine Learning and deterministic mix validation.

A common pitfall in music classification is relying solely on black-box spectrograms or solely on summary statistics. To solve this, we benchmarked a hybrid classification and heuristic validation architecture:

[01] Tabular Gradient Boosted Trees (XGBoost on 38-D DSP Vectors)
Trained on 20-band MFCCs, 12-band Chroma pitch energy, HPSS harmonic-percussive ratios, spectral centroid/rolloff/flux, and dynamic crest factor, achieving an 88.2% Macro F1-score across multi-genre benchmarks.

[02] 2D Mel-Spectrogram CNN & Late-Fusion Ensemble
Combining time-frequency 2D Mel-CNN representations (87.6% Macro F1) with our tabular XGBoost model via probability late-fusion boosted overall multi-genre Macro F1 to 90.9% (ROC-AUC: 0.964).

[03] Feature Attribution & Signal Explainability
Gain importance analysis revealed that HPSS Harmonic-Percussive Ratio (17.4%), Mean Spectral Centroid (16.2%), and MFCC Band 1 Spectral Slope (14.6%) carry the strongest discriminative power across genres.

[04] Deterministic Acoustic Validation Heuristics
Implemented programmatic studio boundary rules (sub-bass dominance, 6-8 kHz sibilance risk, and <14 dB hyper-compression flags) that gate downstream LLM mastering critiques.

Next up: Exposing our classification and multi-agent pipeline through high-throughput FastAPI streaming endpoints and fine-tuning our Mastering Critic LLM!

To ML engineers and audio researchers: When working with audio data, do you prefer end-to-end spectrogram CNNs/Transformers, tabular DSP feature boosting, or hybrid ensembles?

#MachineLearning #AudioML #DataScience #XGBoost #DeepLearning #MusicInformationRetrieval #Python #AudioDSP #MultimodalAI #SoundScopeAI
```

---

## ▸ Post 2: Apoorv Pillai (Focus: LangGraph Multi-Agent State Graph & Verification Guardrails)

```text
Orchestrating Domain-Specialized Audio & Lyric Agents with Zero Hallucinations in SoundScope-AI!

General-purpose LLMs struggle when asked to critique music production: without grounding in physical signal metrics, they frequently hallucinate studio advice (like suggesting a treble boost on an already bright mix).

In our latest milestone on SoundScope-AI, I led the design and implementation of our stateful LangGraph Multi-Agent Orchestration pipeline to bridge low-level signal physics and poetic semantics into verified studio feedback:

[01] Typed Multi-Agent State Graph (TrackState)
Engineered a structured state graph coordinating five sequential execution nodes with an end-to-end latency of 1.64 seconds per track.

[02] Acoustic Signal Analyst & Lyric Semantic Agents
The Signal Analyst translates spectral centroid, dynamic crest, and HPSS ratios into mix assessments, while the Lyric Semantic Agent evaluates rhyme cadence, Type-Token Ratio, and 2D Valence-Arousal alignment.

[03] Cross-Modal Synergy & Tension Detection
Our orchestration layer cross-examines acoustic tempo/energy against lyrical valence — distinguishing between cohesive pastoral arrangements and intentional dramatic contrast (e.g., high-BPM electronic beats paired with nocturnal lyrics).

[04] Deterministic Verification Guardrail Agent
Before any mastering recommendation reaches the user, the Verification Guard cross-checks the critique against ground-truth DSP measurements, intercepting 100% of contradictory statements across 50 adversarial test cases.

Next up: Fine-tuning our open-weight Music Critic LLM with QLoRA and integrating real-time API streaming!

Question for AI engineers building agentic workflows: What guardrail patterns have you found most effective for keeping LLM agents grounded in deterministic numerical data?

#LangGraph #MultiAgentSystems #LLM #NLP #AIAgents #DataScience #MachineLearning #MusicTech #Python #SoundScopeAI
```

