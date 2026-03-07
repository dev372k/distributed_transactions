from fastapi import FastAPI
from transaction_manager import execute_transaction
from recovery_manager import recover_pending_transactions

app = FastAPI()

@app.on_event("startup")
def startup_event():

    recover_pending_transactions()


@app.post("/transaction")
def run_transaction(transaction: dict):

    result = execute_transaction(transaction)

    return result

@app.get("/get/{key}")
def read_key(key: str):
    return read_key(key)