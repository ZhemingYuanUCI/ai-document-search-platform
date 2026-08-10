from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello, AI Document Search Platform!"}


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    return {
        "status": "ok",
        "database_session": db.is_active,
    }
