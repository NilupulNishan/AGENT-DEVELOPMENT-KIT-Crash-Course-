from google.adk.agents import Agent

root_agent = Agent(
    name = "greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model ="gemini-2.0-flash",
    # model ="gpt-35-turbo",
    description="Greeting agent",
    instruction="""
    You are a helpful assitant that greets the user.
    Ask for the user's name and greet them by name.
    """,
)