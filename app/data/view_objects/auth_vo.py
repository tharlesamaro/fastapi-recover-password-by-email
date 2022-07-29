from pydantic import BaseModel


class AuthVO(BaseModel):
    token_type: str
    expires_in: float
    access_token: str
