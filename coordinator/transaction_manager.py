import requests
import time
from ledger import create_transaction_record, update_transaction_status

PARTITIONS = {
    "node1": {
        "range": ("A", "F"),
        "url": "http://localhost:8001"
    },
    "node2": {
        "range": ("G", "M"),
        "url": "http://localhost:8002"
    },
    "node3": {
        "range": ("N", "Z"),
        "url": "http://localhost:8003"
    }
}

def get_node_for_key(key):

    first_letter = key[0].upper()

    for node in PARTITIONS.values():
        start, end = node["range"]

        if start <= first_letter <= end:
            return node["url"]

    raise Exception("Partition not found")

def execute_transaction(transaction, retries=3):

    for attempt in range(retries):

        timestamp = int(time.time())

        # PREPARE PHASE
        success = True

        for op in transaction["operations"]:

            node = get_node_for_key(op["key"])

            r = requests.post(
                f"{node}/prepare",
                json={
                    "key": op["key"],
                    "value": op["value"],
                    "timestamp": timestamp
                }
            )

            if not r.json()["success"]:
                success = False
                break

        if not success:
            print("Conflict detected. Retrying...")
            time.sleep(1)
            continue

        # COMMIT PHASE
        for op in transaction["operations"]:

            node = get_node_for_key(op["key"])

            requests.post(
                f"{node}/commit",
                json={
                    "key": op["key"],
                    "value": op["value"],
                    "timestamp": timestamp
                }
            )

        return {"status": "committed"}

    return {"status": "aborted_due_to_conflict"}

def read_key(key):
    node = get_node_for_key(key)
    r = requests.get(f"{node}/get/{key}")
    return r.json()