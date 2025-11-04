import requests
from dotenv import load_dotenv

load_dotenv()

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ",
}

user_products_url = "http://localhost:3000/api/user-products"

print("=== Testing User Products API ===\n")

# Test 1: Get all products for user
print("1. Get all products for user 'Playeds':")
query_data1 = {
    "username": "Playeds",
    "include_metadata": True,
    "page": 1,
    "limit": 10,
    "product_type": "all",
}
response1 = requests.post(user_products_url, json=query_data1, headers=headers)
print("Status Code:", response1.status_code)
print("Response:", response1.json())
