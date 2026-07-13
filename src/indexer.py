from pathlib import Path

from pdf_loader import load_pdf
from chunker import chunk_text
from embeddings import generate_embeddings
from qdrant_manager import QdrantManager


BASE_DIR = Path(__file__).resolve().parent.parent


def index_pdf(pdf_path):

    print("Loading PDF...")

    text = load_pdf(pdf_path)

    print("Chunking document...")

    chunks = chunk_text(text)

    print(f"Created {len(chunks)} chunks")

    print("Generating embeddings...")

    embeddings = generate_embeddings(chunks)

    print("Connecting to Qdrant...")

    qdrant = QdrantManager(reset=True)

    print("Storing vectors...")

    qdrant.add_chunks(chunks, embeddings)

    print("Indexing Completed Successfully!")


if __name__ == "__main__":

    pdf_path = BASE_DIR / "data" / "documents" / "sample.pdf"

    index_pdf(pdf_path)