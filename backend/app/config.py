# backend/app/config.py
# Use BaseSettings from pydantic_settings (required for newer pydantic versions)

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_name: str = "gpt-4o"
    temperature: float = 0.2
    max_tokens: int = 1500

    class Config:
        env_file = ".env"

settings = Settings()
