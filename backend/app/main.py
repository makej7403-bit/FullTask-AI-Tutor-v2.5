# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import router as api_router

app = FastAPI(title="FullTask AI Tutor 6.5")

# CORS for local testing; tighten in prod
app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"],
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
 return {"message": "FullTask AI Tutor 6.5 is running"}
