"""
🛡️ moderation.py — ECOD Comment Filter

This module provides basic moderation logic for ECOD’s participatory threads.
It currently uses a keyword-based stub to flag potentially toxic or disruptive
comments, and is designed to be replaced with a more robust ML model such as
Detoxify or a custom transformer pipeline.

🔧 Core Function:
- `moderate_comment(text)`:
  Scans incoming comment text for flagged keywords (e.g., "panic", "scam").
  Returns a status of `"flagged"` or `"approved"` with matched terms.

🧠 Strategic Role:
- Supports ECOD’s **moderation principle** by filtering out harmful or distracting content.
- Enables **constructive engagement** by keeping threads focused and civil.
- Designed for future expansion into ML-based moderation with explainable outputs.

This stub ensures basic safety while allowing rapid iteration. It can be swapped
for a model-based filter without disrupting the API contract or backend flow.
"""


# Stub moderation logic – replace with Detoxify or custom ML later
def moderate_comment(text):
    flagged_keywords = ["panic", "scam", "rugpull", "dump"]
    flags = [word for word in flagged_keywords if word in text.lower()]
    
    if flags:
        return {
            "status": "flagged",
            "flags": flags
        }
    return {
        "status": "approved",
        "flags": []
    }
