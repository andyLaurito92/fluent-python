"""
Common example of descriptors: Managing public attributes:

Instead of using properties?
"""

import logging

logging.basicConfig(level=logging.INFO)

class loggedAttribute:
    def __set_name__(self, owner, name):
        """ Util function which receives the name of the variable to which this
        descriptor is assigned
        """
        self.public_name = name
        self.private_name = '_' + name

    def __set__(self, obj, value):
        logging.info(f"Setting attribute {self.public_name} val {value}")
        setattr(obj, self.private_name , value)

    def __get__(self, obj, objtype=None):
        logging.info(f"Getting attribute {self.public_name}")
        return getattr(obj, self.private_name)


class Person:
    age = loggedAttribute()
    name = loggedAttribute()

    def __init__(self, name, age):
        self.age = age
        self.name = name


andy = Person("Andres", 32)

print(andy.age)

andy.age -= 1 # I want to become younger :)

# private attributes are defined in the instance
print(vars(andy))

# Given that a descriptor is a class, we can ask for
# it's variables! -> Remember that attributes are defined
# in the class
print(vars(vars(Person)['age']))
