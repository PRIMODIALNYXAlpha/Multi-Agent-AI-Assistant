from groq import Groq
from app.config import get_secret

def task_agent(state):
    api_key = get_secret("GROQ_API_KEY")

    if not api_key:
        return {"error": "Missing GROQ_API_KEY"}

    client = Groq(api_key=api_key)

    user_input = state["input"]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a senior software engineer. Break this task into clear coding steps."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return {
        "input": user_input,
        "task": response.choices[0].message.content
    }