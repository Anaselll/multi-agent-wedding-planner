# Wedding Planner Multi-Agent System

Simple multi-agent project using LangChain to plan weddings.

## Features

* Flights search
* Venue suggestions
* Music playlist generation
* Coordinator agent that combines everything

## Run

```bash
uv run python main.py
```

## Example

Input:

```
Plan a wedding in Spain with good flights and loud music
```

Output:

* Flights options
* Venue suggestions
* Playlist ideas
* Basic wedding plan

## Structure

```
app/
 ├── agents/
 ├── tools/
 └── services/
```

## Notes

* Uses multiple agents
* Coordinator decides which tool to call
* Results depend on tools (like web search)
