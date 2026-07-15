import os
import streamlit as st
import requests

from indexer import index_pdf
from resume_loader import extract_resume_text
from resume_analyzer import analyze_resume
from ats_matcher import ats_match

# Page Config

st.set_page_config(
    page_title="DocuMentor AI",
    page_icon="📘",
    layout="wide"
)

# Session State

if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = None

# Sidebar

st.sidebar.title("📄 DocuMentor AI")

mode = st.sidebar.selectbox(
    "Choose Mode",
    [
        "🤖 AI Assistant",
        "📘 Chat with Document",
        "📄 Resume Analyzer",
        "🎯 ATS Resume Match"
    ]
)

if st.session_state.current_pdf:
    st.sidebar.success(f"Current PDF:\n\n{st.session_state.current_pdf}")
else:
    st.sidebar.info("No PDF uploaded")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Main Title

st.title("📄 DocuMentor AI")
st.caption("AI-Powered Document Chat, Resume Analyzer & ATS Matcher")

# PDF Upload

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

save_path = None

if uploaded_file is not None:

    MAX_FILE_SIZE = 50 * 1024 * 1024

    if uploaded_file.size > MAX_FILE_SIZE:
        st.error("Please upload a PDF smaller than 50 MB.")
        st.stop()

    os.makedirs("data/documents", exist_ok=True)

    save_path = os.path.join(
        "data",
        "documents",
        uploaded_file.name
    )

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Index only for Document Chat
    if (
        mode == "📘 Chat with Document"
        and uploaded_file.name != st.session_state.current_pdf
    ):

        with st.spinner("Indexing PDF..."):
            index_pdf(save_path)

        st.session_state.current_pdf = uploaded_file.name

        st.success("✅ PDF indexed successfully!")

# MODE 1 : AI Assistant

if mode == "🤖 AI Assistant":

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask anything...")

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                    response = requests.post(
                        "http://127.0.0.1:8000/chat",
                        json={
                            "question": question
                        }
                    )
                    result = response.json()
                    answer=result["answer"]

            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

# MODE 2 : Chat with Document

elif mode == "📘 Chat with Document":

    if uploaded_file is None:

        st.info("Upload a PDF to start chatting.")

    else:

        for message in st.session_state.messages:

            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        question = st.chat_input("Ask a question about the document...")

        if question:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            with st.chat_message("user"):
                st.markdown(question)

            with st.chat_message("assistant"):

                with st.spinner("Thinking..."):

                     response = requests.post(
                        "http://127.0.0.1:8000/chat",
                        json={
                             "question": question
                        }
                     )

                     result = response.json()

                     answer = result["answer"]

                     st.markdown(answer)                    

                

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

# MODE 3 : Resume Analyzer

elif mode == "📄 Resume Analyzer":

    if uploaded_file is None:

        st.info("Upload your resume PDF.")

    else:

        if st.button("📄 Analyze Resume"):

            with st.spinner("Analyzing Resume..."):

                resume_text = extract_resume_text(save_path)

                analysis = analyze_resume(resume_text)

            st.markdown(analysis)

# MODE 4 : ATS Resume Match

elif mode == "🎯 ATS Resume Match":

    if uploaded_file is None:

        st.info("Upload your resume PDF.")

    else:

        job_description = st.text_area(
            "Paste Job Description",
            height=250
        )

        if st.button("🎯 Analyze ATS Match"):

            if not job_description.strip():

                st.warning("Please paste a Job Description.")

            else:

                with st.spinner("Analyzing ATS Match..."):

                    resume_text = extract_resume_text(save_path)

                    result = ats_match(
                        resume_text,
                        job_description
                    )

                st.markdown(result)