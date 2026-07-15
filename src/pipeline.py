from src.retriever import retrieve
from src.llm import generate_response

def ask(question):

    """
    Hybrid RAG pipeline:

    1. Try to answer from uploaded document.
    2. If no useful document context is found,
       use Groq as a general AI assistant.
    """

    # Retrieve relevant document chunks
    results = retrieve(question)

    # Case 1: No document context found
    if not results:

        prompt = f"""
You are EduExplain, a helpful AI assistant.

The user may ask questions unrelated to the uploaded document.
Answer the question normally using your general knowledge.

Question:
{question}

Answer:
"""

        answer = generate_response(prompt)

        return answer, []


    # Case 2: Document context found

    context = "\n\n".join(results)


    prompt = f"""
You are DocuMentor AI, an AI assistant.

Use the document context when it is relevant.

If the document does not contain enough information,
answer using your general knowledge.

Document Context:
{context}


Question:
{question}


Answer:
"""


    answer = generate_response(prompt)


    return answer, results