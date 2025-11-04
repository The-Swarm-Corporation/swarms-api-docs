import requests
from dotenv import load_dotenv

load_dotenv()

# First, add a prompt to get an ID
prompt_data = {
    "name": "Test Prompt for Editing",
    "prompt": "This is a test prompt that will be edited.",
    "description": "A test prompt for editing functionality.",
    "useCases": [
        {"title": "Testing", "description": "Used for testing edit functionality."}
    ],
    "tags": "test,editing",
    "is_free": True,
    "category": "test",
}

add_url = "http://localhost:3000/api/add-prompt"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ",
}

# Add the prompt first
add_response = requests.post(add_url, json=prompt_data, headers=headers)
print("Add Prompt Response:")
print("Status Code:", add_response.status_code)
print("Response:", add_response.json())

# If successful, edit the prompt
if add_response.status_code == 200:
    prompt_id = add_response.json().get("id")

    # Update data
    update_data = {
        "id": prompt_id,
        "name": "Updated Test Prompt",
        "prompt": "This is an UPDATED test prompt with new content and image.",
        "description": "Updated description with enhanced features.",
        "useCases": [
            {
                "title": "Updated Testing",
                "description": "Enhanced testing functionality with new features.",
            }
        ],
        "tags": "test,editing,updated,enhanced",
        "is_free": True,
        "category": ["test", "updated"],
        "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&h=400&fit=crop",
        "links": [
            {"name": "Test Documentation", "url": "https://example.com/test-docs"}
        ],
    }

    # Edit the prompt
    edit_url = "http://localhost:3000/api/edit-prompt"
    edit_response = requests.post(edit_url, json=update_data, headers=headers)
    print("\nEdit Prompt Response:")
    print("Status Code:", edit_response.status_code)
    print("Response:", edit_response.json())
else:
    print("Failed to add prompt, skipping edit test")
