from app.agents.cordinator import agent_coordinator

def main():
    print("Hello from weddingplanner!")
    
    response = agent_coordinator.invoke({
        "messages": [
            {
                "role": "user",
                "content": "I want to plan a wedding as soon as possible in spain find me a good price flight and loud music in month 5"
            }
        ]
    })
    
    print(response)
    return response


if __name__ == "__main__":
    main()