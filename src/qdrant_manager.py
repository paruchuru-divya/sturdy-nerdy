from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct


class QdrantManager:

    def __init__(self, reset=False):

        self.client = QdrantClient(path="qdrant_db")
        self.collection_name = "edu_explain"

        if reset:
            self.reset_collection()

    def reset_collection(self):

        collections = self.client.get_collections().collections
        names = [c.name for c in collections]

        if self.collection_name in names:
            self.client.delete_collection(self.collection_name)

        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

        print("Collection Ready")

    def add_chunks(self, chunks, embeddings):

        points = []

        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            points.append(
                PointStruct(
                    id=i,
                    vector=embedding.tolist(),
                    payload={"text": chunk}
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

        print(f"{len(points)} chunks stored successfully.")