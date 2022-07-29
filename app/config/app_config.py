from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class AppConfig(BaseSettings):
    APP_NAME: str
    APP_DESCRIPTION: str
    APP_URL: str
    APP_ENV: str = "production"


app_config = AppConfig()
