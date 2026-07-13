import chromadb
from ..ingestion.embedding_service import embedder
from ..utils.utils import compute_file_hash
from pathlib import Path
CHROMA_PATH = "data/chroma_db"
COLLECTION_NAME = "engineering_docs"

def is_file_indexed(file_hash: str) -> bool:
    collection=get_collection()
    results = collection.get(
        where={"source_hash": file_hash},
        limit=1
    )
    return len(results["ids"]) > 0

def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    return client.get_or_create_collection(
        name=COLLECTION_NAME
    )


def index_embeddings(file):
    collection = get_collection()

    for chunk in embedder(file):
        collection.add(
            ids=[str(chunk["chunk_id"])],
            embeddings=[chunk["embedding"]],
            documents=[chunk["text"]],
            metadatas=[{
                "source": chunk["source"],
                "page": chunk["page"],
                "chunk_id": chunk["chunk_id"],
                "source_hash":chunk["source_hash"],
                "start_word": chunk["start_word"],
                "end_word": chunk["end_word"],
            }]
        )