class Coordinates:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

buenos_aires = Coordinates(-34.61, -58.38)
print(buenos_aires.latitude)  # -34.61

location_buenosaires = Coordinates(latitude=-34.61, longitude=-58.38)

"""
First problem w/above class: It doesn't have a __eq__ method, so the comparison will be done by memory address, not by the values of the attributes.
Second problem: The __init__ method is too verbose. We can use dataclasses to make it more concise.
Third problem: The __repr__ method is not implemented, so the print function will return the memory address of the object.
"""
print(buenos_aires == location_buenosaires)  # False
print(buenos_aires)  # <__main__.Coordinates object at 0x7f8b1c7b3d30>


"""
First data class we are gonna see: namedtuple
"""

from collections import namedtuple

Coordinates = namedtuple('Coordinates', ['latitude', 'longitude'])
isinstance(Coordinates, tuple)  # True

buenos_aires = Coordinates(-34.61, -58.38)
location_buenosaires = Coordinates(latitude=-34.61, longitude=-58.38)

# Equality is now based on the values of the attributes
print(buenos_aires == location_buenosaires)  # True
print(buenos_aires.latitude)  # -34.61


"""
We can build the same than above using NamedTuple. NamedTuple is a factory function that creates a new class with the given name and attributes. You can specify types for the attributes, and it will return a class that inherits from tuple.
"""

import typing

TypedCoordinate = typing.NamedTuple('TypedCoordinate', [('latitude', float), ('longitude', float)])

buenos_aires_typed = TypedCoordinate(-34.61, -58.38)
print(buenos_aires_typed)

print(f"Type hints: {typing.get_type_hints(TypedCoordinate)}")

bad_example = TypedCoordinate(-34.61, 'wrong')
print(bad_example)  # TypedCoordinate(latitude=-34.61, longitude='wrong')

# We can provide keyword arguments to the constructor
sao_pablo = TypedCoordinate(latitude=-23.55,longitude=-46.63)
sao_pablo == buenos_aires_typed  # False


"""
Let's use NamedTuple to define a new class. Valid for Python 3.6+
"""

class AnotherCoordinate(typing.NamedTuple):
    latitude: float
    longitude: float

    def __str__(self):
        ns = 'NS'[self.latitude < 0]
        ew = 'EW'[self.longitude < 0]
        return f"{abs(self.latitude):.1f}°{ns}, {abs(self.longitude):.1f}°{ew}"
        

paris = AnotherCoordinate(48.85, 2.35)
print(paris)  # 48.9°N, 2.4°E
print(paris.latitude)  # 48.85

"""
Note: AnotherCoordinate is not a subclass of NamedTuple.
"""

try:
    print(issubclass(AnotherCoordinate, typing.NamedTuple))
except Exception as e:
    print("issubclass throwed the following error: ", e)

