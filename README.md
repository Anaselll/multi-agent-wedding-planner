# Wedding Planner Multi-Agent System

Simple multi-agent project using LangChain and MCP to plan weddings.

## Features

- Flights search (MCP Kiwi integration)  
- Venue suggestions  
- Music playlist generation  
- Coordinator agent that combines everything into a full plan  

## Run

```bash
uv run python -m app.main
```

## Example

**Input:**
```
Plan a wedding in Spain with good flights and loud music
```

**Output:**
- Flight options  
- Venue suggestions  
- Playlist ideas  
- Complete wedding plan  

## Structure

```
app/
├── agents/        # flight, venue, playlist agents + coordinator
├── mcp/           # MCP integrations (Kiwi flight server)
├── tools/         # web search tools
├── services/      # model (Gemini, etc.)
└── main.py
```