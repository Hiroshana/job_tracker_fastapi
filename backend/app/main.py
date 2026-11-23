from fastapi import FastAPI, Depends
from app.core.config import settings
from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.db.session import get_db

app = FastAPI(
    title=settings.app_name,
    description="This is a developed by FastAPI.",
    version="1.0.0",
)


@app.get("/")
async def home():
    return {"message": "Welcome to the My Job Application Tracker"}


@app.get("/health")
async def health(db: Annotated[AsyncSession, Depends(get_db)]):
    await db.execute(text("SELECT 1"))
    return {"status": "ok", "database": "ok"}
