# test_redis.py
from backend.utils.redis_client import get_redis_connection

r = get_redis_connection()
r.set("ecod_test_key", "hello_ecod")
print("Redis says:", r.get("ecod_test_key"))
