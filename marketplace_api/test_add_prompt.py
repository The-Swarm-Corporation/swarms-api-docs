import requests
from dotenv import load_dotenv

load_dotenv()

# Test data for adding a prompt
prompt_data = {
    "name": "Advanced Data Analysis Prompt",
    "prompt": "You are an expert data analyst. Given a dataset, perform comprehensive analysis including statistical summaries, visualizations, and actionable insights.",
    "description": "A comprehensive prompt for data analysis tasks with statistical and visualization capabilities.",
    "useCases": [
        {
            "title": "Business Intelligence",
            "description": "Analyze business data to extract insights and trends.",
        },
        {
            "title": "Research Data Analysis",
            "description": "Process research data for academic and scientific purposes.",
        },
    ],
    "tags": "data analysis,statistics,visualization,business intelligence,research",
    "is_free": True,
    "category": "analytics",
    "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500&h=300&fit=crop",
}

# API endpoint
url = "http://localhost:3000/api/add-prompt"

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ",
}

# Test adding prompt
response = requests.post(url, json=prompt_data, headers=headers)
print("Add Prompt Response:")
print("Status Code:", response.status_code)
print("Response:", response.json())
