from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, APIRouter, status
from app.schemas.user import UserCreate, UserOut
from app.db.session import get_db
from fastapi.concurrency import run_in_threadpool
from app.core.security import hash_password
from app.models import User

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def signup(user_in: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    """
    Create a new user in the database.
    """
    # Hash the password
    hashed = await run_in_threadpool(hash_password, user_in.password)

    # Create a new user instance
    new_user = User(
        email=user_in.email,
        hashed_password=hashed,
        full_name=user_in.full_name,
    )

    # Add the new user to the database
    db.add(new_user)  # Staging the new user instance to the session
    await db.commit()  # Committing the transaction to persist the new user in the database
    await db.refresh(
        new_user
    )  # Refreshing the new user instance to get the updated state from the database

    return new_user
