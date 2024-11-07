import logging
from abc import abstractmethod, ABC

logging.basicConfig(level=logging.INFO)

class Validator(ABC):
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        logging.info(f"Getting value of {self.public_name}")
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class OneOf(Validator):
    def __init__(self, *options):
        self.options = options
        
    def validate(self, value):
        if value not in self.options:
            raise AttributeError(f"Value {value} is not one of the expected values")

class Number(Validator):
    def __init__(self, minval, maxval):
        self.minvalue = minval
        self.maxvalue = maxval

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Expected {value!r} to be at least {self.minvalue!r}')
        if value < self.minvalue:
            raise ValueError(f'{value} cannot be less than {self.minvalue}')
        elif value > self.maxvalue:
            raise ValueError(f'{value} cannot be greater than {self.maxvalue}')
        

class Person:
    age = Number(1, 99)
    name = OneOf('Andy', 'Luca', 'Gaby', 'Justin')

    def __init__(self, age, member):
        self.age = age
        self.member = member


matusalen = Person(30, 'Andy')

try: 
    invalid_person = Person(101, 'Justin')
except ValueError as e:
    print(e)
