from fastapi import FastAPI
from app.core.config import settings

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, AI Document Search Platform!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}