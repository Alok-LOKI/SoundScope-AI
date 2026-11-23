"""
Rename all chat screenshots and LinkedIn screenshots with clean, academic descriptive names.
"""
import os
import shutil

CHATS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "chats with ai")
LINKEDIN_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "linkdin post ss")

CHAT_RENAME_MAP = {
    "Screenshot 2026-10-26 223053.png": "01_dialogue1_dual_branch_vs_monolithic_table.png",
    "Screenshot 2026-10-26 223150.png": "02_dialogue1_modular_architecture_flow.png",
    "Screenshot 2026-10-26 223208.png": "03_dialogue2_audio_dataset_selection.png",
    "Screenshot 2026-10-26 223226.png": "04_dialogue2_unlabelled_audio_and_transcription.png",
    "Screenshot 2026-10-26 223443.png": "05_dialogue3_llm_hallucination_prevention.png",
    "Screenshot 2026-10-26 223302.png": "06_dialogue3_deterministic_verifier_node.png",
    "Screenshot 2026-10-26 223319.png": "07_dialogue4_sprint_timeline_plan.png",
    "Screenshot 2026-10-26 223603.png": "08_dialogue4_sprint_rules_and_milestones.png",
}

LINKEDIN_RENAME_MAP = {
    "Screenshot 2026-10-26 223715.png": "linkedin_post_01_text_and_author_profile.png",
    "Screenshot 2026-10-26 223755.png": "linkedin_post_02_attached_images_and_engagement.png",
}

print("--- Renaming Chat Screenshots ---")
for old_name, new_name in CHAT_RENAME_MAP.items():
    old_p = os.path.join(CHATS_DIR, old_name)
    new_p = os.path.join(CHATS_DIR, new_name)
    if os.path.exists(old_p):
        os.rename(old_p, new_p)
        print(f"Renamed: {old_name} -> {new_name}")
    elif os.path.exists(new_p):
        print(f"Already renamed: {new_name}")

print("\n--- Renaming LinkedIn Post Screenshots ---")
for old_name, new_name in LINKEDIN_RENAME_MAP.items():
    old_p = os.path.join(LINKEDIN_DIR, old_name)
    new_p = os.path.join(LINKEDIN_DIR, new_name)
    if os.path.exists(old_p):
        os.rename(old_p, new_p)
        print(f"Renamed: {old_name} -> {new_name}")
    elif os.path.exists(new_p):
        print(f"Already renamed: {new_name}")

print("\nAll files successfully renamed!")
