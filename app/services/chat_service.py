import asyncio
import os
from dotenv import load_dotenv
from groq import Groq
from app.config import MODEL_NAME
from app.utils.memory import add_message, get_session_history

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def build_prompt(history: list, user_msg: str):
    """
    Create messages with system prompt for the chatbot
    """
    system_prompt = (
        "You are a friendly AI assistant. "
        "Reply in one clear, simple sentence. "
        "No suggestions, no bullet points, no tables, no markdown. "
        "Only short conversational answers."
    )

    # Start messages with system role
    messages = [{"role": "system", "content": system_prompt}]

    # Add history messages
    for msg in history:
        messages.append({"role": msg["role"], "content": msg["message"]})

    # Add the new user message
    messages.append({"role": "user", "content": user_msg})

    return messages

async def call_groq_api(messages: list) -> str:
    """Call Groq chat API asynchronously"""
    def sync_call():
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages
        )
        return response
    response = await asyncio.to_thread(sync_call)
    return response.choices[0].message.content

async def generate_reply(user_id: str, session_id: str, user_msg: str) -> str:
    # Save user message
    await add_message(user_id, session_id, "user", user_msg)

    # Load session history
    history = await get_session_history(user_id, session_id)

    # Build prompt with system instruction
    messages = build_prompt(history, user_msg)

    # Call LLM API
    reply = await call_groq_api(messages)

    # Save assistant reply without additional cleaning
    await add_message(user_id, session_id, "assistant", reply)

    return reply
