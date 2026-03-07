from fastapi import FastAPI
from fastapi.responses import FileResponse
import requests
import redis
import json

app = FastAPI()

NODES = [
    "http://storage_node1:8001",
    "http://storage_node2:8002",
    "http://storage_node3:8003"
]

REDIS_PORTS = [6379, 6380, 6381]


@app.get("/nodes")
def node_status():

    status = []

    for node in NODES:

        try:
            r = requests.get(f"{node}/docs")

            if r.status_code == 200:
                status.append({"node": node, "status": "healthy"})
            else:
                status.append({"node": node, "status": "error"})

        except:
            status.append({"node": node, "status": "down"})

    return status


@app.get("/redis")
def redis_stats():

    stats = []

    for port in REDIS_PORTS:

        r = redis.Redis(host="localhost", port=port, decode_responses=True)

        keys = r.keys("*")

        stats.append({
            "redis_port": port,
            "key_count": len(keys),
            "keys": keys
        })

    return stats


@app.get("/transactions")
def transaction_stats():

    committed = 0
    aborted = 0
    pending = 0

    try:

        with open("../coordinator/transaction_ledger.log", "r") as f:

            for line in f:

                rec = json.loads(line)

                if rec["status"] == "COMMITTED":
                    committed += 1

                elif rec["status"] == "ABORTED":
                    aborted += 1

                elif rec["status"] == "PENDING":
                    pending += 1

    except:
        pass

    return {
        "committed": committed,
        "aborted": aborted,
        "pending": pending
    }

@app.get("/")
def dashboard():
    return FileResponse("dashboard.html")