from langchain.agents import create_agent
from app.services.google import  model

from app.tools.search_web import search_web

agent_flights = create_agent(
    model=model,
    tools=[search_web],
    system_prompt="You are a flight search assistant that finds and returns the best available flight options using tools, prioritizing accuracy, price, and convenience  and presenting clear, concise results without inventing information."
)
