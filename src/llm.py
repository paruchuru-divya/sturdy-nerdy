import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_response(prompt):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":

    answer = generate_response(
        "Explain Machine Learning in simple words."
    )

    print(answer)