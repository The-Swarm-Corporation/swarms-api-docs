import requests
from dotenv import load_dotenv

load_dotenv()

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ",
}

print("=== Testing Image Upload Functionality ===\n")

# Test 1: Prompt with image
print("1. Testing prompt creation with image:")
prompt_with_image = {
    "name": "Image Test Prompt",
    "prompt": "This is a test prompt with an image to verify image upload functionality.",
    "description": "Testing image upload capabilities for prompts.",
    "useCases": [
        {
            "title": "Image Testing",
            "description": "Testing image upload and display functionality.",
        }
    ],
    "tags": "image,test,upload",
    "is_free": True,
    "category": "test",
    "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500&h=300&fit=crop&ixlib=rb-4.1.0",
}

response1 = requests.post(
    "http://localhost:3000/api/add-prompt", json=prompt_with_image, headers=headers
)
print("Status Code:", response1.status_code)
print("Response:", response1.json())
print()

# Test 2: Agent with image
print("2. Testing agent creation with image:")
agent_with_image = {
    "name": "Image Test Agent",
    "agent": "This is a test agent with an image to verify image upload functionality.",
    "description": "Testing image upload capabilities for agents.",
    "requirements": [{"package": "requests", "installation": "pip install requests"}],
    "useCases": [
        {
            "title": "Image Testing",
            "description": "Testing image upload and display functionality.",
        }
    ],
    "tags": "image,test,upload",
    "is_free": True,
    "category": "test",
    "language": "python",
    "image_url": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=500&h=300&fit=crop&ixlib=rb-4.1.0",
}

response2 = requests.post(
    "http://localhost:3000/api/add-agent", json=agent_with_image, headers=headers
)
print("Status Code:", response2.status_code)
print("Response:", response2.json())
print()

# Test 3: Update prompt with different image
if response1.status_code == 200:
    prompt_id = response1.json().get("id")
    print("3. Testing prompt update with different image:")

    update_prompt = {
        "id": prompt_id,
        "name": "Updated Image Test Prompt",
        "prompt": "This is an updated test prompt with a different image.",
        "description": "Updated description with new image.",
        "useCases": [
            {
                "title": "Updated Image Testing",
                "description": "Testing image update functionality.",
            }
        ],
        "tags": "image,test,upload,updated",
        "is_free": True,
        "category": ["test", "updated"],
        "image_url": "https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=600&h=400&fit=crop&ixlib=rb-4.1.0",
    }

    response3 = requests.post(
        "http://localhost:3000/api/edit-prompt", json=update_prompt, headers=headers
    )
    print("Status Code:", response3.status_code)
    print("Response:", response3.json())
    print()

# Test 4: Update agent with different image
if response2.status_code == 200:
    agent_id = response2.json().get("id")
    print("4. Testing agent update with different image:")

    update_agent = {
        "id": agent_id,
        "name": "Updated Image Test Agent",
        "agent": "This is an updated test agent with a different image.",
        "description": "Updated description with new image.",
        "requirements": [
            {"package": "requests", "installation": "pip install requests"}
        ],
        "useCases": [
            {
                "title": "Updated Image Testing",
                "description": "Testing image update functionality.",
            }
        ],
        "tags": "image,test,upload,updated",
        "is_free": True,
        "category": ["test", "updated"],
        "language": "python",
        "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&h=400&fit=crop&ixlib=rb-4.1.0",
    }

    response4 = requests.post(
        "http://localhost:3000/api/edit-agent", json=update_agent, headers=headers
    )
    print("Status Code:", response4.status_code)
    print("Response:", response4.json())
    print()

# Test 5: Test with invalid image URL
print("5. Testing with invalid image URL (should still work but image won't load):")
invalid_image_prompt = {
    "name": "Invalid Image Test Prompt",
    "prompt": "This is a test prompt with an invalid image URL.",
    "description": "Testing with invalid image URL.",
    "useCases": [
        {
            "title": "Invalid Image Test",
            "description": "Testing with invalid image URL.",
        }
    ],
    "tags": "image,test,invalid",
    "is_free": True,
    "category": "test",
    "image_url": "https://invalid-url-that-does-not-exist.com/image.jpg",
}

response5 = requests.post(
    "http://localhost:3000/api/add-prompt", json=invalid_image_prompt, headers=headers
)
print("Status Code:", response5.status_code)
print("Response:", response5.json())
