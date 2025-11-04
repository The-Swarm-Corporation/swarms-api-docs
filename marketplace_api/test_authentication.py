import requests
from dotenv import load_dotenv

load_dotenv()

print("=== Testing Authentication Requirements ===\n")

# Test data
prompt_data = {
    "name": "Authentication Test Prompt",
    "prompt": "This is a test prompt for authentication testing.",
    "description": "Testing authentication requirements.",
    "useCases": [
        {
            "title": "Authentication Test",
            "description": "Testing authentication functionality.",
        }
    ],
    "tags": "auth,test",
    "is_free": True,
    "category": "test",
}

agent_data = {
    "name": "Authentication Test Agent",
    "agent": "This is a test agent for authentication testing.",
    "description": "Testing authentication requirements.",
    "requirements": [{"package": "requests", "installation": "pip install requests"}],
    "useCases": [
        {
            "title": "Authentication Test",
            "description": "Testing authentication functionality.",
        }
    ],
    "tags": "auth,test",
    "is_free": True,
    "category": "test",
    "language": "python",
}

# Test 1: No authentication
print("1. Testing without authentication (should fail):")
print("   Prompt creation:")
response1 = requests.post("http://localhost:3000/api/add-prompt", json=prompt_data)
print(f"   Status Code: {response1.status_code}")
print(f"   Response: {response1.json()}")
print()

print("   Agent creation:")
response2 = requests.post("http://localhost:3000/api/add-agent", json=agent_data)
print(f"   Status Code: {response2.status_code}")
print(f"   Response: {response2.json()}")
print()

# Test 2: Invalid API key
print("2. Testing with invalid API key (should fail):")
invalid_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer invalid-api-key-12345",
}

print("   Prompt creation:")
response3 = requests.post(
    "http://localhost:3000/api/add-prompt", json=prompt_data, headers=invalid_headers
)
print(f"   Status Code: {response3.status_code}")
print(f"   Response: {response3.json()}")
print()

print("   Agent creation:")
response4 = requests.post(
    "http://localhost:3000/api/add-agent", json=agent_data, headers=invalid_headers
)
print(f"   Status Code: {response4.status_code}")
print(f"   Response: {response4.json()}")
print()

# Test 3: Valid API key
print("3. Testing with valid API key (should succeed):")
valid_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ",
}

print("   Prompt creation:")
response5 = requests.post(
    "http://localhost:3000/api/add-prompt", json=prompt_data, headers=valid_headers
)
print(f"   Status Code: {response5.status_code}")
print(f"   Response: {response5.json()}")
print()

print("   Agent creation:")
response6 = requests.post(
    "http://localhost:3000/api/add-agent", json=agent_data, headers=valid_headers
)
print(f"   Status Code: {response6.status_code}")
print(f"   Response: {response6.json()}")
print()

# Test 4: Query endpoints without authentication (should work)
print("4. Testing query endpoints without authentication (should work):")
print("   Query prompts:")
response7 = requests.get("http://localhost:3000/api/query-prompts?q=test")
print(f"   Status Code: {response7.status_code}")
print(f"   Response: {response7.json()}")
print()

print("   Query agents:")
response8 = requests.get("http://localhost:3000/api/query-agents?q=test")
print(f"   Status Code: {response8.status_code}")
print(f"   Response: {response8.json()}")
