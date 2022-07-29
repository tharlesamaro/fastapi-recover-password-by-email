from app_config import app_config

from .auth_config import auth_config
from .database_config import database_config
from .mail_config import mail_config

__all__ = [
    "app_config",
    "auth_config",
    "database_config",
    "mail_config",
]
