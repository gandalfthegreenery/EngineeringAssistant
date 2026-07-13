from ..retrieval.retriever import retrieve
from ..retrieval.prompt_builder import build_prompt
from  .llm_service import generate_answer

import re

def extract_source_numbers(answer: str) -> set[int]:
    matches = re.findall(r"\[Source (\d+)\]", answer)
    return {int(m) for m in matches}

def format_sources(cited_numbers: set[int], retrieved_chunks: list[dict]) -> str:
    sources = []

    for number in sorted(cited_numbers):
        result = retrieved_chunks[number - 1]
        chunk = result["chunk"]
        sources.append({"chunk_id":chunk["chunk_id"],"document":chunk["source"],"page":chunk["page"]})

    return sources

def orchestrator(query:str,top_k:int=5):
    pertinent_chunks = retrieve(query, top_k=top_k)

    prompt = build_prompt(query, pertinent_chunks)
    llm_answer = generate_answer(prompt)
    cited_answer = extract_source_numbers(llm_answer)
    cited_chunks = format_sources(cited_answer,pertinent_chunks)
    return {"answer":llm_answer,
              "sources":cited_chunks
              }
