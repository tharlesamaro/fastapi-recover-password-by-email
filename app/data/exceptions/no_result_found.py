from app.data.types import ModelType


class NoResultFound(Exception):
    def __init__(self, obj: str | ModelType, info: str = ""):
        self.name: str = str(obj)
        self.info = info

        msg = f"{self.name.title()} not found"
        if info:
            msg += f": {info!r}"

        super().__init__(msg)
