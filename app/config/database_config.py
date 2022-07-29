from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class DatabaseConfig(BaseSettings):
    DB_CONNECTION_STRING: str


database_config = DatabaseConfig()
