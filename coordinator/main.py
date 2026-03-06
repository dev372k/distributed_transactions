from fastapi import FastAPI
from transaction_manager import execute_transaction

app = FastAPI()


@app.post("/transaction")
def run_transaction(transaction: dict):

    result = execute_transaction(transaction)

    return result