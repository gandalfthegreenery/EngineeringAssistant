from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Engineering Knowledge Assistant"
    chroma_path: str = "./chroma_db"
    openai_api_key:str

    class Config:
        env_file = ".env"


settings = Settings()