import faiss
import numpy as np
import pickle
import os


INDEX_FILE = "faiss.index"
CHUNK_FILE = "chunks.pkl"


class FAISSManager:

    def __init__(self):

        self.dimension = 384

        if os.path.exists(INDEX_FILE):

            self.index = faiss.read_index(INDEX_FILE)

            with open(CHUNK_FILE, "rb") as f:
                self.chunks = pickle.load(f)

        else:

            self.index = faiss.IndexFlatL2(self.dimension)
            self.chunks = []

    def add_chunks(self, chunks, embeddings):

        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)

        self.chunks.extend(chunks)

        faiss.write_index(self.index, INDEX_FILE)

        with open(CHUNK_FILE, "wb") as f:
            pickle.dump(self.chunks, f)

    def search(self, embedding, top_k=3):

        embedding = np.array([embedding]).astype("float32")

        distances, indices = self.index.search(
            embedding,
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx != -1:
                results.append(self.chunks[idx])

        return results