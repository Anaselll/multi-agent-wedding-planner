from langchain.agents import create_agent
from app.services.google import  model

from app.tools.search_web import search_web

agent_playlists= create_agent(
    model=model,
    tools=[search_web],
   system_prompt="You are a music playlist assistant that creates and recommends playlists based on user preferences, mood, genre, and context, using tools when needed and providing clear, relevant, and well-structured song selections without inventing information."
)
