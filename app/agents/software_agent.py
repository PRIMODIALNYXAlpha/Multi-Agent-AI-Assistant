from groq import Groq
from app.config import get_secret

def software_agent(state):
    api_key = get_secret("GROQ_API_KEY")

    if not api_key:
        return {"error": "Missing GROQ_API_KEY"}

    client = Groq(api_key=api_key)

    task = state.get("task", "")

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a professional software developer. Write clean and correct code."
            },
            {
                "role": "user",
                "content": task
            }
        ]
    )

    return {
        **state,
        "code": response.choices[0].message.content
    }