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
