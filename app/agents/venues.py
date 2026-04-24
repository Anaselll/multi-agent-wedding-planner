from langchain.agents import create_agent
from app.services.google import ChatGoogleGenerativeAI as model

from tools.search_web import search_web

agent_venues= create_agent(
    model=model,
    tools=[search_web],
    system_prompt="You are a wedding planning assistant specialized in finding venues, using tools to recommend the best options based on location, budget, guest capacity, and wedding style, while asking for missing details and providing clear, concise, and accurate results without hallucinating."
)
