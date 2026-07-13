from sentence_transformers import SentenceTransformer
from ..vectorstore.chroma_store import get_collection
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def retrieve(query: str, top_k: int = 5):
    collection = get_collection()

    query_embedding = model.encode(
        query,
        normalize_embeddings=True
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    retrieved = []

    for i in range(len(results["ids"][0])):
        retrieved.append({
            "score": results["distances"][0][i],
            "chunk": {
                "chunk_id": results["metadatas"][0][i]["chunk_id"],
                "source": results["metadatas"][0][i]["source"],
                "page": results["metadatas"][0][i]["page"],
                "text": results["documents"][0][i],
            }
        })

    return retrieved