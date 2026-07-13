from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.openai_api_key)


def generate_answer(prompt: str, model:str="gpt-5-nano") -> str:
    response = client.responses.create(
        model="gpt-5-nano",
        input=prompt,
    )
    
    return response.output_text