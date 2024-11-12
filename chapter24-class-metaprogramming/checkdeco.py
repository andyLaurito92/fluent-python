from typing import get_type_hints
import logging
"""
In this code snippet I implement a class decorator that
type checks attributes in the decorated class.

The real class to use for application code is dataclass,
you can find the cpython implementation here:
https://github.com/python/cpython/blob/3.9/Lib/dataclasses.py
"""

logging.basicConfig(level=logging.INFO)

class TypedField:
    def __init__(self, name, constructor):
        self.name = name
        self.constructor = constructor

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        else:
            if obj.__dict__.get(self.name) is None:
                setattr(obj, self.name, ...)
            return obj.__dict__[self.name]

    def __set__(self, instance, value):
        if value is ...:
            value = self.constructor()
        elif not isinstance(value, self.constructor):
            raise ValueError(f"{value} is not of type {self.constructor.__name__!r}")
        value = self.constructor(value)
        instance.__dict__[self.name] = value

def checked(theclass: type) -> type: # classes are instances of type
    fields = get_type_hints(theclass)

    for field, typeclss in fields.items():
        typedfield = TypedField(field, typeclss)
        setattr(theclass, field, typedfield)

    old_init = theclass.__init__
    def init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)

        for key,val in kwargs.items():
            if not key in fields.keys():
                logging.info(f'Key {key} is not a typed attribute. Will set it up as normal attribute')
            setattr(self, key, val)


    def repr(self):
        attrs = ', '.join(f'{field}={getattr(self, field)}({val.__name__})' for field, val in fields.items())
        return f'{theclass.__name__}({attrs})'

    theclass.__init__ = init
    theclass.__repr__ = repr
            
    return theclass


@checked
class Student:
    name: str
    age: int
    studentid: str
    university: str

    def __init__(self, *args, **kwargs):
        print("hello")

andy = Student(name="Andy", age=32,
               studentid='xdd', university_typo="Opps!")

andy.name = "Andy"
try:
    andy.name = 3.2
except ValueError as e:
    print(e)
