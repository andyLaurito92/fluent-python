import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)

class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = '_' + name
        
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        raise NotImplementedError

class Quantity(Validator):
    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value should be a number")
        elif value < 0:
            raise ValueError("Value cannot be less than 0")

class NotEmptyString(Validator):
    def validate(self, value):
        if len(value) == 0:
            raise ValueError("Empty strings are not allowed")

class LineItem:
    description = NotEmptyString()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


try:
    wrong_item = LineItem('Testing descriptors', 30, -3)
except ValueError as e:
    logging.info("Error raised " + str(e))


try:
    empty_string = LineItem('', 30, 20)
except ValueError as e:
    logging.info("Error raised " + str(e))

bananas = LineItem("bananas", 3, 8)

print(bananas.price)
print(bananas.weight)
