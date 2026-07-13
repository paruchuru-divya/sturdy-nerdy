import os
import streamlit as st

from indexer import index_pdf
from pipeline import ask

# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="EduExplain",
    page_icon="📘",
    layout="wide"
)

# ----------------------------------
# Session State
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = None

# ----------------------------------
# Sidebar
# ----------------------------------

st.sidebar.title("📘 EduExplain")

st.sidebar.markdown("""
### Features

✅ General AI Assistant

✅ Upload PDF (Optional)

✅ RAG using Qdrant

✅ Google Gemini

✅ Semantic Search
""")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# ----------------------------------
# Main Page
# ----------------------------------

st.title("📘 EduExplain")

st.write(
    "Upload a PDF (optional) and ask questions about it "
    "or ask anything in general."
)

# ----------------------------------
# PDF Upload
# ----------------------------------

uploaded_file = st.file_uploader(
    "Upload PDF (Optional)",
    type=["pdf"]
)

if uploaded_file is not None:

    if uploaded_file.name != st.session_state.current_pdf:

        os.makedirs("data/documents", exist_ok=True)

        save_path = os.path.join(
            "data",
            "documents",
            uploaded_file.name
        )

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Indexing PDF..."):

            index_pdf(save_path)

        st.session_state.current_pdf = uploaded_file.name

        st.success("✅ PDF uploaded and indexed successfully!")

    else:

        st.info(f"📄 Current PDF: {uploaded_file.name}")

# ----------------------------------
# Display Chat
# ----------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------------
# Chat Input
# ----------------------------------

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

            answer, sources = ask(question)

        st.markdown(answer)

        if sources:

            with st.expander("📄 Retrieved Context"):

                for i, source in enumerate(sources, start=1):

                    st.markdown(f"### Chunk {i}")

                    st.write(source.payload["text"])

                    st.divider()

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )