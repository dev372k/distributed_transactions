import requests
import random
import time
from concurrent.futures import ThreadPoolExecutor

URL = "http://localhost:9000/transaction"

keys = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

TOTAL_REQUESTS = 500
CONCURRENCY = 20

results = {
    "committed": 0,
    "aborted": 0
}

latencies = []


def send_transaction():

    key = random.choice(keys)

    transaction = {
        "operations": [
            {"type": "PUT", "key": key, "value": random.randint(1, 1000)}
        ]
    }

    start = time.time()

    try:
        r = requests.post(URL, json=transaction)
        latency = time.time() - start

        latencies.append(latency)

        if r.json()["status"] == "committed":
            results["committed"] += 1
        else:
            results["aborted"] += 1

    except:
        results["aborted"] += 1


start_time = time.time()

with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
    for _ in range(TOTAL_REQUESTS):
        executor.submit(send_transaction)

end_time = time.time()

duration = end_time - start_time

print("\nLoad Test Results")
print("------------------")
print("Total Requests:", TOTAL_REQUESTS)
print("Committed:", results["committed"])
print("Aborted:", results["aborted"])
print("Duration:", round(duration, 2), "seconds")

if latencies:
    print("Average Latency:", round(sum(latencies)/len(latencies), 4), "seconds")

print("Throughput:", round(TOTAL_REQUESTS/duration, 2), "tx/sec")