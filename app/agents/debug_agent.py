from groq import Groq
from app.config import get_secret

def debug_agent(state):
    api_key = get_secret("GROQ_API_KEY")

    if not api_key:
        return {"error": "Missing GROQ_API_KEY"}

    client = Groq(api_key=api_key)

    code = state.get("code", "")

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a debugging expert. Fix errors and improve the code."
            },
            {
                "role": "user",
                "content": code
            }
        ]
    )

    return {
        **state,
        "final_code": response.choices[0].message.content
    }