# 🤖 RAG Assistant

A Retrieval-Augmented Generation (RAG) web application that allows users to ask questions about a collection of PDF documents and receive grounded answers based on retrieved document context.

## 📌 Project Overview

This project implements an end-to-end RAG pipeline starting from PDF document collection and text extraction to embeddings, vector search, LLM-based answer generation, backend API development, evaluation, and a Streamlit frontend.

The system retrieves relevant document chunks before generating an answer, helping keep responses grounded in the provided documents.

## 🏗️ Architecture

The application follows this workflow:

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

## 📂 Project Structure

```text
rag-assistant-project/
│
├── data/
│   └── documents/
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
│       │   │   ├── embedding_service.py
│       │   │   ├── vector_service.py
│       │   │   ├── llm_service.py
│       │   │   └── quick_index.py
│       │   │
│       │   └── main.py
│       │
│       ├── tests/
│       │   └── test_query.py
│       │
│       ├── streamlit_app.py
│       └── .env
│
├── .gitignore
├── requirements.txt
└── README.md
Technologies
Python
FastAPI
Streamlit
ChromaDB
Sentence Transformers
Hugging Face
PyPDF
Pandas
Pytest

Installation

Clone the repository:
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd rag-assistant-project
 
 python -m venv .venv

 .venv\Scripts\activate

pip install -r requirements.txt

Environment Variables

Create a .env file inside the backend directory:
API_URL=http://127.0.0.1:8000

Running the Backend

Navigate to the backend directory:
cd notebooks/backend

Run FastAPI:
uvicorn app.main:app --reload
The API will be available at:
http://127.0.0.1:8000
Running the Frontend

Keep the FastAPI server running and open another terminal.
cd notebooks/backend

Run Streamlit:
streamlit run streamlit_app.py

Example Query
What is deep learning?
The application returns:

Generated answer
Retrieved document sources
Page numbers of the retrieved documents
🧪 Evaluation

The RAG pipeline was evaluated using 10 questions.

Evaluation results included:

Generated answers
Retrieved sources
Number of retrieved sources per question

Average number of retrieved sources per question:

3.0
Testing

The backend includes automated tests using Pytest.

Run:

python -m pytest

Current test result:

1 passed
Grounded Responses

The system generates answers using retrieved document context rather than relying only on the language model's internal knowledge.

Each response also provides the source document and page number used during retrieval.

🔒 Files Excluded from GitHub

The following files and directories are intentionally excluded:

.venv/
.env
Python cache files
Vector database files
IDE configuration files
Jupyter checkpoints
Author

AI Engineering Student

📄 License

This project was developed as an individual academic assignment.