# schemas/chat.py
from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_id: str
    session_id: str
    message: str

class ChatResponse(BaseModel):
    user_id: str
    session_id: str
    reply: str

class SessionHistory(BaseModel):
    session_id: str
    history: list

class UserHistory(BaseModel):
    user_id: str
    sessions: dict  # key: session_id, value: list of messages
