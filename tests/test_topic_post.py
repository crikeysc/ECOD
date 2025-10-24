import requests

payload = {
    "alert_id": "solar_flare_20250906",
    "title": "X-Class Solar Flare Detected",
    "alert_type": "space_weather",
    "ttl_seconds": 1800
}

res = requests.post("http://localhost:5000/topic", json=payload)
print("Response:", res.status_code)
print("Payload:", res.json())
