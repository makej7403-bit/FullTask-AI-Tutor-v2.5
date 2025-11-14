import os
import openai

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def ask_ai(system_prompt: str, user_prompt: str, model: str = "gpt-4o",
           temperature: float = 0.2, max_tokens: int = 1500):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    resp = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1.0,
        n=1
    )
    return resp.choices[0].message["content"].strip()
