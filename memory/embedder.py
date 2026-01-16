import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    use_auth_token=HF_API_KEY
)

def embed_text(text: str):
    """
    Returns embedding vector for input text
    """
    return model.encode(text, normalize_embeddings=True)
