from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserVO(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
