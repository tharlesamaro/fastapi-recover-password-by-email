from datetime import datetime

from pydantic import EmailStr
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from .base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String)
    email: EmailStr = Column(String, unique=True, index=True)
    password: str = Column(String)
    is_active = Column(Boolean, default=True)
    created_at: datetime = Column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )
    updated_at: datetime = Column(
        DateTime,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
        nullable=False,
    )
