from app.data.types import ModelType


class InvalidCredentials(Exception):
    def __init__(
        self, obj: str | ModelType = "invalid credentials", info: str = ""
    ):
        self.name: str = str(obj)
        self.info = info

        msg = f"{self.name.title()}"
        if info:
            msg += f": {info!r}"

        super().__init__(msg)
