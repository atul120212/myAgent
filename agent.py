import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini

load_dotenv()

# Initialize Gemini correctly (positional argument)
model = Gemini("gemini-2.5-flash")

packaging_agent = Agent(
    name="Packaging Analyst",
    model=model,
    instructions="""
You are a professional logistics AI agent.

ALWAYS respond STRICTLY in the following format:

SUMMARY:
- Short overview in 1–2 lines

KEY FINDINGS:
- Bullet points

RISKS / ISSUES:
- Bullet points (or write 'None')

RECOMMENDED ACTIONS:
- Clear actionable steps

CONFIDENCE LEVEL:
- High / Medium / Low
"""
)
