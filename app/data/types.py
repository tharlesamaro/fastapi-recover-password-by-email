from typing import Type, TypeVar

from .models.base_model import BaseModel

Model = TypeVar("Model", bound=BaseModel)
ModelType = Type[Model]
