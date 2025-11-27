from fastapi import FastAPI
from app.api.v1 import api_router
from app.utils.memory import get_session_history

app = FastAPI(title="Async Chatbot with Memory")

# Include API routes
app.include_router(api_router, prefix="/api/v1")


# --------------------------------------------------------
# GET endpoint to retrieve full conversation by session_id
# --------------------------------------------------------
#@app.get("/sessions/{session_id}")
#async def read_session(session_id: str):
  #  """
    #Returns the full conversation history for a given session_id.
    #"""
    #history = await get_session_history(session_id)
    #return {
       # "session_id": session_id,
        #"conversation": history
    #}
