
import requests
from dotenv import load_dotenv

load_dotenv()

# Test data for assembly line defect analysis agent prompt
free_prompt = {
    "name": "Assembly Line Defect Analysis Agent",
    "prompt": (
        "You are an expert agent specializing in defect analysis on assembly lines. Given a sequence of assembly steps, sensor data, "
        "quality inspection reports, and a list of detected anomalies, analyze the root causes of defects, identify patterns or recurring issues, "
        "and recommend actionable improvements. Output a step-by-step diagnostic reasoning, a summary of key findings, and a JSON report "
        "listing each defect, its likely cause, affected assembly step, and suggested corrective action."
    ),
    "description": (
        "Analyzes defects on assembly lines by processing sensor data and inspection reports to determine root causes and recommend improvements. "
        "Returns a detailed diagnostic workflow and a structured JSON report for quality assurance teams."
    ),
    "useCases": [
        {
            "title": "Automotive Assembly Defect Diagnosis",
            "description": "Identifying and resolving recurring defects in automotive assembly lines using sensor and inspection data.",
        },
        {
            "title": "Electronics Manufacturing Quality Control",
            "description": "Analyzing PCB assembly defects and suggesting process improvements in electronics manufacturing.",
        },
    ],
    "tags": "assembly,defect analysis,quality control,manufacturing,diagnostics,root cause,automation",
    "is_free": True,
    "category": "industrial",
    "image_url": "https://images.unsplash.com/photo-1716194583732-0b9874234218?q=80&w=2340&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
}

# API endpoint
url = "http://localhost:3000/api/add-prompt"

# Headers (replace with your API key)
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ",
}

# Test free prompt
response1 = requests.post(url, json=free_prompt, headers=headers)
print("Free prompt response:", response1.status_code, response1.json())

# Test agent creation
agent_data = {
    "name": "Assembly Line Quality Control Agent",
    "agent": "You are an AI agent specialized in assembly line quality control. Monitor sensor data, detect anomalies, and provide real-time quality assessments.",
    "description": "An intelligent agent for monitoring and controlling assembly line quality using AI and machine learning.",
    "requirements": [
        {"package": "tensorflow", "installation": "pip install tensorflow"},
        {"package": "opencv-python", "installation": "pip install opencv-python"},
    ],
    "useCases": [
        {
            "title": "Real-time Quality Monitoring",
            "description": "Monitor assembly line quality in real-time using computer vision and sensor data.",
        },
        {
            "title": "Defect Detection",
            "description": "Automatically detect and classify defects in manufactured products.",
        },
    ],
    "tags": "quality control,assembly line,ai,computer vision,manufacturing,automation",
    "is_free": True,
    "category": "industrial",
    "language": "python",
    "image_url": "https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=500&h=300&fit=crop",
}

agent_url = "http://localhost:3000/api/add-agent"
agent_response = requests.post(agent_url, json=agent_data, headers=headers)
print("Agent response:", agent_response.status_code, agent_response.json())

# Test query methods
print("\n=== Testing Query Methods ===")

# Query prompts by search
query_prompts_url = "http://localhost:3000/api/query-prompts"
query_response = requests.get(f"{query_prompts_url}?q=assembly", headers=headers)
print("Query prompts by search:", query_response.status_code, query_response.json())

# Query agents by search
query_agents_url = "http://localhost:3000/api/query-agents"
query_agents_response = requests.get(f"{query_agents_url}?q=quality", headers=headers)
print(
    "Query agents by search:",
    query_agents_response.status_code,
    query_agents_response.json(),
)

# Test slug-based query
if response1.status_code == 200:
    prompt_id = response1.json().get("id")
    if prompt_id:
        # Query by ID
        id_query = requests.get(f"{query_prompts_url}?q={prompt_id}", headers=headers)
        print("Query prompt by ID:", id_query.status_code, id_query.json())

        # Query by slug (name converted to slug)
        slug_query = requests.get(
            f"{query_prompts_url}?q=assembly-line-defect-analysis-agent&type=slug",
            headers=headers,
        )
        print("Query prompt by slug:", slug_query.status_code, slug_query.json())

if agent_response.status_code == 200:
    agent_id = agent_response.json().get("id")
    if agent_id:
        # Query agent by ID
        agent_id_query = requests.get(
            f"{query_agents_url}?q={agent_id}", headers=headers
        )
        print("Query agent by ID:", agent_id_query.status_code, agent_id_query.json())

        # Query agent by slug
        agent_slug_query = requests.get(
            f"{query_agents_url}?q=assembly-line-quality-control-agent&type=slug",
            headers=headers,
        )
        print(
            "Query agent by slug:",
            agent_slug_query.status_code,
            agent_slug_query.json(),
        )
