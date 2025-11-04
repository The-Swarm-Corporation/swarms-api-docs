import requests
from dotenv import load_dotenv

load_dotenv()

# First, add an agent to get an ID
agent_data = {
    "name": "Test Agent for Editing",
    "agent": "This is a test agent that will be edited.",
    "description": "A test agent for editing functionality.",
    "requirements": [{"package": "requests", "installation": "pip install requests"}],
    "useCases": [
        {"title": "Testing", "description": "Used for testing edit functionality."}
    ],
    "tags": "test,editing",
    "is_free": True,
    "category": "test",
    "language": "python",
}

add_url = "http://localhost:3000/api/add-agent"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ",
}

# Add the agent first
add_response = requests.post(add_url, json=agent_data, headers=headers)
print("Add Agent Response:")
print("Status Code:", add_response.status_code)
print("Response:", add_response.json())

# If successful, edit the agent
if add_response.status_code == 200:
    agent_id = add_response.json().get("id")

    # Update data
    update_data = {
        "id": agent_id,
        "name": "Updated Test Agent",
        "agent": "This is an UPDATED test agent with enhanced capabilities and new features.",
        "description": "Updated description with advanced functionality and improved performance.",
        "requirements": [
            {"package": "requests", "installation": "pip install requests"},
            {"package": "numpy", "installation": "pip install numpy"},
        ],
        "useCases": [
            {
                "title": "Updated Testing",
                "description": "Enhanced testing functionality with advanced features.",
            },
            {
                "title": "Performance Testing",
                "description": "Test system performance and optimization.",
            },
        ],
        "tags": "test,editing,updated,enhanced,performance",
        "is_free": True,
        "category": ["test", "updated"],
        "language": "python",
        "image_url": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=600&h=400&fit=crop",
        "links": [
            {"name": "Agent Documentation", "url": "https://example.com/agent-docs"}
        ],
    }

    # Edit the agent
    edit_url = "http://localhost:3000/api/edit-agent"
    edit_response = requests.post(edit_url, json=update_data, headers=headers)
    print("\nEdit Agent Response:")
    print("Status Code:", edit_response.status_code)
    print("Response:", edit_response.json())
else:
    print("Failed to add agent, skipping edit test")
