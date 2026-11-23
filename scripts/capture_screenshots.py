"""
Script to capture high-resolution LinkedIn screenshots of SoundScope-AI.
Captures:
1. soundscope_dashboard_hero.png (High-DPI viewport of the main studio dashboard)
2. soundscope_multi_agent_system.png (Close-up of LangGraph agents & verification guardrails)
3. soundscope_full_overview.png (Complete full-page dashboard overview)
"""

import os
import time
from playwright.sync_api import sync_playwright

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "screenshots")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def capture_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # 1920x1080 with 2x device scale factor for ultra-sharp Retina rendering
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=2
        )
        page = context.new_page()

        print("Navigating to http://127.0.0.1:8000...")
        page.goto("http://127.0.0.1:8000", wait_until="networkidle")

        # Give 2.5 seconds for waveform canvas and state to settle
        time.sleep(2.5)

        # 1. Capture Hero Overview (Studio Dual-Branch Ingestion + Metrics)
        hero_path = os.path.join(OUTPUT_DIR, "01_soundscope_dashboard_hero.png")
        page.screenshot(path=hero_path)
        print(f"Captured: {hero_path}")

        # 2. Scroll to LangGraph Multi-Agent & Guardrail section
        agent_section = page.locator("section:has-text('LangGraph Multi-Agent')")
        if agent_section.count() > 0:
            agent_section.scroll_into_view_if_needed()
            time.sleep(1.0)
            agent_path = os.path.join(OUTPUT_DIR, "02_soundscope_multi_agent_guardrails.png")
            agent_section.screenshot(path=agent_path)
            print(f"Captured: {agent_path}")
        else:
            # Fallback scroll
            page.evaluate("window.scrollTo(0, 500)")
            time.sleep(1.0)
            agent_path = os.path.join(OUTPUT_DIR, "02_soundscope_multi_agent_guardrails.png")
            page.screenshot(path=agent_path)
            print(f"Captured: {agent_path}")

        # 3. Full page capture
        full_path = os.path.join(OUTPUT_DIR, "03_soundscope_full_system.png")
        page.screenshot(path=full_path, full_page=True)
        print(f"Captured: {full_path}")

        browser.close()
        print("All screenshots successfully captured!")

if __name__ == "__main__":
    capture_screenshots()
