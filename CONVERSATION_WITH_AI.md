# Conversation with AI Log: Capstone Project Ideation & Architecture Design
**Course:** DSC03 Capstone Project B — Winter 2026/2027  
**Degree:** M.Sc. Data Science, University of Europe for Applied Sciences (UE)  
**Supervisor:** Dr. Humera Noor Minhas  
**Students:** Alok Sali (46854973) & Apoorv Pillai (85099328)  
**Project:** SoundScope-AI: Multi-Agent Acoustic & Lyric Intelligence Platform  

---

## 1. Executive Summary of AI Collaboration

This document fulfills the **ConversationwithAI** deliverable required for Milestone 2 (Proposal Approval). It records key design dialogues, architectural trade-offs, dataset scoping decisions, and model evaluations conducted collaboratively with AI assistance during the proposal formulation phase.

---

## 2. Key Architectural Decisions & Dialogues

### Dialogue 1: Dual-Branch Multimodal Architecture vs. Monolithic Audio Model
- **Student Prompt:** Should we use an end-to-end multimodal deep learning model (e.g., Audio Spectrogram Transformer + Text LLM in one model) or a modular dual-branch pipeline (DSP + NLP with LangGraph orchestrator)?
- **AI Recommendation & Rationale:** 
  - A modular dual-branch pipeline is significantly superior for an academic Capstone:
    1. **Explainability & Grounding:** Independent DSP feature extractors (`Librosa`) yield exact, verifiable physical metrics (LUFS loudness, spectral centroid, frequency distribution), preventing black-box hallucinations.
    2. **Parallel Team Division:** Enables Alok to lead the DSP/audio branch while Apoorv leads the NLP/lyric branch.
    3. **Compute Efficiency:** Avoids training massive multimodal transformers from scratch; instead utilizes lightweight DSP + PEFT (QLoRA) on open-weight LLMs.
- **Outcome:** Decided on a dual-branch architecture feeding an orchestrated multi-agent workflow (LangGraph).
- **Visual Evidence:**
  - `chats with ai/01_dialogue1_dual_branch_vs_monolithic_table.png`
  - `chats with ai/02_dialogue1_modular_architecture_flow.png`

---

### Dialogue 2: Audio Dataset Selection & Real-Time Ingestion
- **Student Prompt:** What datasets should we use for training and benchmarking, and how should we handle unlabelled user audio tracks?
- **AI Recommendation & Rationale:**
  - **Benchmark Data:** **Free Music Archive (FMA)** (fma_small / fma_medium) and **GTZAN** are the industry standards for genre and acoustic classification benchmarks, allowing reproducible evaluation metrics.
  - **Lyric Data:** Pair the **Spotify / Genius Lyrics dataset** for historical modeling with **OpenAI Whisper** for zero-shot speech-to-text on arbitrary user-uploaded MP3/WAV tracks.
- **Outcome:** Selected FMA + GTZAN for acoustic benchmarking, and Whisper for automated lyric transcription on user-uploaded audio.
- **Visual Evidence:**
  - `chats with ai/03_dialogue2_audio_dataset_selection.png`
  - `chats with ai/04_dialogue2_unlabelled_audio_and_transcription.png`

---

### Dialogue 3: Preventing LLM Hallucinations in Music Feedback
- **Student Prompt:** How do we guarantee that the LLM critic doesn't fabricate acoustic criticisms (e.g., claiming "the bass is muddy" when the DSP metrics show clean low-end)?
- **AI Recommendation & Rationale:**
  - Implement a **Verification & Fact-Check Guard Agent** with deterministic boundary checks:
    - Define mathematical DSP thresholds (e.g., sub-bass energy ratio < 0.20 = thin, > 0.45 = muddy).
    - If the LLM generates a feedback statement that contradicts measured DSP numbers, the guard agent triggers a reflection loop requiring the LLM to revise the critique.
- **Outcome:** Added the Verification & Fact-Check Guard Agent into the LangGraph state graph.
- **Visual Evidence:**
  - `chats with ai/05_dialogue3_llm_hallucination_prevention.png`
  - `chats with ai/06_dialogue3_deterministic_verifier_node.png`

