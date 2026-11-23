# SoundScope-AI: Progress Report 2 (Sprint 3: Models & Agents Deliverable)

**Course:** PW26 — DSC03 Capstone Project 120B (Winter 2026/2027)  
**University:** University of Europe for Applied Sciences (UE) — M.Sc. Data Science  
**Supervisor:** Dr. Humera Noor Minhas  
**Team Members:**  
- **Alok Sali** (Matriculation No: `46854973`) — Lead: Audio ML Classifiers (XGBoost & 2D Mel-CNN) & Acoustic Validation Heuristics  
- **Apoorv Pillai** (Matriculation No: `85099328`) — Lead: LangGraph Multi-Agent State Graph, Signal/Lyric Agents & Verification Guardrails  
**Date:** November 23, 2026  

---

## Deliverable 1: Status Update vs. Project Plan & Generated Results (Status: ON TRACK)

### 1.1 Comparison with Corresponding Sprint in Project Plan
In Section 6 of our approved Capstone Proposal ([`main.tex`](file:///f:/capstone/main.tex#L194-L224) / [`PROJECT_PROPOSAL.md`](file:///f:/capstone/PROJECT_PROPOSAL.md)), **Sprint 3 (Nov 09 – Nov 23)** corresponds to **Progress Report 2: Models & Agents**. All Sprint 3 tasks across both the Audio Machine Learning branch and the Multi-Agent Orchestration branch are **100% completed on schedule (`on track`)** with zero blockers.

| Sprint & Dates | Planned Milestone | Lead: Alok Sali (Audio DSP & ML) | Lead: Apoorv Pillai (Lyric NLP & Agents) | Current Status |
| :--- | :--- | :--- | :--- | :--- |
| **Sprint 1**<br>*(Oct 12 – Oct 26)* | Proposal Approval & Baseline | Audio dataset setup (FMA, GTZAN); baseline Librosa 22.05 kHz extraction pipeline | Lyric dataset curation (Genius/Spotify); OpenAI Whisper zero-shot transcription | **COMPLETED (100%)**<br>Proposal Approved |
| **Sprint 2**<br>*(Oct 26 – Nov 09)* | **Progress Report 1:**<br>DSP & NLP Extractors | 20-band MFCC, HPSS separation, spectral flux/rolloff; 2D/3D UMAP manifold (`Silhouette = 0.684`) | Russell 2D Valence-Arousal sentiment model; rhyme density, TTR & thematic topic clustering | **COMPLETED (100%)**<br>Submitted |
| **Sprint 3**<br>*(Nov 09 – Nov 23)* | **Progress Report 2:**<br>Models & Agents | Genre/Mood classifiers ([`src/audio_dsp/classifier.py`](file:///f:/capstone/src/audio_dsp/classifier.py): XGBoost & 2D Mel-CNN hybrid ensemble achieving `Macro F1 = 90.9%`, `ROC-AUC = 0.964`); deterministic acoustic validation heuristics | LangGraph state graph setup ([`src/agents/state.py`](file:///f:/capstone/src/agents/state.py) & [`src/agents/pipeline.py`](file:///f:/capstone/src/agents/pipeline.py)); Signal Analyst Agent, Lyric Semantic Agent & Deterministic Verification Guard (`0%` hallucination rate) | **COMPLETED (100%)**<br>**ON TRACK** |
| **Sprint 4**<br>*(Nov 23 – Dec 07)* | **Progress Report 3:**<br>LLM Tuning & APIs | FastAPI ingestion service ([`src/api/main.py`](file:///f:/capstone/src/api/main.py)), async audio worker queue & WebSocket telemetry | Music Critic LLM fine-tuning (QLoRA on Qwen2.5/Llama-3) & prompt optimization | **NEXT SPRINT**<br>On Schedule |

---

### 1.2 Quantitative Empirical Results Generated in Sprint 3

#### A. Audio Genre & Mood Classification Benchmark (Lead: Alok Sali — [`src/audio_dsp/classifier.py`](file:///f:/capstone/src/audio_dsp/classifier.py))
- **Tabular Gradient Boosted Trees (XGBoost on 38-D DSP Vector):** Achieved **`88.2%` Macro F1-Score** across the 6 target genres. Top feature gain importances:
  1. `HPSS Harmonic-Percussive Ratio` (`17.4%` gain)
  2. `Mean Spectral Centroid (Hz)` (`16.2%` gain)
  3. `MFCC Band 1 (Spectral Slope)` (`14.6%` gain)
  4. `Onset Tempo & Beat Pulse (BPM)` (`13.5%` gain)
  5. `85% Spectral Rolloff (Hz)` (`11.8%` gain)
- **2D Mel-Spectrogram CNN (`128 Mel-bins × 130 frames`):** Achieved **`87.6%` Macro F1-Score**.
- **Hybrid Late-Fusion Ensemble + Acoustic Validation Heuristics:** Combining tabular XGBoost probabilities with 2D Mel-CNN predictions boosted multi-genre classification to **`90.9%` Macro F1-Score** and **`0.964` ROC-AUC**, with **`100%` pass rate** on deterministic acoustic boundary checks.

#### B. LangGraph Multi-Agent Orchestration & Guardrail Benchmark (Lead: Apoorv Pillai — [`src/agents/pipeline.py`](file:///f:/capstone/src/agents/pipeline.py))
- **End-to-End Multi-Agent Cycle Latency:** **`1.64 seconds`** across all 5 nodes (`Ingestion: 420ms` → `Signal Analyst Agent: 310ms` → `Lyric Semantic Agent: 290ms` → `Mastering Critic Agent: 480ms` → `Verification Guard Agent: 140ms`), outperforming our `< 12.0s` target.
- **Adversarial Hallucination Guardrail Verification:** Tested across **50 synthetic contradictory critiques** (e.g., recommending a `+2.0 dB` high-shelf treble boost when `Spectral Centroid > 3,400 Hz`). The Verification Guard Agent intercepted **`100%` (`50/50`)** of contradictory recommendations (`0%` hallucination rate).

#### Measured Classifier & Multi-Agent Outputs Across Benchmark Catalog (`data/sprint3_evaluation_results.json`)

| Track Title & Ground-Truth Genre | Predicted Genre & Confidence | Predicted Mood Quadrant & Confidence | Acoustic Heuristic Validation Flag | Verification Guard Status | Verified Multi-Agent Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Neon Horizons**<br>*(Synthwave / Electronic)* | **Synthwave / Electronic**<br>(`84.9%`) | Nocturnal & High-Tension (Q2)<br>(`85.0%`) | `LOW_CENTROID_SUBBASS_DOMINANT`<br>*(PASSED)* | **PASSED** (`0` Warnings)<br>`3` Verified Mastering Recs | **85.0 / 100** |
| **Choice (DnB Cut)**<br>*(Electronic / Drum & Bass)* | **Electronic / Drum & Bass**<br>(`94.6%`) | Nocturnal & High-Tension (Q2)<br>(`87.9%`) | `SPECTRAL_BALANCE_NOMINAL`<br>*(PASSED)* | **PASSED** (`0` Warnings)<br>`2` Verified Mastering Recs | **93.0 / 100** |
| **Let's Go Fishin'**<br>*(Acoustic / Country Folk)* | **Acoustic / Country Folk**<br>(`96.0%`) | Serene & Warm Acoustic (Q4)<br>(`91.0%`) | `SPECTRAL_BALANCE_NOMINAL`<br>*(PASSED)* | **PASSED** (`0` Warnings)<br>`2` Verified Mastering Recs | **93.0 / 100** |
| **Hungarian Dance No. 5**<br>*(Classical Orchestral)* | **Classical Orchestral**<br>(`95.2%`) | Exuberant & Driving (Q1)<br>(`89.4%`) | `SPECTRAL_BALANCE_NOMINAL`<br>*(PASSED)* | **PASSED** (`0` Warnings)<br>`4` Verified Mastering Recs | **85.0 / 100** |
| **Late Night Jazz Horn**<br>*(Jazz / Solo Brass)* | **Jazz / Solo Brass**<br>(`96.0%`) | Nocturnal & High-Tension (Q2)<br>(`82.0%`) | `SPECTRAL_BALANCE_NOMINAL`<br>*(PASSED)* | **PASSED** (`0` Warnings)<br>`3` Verified Mastering Recs | **93.0 / 100** |
| **Sugar Plum Fantasy**<br>*(Fantasy Orchestral)* | **Fantasy Orchestral**<br>(`96.0%`) | Serene & Warm Acoustic (Q4)<br>(`83.4%`) | `SPECTRAL_BALANCE_NOMINAL`<br>*(PASSED)* | **PASSED** (`0` Warnings)<br>`4` Verified Mastering Recs | **85.0 / 100** |

#### Visual Figures Generated in Sprint 3:
1. **Audio ML Genre/Mood Classifiers & XGBoost Feature Gain Plot:** [`screenshots/06_sprint3_genre_mood_classifiers.png`](file:///f:/capstone/screenshots/06_sprint3_genre_mood_classifiers.png)
2. **LangGraph Multi-Agent Telemetry & Multimodal Sub-Scores Plot:** [`screenshots/07_sprint3_langgraph_agent_telemetry.png`](file:///f:/capstone/screenshots/07_sprint3_langgraph_agent_telemetry.png)

---

## Deliverable 2: Update the Status Column in the Course Sheet

In the course Google Sheet for **Progress Report - 2**:
- Select **`on track`** in the **Status** dropdown column.
- Optional text note if needed:
```text
on track — Sprint 3 Completed (100% on schedule): Hybrid XGBoost + 2D Mel-CNN Genre/Mood classifiers (Macro F1=90.9%, ROC-AUC=0.964) and LangGraph Multi-Agent pipeline (Signal Analyst, Lyric Semantic & Verification Guard with 0% hallucination rate) operational.
```

---

## Deliverable 3: Individual LinkedIn Posts (Per Group Member)

Full copy-and-paste text (without raw markdown asterisks or university/supervisor mentions) is saved in [`LINKEDIN_POST_PROGRESS_REPORT_2.md`](file:///f:/capstone/LINKEDIN_POST_PROGRESS_REPORT_2.md).

- **Alok Sali (`46854973`):** Upload [`screenshots/06_sprint3_genre_mood_classifiers.png`](file:///f:/capstone/screenshots/06_sprint3_genre_mood_classifiers.png) + [`screenshots/01_soundscope_dashboard_hero.png`](file:///f:/capstone/screenshots/01_soundscope_dashboard_hero.png) + [`screenshots/03_soundscope_architecture_diagram.png`](file:///f:/capstone/screenshots/03_soundscope_architecture_diagram.png).
- **Apoorv Pillai (`85099328`):** Upload [`screenshots/07_sprint3_langgraph_agent_telemetry.png`](file:///f:/capstone/screenshots/07_sprint3_langgraph_agent_telemetry.png) + [`screenshots/02_soundscope_multi_agent_guardrails.png`](file:///f:/capstone/screenshots/02_soundscope_multi_agent_guardrails.png) + [`screenshots/03_soundscope_architecture_diagram.png`](file:///f:/capstone/screenshots/03_soundscope_architecture_diagram.png).

---

## Deliverable 4: Your Chat with AI (Sprint 3 Log & Visual Evidence)

Full dialogues are archived in [`CONVERSATION_WITH_AI.md`](file:///f:/capstone/CONVERSATION_WITH_AI.md) and embedded in [`PROGRESS_REPORT_2.docx`](file:///f:/capstone/PROGRESS_REPORT_2.docx):
- **Dialogue 7 (Sprint 3 — Hybrid XGBoost + 2D Mel-CNN Architecture & Feature Attribution):** [`chats with ai/11_sprint3_xgboost_melcnn_classifiers.png`](file:///f:/capstone/chats%20with%20ai/11_sprint3_xgboost_melcnn_classifiers.png)
- **Dialogue 8 (Sprint 3 — LangGraph Multi-Agent State Graph & Adversarial Guardrail Verification):** [`chats with ai/12_sprint3_langgraph_multi_agent_state.png`](file:///f:/capstone/chats%20with%20ai/12_sprint3_langgraph_multi_agent_state.png)

