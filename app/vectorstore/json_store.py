import json 
import os
from ..ingestion.embedding_service import embedder

def write_to_json():
    with open('../embeddings/embeddings.json',"w")as file:
        file.write("[")
        first = True
        for i in embedder():
            if not first:
                file.write(',')
            first=False
            file.write(json.dumps(i))
        file.write("]")
        file.close()
        print("Background PDF's successfully embedded to json.")
    return