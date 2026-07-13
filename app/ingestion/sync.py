from pathlib import Path
from ..vectorstore.chroma_store import index_embeddings,is_file_indexed
from ..utils.utils import compute_file_hash

def sync_upload_folder():
    uploaded_files = [f for f in Path('data/uploads').iterdir()if f.is_file()]

    for file in uploaded_files:
        file_hash = compute_file_hash(file)
        if is_file_indexed(file_hash):
            continue
        index_embeddings(file)
