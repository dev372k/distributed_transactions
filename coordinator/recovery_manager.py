from ledger import read_ledger, update_transaction_status

def recover_pending_transactions():

    records = read_ledger()

    for rec in records:

        if rec["status"] == "PENDING":

            print(f"Recovering transaction {rec['transaction_id']}")

            # For now we mark it aborted
            update_transaction_status(rec["transaction_id"], "ABORTED")

            print("Marked as ABORTED")