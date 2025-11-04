import requests
import time
from dotenv import load_dotenv

load_dotenv()

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ",
}

print("=== Testing Rate Limiting ===\n")

# Test prompt creation rate limiting
print("Testing prompt creation rate limiting...")
prompt_url = "http://localhost:3000/api/add-prompt"

success_count = 0
rate_limited_count = 0
failed_count = 0

for i in range(10):
    prompt_data = {
        "name": f"Rate Limit Test Prompt {i+1}",
        "prompt": f"This is test prompt {i+1} for rate limiting testing.",
        "description": f"Test prompt {i+1} for rate limiting validation.",
        "useCases": [
            {
                "title": "Rate Limiting Test",
                "description": f"Testing rate limiting with prompt {i+1}.",
            }
        ],
        "tags": f"rate,limit,test,prompt-{i+1}",
        "is_free": True,
        "category": "test",
    }

    response = requests.post(prompt_url, json=prompt_data, headers=headers)

    if response.status_code == 200:
        success_count += 1
        print(f"✅ Prompt {i+1}: Success")
    elif response.status_code == 429:
        rate_limited_count += 1
        print(f"🚫 Prompt {i+1}: Rate Limited")
        print(f"   Response: {response.json()}")
    else:
        failed_count += 1
        print(f"❌ Prompt {i+1}: Failed (Status: {response.status_code})")
        print(f"   Response: {response.json()}")

    # Small delay between requests
    time.sleep(0.1)

print("\nRate Limiting Results:")
print(f"Successful: {success_count}")
print(f"Rate Limited: {rate_limited_count}")
print(f"Failed: {failed_count}")

# Test agent creation rate limiting
print("\n" + "=" * 50)
print("Testing agent creation rate limiting...")
agent_url = "http://localhost:3000/api/add-agent"

agent_success_count = 0
agent_rate_limited_count = 0
agent_failed_count = 0

for i in range(5):
    agent_data = {
        "name": f"Rate Limit Test Agent {i+1}",
        "agent": f"You are test agent {i+1} for rate limiting testing.",
        "description": f"Test agent {i+1} for rate limiting validation.",
        "requirements": [
            {"package": "requests", "installation": "pip install requests"}
        ],
        "useCases": [
            {
                "title": "Rate Limiting Test",
                "description": f"Testing rate limiting with agent {i+1}.",
            }
        ],
        "tags": f"rate,limit,test,agent-{i+1}",
        "is_free": True,
        "category": "test",
        "language": "python",
    }

    response = requests.post(agent_url, json=agent_data, headers=headers)

    if response.status_code == 200:
        agent_success_count += 1
        print(f"✅ Agent {i+1}: Success")
    elif response.status_code == 429:
        agent_rate_limited_count += 1
        print(f"🚫 Agent {i+1}: Rate Limited")
        print(f"   Response: {response.json()}")
    else:
        agent_failed_count += 1
        print(f"❌ Agent {i+1}: Failed (Status: {response.status_code})")
        print(f"   Response: {response.json()}")

    # Small delay between requests
    time.sleep(0.1)

print("\nAgent Rate Limiting Results:")
print(f"Successful: {agent_success_count}")
print(f"Rate Limited: {agent_rate_limited_count}")
print(f"Failed: {agent_failed_count}")
