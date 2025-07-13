import os
import httpx
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

async def ask_llm(prompt: str, context: str = "") -> str:
    full_prompt = f"""Use the following context to answer the question:

    {context}

    Question: {prompt}
    """

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",  # mixtral-8x7b-32768 model was not working
        "messages": [
            {"role": "system", "content": "You are an AI assistant specialized in commercial real estate."},
            {"role": "user", "content": full_prompt}
        ],
        "temperature": 0.7
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )
        data = response.json()
        return data["choices"][0]["message"]["content"]
