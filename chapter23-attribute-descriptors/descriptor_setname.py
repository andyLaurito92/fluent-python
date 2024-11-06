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


# Note that is not the same invoking the descriptor
print(andy.age)
# than getting the descriptor instance
print(vars(Person)['age'])
# In the second call, we get the descriptor instance which is never called

"""
Descriptors only work when used as class variables. When put in instances, they have no effect.

The main motivation for descriptors is to provide a hook allowing objects stored in class variables to control what happens during attribute lookup.

Common tools like classmethod(), staticmethod(), property(), and functools.cached_property() are all implemented as descriptors.
"""
