import requests

transaction = {
    "operations": [
        {"type": "PUT", "key": "a550e8400-e29b-41d4-a716-446655440000", "value": {"user_id": 1, "name": "Alice Brown"}},
        {"type": "PUT", "key": "b3fa85f64-5717-4562-b3fc-2c963f66afa6", "value": {"user_id": 2, "name": "Carlos Diaz"}},
        {"type": "PUT", "key": "c9b2c2d31-1c6a-4d1c-9c0f-5b3a1a2c4d5e", "value": {"user_id": 3, "name": "Fatima Khan"}},
        {"type": "PUT", "key": "d7c9e6679-7425-40de-944b-e07fc1f90ae7", "value": {"user_id": 4, "name": "Hiro Tanaka"}},
        {"type": "PUT", "key": "e1d7f3a20-98b1-4b0e-8c5f-2a8c0f7e1234", "value": {"user_id": 5, "name": "George Hill"}},
        {"type": "PUT", "key": "f2e1c4b70-0c4b-4c7d-a8a5-8d7a1c9b5678", "value": {"user_id": 6, "name": "Isabella Garcia"}},
        {"type": "PUT", "key": "g123e4567-e89b-12d3-a456-426614174000", "value": {"user_id": 7, "name": "Mia Novak"}},
        {"type": "PUT", "key": "h987f6543-b21c-45d6-a123-789456123abc", "value": {"user_id": 8, "name": "Omar Hassan"}},
        {"type": "PUT", "key": "i4567abcd-1234-4abc-9def-abcdef123456", "value": {"user_id": 9, "name": "Nina Olsen"}},
        {"type": "PUT", "key": "j321cba98-7654-4fed-b321-fedcba654321", "value": {"user_id": 10, "name": "Peter Novak"}},
        {"type": "PUT", "key": "k741852963-a1b2-4c3d-9e8f-123abc456def", "value": {"user_id": 11, "name": "Zara Ali"}},
        {"type": "PUT", "key": "l159753486-c1d2-4e3f-a9b8-456def789abc", "value": {"user_id": 12, "name": "Ben Zhou"}}
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