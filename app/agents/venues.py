from langchain.agents import create_agent
from app.services.google import model

from app.tools.search_web import search_web

agent_venues = create_agent(
    model=model,
    tools=[search_web],
    system_prompt="""
    You are a venue specialist. Search for venues in the desired location, and with the desired capacity.
    You are not allowed to ask any more follow up questions, you must find the best venue options based on the following criteria:
    - Price (lowest)
    - Capacity (exact match)
    - Reviews (highest)
    You may need to make multiple searches to iteratively find the best options. 
    You have a suggested limit of 12 web searches. Count every web_search call you make.
    After 12 searches, you should stop searching and summarize the best options you have
    found so far.
    """
)