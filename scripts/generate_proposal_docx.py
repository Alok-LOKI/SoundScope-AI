"""
Generate high-quality Microsoft Word (.docx) file from PROJECT_PROPOSAL.md.
Includes styled headings, embedded architecture diagrams, and custom-styled tables.
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

DOCX_OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "PROJECT_PROPOSAL.docx")
DOCX_ALT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "SoundScope_AI_Project_Proposal.docx")
SCREENSHOTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "screenshots")

def set_cell_background(cell, fill_hex):
    """Sets background color of a table cell."""
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tc_pr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets internal padding for a table cell."""
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tc_mar.append(node)
    tc_pr.append(tc_mar)

def create_proposal_docx():
    doc = Document()

    # Page Margins: 1 inch all around
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)
        
        # Header & Footer
        footer = s.footer
        f_p = footer.paragraphs[0]
        f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        f_run = f_p.add_run("SoundScope-AI | Capstone Project Proposal — Winter 2026/2027")
        f_run.font.name = "Calibri"
        f_run.font.size = Pt(8.5)
        f_run.font.color.rgb = RGBColor(120, 120, 120)

    # Styles
    styles = doc.styles
    normal_style = styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(40, 40, 40)
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(6)

    # Title Banner
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(4)
    run_title = p_title.add_run("SoundScope-AI: Multi-Agent Acoustic & Lyric Intelligence Platform")
    run_title.font.name = 'Arial'
    run_title.font.size = Pt(22)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(16, 75, 140) # Deep Navy Accent

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(18)
    run_sub = p_sub.add_run("Formal Project Proposal — Capstone Project B (DSC03)\n")
    run_sub.font.size = Pt(13)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(80, 80, 80)
    
    run_sub2 = p_sub.add_run("University of Europe for Applied Sciences (UE)  •  M.Sc. Data Science  •  Winter 2026/2027\nSupervisor: Dr. Humera Noor Minhas")
    run_sub2.font.size = Pt(10.5)
    run_sub2.font.italic = True
    run_sub2.font.color.rgb = RGBColor(100, 100, 100)

    # Divider line
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_after = Pt(14)
    r_div = p_div.add_run("—" * 65)
    r_div.font.color.rgb = RGBColor(200, 200, 200)

    # Helper function for Section Headings
    def add_heading_1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(16)
        h.paragraph_format.space_after = Pt(6)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = 'Arial'
        r.font.size = Pt(15)
        r.font.bold = True
        r.font.color.rgb = RGBColor(16, 75, 140)
        return h

    def add_heading_2(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(12)
        h.paragraph_format.space_after = Pt(4)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = 'Arial'
        r.font.size = Pt(12.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(45, 55, 72)
        return h

    def add_bullet(text, bold_prefix="", indent=0):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.left_indent = Inches(0.25 * (indent + 1))
        if bold_prefix:
            r_b = p.add_run(bold_prefix)
            r_b.bold = True
        p.add_run(text)
        return p

    # --- SECTION 1 ---
    add_heading_1("1. Project Overview")
    add_bullet(" Alok Sali (Matriculation No: 46854973) & Apoorv Pillai (Matriculation No: 85099328)", "Authors: ")
    add_bullet(" Master of Science in Data Science (M.Sc. Data Science)", "Degree Program: ")
    add_bullet(" University of Europe for Applied Sciences (UE), Germany", "Institution: ")
    add_bullet(" DSC03 Capstone Project B — Winter 2026/2027", "Module: ")
    add_bullet(" Dr. Humera Noor Minhas", "Academic Supervisor: ")
    add_bullet(" https://lnkd.in/p/dK-aYDwb (Milestone 2 Deliverable)", "Live LinkedIn Post: ")
    
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    r = p.add_run("Lecture Tracks Addressed (Directly covering the Capstone Lecture curriculum):")
    r.bold = True
    add_bullet(" Orchestrated multi-agent workflow (LangGraph) coordinating specialized signal, lyric, and mastering agents with reflection loops.", "Agent Pipelines: ")
    add_bullet(" Domain adaptation (LoRA / QLoRA) on open-weight LLMs (Llama-3 / Qwen2.5) specialized in music theory, production critique, and acoustic feedback.", "LLM Fine-Tuning: ")
    add_bullet(" Whisper speech-to-text transcription, rhyme density quantification, emotional valence-arousal trajectory modeling, and thematic topic modeling (BERTopic).", "Natural Language Processing (NLP): ")
    add_bullet(" Digital Signal Processing (DSP), mathematical feature engineering (20-band MFCCs, spectral moments, HPSS), manifold learning (PCA, UMAP), and multi-class genre/mood classification.", "Data Science & ML: ")
    add_bullet(" Asynchronous FastAPI microservices, audio processing background queue, and clean RESTful API telemetry.", "Software Development & API: ")
    add_bullet(" Interactive web studio featuring real-time audio playback, dynamic waveforms, radar charts, and explainable multi-agent critique cards.", "Fullstack Application: ")

    # --- SECTION 2 ---
    add_heading_1("2. Problem Statement & Motivation")
    doc.add_paragraph(
        "Music is an inherently multimodal medium combining acoustic signal physics (timbre, rhythm, frequency distribution, dynamics) "
        "and textual poetry (lyrics, narrative progression, emotion). However, current music technology tools operate in isolated silos:"
    )
    add_bullet(" DSP and Music Information Retrieval (MIR) tools output raw mathematical numbers (e.g., Spectral Centroid = 2,400 Hz) with zero contextual, creative interpretation for creators.", "1. Isolated Signal Analytics: ")
    add_bullet(" Streaming recommendation systems rely on shallow metadata tags or black-box collaborative filtering click logs, ignoring subtle linguistic metaphors, sentiment trajectories, and vocabulary richness.", "2. Superficial Lyric Processing: ")
    add_bullet(" Independent musicians receive zero explainable feedback on why a mix fails to engage listeners or which technical adjustments (compression, EQ balance, narrative pacing) would elevate their production.", "3. Black-Box Cold-Start Problem: ")
    doc.add_paragraph(
        "SoundScope-AI bridges this gap by uniting Acoustic Data Science and Natural Language Processing within an Orchestrated Multi-Agent Architecture. "
        "It ingests audio tracks, transcribes and analyzes lyrics, extracts high-dimensional DSP acoustic fingerprints, and generates explainable, professional production critiques powered by a fine-tuned music intelligence LLM."
    )

    # --- SECTION 3 ---
    add_heading_1("3. System Architecture")
    doc.add_paragraph(
        "The system follows a dual-branch processing paradigm where continuous time-series audio data and discrete linguistic text "
        "are analyzed simultaneously and orchestrated through specialized autonomous agents:"
    )

    # Insert Architecture Diagram Image if available
    arch_img_path = os.path.join(SCREENSHOTS_DIR, "03_soundscope_architecture_diagram.png")
    if os.path.exists(arch_img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(arch_img_path, width=Inches(6.4))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(10)
        r_cap = p_cap.add_run("Figure 1: SoundScope-AI Dual-Branch Multimodal Architecture & Multi-Agent Flow")
        r_cap.font.size = Pt(9)
        r_cap.font.italic = True
        r_cap.font.color.rgb = RGBColor(100, 100, 100)

    doc.add_paragraph("The five core architectural layers comprise:")
    add_bullet(" Interactive web dashboard with real-time audio waveform scrubbing, 20-band mel spectrum, and acoustic radar cards.", "1. Fullstack Client Application: ")
    add_bullet(" Asynchronous audio ingestion, chunking, and worker task management.", "2. API & Ingestion Service (FastAPI): ")
    add_bullet(" Simultaneous extraction of acoustic physics (Librosa/Essentia) and lyrical poetry (Whisper/Transformers).", "3. Dual-Branch Data Science & NLP Engine: ")
    add_bullet(" Specialized domain agents (Signal Analyst, Lyric Semanticist, Mastering Critic, and Verification Guardrail).", "4. LangGraph Multi-Agent Pipeline: ")
    add_bullet(" Qdrant / ChromaDB for acoustic manifold embeddings and PostgreSQL for session telemetry.", "5. Persistence & Vector Storage: ")

    # --- SECTION 4 ---
    add_heading_1("4. Multi-Agent Pipeline Roles & LLM Fine-Tuning")
    add_heading_2("The Four Cooperating Agents (LangGraph):")
    add_bullet(" Ingests mathematical DSP metrics (spectral balance, dynamic range dB, crest factor, tempo consistency) and translates them into acoustic engineering terms (e.g., 'excessive low-end muddiness below 200 Hz').", "1. Acoustic Signal Analyst Agent:")
    add_bullet(" Evaluates narrative progression, rhyme density score, vocabulary diversity (Type-Token Ratio), and emotional dissonance (e.g., cheerful acoustic tempo paired with sorrowful lyrics).", "2. Lyric & NLP Semantic Agent:")
    add_bullet(" Powered by a fine-tuned open LLM (Qwen2.5-7B / Llama-3-8B via LoRA), this agent synthesizes acoustic and lyrical insights into actionable EQ, arrangement, and mastering suggestions.", "3. Mastering Critic & Recommender Agent:")
    add_bullet(" Deterministically cross-checks LLM suggestions against ground-truth DSP metrics to mathematically eliminate hallucinations.", "4. Verification & Fact-Check Guard Agent:")

    add_heading_2("LLM Fine-Tuning Strategy:")
    add_bullet(" Qwen2.5-Coder / Llama-3-8B-Instruct", "Base Model: ")
    add_bullet(" Parameter-Efficient Fine-Tuning (PEFT) using 4-bit QLoRA (rank r = 16, alpha = 32) via Unsloth and BitsAndBytes.", "Method: ")
    add_bullet(" Curated corpus of professional audio engineering mastering reviews, musicological analyses, and paired audio-lyric critiques.", "Training Corpus: ")

    # --- SECTION 5 ---
    add_heading_1("5. Technical Stack")
    doc.add_paragraph("The platform leverages modern production-tested open-source frameworks across each domain:")

    tech_data = [
        ("Agent Pipelines", "LangGraph, LangChain Core"),
        ("LLM Fine-Tuning", "Unsloth / PEFT, Hugging Face Transformers, BitsAndBytes"),
        ("NLP & Speech-to-Text", "OpenAI Whisper, NLTK, Spacy, BERTopic, RoBERTa Sentiment"),
        ("Audio DSP & Machine Learning", "Librosa, Essentia, SciPy, Scikit-learn, XGBoost, PyTorch"),
        ("Manifold Learning", "UMAP, t-SNE, PCA"),
        ("Backend & REST APIs", "FastAPI, Uvicorn, Celery, Redis, Pydantic"),
        ("Frontend Application", "HTML5 Canvas, React / Vite, Wavesurfer.js, CSS Glassmorphism"),
        ("Databases", "PostgreSQL (Telemetry), Qdrant / ChromaDB (Acoustic embeddings)")
    ]

    table_tech = doc.add_table(rows=len(tech_data) + 1, cols=2)
    table_tech.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_tech.autofit = False

    # Header Row
    hdr_cells = table_tech.rows[0].cells
    hdr_cells[0].text = "Category"
    hdr_cells[1].text = "Technologies & Frameworks"
    hdr_cells[0].paragraphs[0].runs[0].font.bold = True
    hdr_cells[1].paragraphs[0].runs[0].font.bold = True
    set_cell_background(hdr_cells[0], "104B8C")
    set_cell_background(hdr_cells[1], "104B8C")
    hdr_cells[0].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    hdr_cells[1].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)

    col_widths = [Inches(2.2), Inches(4.3)]
    for row_idx, (cat, techs) in enumerate(tech_data, start=1):
        row_cells = table_tech.rows[row_idx].cells
        row_cells[0].text = cat
        row_cells[1].text = techs
        row_cells[0].paragraphs[0].runs[0].font.bold = True
        row_cells[0].paragraphs[0].runs[0].font.size = Pt(10)
        row_cells[1].paragraphs[0].runs[0].font.size = Pt(10)
        
        bg_color = "F7F9FB" if row_idx % 2 == 1 else "FFFFFF"
        set_cell_background(row_cells[0], bg_color)
        set_cell_background(row_cells[1], bg_color)

    for row in table_tech.rows:
        for i, cell in enumerate(row.cells):
            cell.width = col_widths[i]
            set_cell_margins(cell, top=80, bottom=80, left=120, right=120)

    # --- SECTION 6 & 8: SPRINTS & DIVISION OF RESPONSIBILITIES ---
    add_heading_1("6. Detailed Sprint Breakdown & Division of Responsibilities")
    doc.add_paragraph(
        "The project spans the 14-week Winter Semester 2026/2027. While both team members maintain joint ownership "
        "of the end-to-end delivery, dedicated domain leads ensure accountable, parallel execution:"
    )

    sprints = [
        ("Sprint 1\n(Oct 12 – Oct 26)", "Proposal Approval & Baseline", 
         "Audio dataset setup (FMA, GTZAN); baseline Librosa feature extraction pipeline", 
         "Lyric dataset curation (Genius); Whisper baseline transcription test", 
         "Formal Proposal Document, System Architecture Diagram, University Form"),
        
        ("Sprint 2\n(Oct 26 – Nov 09)", "Progress Report 1:\nDSP & NLP Foundations", 
         "20-band MFCC, HPSS, spectral flux/rolloff extractor; UMAP 2D/3D manifold projections", 
         "RoBERTa valence-arousal sentiment model; BERTopic lyrical topic clustering", 
         "Progress Report 1 & Individual LinkedIn Milestone Posts"),
        
        ("Sprint 3\n(Nov 09 – Nov 23)", "Progress Report 2:\nModels & Agent Core", 
         "Genre/Mood classifiers (XGBoost & 2D Mel-CNN); acoustic metric validation heuristics", 
         "LangGraph state graph setup; Signal Analyst Agent & Lyric Semantic Agent", 
         "Progress Report 2 & Individual LinkedIn Milestone Posts"),
        
        ("Sprint 4\n(Nov 23 – Dec 07)", "Progress Report 3:\nLLM Tuning & APIs", 
         "FastAPI ingestion service, async Celery audio worker queue, WebSocket telemetry", 
         "Music Critic LLM fine-tuning (QLoRA on Qwen2.5/Llama-3); prompt engineering & guardrails", 
         "Progress Report 3 & Individual LinkedIn Milestone Posts"),
        
        ("Sprint 5\n(Dec 07 – Dec 21)", "Progress Report 4:\nFullstack Studio UI", 
         "3D UMAP interactive visualization, audio waveform player (Wavesurfer.js)", 
         "Multi-agent critique chat interface, radar charts, fullstack integration", 
         "Progress Report 4 & Individual LinkedIn Milestone Posts"),
        
        ("Sprint 6\n(Dec 21 – Jan 04)", "Final Capstone Report Submission", 
         "Quantitative benchmarking (F1, Silhouette, RAGAS critique fidelity); code refactoring", 
         "Capstone Academic Report drafting (Methodology, Literature Review, Discussion)", 
         "Comprehensive Academic Report (PDF/Word), clean GitHub repository"),
        
        ("Sprint 7\n(Jan 04 – Jan 18)", "Final Presentation & Pitch", 
         "Presentation slide deck design; live demo recording", 
         "15–20 min presentation video recording; 2-minute elevator pitch video", 
         "Final Slide Deck, Full Presentation Video, Elevator Pitch Video")
    ]

    table_sprints = doc.add_table(rows=len(sprints) + 1, cols=5)
    table_sprints.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_sprints.autofit = False

    s_headers = ["Sprint & Dates", "Milestone", "Lead: Alok Sali", "Lead: Apoorv Pillai", "Joint Deliverable"]
    for i, h_text in enumerate(s_headers):
        cell = table_sprints.rows[0].cells[i]
        cell.text = h_text
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(9.5)
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        set_cell_background(cell, "104B8C")

    s_col_widths = [Inches(1.2), Inches(1.2), Inches(1.5), Inches(1.5), Inches(1.4)]
    for r_idx, row_data in enumerate(sprints, start=1):
        for c_idx, text in enumerate(row_data):
            cell = table_sprints.rows[r_idx].cells[c_idx]
            cell.text = text
            if len(cell.paragraphs[0].runs) > 0:
                cell.paragraphs[0].runs[0].font.size = Pt(8.5)
            bg_color = "F7F9FB" if r_idx % 2 == 1 else "FFFFFF"
            set_cell_background(cell, bg_color)

    for row in table_sprints.rows:
        for i, cell in enumerate(row.cells):
            cell.width = s_col_widths[i]
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)

    # --- SECTION 7 ---
    add_heading_1("7. Quantitative Evaluation Metrics")
    add_bullet(" Multi-class Genre & Mood classification accuracy, Macro F1-score, and ROC-AUC on GTZAN and Free Music Archive (FMA).", "Acoustic & Classification Benchmarks: ")
    add_bullet(" UMAP / t-SNE cluster separation evaluated via Silhouette Coefficient and Davies-Bouldin Index.", "Manifold Clustering: ")
    add_bullet(" Word Error Rate (WER) using Whisper speech-to-text on noisy audio stems.", "NLP Transcription: ")
    add_bullet(" Valence-arousal trajectory consistency and thematic classification precision.", "Sentiment & Themes: ")
    add_bullet(" Critique faithfulness and recommendation relevance scored via RAGAS / LLM-as-a-judge against human sound engineer annotations.", "Agent Evaluation: ")
    add_bullet(" Measuring whether the agent claims acoustic issues not present in the ground-truth DSP data (target: 0% verified).", "Hallucination Rate: ")
    add_bullet(" End-to-end processing latency for a 3-minute song under 12 seconds on GPU hardware.", "Processing Latency: ")

    # --- SECTION 9 ---
    add_heading_1("8. Risk Assessment & Mitigation Strategies")
    
    risks = [
        ("GPU Compute Bottlenecks for LLM Tuning", "Medium", "High", 
         "Utilize 4-bit QLoRA via Unsloth/BitsAndBytes to reduce VRAM requirements under 12GB (Google Colab T4/A100 or Kaggle GPU)."),
        ("Whisper Transcription Latency on Long Audio", "Medium", "Medium", 
         "Implement chunked parallel audio processing and use faster-whisper (CTranslate2) for 4x inference speedup."),
        ("LLM Hallucinations in Music Feedback", "Medium", "High", 
         "Implement a dedicated Verification Guard Agent that programmatically cross-checks LLM text claims against measured DSP metric ranges."),
        ("Multimodal Alignment Dissonance", "Low", "Medium", 
         "Define explicit mathematical correlation heuristics between acoustic arousal (tempo/energy) and lyrical valence.")
    ]

    table_risks = doc.add_table(rows=len(risks) + 1, cols=4)
    table_risks.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_risks.autofit = False

    r_headers = ["Risk Factor", "Probability", "Impact", "Mitigation Strategy"]
    for i, h_text in enumerate(r_headers):
        cell = table_risks.rows[0].cells[i]
        cell.text = h_text
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(9.5)
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        set_cell_background(cell, "104B8C")

    r_col_widths = [Inches(1.8), Inches(1.0), Inches(0.9), Inches(2.9)]
    for r_idx, row_data in enumerate(risks, start=1):
        for c_idx, text in enumerate(row_data):
            cell = table_risks.rows[r_idx].cells[c_idx]
            cell.text = text
            if len(cell.paragraphs[0].runs) > 0:
                cell.paragraphs[0].runs[0].font.size = Pt(9)
            bg_color = "F7F9FB" if r_idx % 2 == 1 else "FFFFFF"
            set_cell_background(cell, bg_color)

    for row in table_risks.rows:
        for i, cell in enumerate(row.cells):
            cell.width = r_col_widths[i]
            set_cell_margins(cell, top=70, bottom=70, left=90, right=90)

    # --- SECTION 10 ---
    add_heading_1("9. Compute Resources, Ethics & Data Licensing")
    add_bullet(" Python 3.10+, PyTorch with CUDA acceleration, FastAPI backend, Vite/React frontend. Local development supplemented by cloud GPU (Google Colab Pro / Kaggle).", "Compute Environment: ")
    add_bullet(" Creative Commons (CC-BY, CC-BY-NC) for non-commercial educational research.", "Free Music Archive (FMA): ")
    add_bullet(" Academic educational research use.", "GTZAN Benchmark: ")
    add_bullet(" Audio and lyrics are processed purely for research and educational critique under fair use standards. User audio uploads are processed ephemerally in session memory without unauthorized redistribution.", "Ethics & Privacy: ")

    # Dashboard Screenshot Callout at end
    dash_img_path = os.path.join(SCREENSHOTS_DIR, "01_soundscope_dashboard_hero.png")
    if os.path.exists(dash_img_path):
        doc.add_page_break()
        add_heading_1("10. Appendix: Platform Prototype Preview")
        doc.add_paragraph("High-fidelity interactive studio dashboard displaying DSP acoustic features, 20-band mel spectrum, and real-time lyric analysis:")
        p_dash = doc.add_paragraph()
        p_dash.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_dash.paragraph_format.space_before = Pt(6)
        r_dash = p_dash.add_run()
        r_dash.add_picture(dash_img_path, width=Inches(6.4))
        
        p_dash_cap = doc.add_paragraph()
        p_dash_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_dcap = p_dash_cap.add_run("Figure 2: SoundScope-AI Studio Dashboard & Multi-Agent Evaluation Interface")
        r_dcap.font.size = Pt(9)
        r_dcap.font.italic = True
        r_dcap.font.color.rgb = RGBColor(100, 100, 100)

    # Save documents
    doc.save(DOCX_OUTPUT_PATH)
    doc.save(DOCX_ALT_PATH)
    print(f"Generated Word Document: {DOCX_OUTPUT_PATH}")
    print(f"Generated Word Document: {DOCX_ALT_PATH}")

if __name__ == "__main__":
    create_proposal_docx()
