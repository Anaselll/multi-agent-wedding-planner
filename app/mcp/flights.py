from langchain_mcp_adapters.client import MultiServerMCPClient
client = MultiServerMCPClient(
    {
        "travel_server": {
                "transport": "streamable_http",
                "url": "https://mcp.kiwi.com"
            }
    },
)
