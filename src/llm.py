import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_response(prompt):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print(e)

        return (
            "⚠️ Gemini is currently unavailable or experiencing high demand.\n\n"
            "Please wait a few moments and try again."
        )


if __name__ == "__main__":

    print(
        generate_response(
            "What is Machine Learning?"
        )
    )