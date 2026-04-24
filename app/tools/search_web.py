from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()
import os 

TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")
from tavily import TavilyClient

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)


@tool
def search_web(query:str):
    """  search in the web """
    response = tavily_client.search(query)
    return response
