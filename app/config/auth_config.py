from dotenv import load_dotenv
from pydantic import BaseSettings, EmailStr

load_dotenv()


class AuthConfig(BaseSettings):
    PEPPER: str
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_HOURS: int = 1
    JWT_TOKEN_TYPE: str = "Bearer"


auth_config = AuthConfig()
