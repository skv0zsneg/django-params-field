from typing import Any, Generic, Optional

from django.core.exceptions import ValidationError
from django.db.models.fields import BinaryField

from django_params_field.serializer import V, Serializer


class ParamsField(BinaryField, Generic[V]):
    """Storing a set of params in one field."""

    def __init__(self, schema: Optional[V] = None, *args, **kwargs) -> None:
        self.schema = schema
        self.serializer = Serializer(self.schema)
        super().__init__(*args, **kwargs)

    def deconstruct(self) -> tuple[Any, Any, Any, Any]:
        name, path, args, kwargs = super().deconstruct()
        kwargs["schema"] = self.schema
        return name, path, args, kwargs

    def from_db_value(self, value: bytes, *args, **kwargs) -> V:
        return self.serializer.deserialize(value)

    def to_python(self, value: V) -> V:
        return value

    def get_db_prep_value(self, value: V, *args, **kwargs) -> bytes:
        return self.serializer.serialize(value)

    def validate(self, value: V, *args, **kwargs) -> None:
        if not self.serializer.is_valid(value):
            raise ValidationError(f"Given value '{value}' is not valid!")
