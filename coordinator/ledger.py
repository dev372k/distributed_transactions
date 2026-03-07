import json
import time
import uuid

LEDGER_FILE = "transaction_ledger.log"

def create_transaction_record(transaction):

    record = {
        "transaction_id": str(uuid.uuid4()),
        "timestamp": int(time.time()),
        "operations": transaction["operations"],
        "status": "PENDING"
    }

    with open(LEDGER_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")

    return record


def update_transaction_status(transaction_id, status):

    records = []

    with open(LEDGER_FILE, "r") as f:
        for line in f:
            rec = json.loads(line)

            if rec["transaction_id"] == transaction_id:
                rec["status"] = status

            records.append(rec)

    with open(LEDGER_FILE, "w") as f:
        for rec in records:
            f.write(json.dumps(rec) + "\n")

def read_ledger():

    records = []

    try:
        with open(LEDGER_FILE, "r") as f:
            for line in f:
                records.append(json.loads(line))
    except FileNotFoundError:
        return []

    return records