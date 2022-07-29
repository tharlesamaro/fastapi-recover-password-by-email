from app.data.types import ModelType


class DuplicateEntry(Exception):
    def __init__(self, obj: str | ModelType, info: str = ""):
        self.name: str = str(obj)
        self.info = info

        msg = f"{self.name.title()} already exists"
        if info:
            msg += f": {info!r}"

        super().__init__(msg)
