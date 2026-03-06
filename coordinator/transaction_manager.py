import requests
import time

STORAGE_NODES = [
    "http://localhost:8001",
    "http://localhost:8002",
    "http://localhost:8003"
]


def execute_transaction(transaction):

    timestamp = int(time.time())

    # PREPARE PHASE
    for op in transaction["operations"]:

        for node in STORAGE_NODES:

            r = requests.post(
                f"{node}/prepare",
                json={
                    "key": op["key"],
                    "value": op["value"],
                    "timestamp": timestamp
                }
            )

            if not r.json()["success"]:
                return {"status": "aborted"}

    # COMMIT PHASE
    for op in transaction["operations"]:

        for node in STORAGE_NODES:

            requests.post(
                f"{node}/commit",
                json={
                    "key": op["key"],
                    "value": op["value"],
                    "timestamp": timestamp
                }
            )

    return {"status": "committed"}