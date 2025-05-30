from django.db import models

from django_params_field import ParamsField


class ModelForTest(models.Model):
    """Simple model using for test ParamsField."""

    params_field_default = ParamsField()
