# api/v1/endpoints/chat.py
from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse, UserHistory, SessionHistory
from app.services.chat_service import generate_reply
from app.utils.memory import get_user_history, get_session_history

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(payload: ChatRequest):
    reply = await generate_reply(payload.user_id, payload.session_id, payload.message)
    return ChatResponse(user_id=payload.user_id, session_id=payload.session_id, reply=reply)

@router.get("/user/{user_id}", response_model=UserHistory)
async def get_user_conversations(user_id: str):
    sessions = await get_user_history(user_id)
    return UserHistory(user_id=user_id, sessions=sessions)

@router.get("/user/{user_id}/session/{session_id}", response_model=SessionHistory)
async def get_user_session(user_id: str, session_id: str):
    history = await get_session_history(user_id, session_id)
    return SessionHistory(session_id=session_id, history=history)
