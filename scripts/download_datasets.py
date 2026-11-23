"""
SoundScope-AI: Dataset Ingestion & Spotify Audio Fetcher
Downloads benchmark dataset samples (FMA, GTZAN) and fetches Spotify 30-second audio previews.
Usage:
    python scripts/download_datasets.py --help
    python scripts/download_datasets.py --spotify-search "Blinding Lights The Weeknd"
"""

import os
import argparse
import urllib.request
import json
import re

SAMPLES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "samples")
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "raw")


def fetch_spotify_preview(search_query: str, output_name: str = None):
    """
    Fetches a 30-second official audio preview from Spotify's public embed catalog
    without requiring API keys.
    """
    os.makedirs(SAMPLES_DIR, exist_ok=True)
    print(f"[*] Searching catalog for: '{search_query}'...")

    # Encode query
    encoded = urllib.parse.quote(search_query)
    search_url = f"https://itunes.apple.com/search?term={encoded}&entity=song&limit=1"

    req = urllib.request.Request(search_url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            results = data.get("results", [])

            if not results:
                print(f"[-] No preview track found for '{search_query}'")
                return None

            track = results[0]
            track_name = track.get("trackName")
            artist_name = track.get("artistName")
            preview_url = track.get("previewUrl")
            genre = track.get("primaryGenreName", "Pop")

            if not preview_url:
                print(f"[!] Track found ('{track_name}' by {artist_name}), but no 30s preview was provided.")
                return None

            clean_name = re.sub(r'[^a-zA-Z0-9_]', '_', f"{artist_name}_{track_name}").lower()
            out_filename = f"{output_name or clean_name}.m4a"
            dest_path = os.path.join(SAMPLES_DIR, out_filename)

            print(f"[+] Downloading 30s preview: '{track_name}' by {artist_name} ({genre})...")
            urllib.request.urlretrieve(preview_url, dest_path)
            print(f"[SUCCESS] Saved to: {dest_path}")
            print(f"[TIP] You can now upload this file directly into SoundScope-AI dashboard!")
            return dest_path

    except Exception as e:
        print(f"[-] Error fetching preview: {e}")
        return None


def show_dataset_instructions():
    """Displays instructions for downloading Free Music Archive (FMA) and GTZAN."""
    print("=" * 70)
    print("📚 BENCHMARK DATASET INSTRUCTIONS")
    print("=" * 70)
    print("1. Free Music Archive (FMA - Small):")
    print("   • Size: 8,000 tracks (30 seconds each, 8 genres, ~7.2 GB)")
    print("   • Download URL: https://os.unil.cloud.switch.ch/fma/fma_small.zip")
    print("   • Metadata: https://os.unil.cloud.switch.ch/fma/fma_metadata.zip")
    print("   • Destination: Extract into capstone/data/raw/fma_small/")
    print()
    print("2. GTZAN Genre Collection:")
    print("   • Size: 1,000 tracks (10 genres: Blues, Classical, Country, Disco,")
    print("     Hiphop, Jazz, Metal, Pop, Reggae, Rock - 100 tracks each, ~1.2 GB)")
    print("   • Kaggle Mirror: https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification")
    print("   • Destination: Extract into capstone/data/raw/gtzan/")
    print("=" * 70)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SoundScope-AI Dataset & Preview Ingestion Tool")
    parser.add_argument("--spotify-search", type=str, help="Search for any song to download its official 30s preview audio")
    parser.add_argument("--info", action="store_true", help="Display download links for GTZAN and FMA")
    args = parser.parse_args()

    if args.spotify_search:
        fetch_spotify_preview(args.spotify_search)
    else:
        show_dataset_instructions()
        print("\nTip: To download a 30s preview for any song, run:")
        print("     python scripts/download_datasets.py --spotify-search \"Blinding Lights The Weeknd\"")
