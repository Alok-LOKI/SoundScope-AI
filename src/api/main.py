"""
SoundScope-AI: FastAPI Application Backend
Exposes endpoints for Audio DSP extraction, Lyric NLP analysis, and Multi-Agent Critique.
Supports multiple genre demo tracks and external dataset sample evaluation.
"""

import os
import io
import tempfile
from typing import Optional, Dict, Any
import numpy as np
import soundfile as sf
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response, FileResponse
from pydantic import BaseModel

from src.audio_dsp.features import AudioFeatureExtractor
from src.lyric_nlp.analyzer import LyricAnalyzer
from src.agents.pipeline import MultiAgentPipeline

app = FastAPI(
    title="SoundScope-AI",
    description="Multimodal Acoustic & Lyric Intelligence Platform",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

extractor = AudioFeatureExtractor()
analyzer = LyricAnalyzer()
agent_pipeline = MultiAgentPipeline()

SAMPLES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data", "samples")

# Multi-genre demo catalog
TRACK_CATALOG: Dict[str, Dict[str, Any]] = {
    "synthwave_neon": {
        "id": "synthwave_neon",
        "title": "Neon Horizons",
        "artist": "SoundScope Lab",
        "genre": "Synthwave / Electronic",
        "type": "synthetic",
        "lyrics": """[Verse 1]
Midnight shadows fade into the neon glow
City rhythms whisper what we used to know
We keep running searching for the morning light
Broken echoes fading in the velvet night

[Chorus]
Hold on to the flame before it drifts away
Every silent heartbreak is a price we pay
Feel the frequency inside the sound
We are rising up from underground"""
    },
    "drum_and_bass_electronic": {
        "id": "drum_and_bass_electronic",
        "title": "Choice (DnB Cut)",
        "artist": "admiralbob77",
        "genre": "Electronic / Drum & Bass",
        "file": "drum_and_bass_electronic.wav",
        "type": "real_recording",
        "lyrics": """[Verse 1]
Speeding through the static in the digital haze
Rhythms taking over through the neon maze
Sub-bass rumbling rattling the floor
Can you feel the tempo asking for more

[Chorus]
Sync the signal lock the beat
Electric fire under our feet
We don't slow down we don't look back
Riding high on the audio track"""
    },
    "acoustic_folk_country": {
        "id": "acoustic_folk_country",
        "title": "Let's Go Fishin'",
        "artist": "Karissa Hobbs",
        "genre": "Acoustic / Country Folk",
        "file": "acoustic_folk_country.wav",
        "type": "real_recording",
        "lyrics": """[Verse 1]
Early in the morning before the sun can wake
Walking down the gravel path beside the quiet lake
Got an old cane pole and a piece of twine
Gentle morning breeze blowing through the pine

[Chorus]
Cast a line and watch the water gleam
Floating peaceful in a simple dream
No worries here beneath the open sky
Just watching sunny clouds go drifting by"""
    },
    "classical_orchestral": {
        "id": "classical_orchestral",
        "title": "Hungarian Dance No. 5",
        "artist": "Johannes Brahms",
        "genre": "Classical Orchestral",
        "file": "classical_orchestral.wav",
        "type": "real_recording",
        "lyrics": """[Movement 1]
Strings allegro dancing with fiery passion
Grand orchestra rising in classical fashion
Crescendo building with dramatic grace
Echoes resonate throughout the hall's embrace"""
    },
    "jazz_solo_trumpet": {
        "id": "jazz_solo_trumpet",
        "title": "Late Night Jazz Horn",
        "artist": "Sorohanro",
        "genre": "Jazz / Solo Brass",
        "file": "jazz_solo_trumpet.wav",
        "type": "real_recording",
        "lyrics": """[Verse 1]
Dim lights smokin' in the midnight lounge
Soulful trumpet notes the only sound around
Improvising tears on a silver bell
Stories that the blues only know to tell"""
    },
    "dance_sugar_plum": {
        "id": "dance_sugar_plum",
        "title": "Sugar Plum Fantasy",
        "artist": "Tchaikovsky",
        "genre": "Fantasy Orchestral",
        "file": "dance_sugar_plum.wav",
        "type": "real_recording",
        "lyrics": """[Theme]
Delicate celesta ringing through the winter snow
Spirits dancing softly in the frosted glow
Whimsical enchantment twirling in the air
Fairy tale wonders everywhere"""
    }
}

# Cache computed track features for instant switching
TRACK_CACHE: Dict[str, Dict[str, Any]] = {}


class LyricRequest(BaseModel):
    lyrics: str
    track_title: Optional[str] = "Untitled Track"
    artist_name: Optional[str] = "Unknown Artist"


class CritiqueRequest(BaseModel):
    audio_metrics: dict
    lyric_metrics: dict
    track_title: Optional[str] = "Untitled Track"
    artist_name: Optional[str] = "Unknown Artist"


@app.get("/api/health")
def health_check():
    return {"status": "online", "platform": "SoundScope-AI", "version": "1.0.0"}


@app.get("/api/tracks")
def get_track_list():
    """Returns the list of available multi-genre demo tracks."""
    return [
        {
            "id": t["id"],
            "title": t["title"],
            "artist": t["artist"],
            "genre": t["genre"],
            "type": t["type"],
        }
        for t in TRACK_CATALOG.values()
    ]


@app.get("/api/tracks/{track_id}/audio")
def get_track_audio(track_id: str):
    """Streams audio for the specified demo track."""
    if track_id not in TRACK_CATALOG:
        raise HTTPException(status_code=404, detail="Track not found")

    track_info = TRACK_CATALOG[track_id]

    if track_info.get("type") == "synthetic":
        # Generate synthetic 120 BPM audio
        sr = 22050
        duration = 6.0
        t = np.linspace(0, duration, int(sr * duration), endpoint=False)
        bass = 0.35 * np.sin(2 * np.pi * 80 * t) + 0.15 * np.sin(2 * np.pi * 160 * t)
        chord = 0.12 * (np.sin(2 * np.pi * 261.63 * t) + np.sin(2 * np.pi * 329.63 * t) + np.sin(2 * np.pi * 392.00 * t))
        pulse = np.zeros_like(t)
        interval = int(sr * 0.5)
        for idx in range(0, len(t), interval):
            hit_len = min(int(sr * 0.04), len(t) - idx)
            pulse[idx:idx + hit_len] += np.hanning(hit_len) * 0.6
        signal = (bass + chord + pulse) / (np.max(np.abs(bass + chord + pulse)) + 1e-6)
        buf = io.BytesIO()
        sf.write(buf, signal, sr, format="WAV")
        buf.seek(0)
        return Response(content=buf.read(), media_type="audio/wav")

    file_name = track_info.get("file")
    file_path = os.path.join(SAMPLES_DIR, file_name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Sample audio file missing")
    return FileResponse(file_path, media_type="audio/wav")


@app.get("/api/tracks/{track_id}/data")
def get_track_data(track_id: str):
    """Extracts DSP features, lyric metrics, and critique for the selected track."""
    if track_id not in TRACK_CATALOG:
        raise HTTPException(status_code=404, detail="Track not found")

    if track_id in TRACK_CACHE:
        return TRACK_CACHE[track_id]

    track_info = TRACK_CATALOG[track_id]
    lyrics = track_info.get("lyrics", "")

    if track_info.get("type") == "synthetic":
        sr = 22050
        duration = 6.0
        t = np.linspace(0, duration, int(sr * duration), endpoint=False)
        bass = 0.35 * np.sin(2 * np.pi * 80 * t)
        chord = 0.15 * np.sin(2 * np.pi * 330 * t)
        pulse = np.zeros_like(t)
        interval = int(sr * 0.5)
        for idx in range(0, len(t), interval):
            hit_len = min(int(sr * 0.04), len(t) - idx)
            pulse[idx:idx + hit_len] += np.hanning(hit_len) * 0.5
        signal = bass + chord + pulse
        audio_metrics = extractor.extract_from_array(signal, sr).to_dict()
    else:
        file_path = os.path.join(SAMPLES_DIR, track_info["file"])
        audio_metrics = extractor.extract_from_file(file_path).to_dict()

    lyric_metrics = analyzer.analyze_text(lyrics).to_dict()
    critique = agent_pipeline.run(
        audio_metrics=audio_metrics,
        lyric_metrics=lyric_metrics,
        track_title=track_info["title"],
        artist_name=track_info["artist"],
    )

    result = {
        "track_id": track_id,
        "track_title": track_info["title"],
        "artist_name": track_info["artist"],
        "genre": track_info["genre"],
        "sample_lyrics": lyrics,
        "audio_metrics": audio_metrics,
        "lyric_metrics": lyric_metrics,
        "critique": critique,
    }
    TRACK_CACHE[track_id] = result
    return result


@app.post("/api/analyze-audio")
async def analyze_audio(file: UploadFile = File(...)):
    """Receives user audio file (WAV/MP3/FLAC) and extracts acoustic DSP metrics."""
    suffix = os.path.splitext(file.filename or "audio.wav")[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        metrics = extractor.extract_from_file(tmp_path)
        return {"filename": file.filename, "metrics": metrics.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Audio processing failed: {str(e)}")
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)


@app.post("/api/analyze-lyrics")
def analyze_lyrics(req: LyricRequest):
    """Computes poetic meter, rhyme density, and sentiment metrics on song lyrics."""
    if not req.lyrics.strip():
        raise HTTPException(status_code=400, detail="Lyrics text cannot be empty.")
    metrics = analyzer.analyze_text(req.lyrics)
    return {
        "track_title": req.track_title,
        "artist_name": req.artist_name,
        "metrics": metrics.to_dict(),
    }


@app.post("/api/critique")
def generate_critique(req: CritiqueRequest):
    """Executes the multi-agent critique workflow."""
    state = agent_pipeline.run(
        audio_metrics=req.audio_metrics,
        lyric_metrics=req.lyric_metrics,
        track_title=req.track_title or "Untitled Track",
        artist_name=req.artist_name or "Unknown Artist",
    )
    return state


# Legacy demo endpoints for backwards compatibility
@app.get("/api/demo-audio")
def get_legacy_demo_audio():
    return get_track_audio("synthwave_neon")


@app.get("/api/demo-data")
def get_legacy_demo_data():
    return get_track_data("synthwave_neon")


# Mount static web directory
web_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "web")
if not os.path.exists(web_dir):
    os.makedirs(web_dir, exist_ok=True)

app.mount("/", StaticFiles(directory=web_dir, html=True), name="web")
