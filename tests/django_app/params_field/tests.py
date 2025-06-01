import pytest
from django.core.exceptions import ValidationError

from .models import ModelForTest


@pytest.mark.django_db
def test_model_full_clean_with_correct_value():
    """Test model `clean()` params_field_default."""
    test_model = ModelForTest.objects.create(params_field_default={"just": "test"})
    # check that no exception raised
    assert test_model.full_clean() is None


@pytest.mark.django_db
def test_model_full_clean_with_bas_value():
    """Test model `clean()` params_field_default."""
    test_model = ModelForTest.objects.create(params_field_default="I'm Not Valid!")
    with pytest.raises(ValidationError):
        test_model.full_clean()


@pytest.mark.django_db
@pytest.mark.parametrize("dict_size", [1000, 10_000, 100_000, 1_000_000])
def test_set_and_get_params_field_default(dict_size):
    """Test set and get params fields different size with default ``params_type``."""
    test_model = ModelForTest.objects.create()
    simple_data_struct = {i: i for i in range(dict_size)}
    test_model.params_field_default = simple_data_struct
    test_model.save()

    test_model_from_query = ModelForTest.objects.get(pk=test_model.pk)
    assert test_model_from_query.params_field_default == simple_data_struct


@pytest.mark.django_db
@pytest.mark.parametrize("dict_size", [1000, 10_000, 100_000, 1_000_000])
def test_update_params_field_default(dict_size):
    """Test update params fields different size with default ``params_type``."""
    simple_data_struct = {i: i for i in range(dict_size)}
    test_model = ModelForTest.objects.create(params_field_default=simple_data_struct)

    test_model.params_field_default[0] = "test-change-value"
    test_model.save()
    test_model_from_query = ModelForTest.objects.get(pk=test_model.pk)
    assert test_model_from_query.params_field_default[0] == "test-change-value"


@pytest.mark.django_db
@pytest.mark.parametrize("dict_size", [1000, 10_000, 100_000, 1_000_000])
def test_delete_params_field_default(dict_size):
    """Test delete params fields different size with default ``params_type``."""
    simple_data_struct = {i: i for i in range(dict_size)}
    test_model = ModelForTest.objects.create(params_field_default=simple_data_struct)

    keys_num_before = len(test_model.params_field_default.keys())
    del test_model.params_field_default[1]
    test_model.save()
    test_model_from_query = ModelForTest.objects.get(pk=test_model.pk)
    assert len(test_model_from_query.params_field_default.keys()) == keys_num_before - 1
