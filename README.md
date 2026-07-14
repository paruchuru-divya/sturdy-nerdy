# 📄 DocuMentor AI

An AI-powered application that combines **Retrieval-Augmented Generation (RAG)**, **Groq Llama 3.3**, and **FAISS** to provide intelligent document question answering, resume analysis, and ATS-style resume matching through an interactive Streamlit interface.

---

## 🚀 Features

### 🤖 AI Assistant

* Ask general questions on any topic.
* Powered by **Groq Llama 3.3 70B Versatile**.
* Provides fast and accurate responses.

### 📘 Chat with Document (RAG)

* Upload PDF documents.
* Extract text from PDFs.
* Split documents into semantic chunks.
* Generate embeddings using Sentence Transformers.
* Store vectors using FAISS.
* Retrieve the most relevant document chunks.
* Answer questions using document context.
* Falls back to the LLM's general knowledge when information is unavailable in the uploaded document.

### 📄 Resume Analyzer

Upload a resume and receive:

* Professional Summary
* Skills Identification
* Experience Overview
* Strengths
* Areas for Improvement
* Suggested Job Roles
* Interview Questions

### 🎯 ATS Resume Match

Compare a resume with a Job Description to generate:

* ATS Match Score
* Matching Skills
* Missing Skills
* Resume Feedback
* Improvement Suggestions

---

# 🛠 Tech Stack

| Category              | Technologies                             |
| --------------------- | ---------------------------------------- |
| Language              | Python                                   |
| Frontend              | Streamlit                                |
| LLM                   | Groq API (Llama 3.3 70B Versatile)       |
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
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

# ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/paruchuru-divya/DocuMentor-AI.git
cd DocuMentor-AI
```

### Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root.

```text
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Application

```bash
streamlit run src/app.py
```

---

# 💡 Workflow

### Document Chat

1. Upload a PDF.
2. Extract text from the document.
3. Split the text into chunks.
4. Generate embeddings using Sentence Transformers.
5. Store vectors in FAISS.
6. Retrieve the most relevant chunks.
7. Send the retrieved context and user question to Groq Llama 3.3.
8. Display the generated response.

### Resume Analyzer

1. Upload a resume.
2. Extract text from the PDF.
3. Analyze the resume using Groq.
4. Generate:

   * Summary
   * Skills
   * Experience
   * Strengths
   * Improvements
   * Suggested Roles
   * Interview Questions

### ATS Resume Match

1. Upload a resume.
2. Paste a Job Description.
3. Compare both documents using Groq.
4. Generate:

   * ATS Match Score
   * Matching Skills
   * Missing Skills
   * Resume Feedback
   * Suggestions

---

# 📸 Screenshots

Add screenshots of:

* Home Page
* AI Assistant
* Document Chat
* Resume Analyzer
* ATS Resume Match

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
* ATS Resume Matching

---

# 🔮 Future Enhancements

* Multi-document support
* Conversation history
* Export reports as PDF
* Cloud deployment
* User authentication
* Support for additional LLM providers

---

# 👩‍💻 Author

**Divya Paruchuru**

Aspiring AI/GenAI Engineer passionate about building intelligent applications using Large Language Models, Retrieval-Augmented Generation (RAG), Prompt Engineering, and Machine Learning.
