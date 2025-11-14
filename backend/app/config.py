# backend/app/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    model_name: str = "gpt-4o"
    temperature: float = 0.2
    max_tokens: int = 1500

    class Config:
        env_file = ".env"

settings = Settings()
