from typing import ClassVar, Generic, Optional, TypeVar

from django_params_field.exceptions import ParamsFieldException, SchemeValidationError

S = TypeVar("S")


class SchemaValidator(Generic[S]):
    """``ParamsField`` scheme validation."""

    ALLOWED_SCHEME_TYPE: ClassVar[tuple[type, ...]] = (dict,)
    ALLOWED_SCHEME_VALUE_TYPES: ClassVar[tuple[type, ...]] = (
        int,
        float,
        str,
        list,
        tuple,
        set,
        dict,
    )

    def __init__(self, schema: Optional[S]) -> None:
        schema_type = type(schema)
        if schema_type not in self.ALLOWED_SCHEME_TYPE:
            raise ParamsFieldException(f"Unknown scheme type {type(schema)}.")
        scheme_validator = getattr(self, "validate_" + schema_type.__name__ + "_scheme", None)
        if scheme_validator is None:
            raise ParamsFieldException(f"There is no validator for '{schema_type}' scheme type.")

        scheme_validator(schema)
        self.scheme = schema

    def validate_dict_scheme(self, scheme: dict) -> None:
        scheme_key_types = (type(value) for value in scheme.keys())
        if not all(isinstance(key, str) for key in scheme_key_types):
            raise SchemeValidationError("For ``dict`` scheme only ``str`` keys are available.")

        scheme_value_types = (type(value) for value in scheme.values())
        if not all(type(value) in self.ALLOWED_SCHEME_VALUE_TYPES for value in scheme_value_types):
            formatted_allowed_scheme_value_types = ", ".join(
                str(type_) for type_ in self.ALLOWED_SCHEME_VALUE_TYPES
            )
            raise SchemeValidationError(
                f"For ``dict`` scheme only {formatted_allowed_scheme_value_types}"
            )
