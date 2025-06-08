import bz2
import pickle
from typing import Any, ClassVar, Generic, Optional, TypeVar

from django_params_field.schema_validator import S, SchemaValidator

V = TypeVar("V")


class Serializer(Generic[V]):
    """Params serializer & deserializer."""

    ALLOWED_VALUE_TYPES: ClassVar[tuple[Any, ...]] = (dict,)

    def __init__(self, schema: Optional[S] = None) -> None:
        self.schema = SchemaValidator(schema)

    def serialize(self, value: V) -> bytes:
        serialized = pickle.dumps(value)
        compressed = bz2.compress(serialized)
        return compressed

    def deserialize(self, value: bytes) -> V:
        decompressed = bz2.decompress(value)
        deserialized = pickle.loads(decompressed)
        return deserialized

    def is_valid(self, value: V) -> bool:
        return any(
            map(
                lambda allowed_type: isinstance(value, allowed_type), self.ALLOWED_VALUE_TYPES
            )
        )
