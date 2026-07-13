def build_prompt(query:str,retrieved_chunks:list[dict]):
    context_blocks = []
    for idx, result in enumerate(retrieved_chunks,start=1):
        chunk=result["chunk"]
        context_blocks.append(
            f"""
[Source {idx}]
Document:{chunk["source"]}
page:{chunk["page"]}
Text:
{chunk["text"]}
            """
        )
    context = "\n".join(context_blocks)
    return f"""
You are an engineering knowledge assistant.

Please answer the question using only the provided context.
If the context does not contain enough information, tell the user you do not know.
Cite the relevant source number(s) in your answer in the format [Source i] [Source j]... etc. 

Context:
{context}

Question:
{query}

Answer:
"""