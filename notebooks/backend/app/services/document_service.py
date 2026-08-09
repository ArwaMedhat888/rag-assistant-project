from pathlib import Path
from pypdf import PdfReader

from app.services.embedding_service import create_embedding
from app.services.vector_service import add_embedding


DOCUMENTS_DIR = Path(r"D:\rag-assistant-project\data\documents")


def load_documents():
    documents = []

    for pdf_path in DOCUMENTS_DIR.glob("*.pdf"):
        reader = PdfReader(str(pdf_path))

        for page_number, page in enumerate(reader.pages):
            text = page.extract_text()

            if text and text.strip():
                documents.append({
                    "file": pdf_path.name,
                    "page": page_number + 1,
                    "text": text
                })

    return documents


def index_documents():
    documents = load_documents()

    for document in documents:
        embedding = create_embedding(document["text"])
        add_embedding(embedding)

    return documents