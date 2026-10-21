import json
import os
from google import genai
from google.genai import types

# Initialize Gemini Client
client = genai.Client()

def task_decomposer_agent(user_prompt: str) -> dict:
    """Decomposes a high-level goal into structured execution steps."""
    system_instruction = """
    You are an AI Task Planning Agent. Given a high-level user goal:
    1. Break it down into 3 clear, execution-ready sub-tasks.
    2. Define expected output for each sub-task.
    3. Return output strictly in valid JSON format with keys: 'goal', 'steps'.
    """
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_prompt,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        response_mime_type="application/json"
    )
)
    return json.loads(response.text)

if __name__ == "__main__":
    goal = "Build a lightweight web scraper for technology news headlines."
    print(f"--- Decomposing Goal: {goal} ---")
    plan = task_decomposer_agent(goal)
    print(json.dumps(plan, indent=2))