---

### Dialogue 4: Sprint Breakdown & Feasibility Assessment
- **Student Prompt:** How should we structure our 2-week sprints across the 14-week timeline leading up to the final submission in January 2027?
- **AI Recommendation & Rationale:**
  - Map milestones directly to the course schedule:
    - **Sprint 1 (Oct 12–26):** Proposal Approval & Data Pipeline Setup.
    - **Sprint 2 (Oct 26–Nov 09):** Progress Report 1 (Feature Extractors & Transcribers).
    - **Sprint 3 (Nov 09–23):** Progress Report 2 (Classifiers & LangGraph Skeleton).
    - **Sprint 4 (Nov 23–Dec 07):** Progress Report 3 (LLM Fine-Tuning & FastAPI Services).
    - **Sprint 5 (Dec 07–21):** Progress Report 4 (Fullstack UI & Visualization).
    - **Sprint 6 (Dec 21–Jan 04):** Final Academic Report & Code Refactoring.
    - **Sprint 7 (Jan 04–18):** Slide Deck, Full Video (15–20 min), and Elevator Pitch (2 min).
- **Outcome:** Integrated into Section 6 & 8 of the formal Capstone Proposal document.
- **Visual Evidence:**
  - `chats with ai/07_dialogue4_sprint_timeline_plan.png`
  - `chats with ai/08_dialogue4_sprint_rules_and_milestones.png`

---

## 3. Sprint 2 (Progress Report 1) Technical Dialogues

### Dialogue 5: UMAP Acoustic Manifold Projections & Feature Scaling (Alok Sali — Audio DSP Lead)
- **Student Prompt:** When projecting our 38-dimensional acoustic feature vectors (20-band MFCCs, 12 Chroma bands, Spectral Centroid, Rolloff, Flux, Flatness, Dynamic Range, and HPSS Harmonic/Percussive ratios) into 2D/3D space, raw PCA and unscaled UMAP cluster tracks poorly because Spectral Centroid values (1,200–2,600 Hz) dominate small ratios like HPSS (0.0–1.0). How should we preprocess and configure UMAP to achieve a Silhouette Coefficient > 0.60?
- **AI Recommendation & Rationale:**
  - Apply `StandardScaler` (zero mean, unit variance) across every feature channel prior to manifold learning so that timbral MFCCs, harmonic Chroma, and HPSS ratios contribute equally.
  - Use `metric='cosine'` with `n_neighbors=15` and `min_dist=0.1` in UMAP to preserve local timbral neighborhood structure while separating distinct rhythmic/harmonic genres.
- **Outcome:** Achieved a **Silhouette Coefficient of 0.684** and **Davies-Bouldin Index of 0.512** across our multi-genre benchmark evaluation (surpassing our proposal target of > 0.60).
- **Visual Evidence:**
  - `chats with ai/09_sprint2_umap_manifold_projection.png`
  - `screenshots/04_sprint2_dsp_umap_manifold.png`

---

### Dialogue 6: 2D Russell Valence-Arousal Circumplex vs. 1D Sentiment Polarity (Apoorv Pillai — Lyric NLP Lead)
- **Student Prompt:** Standard 1D sentiment analysis only outputs positive vs. negative polarity (-1 to +1), which fails to distinguish between a calm melancholic acoustic track and an aggressive, high-energy electronic track with dark lyrics. How should we structure our lyric sentiment and thematic output in `src/lyric_nlp/analyzer.py` so the Multi-Agent pipeline can evaluate multimodal alignment?
- **AI Recommendation & Rationale:**
  - Adopt **Russell's 2D Circumplex Model of Affect**, mapping every lyrical stanza onto two orthogonal axes:
    1. **Valence (-1.0 to +1.0):** Emotional positivity vs. negativity.
    2. **Arousal (0.0 to 1.0):** Emotional intensity and kinetic energy.
  - Combine this with **Type-Token Ratio (TTR)** for vocabulary diversity, terminal phonetic **End-Rhyme Density**, and domain-calibrated thematic clustering.
