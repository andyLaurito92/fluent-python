from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int = 31
    city = 'Buenos Aires'


# Only attributes name & age become annotations
print(Person.__annotations__)

try: 
    print(Person.name)
except Exception as e:
    print("When the attribute is not defined in the class, Python returns an"
    " attribute error instead of returning None", e)

"""
Note how the above behavior is different from the one in the NamedTuple example,
where the attribute was returned as a descriptor.
"""

print(Person.age)

"""
From the dataclass annotation, the parameters that are passed are:
- frozen: Makes the class immutable. If you try to change an attribute, it will raise an exception.
- eq: If True, the class implements __eq__() method. Default is True.
- order: If True, the class implements __lt__(), __le__(), __gt__(), and __ge__() methods. Default is False.
- init: If True, the class implements a __init__() method that initializes the attributes. Default is True.
- repr: If True, the class implements a __repr__() method. Default is True.
- unsafe_hash: If True, the class implements a __hash__() method. Default is False.

Frozen and order are the more likely to be changed.
"""


"""
Hashing dataclasses

Note the difference between the following two classes:
"""

@dataclass
class UnhashableCity:
    name: str
    population: int
    country: str
    coordinate: tuple

@dataclass(frozen=True)
class City:
    name: str
    population: int
    country: str
    coordinate: tuple


buenosaires_hashable = City('Buenos Aires', 2891000, 'AR', (-34.61, -58.38))
buenosaires_unhashable = UnhashableCity('Buenos Aires', 2891000, 'AR', (-34.61, -58.38))

print(f"Hash of buenos aires: {hash(buenosaires_hashable)}")

try: 
    print(hash(buenosaires_unhashable))
except Exception as e:
    print("When trying to hash a dataclass which can be mutable (frozen = False), then an exception is thrown ", e)
