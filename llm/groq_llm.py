from langchain_groq import ChatGroq

def get_llm():
    """
    Centralized Groq LLM configuration
    """
    return ChatGroq(
        model="llama-3.3-70b-versatile",  # ✅ supported model
        temperature=0.2
    )
