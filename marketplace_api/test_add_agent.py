import requests
from dotenv import load_dotenv

load_dotenv()

# Test data for adding an agent
agent_data = {
    "name": "Machine Learning Model Trainer Agent",
    "agent": "You are an AI agent specialized in training machine learning models. Given a dataset and requirements, automatically select the best algorithm, tune hyperparameters, and train an optimized model.",
    "description": "An intelligent agent that automates the entire machine learning model training pipeline from data preprocessing to model deployment.",
    "requirements": [
        {"package": "scikit-learn", "installation": "pip install scikit-learn"},
        {"package": "pandas", "installation": "pip install pandas"},
        {"package": "numpy", "installation": "pip install numpy"},
    ],
    "useCases": [
        {
            "title": "Automated Model Training",
            "description": "Train machine learning models automatically with optimal hyperparameters.",
        },
        {
            "title": "Data Science Pipeline",
            "description": "Complete data science workflow from data cleaning to model deployment.",
        },
    ],
    "tags": "machine learning,ai,automation,data science,model training",
    "is_free": True,
    "category": "ai",
    "language": "python",
    "image_url": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=500&h=300&fit=crop",
}

# API endpoint
url = "http://localhost:3000/api/add-agent"

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ",
}

# Test adding agent
response = requests.post(url, json=agent_data, headers=headers)
print("Add Agent Response:")
print("Status Code:", response.status_code)
print("Response:", response.json())
