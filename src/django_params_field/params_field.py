from typing import Any

from django.db.models.fields import BinaryField
from django.utils.translation import gettext_lazy as _

from django_params_field.serializer import Serializer


class ParamsField(BinaryField):
    description = _("Storing a set of params in one field.")

    def __init__(self, params_type: Any | None = None, *args, **kwargs):
        self.params_type = params_type
        self.serializer = Serializer(self.params_type)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["params_type"] = self.params_type
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection) -> dict:
        return self.serializer.deserialize(value)

    def to_python(self, value) -> dict:
        return self.serializer.deserialize(value)

    def get_db_prep_value(self, value, connection, prepared) -> bytes:
        return self.serializer.serialize(value)
