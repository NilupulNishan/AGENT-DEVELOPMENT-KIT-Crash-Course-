from datetime import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search


def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent = Agent(
    name = "tool_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model ="gemini-2.0-flash",
    # model ="gpt-35-turbo",
    description="Tool Agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - get_current_time
    """,
    tools=[get_current_time],
    # tools=[google_search],
    # tools=[google_search, get_current_time], # <-- Doesn't work
)