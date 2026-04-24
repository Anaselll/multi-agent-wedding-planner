from langchain.agents import create_agent
from app.services.google import ChatGoogleGenerativeAI as model
from langchain.tools import tool
from app.agents.venues import agent_venues
from app.agents.playlists import agent_playlists
from app.agents.flights import agent_flights

@tool
def find_venues(query: str):
    """Use for wedding venue search"""
    return agent_venues.invoke(query)

@tool
def find_playlist(query: str):
    """Use for wedding music playlist creation"""
    return agent_playlists.invoke(query)

@tool
def find_flights(query: str):
    """Use for flight planning for wedding guests or couple"""
    return agent_flights.invoke(query)



agent_coordinator= create_agent(
    model=model,
    tools=[find_flights,find_venues,find_playlist],
    system_prompt="You are a wedding planning coordinator agent that analyzes user requests and delegates tasks to the appropriate tools (venue search, playlist creation, flight search), and combining all results into a clear, structured, and actionable wedding plan without hallucinating."
)
