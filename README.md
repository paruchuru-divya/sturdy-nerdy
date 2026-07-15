# 📄 DocuMentor AI

DocuMentor AI is an AI-powered document assistant that enables users to chat with PDF documents, analyze resumes, and evaluate resume compatibility with job descriptions using an ATS-style assessment.

The application combines Retrieval-Augmented Generation (RAG), semantic search, FastAPI, and Groq LLMs to deliver accurate and context-aware responses.

---

## 🚀 Features

- 💬 AI Assistant for general-purpose question answering
- 📚 Chat with PDF documents using RAG
- 📄 Resume Analyzer
- 🎯 ATS Resume Match
- 🔍 Semantic search with FAISS
- ⚡ FastAPI backend with REST APIs
- 🖥️ Streamlit frontend

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python
- Groq API (Llama 3.3)

### Frontend
- Streamlit

### AI & NLP
- Sentence Transformers
- FAISS
- Retrieval-Augmented Generation (RAG)

### Document Processing
- PyMuPDF

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
DocuMentor_AI/
│
├── data/
│   └── documents/
│
├── src/
│   ├── api.py
│   ├── app.py
│   ├── ats_matcher.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── faiss_manager.py
│   ├── indexer.py
│   ├── llm.py
│   ├── model_loader.py
│   ├── pdf_loader.py
│   ├── pipeline.py
│   ├── resume_analyzer.py
│   ├── resume_loader.py
│   └── retriever.py
│
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/DocuMentor-AI.git
cd DocuMentor-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run FastAPI

```bash
uvicorn src.api:app --reload
```

Open Swagger:

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Streamlit

```bash
python -m streamlit run src/app.py
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Home |
| GET | `/health` | Health Check |
| POST | `/chat` | AI Chat |
| POST | `/resume-analysis` | Resume Analysis |
| POST | `/ats-match` | ATS Resume Match |

---

## 📸 Features

- AI-powered document question answering
- Retrieval-Augmented Generation (RAG)
- Resume analysis using LLMs
- ATS compatibility evaluation
- FastAPI REST API backend
- Streamlit interactive interface
- FAISS semantic search
- Groq Llama 3.3 integration

---

## 👩‍💻 Author

**Divya Paruchuru**

Aspiring AI / Data Science Engineer passionate about Generative AI, LLMs, Retrieval-Augmented Generation (RAG), and AI application development.

---

## ⭐ Future Enhancements

- Multi-PDF support
- Chat history
- User authentication
- Cloud deployment (AWS/Azure)
- Docker support
- Database integration