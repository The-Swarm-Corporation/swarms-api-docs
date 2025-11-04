import requests
from dotenv import load_dotenv

load_dotenv()

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ",
}

query_url = "http://localhost:3000/api/query-prompts"

query_data1 = {"prompt_name": "pineapple-agent"}
response1 = requests.post(query_url, json=query_data1, headers=headers)
print(response1.json())