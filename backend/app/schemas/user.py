from pydantic import BaseModel, EmailStr, Field, ConfigDict

import uuid
from datetime import datetime


# This schema is used for creating a new user. It includes validation for the full name, email, and password fields.
class UserCreate(BaseModel):
    full_name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Full name must be between 1 and 100 characters long.",
    )
    email: EmailStr
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        description="Password must be between 8 and 128 characters long.",
    )


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    full_name: str
    email: EmailStr
    created_at: datetime
