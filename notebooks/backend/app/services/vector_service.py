import uuid
import chromadb


chroma_client = chromadb.PersistentClient(
    path=r"D:\rag-assistant-project\backend\data\vector_store"
)

collection = chroma_client.get_or_create_collection(
    name="documents"
)


def add_embedding(embedding, text, source, page):
    collection.add(
        ids=[str(uuid.uuid4())],
        embeddings=[embedding.tolist()],
        documents=[text],
        metadatas=[
            {
                "source": source,
                "page": page
            }
        ]
    )


def search_documents(question_embedding, k=3):
    results = collection.query(
        query_embeddings=[question_embedding.tolist()],
        n_results=k
    )

    retrieved = []

    for i in range(len(results["documents"][0])):
        metadata = results["metadatas"][0][i]

        if metadata is None:
            continue

        retrieved.append({
            "text": results["documents"][0][i],
            "source": metadata["source"],
            "page": metadata["page"]
        })

    return retrieved