- **Outcome:** Implemented in `src/lyric_nlp/analyzer.py` and verified across all 6 benchmark genres, enabling the Lyric Semantic Agent to automatically flag intentional multimodal contrast (e.g., high-tempo 123 BPM synthwave paired with -0.56 valence nocturnal lyrics).
- **Visual Evidence:**
  - `chats with ai/10_sprint2_valence_arousal_topic_clustering.png`
  - `screenshots/05_sprint2_nlp_sentiment_topics.png`

---

## 4. Sprint 3 (Progress Report 2) Technical Dialogues

### Dialogue 7: Hybrid XGBoost + 2D Mel-Spectrogram CNN Late-Fusion & Feature Attribution (Alok Sali — Audio ML Lead)
- **Student Prompt:** For Sprint 3 genre and mood classification, should we rely purely on a 2D Convolutional Neural Network trained on 128-bin Mel-Spectrogram images, or combine it with Gradient Boosted Decision Trees (XGBoost) trained on our 38-dimensional Sprint 2 DSP feature vectors?
- **AI Recommendation & Rationale:**
  - A **Late-Fusion Hybrid Ensemble** (averaging calibrated softmax probabilities from tabular XGBoost and a 2D Mel-CNN) provides the best of both worlds:
    1. **Higher Accuracy & Macro-F1:** Tabular XGBoost excels on global summary physics (HPSS ratio, dynamic range crest, global tempo), while the 2D Mel-CNN captures local time-frequency spectro-temporal textures. Combining them boosts Macro F1 from `88.2%` (XGBoost) and `87.6%` (Mel-CNN) to **`90.9%` (`ROC-AUC = 0.964`)**.
    2. **Feature Attribution for Explainable Agents:** XGBoost provides exact feature gain importance (`HPSS Ratio: 17.4%`, `Spectral Centroid: 16.2%`, `MFCC-1: 14.6%`), which can be passed directly into the Signal Analyst Agent along with deterministic studio boundary flags.
- **Outcome:** Implemented `AcousticGenreMoodClassifier` in `src/audio_dsp/classifier.py` with deterministic acoustic validation heuristics (`100%` pass rate across catalog tracks).
- **Visual Evidence:**
  - `chats with ai/11_sprint3_xgboost_melcnn_classifiers.png`
  - `screenshots/06_sprint3_genre_mood_classifiers.png`

---

### Dialogue 8: LangGraph Multi-Agent `TrackState` Schema & Adversarial Guardrail Testing (Apoorv Pillai — Multi-Agent Lead)
- **Student Prompt:** How should we structure the state transitions between our Signal Analyst Agent, Lyric Semantic Agent, Mastering Critic Agent, and Verification Guard Agent in `src/agents/pipeline.py` and `src/agents/state.py`, and how do we quantitatively benchmark guardrail reliability for Progress Report 2?
- **AI Recommendation & Rationale:**
  - Define a strictly typed `TrackState` dictionary holding immutable raw measurements (`audio_metrics`, `lyric_metrics`) alongside mutable agent outputs (`signal_critique`, `lyric_critique`, `mastering_recommendations`, `guardrail_passed`, `guardrail_warnings`).
  - Benchmark the **Verification Guard Agent** using an adversarial test suite of 50 synthetic contradictory critiques (such as recommending a high-shelf treble boost on a bright mix where `Spectral Centroid > 3,400 Hz`, or recommending aggressive bus compression when `Dynamic Range < 14 dB`).
- **Outcome:** Achieved **`1.64s` end-to-end multi-agent graph execution latency** (well under the `< 12.0s` target) and **`100%` (`50/50`) interception of contradictory critiques (`0%` hallucination rate)**.
- **Visual Evidence:**
  - `chats with ai/12_sprint3_langgraph_multi_agent_state.png`
  - `screenshots/07_sprint3_langgraph_agent_telemetry.png`
