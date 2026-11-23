"""
SoundScope-AI: Application Launcher
Starts the FastAPI server with the interactive web dashboard.
Run with: python app.py
"""

import uvicorn
import webbrowser
import threading
import time

def open_browser():
    time.sleep(1.2)
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    print("=" * 65)
    print(">> Starting SoundScope-AI Platform...")
    print(">> Dashboard URL: http://127.0.0.1:8000")
    print(">> API Docs:      http://127.0.0.1:8000/docs")
    print("=" * 65)

    # Launch browser automatically
    threading.Thread(target=open_browser, daemon=True).start()

    uvicorn.run("src.api.main:app", host="127.0.0.1", port=8000, reload=False)
