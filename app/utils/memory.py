# utils/memory.py
import json
import os
import aiofiles
from typing import Dict
from app.config import MEMORY_FILE

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({}, f)

async def load_memory() -> Dict:
    async with aiofiles.open(MEMORY_FILE, "r") as f:
        content = await f.read()
        return json.loads(content)

async def save_memory(data: Dict):
    async with aiofiles.open(MEMORY_FILE, "w") as f:
        await f.write(json.dumps(data, indent=4))

async def add_message(user_id: str, session_id: str, role: str, message: str):
    memory = await load_memory()
    if user_id not in memory:
        memory[user_id] = {}
    if session_id not in memory[user_id]:
        memory[user_id][session_id] = []
    memory[user_id][session_id].append({"role": role, "message": message})
    await save_memory(memory)

async def get_session_history(user_id: str, session_id: str):
    memory = await load_memory()
    return memory.get(user_id, {}).get(session_id, [])

async def get_user_history(user_id: str):
    memory = await load_memory()
    return memory.get(user_id, {})
