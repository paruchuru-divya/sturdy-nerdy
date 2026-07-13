from model_loader import get_embedding_model
from faiss_manager import FAISSManager

model = get_embedding_model()


def retrieve(query):

    embedding = model.encode(query)

    faiss_db = FAISSManager()

    chunks = faiss_db.search(
        embedding,
        top_k=3
    )

    return chunks