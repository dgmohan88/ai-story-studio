from fastapi import FastAPI

from app.core.config import settings
from app.db.base import Base
from app.db.models import Story
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name} 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "environment": settings.app_env,
        "version": settings.app_version,
    }