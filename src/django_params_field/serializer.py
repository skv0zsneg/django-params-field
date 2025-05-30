import bz2
import pickle
from typing import Any


class Serializer:
    """Params serializer & deserializer."""

    def __init__(self, params_type: Any | None = None) -> None:
        self.params_type = params_type

    def serialize(self, value: Any) -> bytes:
        serialized = pickle.dumps(value)
        compressed = bz2.compress(serialized)
        return compressed

    def deserialize(self, value: bytes) -> Any:
        decompressed = bz2.decompress(value)
        deserialized = pickle.loads(decompressed)
        return deserialized
