# django-params-field

> ⚠️ This project under active developing.

### Roadmap for `0.1.0` and set to public:

**Features**

Base
- [ ] `ParamsField.set` is working.
- [ ] `ParamsField.get` is working.
- [ ] `ParamsField.get(SomeDataclass.some_field)` is working.
- [ ] `ParamsField.update(SomeDataclass.some_field, "some_new_field")` is working.
- [ ] Testing for all base features.

Additional
- [ ] `ParamsField` work with nested `dataclasses`.
- [ ] Migrations on changing `SomeDataclass` passed to `ParamsField` (?).
- [ ] Package work for python version's 3.x -> 3.y and Django 4.x -> 5.x

Project
- [ ] Linting ALL code base.
- [ ] Test coverage.
- [ ] Dep bot for updating deps(?).
- [ ] GitHub actions for testing and linting for all Python and Django version combinations.

## 📍 Purpose

This package is Django extension for storing a lot of parameters in one model field.

For example you have some business logic for storing information about cars and also all car configuration (like engine volume, compression ratio, fuel tank capacity, wheelbase and another N values). You don't need to work with all this data but need to store it.

`django-params-field` allows to put all this data in `ParamsField` and work with it like a charm ✨

## 🚀 Quick start

1. Install `django-params-field`.
```
pip install django-params-field
```

2. In your Django model implement data structure for your params with `dataclasses`.

```python
# car/configuration.py

from dataclasses import dataclass

@dataclass
class CarConfiguration:
    engine_volume: float | None = None
    fuel_tank_capacity: float | None = None
    wheelbase: float | None = None
    # another N configuration params
```

3. Add `ParamField` to your model and pass `dataclass` params to it.

```python
# car/models.py

from django.db.models import Model, CharField, DateTimeField
from django_params_field import ParamsField
from car.configuration import CarConfiguration

class Car(Model):
    # main fields
    make = CharField()
    model = CharField()
    year = DateTimeField()
    # params field
    configuration = ParamsField(CarConfiguration)
```

4. Work with it!

```python
car = Car.objects.get(pk=1)

# set
car_configuration = CarConfiguration(engine_volume=1.6)
car.configuration.set(car_configuration)
car.save()

# update part
car.configuration.update(CarConfiguration.engine_volume, 1.6)
car.save()

# get all
car_configuration = car.configuration.get()
assert isinstance(car_configuration, CarConfiguration)

# get part
assert car.configuration.get(CarConfiguration.engine_volume) == 1.6
```

## 🤔 Why not `JSONField`?

`ParamsField` solve problems like:
* Changing and getting part of DTO objects
* Match Python types
* Serialize and deserialize DTO objects "under the hood"
* Efficient storing data in DB

And some other things that `JSONField` does't provide.

Also, as it clear from the name, `JSONField` is only `JSON`-like data, but using Python buitin `dataclasses` give you free to manipulate DTO like you what it.