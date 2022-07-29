from typing import Any, Coroutine

from app.config import app_config, mail_config
from app.data.models import User

from .base_email import BaseEmail


class SendResetPasswordEmail(BaseEmail):
    async def send(self, user: User, token: str) -> Coroutine[Any, Any, None]:
        app_name = app_config.APP_NAME
        link = f"{app_config.APP_URL}/reset-password?token={token}"
        subject = f"[{app_name}] Password recovery"
        template_name = "send_reset_password_email.html"
        valid_hours = mail_config.MAIL_RESET_TOKEN_EXPIRE_HOURS

        await self.send_email(
            subject=subject,
            recipients=[user.email],
            template_name=template_name,
            template_body={
                "app_name": app_name,
                "link": link,
                "user_name": user.name,
                "user_email": user.email,
                "valid_hours": valid_hours,
            },
        )
