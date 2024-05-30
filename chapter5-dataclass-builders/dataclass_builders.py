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



"""
Let's now use the dataclass decorator to create a class with the same attributes as the NamedTuple above.
"""

from dataclasses import dataclass

"""
The frozen parameter makes the class immutable. If you try to change an attribute, it will raise an exception.
"""
@dataclass(frozen=True)
class DataCoordinate:
    latitude: float
    longitude: float

    def __str__(self):
        ns = 'NS'[self.latitude < 0]
        ew = 'EW'[self.longitude < 0]
        return f"{abs(self.latitude):.1f}°{ns}, {abs(self.longitude):.1f}°{ew}"

berlin = DataCoordinate(52.52, 13.40)
print(berlin)  # 52.5°N, 13.4°E

print(berlin == DataCoordinate(52.52, 13.40))  # True

# Dataclass extends from object while typing.NamedTuple issubclass of tuple
print(issubclass(AnotherCoordinate, tuple))  # True
print(issubclass(DataCoordinate, tuple))  # False


try: 
    berlin.latitude = 52.53  # AttributeError: can't set attribute
except Exception as e:
    print("Error when trying to assign latitude to berlin: ", e)

# Get type hints of a class
print(typing.get_type_hints(DataCoordinate))  # {'latitude': <class 'float'>, '

"""
We can get dictionaries from the data classes built above
"""

import dataclasses
dataclasses.asdict(berlin)  # {'latitude': 52.52, 'longitude': 13.4}

buenos_aires_dict = buenos_aires._asdict()  # {'latitude': -34.61, 'longitude': -58.38}


"""
Get field names & default values
"""
dataclasses.fields(DataCoordinate)


"""
You can create a new instance with some values changed from an existing one. This probably makes sense when the dataclass has many attributes and you're just interested in updating some of them.
"""

new_berlin = dataclasses.replace(berlin, latitude=43.53)  # DataCoordinate(latitude=52.53, longitude=13.4)

print(new_berlin == berlin)  # False


"""
Because namedtuple & typing.NamedTuple are subclass of tuple, you can use them as keys in a dictionary.
"""

print(f"Latitude: {buenos_aires[0]}")
