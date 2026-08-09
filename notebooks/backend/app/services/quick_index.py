from pathlib import Path
from pypdf import PdfReader

from app.services.embedding_service import create_embedding
from app.services.vector_service import add_embedding


DOCUMENTS_DIR = Path(r"D:\rag-assistant-project\data\documents")


def build_index():
    for pdf_path in DOCUMENTS_DIR.glob("*.pdf"):
        reader = PdfReader(str(pdf_path))

        for page_number, page in enumerate(reader.pages[:3], start=1):
            page_text = page.extract_text()

            if page_text and page_text.strip():
                text = page_text.strip()

                embedding = create_embedding(text[:5000])

                add_embedding(
                    embedding,
                    text,
                    pdf_path.name,
                    page_number
                )

    print("Quick index created successfully.")