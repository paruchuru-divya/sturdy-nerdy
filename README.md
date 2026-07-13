# 📘 EduExplain – AI-Powered Document Assistant

EduExplain is a Hybrid Retrieval-Augmented Generation (RAG) application that allows users to either upload a PDF and ask questions about its contents or ask general questions without uploading any document.

The application combines semantic search using Qdrant with Google's Gemini LLM to provide accurate, context-aware responses.

---

## 🚀 Features

* 📄 Upload PDF (Optional)
* 🤖 General AI Assistant using Gemini
* 🔍 Semantic Search with Qdrant
* 🧠 Sentence Transformer Embeddings
* 💬 Chat-style Streamlit Interface
* ⚡ Automatic PDF Indexing
* 📑 Context-based Question Answering
* 🔄 Falls back to Gemini when no relevant document context is found

---

## 🏗️ Architecture

```
User
   │
   ▼
Streamlit UI
   │
   ├──────────────► General Question
   │                     │
   │                     ▼
   │                 Gemini API
   │
   ▼
Upload PDF
   │
   ▼
PDF Loader
   │
   ▼
Chunking
   │
   ▼
Sentence Transformer
   │
   ▼
Qdrant Vector Database
   │
   ▼
Semantic Retrieval
   │
   ▼
Gemini API
   │
   ▼
Response
```

---

## 🛠 Tech Stack

* Python
* Streamlit
* Google Gemini API
* Qdrant Vector Database
* Sentence Transformers
* PyPDF
* Hugging Face Embeddings

---

## 📂 Project Structure

```
EduExplain_RAG/
│
├── src/
│   ├── app.py
│   ├── pdf_loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── qdrant_manager.py
│   ├── pipeline.py
│   ├── indexer.py
│   ├── llm.py
│   └── model_loader.py
│
├── data/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd EduExplain_RAG
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run src/app.py
```

---

## 💡 How It Works

1. Upload a PDF (optional).
2. The PDF is split into text chunks.
3. Embeddings are generated using Sentence Transformers.
4. Chunks are stored in Qdrant.
5. User asks a question.
6. Relevant chunks are retrieved.
7. Gemini generates a grounded answer using the retrieved context.
8. If no relevant context exists, Gemini provides a general answer.

---

## 📈 Future Improvements

* Support multiple PDFs
* Conversation memory
* Source relevance scores
* OCR for scanned PDFs
* Authentication
* Docker deployment
* Cloud-hosted Qdrant

---

## 📸 Screenshots

Add screenshots of:

* Home Page
* PDF Upload
* Chat Interface
* Retrieved Context

---

## 👩‍💻 Author

**Divya Paruchuru**

Aspiring AI / Generative AI Engineer with experience in Machine Learning data operations, Retrieval-Augmented Generation (RAG), LLM integration, and AI application development.
