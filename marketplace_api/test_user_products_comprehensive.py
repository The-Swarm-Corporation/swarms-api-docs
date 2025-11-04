import requests
from dotenv import load_dotenv

load_dotenv()

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ",
}

add_prompt_url = "http://localhost:3000/api/add-prompt"
add_agent_url = "http://localhost:3000/api/add-agent"
user_products_url = "http://localhost:3000/api/user-products"

print("=== Comprehensive User Products Test ===\n")

# First, add some test data
print("1. Adding test prompt 'Data Analysis Expert':")
prompt_data = {
    "name": "Data Analysis Expert",
    "prompt": "You are an expert data analyst specializing in statistical analysis and visualization.",
    "description": "A comprehensive prompt for data analysis tasks.",
    "useCases": [
        {
            "title": "Statistical Analysis",
            "description": "Performs advanced statistical analysis",
        }
    ],
    "tags": "data,analysis,statistics,expert",
    "is_free": True,
    "category": "data-science",
    "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500&h=300&fit=crop",
}
prompt_response = requests.post(add_prompt_url, json=prompt_data, headers=headers)
print("Prompt Status:", prompt_response.status_code)
print("Prompt Response:", prompt_response.json())
print()

print("2. Adding test agent 'Code Review Assistant':")
agent_data = {
    "name": "Code Review Assistant",
    "agent": "You are an AI agent that performs thorough code reviews and provides improvement suggestions.",
    "description": "An intelligent agent for automated code review processes.",
    "requirements": ["Python", "JavaScript", "Code Analysis"],
    "useCases": [
        {
            "title": "Code Review",
            "description": "Reviews code for quality and best practices",
        }
    ],
    "tags": "code,review,quality,assistant",
    "is_free": False,
    "price": 0.5,
    "price_usd": 25.0,
    "category": "development",
    "language": "python",
    "image_url": "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=500&h=300&fit=crop",
}
agent_response = requests.post(add_agent_url, json=agent_data, headers=headers)
print("Agent Status:", agent_response.status_code)
print("Agent Response:", agent_response.json())
print()

print("3. Adding paid prompt 'Advanced ML Model':")
paid_prompt_data = {
    "name": "Advanced ML Model",
    "prompt": "You are an advanced machine learning model with expertise in deep learning and neural networks.",
    "description": "A premium prompt for advanced machine learning tasks.",
    "useCases": [
        {
            "title": "Deep Learning",
            "description": "Handles complex deep learning scenarios",
        }
    ],
    "tags": "machine,learning,deep,neural,premium",
    "is_free": False,
    "price": 1.0,
    "price_usd": 50.0,
    "category": "ai-ml",
    "image_url": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=500&h=300&fit=crop",
}
paid_prompt_response = requests.post(
    add_prompt_url, json=paid_prompt_data, headers=headers
)
print("Paid Prompt Status:", paid_prompt_response.status_code)
print("Paid Prompt Response:", paid_prompt_response.json())
print()

# Now test fetching all user products
print("4. Fetching all user products with metadata:")
user_products_query = {"username": "testuser", "include_metadata": True}
user_products_response = requests.post(
    user_products_url, json=user_products_query, headers=headers
)
print("Status Code:", user_products_response.status_code)
if user_products_response.status_code == 200:
    data = user_products_response.json()
    print("Username:", data.get("username"))
    print("Total Products:", data.get("total_products"))
    print("Summary:")
    summary = data.get("summary", {})
    print(f"  - Prompts: {summary.get('total_prompts', 0)}")
    print(f"  - Agents: {summary.get('total_agents', 0)}")
    print(f"  - Tools: {summary.get('total_tools', 0)}")
    print(f"  - Free Products: {summary.get('free_products', 0)}")
    print(f"  - Paid Products: {summary.get('paid_products', 0)}")
    print(f"  - Total Earnings: ${summary.get('total_earnings_usd', 0)}")
    print()
    print("Products:")
    for product in data.get("prompts", []):
        print(
            f"  Prompt: {product.get('name')} - ${product.get('price_usd', 0)} - {product.get('status')}"
        )
    for product in data.get("agents", []):
        print(
            f"  Agent: {product.get('name')} - ${product.get('price_usd', 0)} - {product.get('status')}"
        )
    for product in data.get("tools", []):
        print(
            f"  Tool: {product.get('name')} - ${product.get('price_usd', 0)} - {product.get('status')}"
        )
else:
    print("Error Response:", user_products_response.json())
