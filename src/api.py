from fastapi import FastAPI
from pydantic import BaseModel

from src.pipeline import ask
from src.resume_loader import extract_resume_text
from src.resume_analyzer import analyze_resume
from src.ats_matcher import ats_match

app = FastAPI(
    title="DocuMentor AI API",
    description="AI-powered Document Assistant with RAG, Resume Analysis and ATS Matching",
    version="1.0.0"
)

# Request Models

class ChatRequest(BaseModel):
    question: str


class ResumeRequest(BaseModel):
    pdf_path: str


class ATSRequest(BaseModel):
    resume_text: str
    job_description: str

# Basic APIs

@app.get("/")
def home():
    return {
        "message": "Welcome to DocuMentor AI API"
    }


@app.get("/health")
def health():
    return {
        "status": "running"
    }

# AI Chat API

@app.post("/chat")
def chat(request: ChatRequest):

    answer, sources = ask(request.question)

    return {
        "answer": answer,
        "sources": sources
    }

# Resume Analyzer API

@app.post("/resume-analysis")
def resume_analysis(request: ResumeRequest):

    resume_text = extract_resume_text(request.pdf_path)

    analysis = analyze_resume(resume_text)

    return {
        "analysis": analysis
    }

# ATS Resume Match API

@app.post("/ats-match")
def ats_resume_match(request: ATSRequest):

    result = ats_match(
        request.resume_text,
        request.job_description
    )

    return {
        "result": result
    }