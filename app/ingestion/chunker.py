from app.ingestion.file_loader import file_loader

def chunker(file):
    chunk_length = 200
    overlap = 50
    step = chunk_length-overlap
    chunk_id=0
    for page in file_loader(file):
        words = page["text"].split()
        for i in range(0,len(words),step):
            chunk = {
                "page":page["page"],
                "source":page["source"],
                "source_hash":page["source_hash"],
                "chunk_id":chunk_id,
                "text":" ".join(words[i:i+chunk_length]),
                "start_word": i,
                "end_word": min(i + chunk_length, len(words)-1)
            }
            chunk_id+=1
            yield chunk