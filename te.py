"""
Test file: exercises every Python code snippet from
  - docs/documentation/multi-agent/round_robin.mdx  (reference)
  - docs/examples/examples/round-robin.mdx           (example)
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = "https://api.swarms.world"
API_KEY = os.environ.get("SWARMS_API_KEY")

headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

# ============================================================
# REFERENCE DOC — Basic RoundRobin Example (round_robin.mdx)
# ============================================================
print("\n" + "=" * 70)
print("TEST 1: Reference Doc — Basic RoundRobin Example")
print("=" * 70)

swarm_config = {
    "name": "Market Strategy Roundtable",
    "description": "Collaborative market strategy discussion with round-robin agent turns",
    "swarm_type": "RoundRobin",
    "task": "Develop a go-to-market strategy for an AI-powered code review tool targeting mid-size engineering teams (20-100 developers). Cover positioning, pricing, channels, and competitive differentiation.",
    "agents": [
        {
            "agent_name": "Product Strategist",
            "description": "Defines product positioning and value proposition",
            "system_prompt": "You are a product strategist. Define the core value proposition, target personas, and competitive positioning. Be specific about what differentiates this product from existing solutions like GitHub Copilot, Codacy, and SonarQube.",
            "model_name": "gpt-4o",
            "max_loops": 1,
            "temperature": 0.5
        },
        {
            "agent_name": "Growth Marketer",
            "description": "Designs acquisition channels and launch campaigns",
            "system_prompt": "You are a growth marketing expert. Propose acquisition channels ranked by expected ROI, design the launch campaign, and suggest pricing tiers. Be data-driven with estimated CAC and conversion benchmarks.",
            "model_name": "gpt-4o",
            "max_loops": 1,
            "temperature": 0.5
        },
        {
            "agent_name": "Sales Engineer",
            "description": "Evaluates technical feasibility and enterprise readiness",
            "system_prompt": "You are a sales engineer. Evaluate the enterprise sales motion, identify technical integration requirements, and propose a proof-of-concept framework. Focus on what mid-size teams need for adoption.",
            "model_name": "gpt-4o",
            "max_loops": 1,
            "temperature": 0.4
        }
    ],
    "max_loops": 1
}

response = requests.post(
    f"{API_BASE_URL}/v1/swarm/completions",
    headers=headers,
    json=swarm_config
)

if response.status_code == 200:
    result = response.json()
    print(json.dumps(result["output"], indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")


# ============================================================
# EXAMPLE DOC — Setup + run_roundtable function (round-robin.mdx)
# ============================================================
print("\n" + "=" * 70)
print("TEST 2: Example Doc — run_roundtable function")
print("=" * 70)

def run_roundtable(topic: str, max_loops: int = 1) -> dict:
    """Run a collaborative round-robin research discussion."""

    swarm_config = {
        "name": "Research Roundtable",
        "description": "Collaborative research with round-robin agent turns",
        "swarm_type": "RoundRobin",
        "task": topic,
        "agents": [
            {
                "agent_name": "Industry Researcher",
                "description": "Gathers market data and industry trends",
                "system_prompt": "You are an industry researcher. Provide data-driven market analysis, cite specific numbers and trends, and identify key players. Build on insights from other team members when available.",
                "model_name": "gpt-4o",
                "max_loops": 1,
                "temperature": 0.4
            },
            {
                "agent_name": "Technology Analyst",
                "description": "Evaluates technical landscape and innovation",
                "system_prompt": "You are a technology analyst. Assess the technical landscape, evaluate emerging technologies, and identify innovation opportunities. Reference and build upon the research data shared by other team members.",
                "model_name": "gpt-4o",
                "max_loops": 1,
                "temperature": 0.4
            },
            {
                "agent_name": "Strategy Advisor",
                "description": "Synthesizes insights into actionable strategy",
                "system_prompt": "You are a strategy advisor. Synthesize insights from the team into actionable strategic recommendations. Identify risks, opportunities, and provide a prioritized roadmap. Reference specific points made by other team members.",
                "model_name": "gpt-4o",
                "max_loops": 1,
                "temperature": 0.5
            }
        ],
        "max_loops": max_loops
    }

    response = requests.post(
        f"{API_BASE_URL}/v1/swarm/completions",
        headers=headers,
        json=swarm_config,
        timeout=180
    )

    return response.json()


# ============================================================
# EXAMPLE DOC — Step 4: Run the Roundtable
# ============================================================
print("\n" + "=" * 70)
print("TEST 3: Example Doc — Run the Roundtable + display loop")
print("=" * 70)

# Define the research topic
topic = """
Analyze the emerging autonomous AI agent market. Cover the current state of
the technology, major players and their approaches, enterprise adoption
barriers, and the most promising near-term use cases. Provide actionable
insights for a startup considering entering this space.
"""

# Run the roundtable discussion
result = run_roundtable(topic)

# Display the collaborative discussion
for output in result.get("output", []):
    agent = output["role"]
    content = output["content"]

    print(f"\n{'='*60}")
    print(f"{agent}")
    print(f"{'='*60}")

    # Handle content as string or list
    if isinstance(content, list):
        content = ' '.join(str(item) for item in content)

    print(str(content)[:800] + "...")


# ============================================================
# EXAMPLE DOC — Step 5: Multi-Loop Refinement
# ============================================================
print("\n" + "=" * 70)
print("TEST 4: Example Doc — Multi-Loop Refinement")
print("=" * 70)

# Run 2 loops — agents go around twice, refining their analysis each time
deep_result = run_roundtable(
    topic="Evaluate the competitive positioning of Anthropic vs OpenAI vs Google in the enterprise AI market. Assess technical capabilities, pricing strategy, ecosystem lock-in, and likely market share in 3 years.",
    max_loops=2
)

# Show the final contributions after 2 rounds of refinement
for output in deep_result.get("output", []):
    print(f"\n{output['role']}:")
    content = output["content"]
    if isinstance(content, list):
        content = ' '.join(str(item) for item in content)
    print(str(content)[:600] + "...")


print("\n" + "=" * 70)
print("ALL TESTS COMPLETE")
print("=" * 70)
