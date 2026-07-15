from src.llm import generate_response


def analyze_resume(resume_text):

    prompt = f"""
You are an expert resume analyzer.

Analyze the resume below and provide:

1. Professional Summary
2. Technical Skills
3. Tools and Technologies
4. Experience Highlights
5. Projects
6. Possible Interview Questions


Resume:

{resume_text}


Analysis:
"""

    response = generate_response(prompt)

    return response