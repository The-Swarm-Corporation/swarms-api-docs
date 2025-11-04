import requests
from dotenv import load_dotenv

load_dotenv()

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ",
}

user_products_url = "http://localhost:3000/api/user-products"

print("=== Debug User Products API ===\n")

# Test 1: Minimal request
print("1. Minimal request:")
query_data1 = {"username": "swarms1212"}
response1 = requests.post(user_products_url, json=query_data1, headers=headers)
print(response1.json())
