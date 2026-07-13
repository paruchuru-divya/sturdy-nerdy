from qdrant_client import QdrantClient
from model_loader import get_embedding_model

model = get_embedding_model()

# Connect to local Qdrant
client = QdrantClient(path="qdrant_db")

COLLECTION_NAME = "edu_explain"


def retrieve(query, top_k=3):

    # Convert question to embedding
    query_embedding = model.encode(query).tolist()

    # Search Qdrant
    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=top_k
    )

    return results.points


if __name__ == "__main__":

    question = "What is machine learning?"

    results = retrieve(question)

    print("\nRetrieved Chunks:\n")

    for i, point in enumerate(results, start=1):
        print(f"{i}. {point.payload['text']}")