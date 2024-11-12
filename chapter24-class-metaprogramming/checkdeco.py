from typing import get_type_hints
"""
TODO: Implement a class decorators that acts as
class define din checkdeco.py
"""

class TypedField:
    def __init__(self, name, constructor):
        self.name = name
        self.constructor = constructor

    def __set__(self, instance, value):
        if value is ...:
            value = self.constructor()
        elif not isinstance(value, self.constructor):
            raise ValueError(f"{value} is not of type {self.constructor.__name__!r}")
        value = self.constructor(value)
        instance.__dict__[self.name] = value

def checked(theclass):
    fields = get_type_hints(theclass)

    for field, typeclss in fields.items():
        typedfield = TypedField(field, typeclss)
        setattr(theclass, field, typedfield)
            
    return theclass


@checked
class Student:
    name: str
    age: int
    studentid: str

andy = Student()

andy.name = "Andy"
try:
    andy.name = 3.2
except ValueError as e:
    print(e)
