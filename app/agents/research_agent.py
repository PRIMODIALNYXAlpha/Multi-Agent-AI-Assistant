from tavily import TavilyClient
from app.config import get_secret

def research_agent(state):
    api_key = get_secret("TAVILY_API_KEY")

    if not api_key:
        return {"error": "Missing TAVILY_API_KEY"}

    client = TavilyClient(api_key=api_key)

    query = state.get("input", "")

    response = client.search(query=query)

    return {
        **state,
        "research": response.get("results", [])
    }