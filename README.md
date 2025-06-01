# django-params-field

> ⚠️ This project under developing.

Django extension for storing a lot of parameters in one model field.

## 📍 Purpose

For example you have some business logic for storing information about cars and also all car configuration (like engine volume, compression ratio, fuel tank capacity, wheelbase and another N values). You don't need to work with all this data but need to store it.

`django-params-field` allows to put all this data in `ParamsField` and work with it like a charm ✨

## 🚀 Quick start

1. Install `django-params-field`.

> ⚠️ Will not work until 0.1.0 version will be realized.

```
pip install django-params-field
```

3. Add `ParamField` to your model.

```python
from django.db.models import Model, CharField, DateTimeField
from django_params_field import ParamsField

class Car(Model):
    # main fields
    make = CharField()
    model = CharField()
    year = DateTimeField()
    # params field
    configuration = ParamsField()
```

4. Work with it!

```python
car = Car.objects.get(pk=1)

# set
car.configuration = {"engine_volume": 1.6}
# get
assert car.configuration == {"engine_volume": 1.6}
# update
car.configuration["engine_volume"] = 1.8
car.configuration["doors"] = 3
# delete
del car.configuration["doors"]
```

## 🤗 Author

Made with love by @skv0zsneg