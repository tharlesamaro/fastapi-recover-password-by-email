from dotenv import load_dotenv
from pydantic import BaseSettings, EmailStr

load_dotenv()


class MailConfig(BaseSettings):
    MAIL_USERNAME: str = ""
    MAIL_PASSWORD: str = ""
    MAIL_FROM: EmailStr
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str = ""
    MAIL_TLS: bool = True
    MAIL_SSL: bool = False
    MAIL_USE_CREDENTIALS: bool = True
    MAIL_VALIDATE_CERTS: bool = True
    MAIL_RESET_TOKEN_EXPIRE_HOURS: int = 24


mail_config = MailConfig()
