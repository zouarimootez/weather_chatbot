from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, AgentType
from tools.tool_registry import TOOLS
from agent.prompt import PROMPT
from agent.chat_memory import get_session_memory
from agent.config import BASE_URL

def create_agent(session_id: str):
    """Create a conversational agent using Ollama."""
    llm = OllamaLLM(
        model="llama3.1:8b",
        base_url= BASE_URL,
        temperature=0.2,
        num_ctx=4096,
    )

    memory = get_session_memory(session_id)

    agent = initialize_agent(
        tools=TOOLS,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
        max_iterations=6,
        early_stopping_method="force",
        handle_parsing_errors=True,
    )
    return agent
