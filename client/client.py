import requests

transaction = {
    "operations": [
        {"type": "PUT", "key": "A", "value": 100},
        {"type": "PUT", "key": "B", "value": 200}
    ]
}

r = requests.post(
    "http://localhost:9000/transaction",
    json=transaction
)

print(r.json())