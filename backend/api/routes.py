# 📡 ECOD API Routes — Flask Interface (with RedisTelemetryClient)

from flask import Flask, request, jsonify
from backend.services.redis_telemetry import RedisTelemetryClient
from backend.services.moderation import moderate_comment

app = Flask(__name__)
redis_client = RedisTelemetryClient()

@app.route("/topic", methods=["POST"])
def create_ttl_topic():
    data = request.get_json()
    alert_id = data.get("alert_id")
    title = data.get("title")
    alert_type = data.get("alert_type")
    ttl_seconds = data.get("ttl_seconds", 3600)

    # ✅ Input validation
    if not all([alert_id, title, alert_type]):
        return jsonify({"error": "Missing required fields: alert_id, title, alert_type"}), 400

    topic_key = redis_client.format_key("ECOD", alert_id, "thread")
    topic_value = f"{title}|{alert_type}"
    redis_client.set_ephemeral(topic_key, topic_value, ttl_seconds)

    return jsonify({"status": "created", "topic_key": topic_key}), 201

@app.route("/comment", methods=["POST"])
def submit_comment():
    data = request.get_json()
    topic_id = data.get("topic_id")
    user = data.get("user")
    text = data.get("text")

    # ✅ Input validation
    if not all([topic_id, user, text]):
        return jsonify({"error": "Missing required fields: topic_id, user, text"}), 400

    moderation = moderate_comment(text)

    # ✅ Moderation feedback
    if moderation["status"] == "flagged":
        return jsonify({
            "status": "rejected",
            "reason": "Comment flagged by moderation filter",
            "scores": moderation.get("scores", {})
        }), 403

    comment_key = redis_client.format_key("ECOD", topic_id, "comment")
    comment_value = f"{user}: {text}"
    redis_client.set_ephemeral(comment_key, comment_value, 3600)
    redis_client.publish("ECOD:comment_updates", comment_value)

    return jsonify({"status": "accepted", "comment_key": comment_key}), 201

# ✅ Health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    if redis_client.is_connected():
        return jsonify({"status": "healthy"}), 200
    else:
        return jsonify({"status": "redis unreachable"}), 503
