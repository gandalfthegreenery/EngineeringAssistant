from sentence_transformers import SentenceTransformer
from .chunker import chunker

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def embedder(file):
    for chunk in chunker(file):
        embedding=model.encode(
            chunk["text"],
            normalize_embeddings=True
        )
        chunk["embedding"]=embedding.tolist()

        yield chunk