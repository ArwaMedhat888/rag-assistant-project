# 🤖 RAG Assistant

A Retrieval-Augmented Generation (RAG) web application that allows users to ask questions about a collection of PDF documents and receive grounded answers based on retrieved document context.

## 📌 Project Overview

This project implements an end-to-end RAG pipeline starting from PDF document collection and text extraction to embeddings, vector search, LLM-based answer generation, backend API development, evaluation, and a Streamlit frontend.

The system retrieves relevant document chunks before generating an answer, helping keep responses grounded in the provided documents.

## 🏗️ Architecture

The application follows this workflow:

```text
PDF Documents
      ↓
Text Extraction
      ↓
Chunking
      ↓
Embeddings
      ↓
ChromaDB Vector Store
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Retrieved Context
      ↓
LLM
      ↓
Grounded Answer
      ↓
Streamlit Interface
```

## 📂 Project Structure

```text
rag-assistant-project/
│
├── notebooks/
│   ├── rag_pipeline.ipynb
│   │
│   └── backend/
│       ├── app/
│       │   ├── api/
│       │   │   └── routes/
│       │   │       └── query.py
│       │   │
│       │   ├── services/
│       │   │   ├── document_service.py
│       │   │   ├── embedding_service.py
│       │   │   ├── embedding_service_new.py
│       │   │   ├── vector_service.py
│       │   │   ├── llm_service.py
│       │   │   └── quick_index.py
│       │   │
│       │   ├── core/
│       │   │   └── config.py
│       │   │
│       │   └── main.py
│       │
│       ├── tests/
│       │   └── test_query.py
│       │
│       ├── streamlit_app.py
│       └── requirements.txt
│
├── .gitignore
└── README.md
```

> The PDF documents and generated vector database are excluded from GitHub to keep the repository clean and avoid uploading large/generated files.

## 🛠️ Technologies

* Python
* FastAPI
* Streamlit
* ChromaDB
* Sentence Transformers
* Hugging Face
* PyPDF
* Pandas
* Pytest

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/ArwaMedhat888/rag-assistant-project.git
cd rag-assistant-project
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r notebooks/backend/requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file inside:

```text
notebooks/backend/
```

Add the required environment variables, for example:

```env
API_URL=http://127.0.0.1:8000
```

> Do not upload the `.env` file to GitHub.

## ▶️ Running the Backend

Navigate to the backend directory:

```bash
cd notebooks/backend
```

Run FastAPI:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 💬 Running the Frontend

Keep the FastAPI server running and open another terminal.

Navigate to:

```bash
cd notebooks/backend
```

Run Streamlit:

```bash
streamlit run streamlit_app.py
```

The Streamlit interface will open in the browser.

## 🧪 Testing

The backend includes automated tests using Pytest.

Run:

```bash
python -m pytest
```

Current test result:

```text
1 passed
```

## 📊 Evaluation

The RAG pipeline was evaluated using 10 questions.

The evaluation included:

* Generated answers
* Retrieved document sources
* Number of retrieved sources per question

Average number of retrieved sources per question:

```text
3.0
```

## 🔎 Grounded Responses

The system generates answers using retrieved document context rather than relying only on the language model's internal knowledge.

Each response also provides the source document and page number used during retrieval.

## 🔒 Files Excluded from GitHub

The following files and directories are intentionally excluded:

```text
.venv/
.env
__pycache__/
*.pyc
chroma_db/
backend/data/vector_store/
data/documents/
```

## 👤 Author

AI Engineering Student

## 📄 License

This project was developed as an individual academic assignment.
