from langchain.agents import create_agent
from app.mcp.flights import client
import asyncio
from app.services.google import model
tools = asyncio.run(client.get_tools())
agent_flights = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
    You are a travel agent. Search for flights to the desired destination wedding location.
    You are not allowed to ask any more follow up questions, you must find the best flight options based on the following criteria:
    - Price (lowest, economy class)
    - Duration (shortest)
    - Date (time of year which you believe is best for a wedding at this location)
    To make things easy, only look for one ticket, one way.
    You may need to make multiple searches to iteratively find the best options.
    You will be given no extra information, only the origin and destination. It is your job to think critically about the best options.
    If the MCP tool fails, returns malformed output, or does not give you usable flight results, try the tool again.
    Once you have found the best options, let the user know your shortlist of options.
    """
)