"""
🔌 redis_client.py — ECOD Redis Connector

This module provides a reusable connection interface to the Redis server,
used throughout ECOD’s backend to manage ephemeral topic and comment data.

🔧 Core Function:
- `get_redis_connection()`:
  Returns a Redis client instance using environment variables for host and port.
  Defaults to localhost:6379 if not explicitly set.

🧠 Strategic Role:
- Powers ECOD’s **ephemerality** by enabling TTL-based storage of threads and comments.
- Keeps Redis logic modular and centralized for easy reuse across `topic_engine.py`, `api_routes.py`, and other backend modules.
- Supports **containerization** and **scalability** by allowing Redis config to be injected via Docker or deployment scripts.

This module is foundational to ECOD’s time-bound discussion model, enabling fast, in-memory storage with automatic expiry.
"""


# 🔌 redis_client.py — ECOD Redis Connector (Enhanced)

import redis
import os

# 🔧 Core Redis Connection
def get_redis_connection():
    return redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        db=0,
        decode_responses=True
    )

# 🛡️ Safe Connection Wrapper (for dev or container fallback)
def safe_get_connection():
    try:
        return get_redis_connection()
    except redis.ConnectionError:
        print("Redis connection failed. Check container linkage.")
        return None

# ⏱️ TTL-Aware Setter
def set_with_ttl(key, value, ttl_seconds):
    client = get_redis_connection()
    client.setex(key, ttl_seconds, value)

# 🏷️ Modular Key Formatter
def format_key(module, topic_id, suffix):
    return f"{module}:{topic_id}:{suffix}"

# 📣 Pub/Sub Publisher (Optional)
def publish_event(channel, message):
    client = get_redis_connection()
    client.publish(channel, message)
