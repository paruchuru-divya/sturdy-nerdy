import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL_NAME = "llama-3.3-70b-versatile"


def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are DocuMentor AI, a helpful AI assistant. "
                        "Answer clearly, accurately, and professionally."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=1024
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    answer = generate_response("Explain Generative AI in simple words.")
    print(answer)