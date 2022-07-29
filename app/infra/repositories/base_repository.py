import re
from typing import Any, Generic

from fastapi_sqlalchemy import db
from sqlalchemy.exc import IntegrityError

from app.data.exceptions import DuplicateEntry, NoResultFound
from app.data.types import Model, ModelType


class BaseRepository(Generic[Model]):
    def __init__(self, model_type: ModelType) -> None:
        self.model_type = model_type

    def create(self, model: Model, /) -> Model:
        try:
            db.session.add(model)
            db.session.commit()
            db.session.refresh(model)
            return model
        except IntegrityError as exc:
            if "unique constraint" in str(exc.orig).lower():
                raise DuplicateEntry(self.model_type) from exc
            if "foreign key constraint" in str(exc.orig).lower():
                field: str = re.findall(r"key \((\w*)\)=", str(exc.orig).lower())[0]
                field = field.removesuffix("_id")
                raise NoResultFound(field) from exc
            raise

    def all(self) -> list[Model]:
        return db.session.query(self.model_type).all()

    def get(self, model_id: Any, /) -> Model | None:
        return db.session.get(self.model_type, model_id)

    def get_by(self, **fields: Any) -> Model | None:
        statement = db.session.query(self.model_type)
        for field in filter(lambda f: f in self.model_type.__mapper__.columns, fields):
            statement = statement.where(
                object.__getattribute__(self.model_type, field) == fields[field]
            )
        return statement.first()

    def delete(self, model_id: Any, /) -> Model:
        if not (model := self.get(model_id)):
            raise NoResultFound(self.model_type)
        db.session.delete(model)
        db.session.commit()
        return model

    def update(cls, model: Model) -> Model:
        db.session.commit()
        db.session.refresh(model)
        return model
