# 🔌 RedisTelemetryClient — ECOD Telemetry Wrapper

from backend.utils.redis_client import get_redis_connection

class RedisTelemetryClient:
    def __init__(self):
        self.client = get_redis_connection()

    # ⏱️ TTL-Aware Setter
    def set_ephemeral(self, key, value, ttl_seconds):
        self.client.setex(key, ttl_seconds, value)

    # 🏷️ Modular Key Formatter
    def format_key(self, module, topic_id, suffix):
        return f"{module}:{topic_id}:{suffix}"

    # 📣 Pub/Sub Publisher
    def publish(self, channel, message):
        self.client.publish(channel, message)

    # 🛡️ Safe Connection Check (Optional)
    def is_connected(self):
        try:
            return self.client.ping()
        except Exception:
            return False
