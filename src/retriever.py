from src.embeddings import generate_embeddings
from src.faiss_manager import FAISSManager


def retrieve(query):

    # Generate embedding for query
    embedding = generate_embeddings([query])[0]

    # Load FAISS index
    faiss_db = FAISSManager()

    # Search similar chunks
    chunks = faiss_db.search(
        embedding,
        top_k=3
    )

    return chunks