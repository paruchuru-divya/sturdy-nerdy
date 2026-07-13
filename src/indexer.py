from pathlib import Path

from pdf_loader import load_pdf
from chunker import chunk_text
from embeddings import generate_embeddings
from faiss_manager import FAISSManager

BASE_DIR = Path(__file__).resolve().parent.parent


def index_pdf(pdf_path):

    text = load_pdf(pdf_path)

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

    faiss_db = FAISSManager()

    faiss_db.add_chunks(
        chunks,
        embeddings
    )

    print("Indexing Complete")


if __name__ == "__main__":

    pdf = BASE_DIR / "data/documents/sample.pdf"

    index_pdf(pdf)