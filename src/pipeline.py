from retriever import retrieve
from llm import generate_response


def ask(question):
    """
    Returns:
        answer (str)
        sources (list)
    """

    try:
        results = retrieve(question)

        # No PDF indexed or no matching chunks
        if not results:
            answer = generate_response(question)
            return answer, []

        context = "\n\n".join(
            [point.payload["text"] for point in results]
        )

        prompt = f"""
You are EduExplain, an AI assistant.

If the uploaded document contains the answer, answer using the document.

If the uploaded document does not contain enough information,
first say:
"I couldn't find enough information in the uploaded document."

Then provide a general explanation using your own knowledge.

Document Context:
{context}

Question:
{question}

Answer:
"""

        answer = generate_response(prompt)

        return answer, results

    except Exception:

        answer = generate_response(question)

        return answer, []