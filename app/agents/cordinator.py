from langchain.agents import create_agent
from app.services.google import model
from langchain.tools import tool

from app.agents.venues import agent_venues
from app.agents.playlists import agent_playlists
from app.agents.flights import agent_flights



@tool
def find_venues(query: str):
    """Use for wedding venue search"""
    return agent_venues.invoke({
        "messages": [
            {"role": "user", "content": f"Wedding venue request: {query}"}
        ]
    })


@tool
def find_playlist(query: str):
    """Use for wedding music playlist creation"""
    return agent_playlists.invoke({
        "messages": [
            {"role": "user", "content": f"Wedding music request: {query}"}
        ]
    })


@tool
def find_flights(query: str):
    """Use for flight planning for wedding guests or couple"""
    return agent_flights.invoke({
        "messages": [
            {"role": "user", "content": f"Flight request for wedding: {query}"}
        ]
    })



agent_coordinator = create_agent(
    model=model,
    tools=[find_flights, find_venues, find_playlist],
    system_prompt="""
You are a professional wedding planning coordinator agent.

Your job:
1. Analyze the user's request carefully
2. Identify ALL required tasks:
   - Flights
   - Venue
   - Music
3. ALWAYS call the appropriate tools when needed
4. NEVER invent information — rely only on tool outputs

After gathering results, produce a structured final answer with:

-  Flights (options, prices, notes)
-  Venue (best options with details)
-  Music (playlist or recommendations)
-  Suggested plan timeline
- Estimated budget insight (if possible)

Be clear, structured, and practical.
"""
)