from langchain.memory import ConversationBufferMemory
from typing import Dict

chat_sessions: Dict[str, ConversationBufferMemory] = {}

def get_session_memory(session_id: str) -> ConversationBufferMemory:
    """Return or create chat memory for a given session."""
    if session_id not in chat_sessions:
        chat_sessions[session_id] = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
    return chat_sessions[session_id]
