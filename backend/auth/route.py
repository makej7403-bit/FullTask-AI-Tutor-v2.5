from fastapi import APIRouter, Depends, HTTPException
from .schemas import TokenData
from ..services.firebase_auth import verify_token

router = APIRouter()

def get_current_user(authorization: str = None):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing auth header")
    token = authorization.replace("Bearer ", "")
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

@router.get("/whoami")
def whoami(current_user: dict = Depends(get_current_user)):
    return {"uid": current_user["uid"], "email": current_user["email"]}
