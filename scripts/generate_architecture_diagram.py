"""
Generates a Spotify-dark aesthetic System Architecture Diagram for SoundScope-AI.
"""
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "screenshots", "03_soundscope_architecture_diagram.png")

fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
fig.patch.set_facecolor("#0a0a0a")
ax.set_facecolor("#0a0a0a")

# Helper for rounded cards
def draw_card(ax, x, y, w, h, title, subtitle, items, border_color="#282828", bg_color="#141414", title_color="#1ed760"):
    rect = patches.FancyBboxPatch((x, y), w, h,
                                  boxstyle="round,pad=0.02,rounding_size=0.03",
                                  facecolor=bg_color, edgecolor=border_color, linewidth=1.5, zorder=2)
    ax.add_patch(rect)
    ax.text(x + w*0.05, y + h*0.84, title, fontsize=12, fontweight='bold', color=title_color, family='sans-serif', zorder=3)
    if subtitle:
        ax.text(x + w*0.05, y + h*0.72, subtitle, fontsize=8.5, color="#888888", family='sans-serif', zorder=3)
    
    start_y = 0.58 if subtitle else 0.68
    for i, it in enumerate(items):
        ax.text(x + w*0.05, y + h*(start_y - i*0.14), f"• {it}", fontsize=9, color="#dcdcdc", family='sans-serif', zorder=3)

# Top Header
ax.text(0.5, 0.94, "SoundScope-AI: Multimodal Acoustic & Lyric Intelligence Architecture",
        fontsize=16, fontweight='bold', color="#ffffff", ha="center", family='sans-serif')
ax.text(0.5, 0.90, "Dual-Branch Signal Physics + NLP Modeling + LangGraph Multi-Agent Verification",
        fontsize=10, color="#1ed760", ha="center", family='sans-serif')

# 1. Input Node
draw_card(ax, 0.35, 0.74, 0.30, 0.12, "Input Audio Signal", "WAV / MP3 / FLAC Stream", 
          ["Time-domain audio & lyric content"], border_color="#1ed760", bg_color="#181818", title_color="#ffffff")

# 2. Dual Branch
# DSP Branch
draw_card(ax, 0.05, 0.44, 0.40, 0.23, "Branch A: Audio DSP Engine", "Physics-grounded signal feature extraction",
          ["20-Band Mel-Frequency Cepstral Coefficients (MFCCs)",
           "Spectral Moments (Centroid, Rolloff, Flux, Flatness)",
           "Dynamic Range (Crest Factor dB) & HPSS Ratios",
           "Tempogram & Beat Tracking (Librosa / Essentia)"],
          border_color="#1ed760", bg_color="#121212")

# NLP Branch
draw_card(ax, 0.55, 0.44, 0.40, 0.23, "Branch B: Lyric & Poetic NLP", "Semantic intelligence & sentiment trajectories",
          ["OpenAI Whisper Speech-to-Text Transcription",
           "Sectional Emotional Valence-Arousal Trajectory",
           "End-Rhyme Density & Metrical Cadence Scoring",
           "Vocabulary Diversity (Type-Token Ratio / BERTopic)"],
          border_color="#1ed760", bg_color="#121212")

# 3. LangGraph Multi-Agent Core
draw_card(ax, 0.05, 0.12, 0.52, 0.24, "LangGraph Multi-Agent Orchestration", "Specialized domain agents with deterministic guardrails",
          ["Signal Analyst Agent: Evaluates mix balance, EQ muddiness & dynamics",
           "Lyric Semanticist Agent: Evaluates emotional arc & narrative tone",
           "LoRA Mastering Critic LLM: Synthesizes explainable studio advice",
           "Physics Verification Guardrail: Eliminates hallucinations via DSP checks"],
          border_color="#22c55e", bg_color="#161b18", title_color="#4ade80")

# 4. Interactive Dashboard / Output
draw_card(ax, 0.65, 0.12, 0.30, 0.24, "Interactive Studio Platform", "FastAPI + Real-time Web Dashboard",
          ["SoundScope Score (0-100)",
           "Physics Verification Badge",
           "Interactive Waveform Scrubber",
           "Actionable Mastering Recommendations"],
          border_color="#1ed760", bg_color="#181818", title_color="#ffffff")

# Connector Arrows
arrow_kw = dict(arrowstyle="->", color="#1ed760", lw=2, mutation_scale=15, zorder=1)
ax.annotate("", xy=(0.25, 0.67), xytext=(0.42, 0.74), arrowprops=arrow_kw)
ax.annotate("", xy=(0.75, 0.67), xytext=(0.58, 0.74), arrowprops=arrow_kw)

ax.annotate("", xy=(0.25, 0.36), xytext=(0.25, 0.44), arrowprops=arrow_kw)
ax.annotate("", xy=(0.45, 0.36), xytext=(0.70, 0.44), arrowprops=arrow_kw)

ax.annotate("", xy=(0.65, 0.24), xytext=(0.57, 0.24), arrowprops=arrow_kw)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.tight_layout()
plt.savefig(OUTPUT_PATH, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
plt.close()
print(f"Generated: {OUTPUT_PATH}")
