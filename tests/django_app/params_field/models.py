from django.db import models

from django_params_field import ParamsField

DICT_SCHEMA = {
    "param_int": int,
    "param_float": float,
    "param_str": str,
    "param_list": list,
    "param_tuple": tuple,
    "param_set": set,
    "param_dict": dict,
}


class ModelForTest(models.Model):
    """Simple model using for test ParamsField."""

    default = ParamsField()
    with_dict_schema = ParamsField(schema=DICT_SCHEMA)
