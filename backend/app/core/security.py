# Simple example; implement JWT if you add multi-user auth
from typing import Optional

def dummy_auth(token: str = "") -> Optional[str]:
    # In production, verify token and return user_id
    if token:
        return token  # stub
    return None
