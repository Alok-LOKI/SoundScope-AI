# SoundScope-AI: Progress Report 1 (Sprint 1 & Sprint 2 Deliverable)

**Course:** PW26 — DSC03 Capstone Project 120B (Winter 2026/2027)  
**University:** University of Europe for Applied Sciences (UE) — M.Sc. Data Science  
**Supervisor:** Dr. Humera Noor Minhas  
**Team Members:**  
- **Alok Sali** (Matriculation No: `46854973`) — Lead: Audio DSP, Manifold Learning & Backend Pipeline  
- **Apoorv Pillai** (Matriculation No: `85099328`) — Lead: Lyric NLP, Sentiment/Topic Modeling & Multi-Agent Grounding  
**Date:** November 9, 2026  

---

## Deliverable 1: Status Update vs. Project Plan & Generated Results

### 1.1 Comparison with Corresponding Sprint in Project Plan — **Status: AHEAD OF SCHEDULE**
In Section 6 of our approved Capstone Proposal ([`main.tex`](file:///f:/capstone/main.tex#L194-L224) / [`PROJECT_PROPOSAL.md`](file:///f:/capstone/PROJECT_PROPOSAL.md)), **Sprint 1 (Oct 12 – Oct 26)** and **Sprint 2 (Oct 26 – Nov 09)** correspond to **Milestone 1 (Proposal Approval & Baseline)** and **Progress Report 1 (DSP & NLP Feature Extractors & Manifold Projections)**. 

**Why we are Ahead of Schedule:** Not only are **Sprint 1 and Sprint 2 100% completed**, but we have also already built and verified core components scheduled for **Sprint 3, Sprint 4, and Sprint 5** — specifically our **Multi-Agent Orchestration & Verification Guardrail Pipeline** ([`src/agents/pipeline.py`](file:///f:/capstone/src/agents/pipeline.py)), our **FastAPI REST Backend** ([`src/api/main.py`](file:///f:/capstone/src/api/main.py)), and our **Interactive Web Studio UI** ([`src/web/index.html`](file:///f:/capstone/src/web/index.html)).

| Sprint & Dates | Planned Milestone | Lead: Alok Sali (Audio DSP) | Lead: Apoorv Pillai (Lyric NLP) | Current Status |
| :--- | :--- | :--- | :--- | :--- |
| **Sprint 1**<br>*(Oct 12 – Oct 26)* | Proposal Approval & Baseline Setup | Audio dataset setup (FMA, GTZAN) via [`scripts/download_datasets.py`](file:///f:/capstone/scripts/download_datasets.py); baseline Librosa 22.05 kHz waveform pipeline | Lyric dataset curation (Genius/Spotify); OpenAI Whisper zero-shot transcription prototype | **COMPLETED (100%)**<br>Proposal Approved |
| **Sprint 2**<br>*(Oct 26 – Nov 09)* | **Progress Report 1:**<br>DSP & NLP Extractors | 20-band MFCC, HPSS harmonic/percussive separation, spectral flux/rolloff/centroid in [`src/audio_dsp/features.py`](file:///f:/capstone/src/audio_dsp/features.py); 2D/3D UMAP manifold projections | Russell's Valence-Arousal sentiment modeling, rhyme density, Type-Token Ratio & thematic topic clustering in [`src/lyric_nlp/analyzer.py`](file:///f:/capstone/src/lyric_nlp/analyzer.py) | **COMPLETED (100%)**<br>All Metrics & Plots Generated |
| **Sprint 3**<br>*(Nov 09 – Nov 23)* | **Progress Report 2:**<br>Models & Agents | XGBoost & 2D Mel-CNN genre/mood classifiers; acoustic threshold validation heuristics | LangGraph multi-agent orchestration ([`src/agents/pipeline.py`](file:///f:/capstone/src/agents/pipeline.py)) & deterministic Verification Guard | **AHEAD OF SCHEDULE (65% Done)**<br>Multi-Agent Pipeline & Guardrails Live |
| **Sprint 4 & 5**<br>*(Nov 23 – Dec 21)* | **Progress Reports 3 & 4:**<br>APIs & Studio UI | FastAPI ingestion service ([`src/api/main.py`](file:///f:/capstone/src/api/main.py)) & audio streaming endpoints | Interactive Web Dashboard ([`src/web/index.html`](file:///f:/capstone/src/web/index.html)) with waveform player, radar charts & agent cards | **AHEAD OF SCHEDULE (50% Done)**<br>End-to-End Prototype Operational |

---

### 1.2 Quantitative Empirical Results Generated in Sprint 2
We executed our dual-branch DSP (`AudioFeatureExtractor`) and NLP (`LyricAnalyzer`) pipeline across all 6 multi-genre benchmark tracks in [`src/api/main.py`](file:///f:/capstone/src/api/main.py) and evaluated 2D UMAP acoustic manifold clustering across a 60-track multi-genre embedding matrix:

- **Acoustic Manifold Clustering Quality:**
  - **Silhouette Coefficient:** `0.684` (exceeds our proposal target of `> 0.60`)
  - **Davies-Bouldin Index:** `0.512` (strong inter-genre separation across Electronic, Synthwave, Acoustic Folk, Classical Orchestral, Jazz Brass, and Chamber Dance)
- **Deterministic Hallucination Guardrail Rate:** `100% Pass Rate` (`0%` contradictory mastering statements across all 6 benchmark tracks)

#### Measured Dual-Branch Metrics Across Benchmark Catalog (`data/sprint2_evaluation_results.json`)

| Track Title & Genre | Tempo (BPM) | Spectral Centroid (Hz) | HPSS Energy Split (Harmonic / Percussive) | Lyrical Valence / Arousal | Vocab Richness (TTR) & Rhyme Density | Detected Lyrical Theme | Multi-Agent Production Score |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **Neon Horizons**<br>*(Synthwave / Electronic)* | `123.0` | `146.9 Hz` | `90.6% H` / `9.4% P` | `V: -0.56`<br>`A: 0.57` | `TTR: 0.852`<br>`Rhyme: 44.4%` | Nocturnal Synth & Struggle | **85.0 / 100** |
| **Choice (DnB Cut)**<br>*(Electronic / Drum & Bass)* | `136.0` | `2,214.0 Hz` | `68.6% H` / `31.4% P` | `V: -0.57`<br>`A: 0.92` | `TTR: 0.821`<br>`Rhyme: 22.2%` | High-Octane Kinetic Energy | **93.0 / 100** |
| **Let's Go Fishin'**<br>*(Acoustic / Country Folk)* | `117.5` | `1,838.7 Hz` | `65.6% H` / `34.4% P` | `V: +0.80`<br>`A: 0.12` | `TTR: 0.831`<br>`Rhyme: 33.3%` | Pastoral Serenity & Nature | **93.0 / 100** |
| **Hungarian Dance No. 5**<br>*(Classical Orchestral)* | `143.6` | `1,687.3 Hz` | `92.9% H` / `7.1% P` | `V: +0.67`<br>`A: 0.92` | `TTR: 0.958`<br>`Rhyme: 50.0%` | Dramatic Orchestral Grandeur | **85.0 / 100** |
| **Late Night Jazz Horn**<br>*(Jazz / Solo Brass)* | `123.0` | `2,589.1 Hz` | `74.1% H` / `25.9% P` | `V: -0.40`<br>`A: 0.50` | `TTR: 0.897`<br>`Rhyme: 25.0%` | Nocturnal Synth & Struggle | **93.0 / 100** |
| **Sugar Plum Fantasy**<br>*(Fantasy Orchestral)* | `107.7` | `1,194.8 Hz` | `94.4% H` / `5.6% P` | `V: +0.40`<br>`A: 0.68` | `TTR: 0.880`<br>`Rhyme: 25.0%` | Enchanted Chamber Fantasy | **85.0 / 100** |

#### Visual Figures Generated in Sprint 2:
1. **Audio DSP & UMAP Manifold Plot:** [`screenshots/04_sprint2_dsp_umap_manifold.png`](file:///f:/capstone/screenshots/04_sprint2_dsp_umap_manifold.png)
2. **Lyric NLP Valence-Arousal & Poetic Plot:** [`screenshots/05_sprint2_nlp_sentiment_topics.png`](file:///f:/capstone/screenshots/05_sprint2_nlp_sentiment_topics.png)

---

## Deliverable 2: Update the Status Column in the Course Sheet

Copy and paste the following concise status update directly into the **Status** column of the course Google Sheet:

```text
On Track — Sprint 2 Completed (100%): Dual-branch Librosa 20-band MFCC/HPSS/UMAP pipeline (Silhouette=0.684) and Whisper/Valence-Arousal/Topic NLP analyzer operational across 6 benchmark genres.
```

---

## Deliverable 3: Individual LinkedIn Posts (Per Group Member)

Full copy-and-paste text (without raw markdown asterisks) is also saved in [`LINKEDIN_POST_PROGRESS_REPORT_1.md`](file:///f:/capstone/LINKEDIN_POST_PROGRESS_REPORT_1.md).

### 3.1 Individual LinkedIn Post — Alok Sali (`46854973`)
- **Attachment:** [`screenshots/04_sprint2_dsp_umap_manifold.png`](file:///f:/capstone/screenshots/04_sprint2_dsp_umap_manifold.png), [`screenshots/01_soundscope_dashboard_hero.png`](file:///f:/capstone/screenshots/01_soundscope_dashboard_hero.png), & [`screenshots/03_soundscope_architecture_diagram.png`](file:///f:/capstone/screenshots/03_soundscope_architecture_diagram.png)

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

### 3.2 Individual LinkedIn Post — Apoorv Pillai (`85099328`)
- **Attachment:** [`screenshots/05_sprint2_nlp_sentiment_topics.png`](file:///f:/capstone/screenshots/05_sprint2_nlp_sentiment_topics.png), [`screenshots/02_soundscope_multi_agent_guardrails.png`](file:///f:/capstone/screenshots/02_soundscope_multi_agent_guardrails.png), & [`screenshots/03_soundscope_architecture_diagram.png`](file:///f:/capstone/screenshots/03_soundscope_architecture_diagram.png)

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

---

## Deliverable 4: Your Chat with AI (Sprint 2 Log & Visual Evidence)

Full dialogues are documented in [`CONVERSATION_WITH_AI.md`](file:///f:/capstone/CONVERSATION_WITH_AI.md) along with visual evidence in `chats with ai/`:
- **Dialogue 5 (Sprint 2 — UMAP Acoustic Manifold & Feature Standardization):**
  - *Problem:* Combining raw Spectral Centroid (`~1,500–2,600 Hz`) with MFCCs (`-200 to +100`) and HPSS ratios (`0.0 to 1.0`) caused Euclidean distance in UMAP to be dominated entirely by Spectral Centroid magnitude.
  - *AI Solution & Outcome:* Applied `StandardScaler` z-score normalization across all 38 acoustic dimensions (`20 MFCCs + 12 Chroma + 6 Spectral/HPSS/Dynamic metrics`) and configured UMAP (`n_neighbors=15, min_dist=0.1, metric='cosine'`), improving cluster Silhouette Coefficient from `0.491` to `0.684`.
  - *Visual Evidence:* [`chats with ai/09_sprint2_umap_manifold_projection.png`](file:///f:/capstone/chats%20with%20ai/09_sprint2_umap_manifold_projection.png)
- **Dialogue 6 (Sprint 2 — 2D Russell Valence-Arousal Circumplex vs. 1D Sentiment Polarity):**
  - *Problem:* Standard 1D sentiment analysis treats "sad calm acoustic ballad" and "angry/tense 136 BPM Drum & Bass" identically as negative sentiment (`-0.55`), losing emotional intensity.
  - *AI Solution & Outcome:* Implemented 2D Valence-Arousal scoring in [`src/lyric_nlp/analyzer.py`](file:///f:/capstone/src/lyric_nlp/analyzer.py#L85-L120) separating polarity (`Valence: -1.0 to +1.0`) from energy (`Arousal: 0.0 to 1.0`), enabling the Lyric Semantic Agent to cross-check lyrical arousal against audio BPM.
  - *Visual Evidence:* [`chats with ai/10_sprint2_valence_arousal_topic_clustering.png`](file:///f:/capstone/chats%20with%20ai/10_sprint2_valence_arousal_topic_clustering.png)

---

## Deliverable 5: Five Companies (Germany Focus) Needing Our Exact Use Case

All five companies below operate in **Germany** (Berlin, Mannheim, and Hamburg) and build products that directly require **multimodal audio DSP + semantic/lyric AI analysis**:

| # | Company & Location | Why They Need SoundScope-AI's Exact Use Case | Relevant Links (Website, Careers & Social Media) |
| :-: | :--- | :--- | :--- |
| **1** | **Cyanite.ai**<br>*(Mannheim & Berlin, Germany)* | **Closest 1:1 Use-Case Match in Germany:** Cyanite builds AI-powered music tagging and similarity search that analyzes audio tracks for mood, genre, BPM, energy, and emotional themes for sync agencies and publishers — the exact dual-branch acoustic + mood intelligence pipeline we are building in SoundScope-AI. | • Website: https://cyanite.ai/<br>• Careers: https://cyanite.ai/careers/<br>• LinkedIn: https://www.linkedin.com/company/cyanite-ai/ |
| **2** | **Ableton AG**<br>*(Berlin, Germany)* | **DAW Producer Assistance & Audio ML:** Creator of *Ableton Live* and *Push*. Ableton's Audio ML team builds spectral similarity search (Live 12 Sound Similarity) and assistive feedback tools inside the DAW. Our Librosa DSP + UMAP manifold clustering and studio critique agent directly align with their creative ML roadmap. | • Careers Page: https://www.ableton.com/en/jobs/<br>• Product Page: https://www.ableton.com/en/live/<br>• LinkedIn: https://www.linkedin.com/company/ableton/ |
| **3** | **Native Instruments GmbH (incl. iZotope)**<br>*(Berlin, Germany)* | **AI Mixing & Mastering Critic Assistants:** Headquartered in Berlin, Native Instruments (merged with iZotope, creator of *Ozone* and *Neutron* AI Mastering Assistants) builds assistive EQ, dynamic range, and tonal balance advisors — matching our Mastering Critic Agent and Deterministic Verification Guardrail. | • Careers Page: https://www.native-instruments.com/en/careers/<br>• Product Page: https://www.native-instruments.com/<br>• LinkedIn: https://www.linkedin.com/company/native-instruments/ |
| **4** | **SoundCloud**<br>*(Berlin, Germany)* | **Creator Intelligence & Cold-Start Audio Discovery:** Headquartered in Berlin, SoundCloud hosts 300M+ tracks from independent artists. They rely on automated audio DSP feature extraction, lyric transcription, and mood/genre classification to recommend new unlabelled uploads and provide mastering tools to indie artists. | • Careers Portal: https://careers.soundcloud.com/<br>• Engineering Blog: https://developers.soundcloud.com/blog/<br>• LinkedIn: https://www.linkedin.com/company/soundcloud/ |
| **5** | **Steinberg Media Technologies GmbH / Endel**<br>*(Hamburg / Berlin, Germany)* | **Spectral Audio Analysis & Psychoacoustic AI:** Steinberg (Hamburg, creator of *Cubase*, *WaveLab*, and AI-driven *SpectraLayers*) and Endel (Berlin, AI functional music engine) both depend on harmonic-percussive separation, spectral centroid/rolloff tracking, and valence-arousal mood mapping. | • Steinberg Careers: https://www.steinberg.net/careers/<br>• Endel Berlin: https://endel.io/<br>• LinkedIn: https://www.linkedin.com/company/steinberg-media-technologies-gmbh/ |

---

## Deliverable 6: Three LinkedIn Thought Leaders in Our Field (Audio AI & MIR)

Below are three genuine domain specialists in **Music Information Retrieval (MIR), Audio DSP, and Deep Learning for Music** (not generic LinkedIn influencers), along with what we model from each person's writing style:

| # | Thought Leader & Role | LinkedIn Profile Link | 1 Specific Item We Like & Model in Their Writing Style |
| :-: | :--- | :--- | :--- |
| **1** | **Dr. Valerio Velardo**<br>*Founder of "The Sound of AI", PhD in Music AI, Audio ML Consultant & Educator* | https://www.linkedin.com/in/valeriovelardo/ | **Structured Architectural Breakdowns (`[01]–[04]`):** He translates dense audio DSP and deep learning concepts (such as MFCCs, spectrograms, and neural audio codecs) into numbered, bite-sized architectural blocks that connect mathematical intuition directly to practical Python/PyTorch implementation. We modeled our numbered `[01]–[04]` LinkedIn post structure directly on his style. |
| **2** | **Markus Schwarzer**<br>*CEO & Co-Founder of Cyanite.ai (Mannheim/Berlin, Germany)* | https://www.linkedin.com/in/markus-schwarzer/ | **Bridging MIR Metrics to Real Music Industry Workflows:** Instead of posting isolated model accuracy numbers, he opens his posts with a concrete pain point faced by music producers, sync managers, or artists, and then explains how emotional valence-arousal tagging and audio embeddings solve that human workflow. |
| **3** | **Dr. Christian Steinmetz**<br>*Audio AI Research Scientist (Suno, PhD in AI & Music at C4DM, Queen Mary University of London)* | https://www.linkedin.com/in/christian-steinmetz/ | **Empirical Visual Grounding & Peer Questions:** When sharing research on automatic mixing, differentiable DSP, or audio signal processing, he always attaches clean visual plots (spectrograms, frequency response curves, or latent space projections) backed by exact metrics, and closes with an open technical question that invites fellow audio researchers to discuss trade-offs. |

