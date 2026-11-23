# SoundScope-AI — Progress Report 1 LinkedIn Posts (Individual per Group Member)

> [!IMPORTANT]
> **Dr. Humera's Requirement (#3):**  
> *"LinkedIn post (individually per group member)"*  
> Below are two distinct, ready-to-copy-and-paste LinkedIn posts written in a clean, professional engineering tone (without university, course, supervisor, or capstone approval mentions):
> - **Post 1 — Alok Sali:** Focuses on the **Audio DSP & Manifold Learning Branch** (20-band MFCCs, Harmonic-Percussive Source Separation, Spectral Centroid/Rolloff/Flux, and 2D/3D UMAP acoustic manifold projections).
> - **Post 2 — Apoorv Pillai:** Focuses on the **Lyric & Poetic NLP Branch** (Whisper speech-to-text transcription, Russell's Valence-Arousal emotional trajectory modeling, phonetic rhyme density, and thematic clustering).

> [!TIP]
> **Formatting & Images to Attach:**
> - All raw markdown asterisks (`**`) have been removed so you can copy (`Ctrl + C`) and paste (`Ctrl + V`) directly into LinkedIn cleanly.
> - **For Alok Sali's Post, attach:**
>   1. `F:\capstone\screenshots\04_sprint2_dsp_umap_manifold.png` (2D UMAP Acoustic Manifold & HPSS Source Separation Chart)
>   2. `F:\capstone\screenshots\01_soundscope_dashboard_hero.png` (SoundScope-AI Studio UI)
>   3. `F:\capstone\screenshots\03_soundscope_architecture_diagram.png` (System Architecture Diagram)
> - **For Apoorv Pillai's Post, attach:**
>   1. `F:\capstone\screenshots\05_sprint2_nlp_sentiment_topics.png` (Valence-Arousal Circumplex Plane & Poetic NLP Metrics Chart)
>   2. `F:\capstone\screenshots\02_soundscope_multi_agent_guardrails.png` (Multi-Agent Critique & Verification Guardrails)
>   3. `F:\capstone\screenshots\03_soundscope_architecture_diagram.png` (System Architecture Diagram)

---

## ▸ Post 1: Alok Sali (Focus: Audio DSP & Acoustic Manifold Learning)

```text
From Raw Audio Waveforms to 2D/3D Acoustic Manifolds in SoundScope-AI!

While building the latest milestone of SoundScope-AI — an orchestrated multi-agent acoustic and lyric intelligence platform — my focus on the Audio Digital Signal Processing (DSP) pipeline was to solve a core problem in music AI: how do we translate raw 22.05 kHz audio waveforms into mathematically verifiable acoustic fingerprints that prevent LLM hallucinations?

Here is what we engineered and benchmarked in this phase:

[01] 20-Band MFCC & Spectral Fingerprinting
Using Librosa, our extraction engine computes 20 Mel-Frequency Cepstral Coefficients (MFCCs) alongside spectral centroid, 85% spectral rolloff, spectral flatness, and onset-driven spectral flux across multi-genre benchmark tracks (Free Music Archive & GTZAN).

[02] Harmonic-Percussive Source Separation (HPSS)
By decomposing each waveform into harmonic and percussive components, we quantify arrangement balance directly from signal energy — for example, separating Classical Orchestral tracks (93% harmonic energy, 1,687 Hz mean centroid) from high-tempo Electronic Drum & Bass cuts (31% percussive energy, 136 BPM).

[03] UMAP Acoustic Manifold Projections
Projecting our 38-dimensional feature vectors (20 MFCCs + 12 Chroma + HPSS + Spectral moments) into a 2D/3D UMAP manifold yielded clear genre cluster separation with a Silhouette Coefficient of 0.684 and a Davies-Bouldin Index of 0.512.

[04] Deterministic Verification Guardrails
Every DSP measurement feeds directly into our LangGraph Verification Guard Agent, ensuring 0% of generated mastering recommendations contradict the underlying audio physics.

Next up: Training our XGBoost & 2D Mel-Spectrogram CNN genre/mood classifiers and expanding the multi-agent orchestration!

To audio engineers, MIR researchers, and data scientists: Which spectral or time-domain features have you found most informative when clustering cross-genre audio?

#DataScience #AudioDSP #MusicInformationRetrieval #MachineLearning #Python #Librosa #UMAP #MultimodalAI #LangGraph #SoundScopeAI
```

---

## ▸ Post 2: Apoorv Pillai (Focus: Lyric NLP, Sentiment & Topic Modeling)

```text
Mapping the Emotional & Poetic DNA of Song Lyrics in SoundScope-AI!

As part of our latest development sprint on SoundScope-AI — a dual-branch acoustic and lyric intelligence platform — my focus has been leading the Natural Language Processing (NLP) pipeline: capturing emotional trajectories, phonetic cadence, and thematic structures from song lyrics and aligning them with the physical audio signal.

Key NLP capabilities we built and benchmarked in this milestone:

[01] Zero-Shot Audio-to-Lyric Transcription Pipeline
Integrated OpenAI Whisper with lyric catalog normalization (Genius / Spotify benchmark subsets) to automatically transcribe and segment unlabelled MP3/WAV uploads into structured verse/chorus stanzas.

[02] Russell's Valence-Arousal Circumplex Modeling
Instead of flat positive/negative sentiment labels, we mapped lyrical stanzas onto a continuous 2D Valence-Arousal plane (Valence: -1.0 to +1.0 positivity; Arousal: 0.0 to 1.0 intensity). This allows our system to detect intentional multimodal tension — such as pairing melancholic lyrics (-0.56 valence) with an energetic 123 BPM synthwave arrangement.

[03] Poetic Meter & Vocabulary Richness Quantification
Built automated extractors for Type-Token Ratio (vocabulary diversity, ranging from 0.82 to 0.96 across benchmark genres), stanza line-length cadence, and terminal end-rhyme density.

[04] Thematic Topic Clustering & Multi-Agent Grounding
Categorized lyrical narratives into interpretable thematic domains (Pastoral Serenity, High-Octane Kinetic Energy, Nocturnal Synth, Dramatic Grandeur) that feed into our LangGraph Lyric Semantic Agent for explainable artist feedback.

Next up: Connecting our Lyric Semantic Agent and Signal Analyst Agent into the full LangGraph state graph alongside deep acoustic classifiers!

Question for NLP practitioners and music tech enthusiasts: How do you handle figurative language and metaphor when modeling sentiment in creative text like song lyrics?

#NLP #DataScience #MachineLearning #MusicTech #SentimentAnalysis #Whisper #LangGraph #MultimodalAI #Python #SoundScopeAI
```
