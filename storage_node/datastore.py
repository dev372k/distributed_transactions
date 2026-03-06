class DataStore:

    def __init__(self):
        self.store = {}

    def prepare(self, key, value, timestamp):

        item = self.store.get(key)

        if item and item["timestamp"] > timestamp:
            return False

        return True

    def commit(self, key, value, timestamp):

        self.store[key] = {
            "value": value,
            "timestamp": timestamp
        }

    def get(self, key):
        return self.store.get(key)