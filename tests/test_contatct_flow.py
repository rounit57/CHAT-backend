import requests

url = "http://localhost:8000/api/contact"

payload = {
    "inquiry_type": "General",
    "first_name": "Test",
    "last_name": "User",
    "email": "test@example.com",
    "state": "Tamil Nadu",
    "city": "Chennai",
    "zipcode": "600036",
    "message": "Testing aligned backend"
}

res = requests.post(url, json=payload)
print(res.status_code, res.json())
