import redis
import os
import json


class DataStore:

    def __init__(self):

        redis_host = os.getenv("REDIS_HOST", "localhost")
        redis_port = int(os.getenv("REDIS_PORT", 6379))

        self.redis = redis.Redis(
            host=redis_host,
            port=redis_port,
            decode_responses=True
        )

    def prepare(self, key, value, timestamp):

        item = self.redis.get(key)

        if item:

            item = json.loads(item)

            last_timestamp = item["timestamp"]

            if timestamp <= last_timestamp:
                print(f"Conflict detected for key {key}")
                return False

        return True

    def commit(self, key, value, timestamp):

        item = {
            "value": value,
            "timestamp": timestamp
        }

        self.redis.set(key, json.dumps(item))

    def get(self, key):

        item = self.redis.get(key)

        if item:
            return json.loads(item)

        return None