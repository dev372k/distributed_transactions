import requests

transaction = {
    "operations": [
        {"type": "PUT", "key": "A", "value": 100},
        {"type": "PUT", "key": "AD", "value": 900},
        {"type": "PUT", "key": "F", "value": 200},
        {"type": "PUT", "key": "G", "value": 300},
        {"type": "PUT", "key": "M", "value": 400},
        {"type": "PUT", "key": "N", "value": 500},
        {"type": "PUT", "key": "Z", "value": 600}
    ]
}

r = requests.post(
    "http://localhost:9000/transaction",
    json=transaction
)

print("Status Code:", r.status_code)
print("Raw Response:", r.text)

try:
    print("JSON:", r.json())
except:
    print("Response is not JSON")