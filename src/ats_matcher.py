from llm import generate_response


def ats_match(resume_text, job_description):

    prompt = f"""
You are an experienced ATS (Applicant Tracking System) evaluator and technical recruiter.

Compare the following resume with the job description.

Provide the output in the following format:

## ATS Match Score
Give an estimated score out of 100.

## Matching Skills
List the skills present in both the resume and the job description.

## Missing Skills
List important skills mentioned in the job description but missing from the resume.

## Resume Strengths
Highlight the strongest aspects of the resume.

## Areas for Improvement
Suggest practical improvements to better match the job description.

## Final Recommendation
Provide a short hiring recommendation.

Resume:
{resume_text}

Job Description:
{job_description}
"""

    return generate_response(prompt)