from typing import Any, Coroutine

from app.config import app_config, mail_config
from app.data.models import User

from .base_email import BaseEmail


class SendResetPasswordEmail(BaseEmail):
    async def send(self, user: User, token: str) -> Coroutine[Any, Any, None]:
        app_name = app_config.APP_NAME
        email_to = user.email
        subject = f"[{app_name}] Password recovery"

        await self.send_email(
            subject=subject,
            recipients=[email_to],
            template_name="send_reset_password_email.html",
            template_body={
                "app_name": app_name,
                "user_name": user.name,
                "user_email": email_to,
                "valid_hours": mail_config.MAIL_RESET_TOKEN_EXPIRE_HOURS,
                "link": f"https://my-fake-website.com/reset-password?token={token}",
            },
        )
