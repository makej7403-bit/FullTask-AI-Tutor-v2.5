# backend/app/api.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from .services.openai_client import ask_ai
from .config import settings  # pydantic BaseSettings

router = APIRouter()

class UserQuery(BaseModel):
    user_id: str
    prompt: str
    subject: str = "general"
    max_tokens: int | None = None
    temperature: float | None = None

@router.post("/ask")
def ask(user_query: UserQuery):
    system_prompt = (
        "You are FullTask AI Tutor 6.5, an expert tutor across multiple subjects. "
        "Give clear, step-by-step explanations. Adapt to user level."
    )
    # Merge per-request overrides
    model = settings.model_name
    temperature = user_query.temperature or settings.temperature
    max_tokens = user_query.max_tokens or settings.max_tokens

    answer = ask_ai(system_prompt, f"Subject: {user_query.subject}\nUser: {user_query.prompt}",
                    model=model, temperature=temperature, max_tokens=max_tokens)
    return {"answer": answer}
