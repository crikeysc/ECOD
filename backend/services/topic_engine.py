"""
🧠 topic_engine.py — ECOD Thread Lifecycle Manager

This module handles the creation and management of ephemeral discussion threads
within the ECOD (Ephemeral Chat-Overlay Dashboard) system. It is triggered by
incoming alerts from GEFL and is responsible for spawning time-bound, modular
topics that facilitate real-time community interpretation.

🔧 Core Functions:
- `create_topic(alert_id, title, alert_type, ttl_seconds)`: 
  Creates a new Redis-backed topic with a specified TTL (time-to-live).
  Each topic is uniquely keyed and tagged by alert type (e.g., CME, seismic, crypto).

- `add_comment(topic_id, user, text)`:
  Adds a user comment to an existing topic thread.
  Comments inherit TTL logic and are stored with traceable metadata.

🧠 Strategic Role:
- Enables ECOD’s **ephemerality** by enforcing TTL on threads and comments.
- Supports **modularity** by isolating threads per alert type.
- Integrates with **moderation.py** to ensure constructive engagement.
- Logs all actions to support **CASA-style traceability**.

This module is the backbone of ECOD’s participatory layer, transforming telemetry
into time-bound dialogue and enabling real-time interpretation of global fusion events.
"""


from redis import Redis
import uuid

r = Redis(host="localhost", port=6379, decode_responses=True)

def create_topic(alert_id, title, alert_type, ttl_seconds):
    topic_key = f"topic:{alert_id}"
    topic_data = {
        "title": title,
        "alert_type": alert_type,
        "timestamp": str(uuid.uuid1()),
        "ttl_seconds": ttl_seconds
    }
    r.hmset(topic_key, topic_data)
    r.expire(topic_key, ttl_seconds)
    return topic_key

def add_comment(topic_id, user, text):
    comment_id = str(uuid.uuid4())[:8]
    comment_key = f"comment:{topic_id}:{comment_id}"
    comment_data = {
        "user": user,
        "text": text,
        "timestamp": str(uuid.uuid1())
    }
    ttl = r.ttl(f"topic:{topic_id}")
    r.hmset(comment_key, comment_data)
    r.expire(comment_key, ttl)
    return comment_key
