# 📄 DocuMentor AI

**DocuMentor AI** is an AI-powered application that combines **Retrieval-Augmented Generation (RAG)** with **Google Gemini** to provide intelligent document question answering, resume analysis, and ATS-style resume matching through an easy-to-use Streamlit interface.

---

## 🚀 Features

### 🤖 AI Assistant

* Ask general questions on any topic.
* Powered by Google Gemini.
* Provides clear and conversational responses.

### 📘 Chat with Documents (RAG)

* Upload PDF documents.
* Extracts text from PDFs.
* Splits documents into semantic chunks.
* Generates embeddings using Sentence Transformers.
* Performs semantic search using FAISS.
* Answers questions using document context.
* Falls back to Gemini's general knowledge if the answer is not found in the document.

### 📄 Resume Analyzer

Upload a resume and receive:

* Professional Summary
* Technical Skills
* Experience Summary
* Project Highlights
* Strengths
* Areas for Improvement
* Suggested Job Roles
* Interview Questions

### 🎯 ATS Resume Match

Compare a resume against a Job Description to generate:

* Estimated ATS Match Score
* Matching Skills
* Missing Skills
* Resume Strengths
* Improvement Suggestions
* Hiring Recommendation

---

# 🛠 Tech Stack

| Category              | Technologies                             |
| --------------------- | ---------------------------------------- |
| Programming Language  | Python                                   |
| Frontend              | Streamlit                                |
| LLM                   | Google Gemini API                        |
| RAG                   | FAISS                                    |
| Embeddings            | Sentence Transformers (all-MiniLM-L6-v2) |
| PDF Processing        | PyPDF                                    |
| Environment Variables | python-dotenv                            |
| Numerical Computing   | NumPy                                    |

---

# 📂 Project Structure

```text
DocuMentor_AI/
│
├── src/
│   ├── app.py
│   ├── pipeline.py
│   ├── llm.py
│   ├── embeddings.py
│   ├── chunker.py
│   ├── pdf_loader.py
│   ├── retriever.py
│   ├── indexer.py
│   ├── faiss_manager.py
│   ├── resume_loader.py
│   ├── resume_analyzer.py
│   └── ats_matcher.py
│
├── data/
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example

# ▶️ Run the Application

```bash
streamlit run src/app.py
```

The application will open automatically in your browser.

---

# 💡 How It Works

## Document Chat

1. Upload a PDF document.
2. Extract text from the PDF.
3. Split the text into smaller chunks.
4. Generate vector embeddings using Sentence Transformers.
5. Store embeddings in FAISS.
6. Retrieve the most relevant chunks based on the user's question.
7. Send the retrieved context and question to Google Gemini.
8. Display the generated response.

---

## Resume Analyzer

1. Upload a resume.
2. Extract text.
3. Send the resume content to Gemini using a structured prompt.
4. Generate:

   * Summary
   * Skills
   * Experience
   * Strengths
   * Improvements
   * Suggested Roles
   * Interview Questions

---

## ATS Resume Match

1. Upload a resume.
2. Paste a Job Description.
3. Gemini compares both documents.
4. Generate:

   * ATS Match Score
   * Matching Skills
   * Missing Skills
   * Resume Feedback
   * Hiring Recommendation

---


# 🔮 Future Enhancements

* Multi-document support
* Conversation history
* Export resume analysis as PDF
* Resume vs Multiple Job Descriptions
* Cloud deployment
* User authentication

---

# 📚 Skills Demonstrated

* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* FAISS
* Prompt Engineering
* Streamlit Application Development
* PDF Processing
* Resume Analysis
* ATS-style Resume Evaluation

---

# 👩‍💻 Author

**Divya Paruchuru**

Aspiring AI/GenAI Engineer passionate about building practical AI applications using Large Language Models, Retrieval-Augmented Generation (RAG), Prompt Engineering, and Machine Learning.
