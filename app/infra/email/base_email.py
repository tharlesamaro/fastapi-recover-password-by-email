from pathlib import Path
from typing import Any, Coroutine

from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from pydantic import EmailStr

from app.config import mail_config


class BaseEmail:
    def __init__(self):
        self.conf = ConnectionConfig(
            MAIL_USERNAME=mail_config.MAIL_USERNAME,
            MAIL_PASSWORD=mail_config.MAIL_PASSWORD,
            MAIL_FROM=mail_config.MAIL_FROM,
            MAIL_PORT=mail_config.MAIL_PORT,
            MAIL_SERVER=mail_config.MAIL_SERVER,
            MAIL_FROM_NAME=mail_config.MAIL_FROM_NAME,
            MAIL_TLS=mail_config.MAIL_TLS,
            MAIL_SSL=mail_config.MAIL_SSL,
            USE_CREDENTIALS=mail_config.MAIL_USE_CREDENTIALS,
            VALIDATE_CERTS=mail_config.MAIL_VALIDATE_CERTS,
            TEMPLATE_FOLDER=Path(__file__).parent.parent.parent / "html/email",
        )

    async def send_email(
        self,
        *,
        subject: str,
        recipients: list[EmailStr],
        template_name: str,
        template_body: list | dict | None = None,
    ) -> Coroutine[Any, Any, None]:
        message = MessageSchema(
            subject=subject, recipients=recipients, template_body=template_body
        )
        fast_mail = FastMail(self.conf)
        await fast_mail.send_message(message, template_name=template_name)
