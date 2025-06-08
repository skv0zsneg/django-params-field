class ParamsFieldException(BaseException):
    """Base `ParamsField` exception."""


class SchemeValidationError(ParamsFieldException):
    """Exception on wrong scheme of ``ParamsField``."""
