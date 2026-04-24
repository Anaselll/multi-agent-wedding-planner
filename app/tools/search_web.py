from typing import Dict, Any
from tavily import TavilyClient
from langchain.tools import tool

tavily_client = TavilyClient()

@tool
def search_web(query: str):
    """Search the web for information.
  
    Queries must use only plain text characters. Do not use accented or special characters     
    """
    return tavily_client.search(query)
