from fastapi import FastAPI
from datastore import DataStore

app = FastAPI()
db = DataStore()


@app.post("/prepare")
def prepare(data: dict):

    key = data["key"]
    value = data["value"]
    timestamp = data["timestamp"]

    success = db.prepare(key, value, timestamp)

    return {"success": success}


@app.post("/commit")
def commit(data: dict):

    key = data["key"]
    value = data["value"]
    timestamp = data["timestamp"]

    db.commit(key, value, timestamp)

    return {"status": "committed"}


@app.get("/get/{key}")
def get(key: str):

    return db.get(key)