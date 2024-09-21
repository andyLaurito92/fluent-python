from typing import NamedTuple

Coordinates = NamedTuple('Coordinates', [('latitude', float), ('longitude', float)])

buenos_aires = Coordinates(-34.61, -58.38)

class CoordinatesWithDefault(NamedTuple):
    latitude: float
    longitude: float
    reference: str = 'WGS84'
   
example_coordinates = CoordinatesWithDefault(-34.61, -58.38)

print(example_coordinates)

bad_coordinate = CoordinatesWithDefault(-34.61, 'wrong')
print(bad_coordinate) 


"""
Important note: Type hints are not enforced by the Python bytecode compiler and interpreter at all. They are only hints that can be used by tools like mypy to check the code for type consistency. Check more about mypy here: https://mypy.readthedocs.io/en/stable/

Type hints have no impact on the runtime behavior of the code. They are not used to validate the types of the arguments passed to functions or the values assigned to variables.

Think type hints as "documentation that can be verified by IDEs and type checkers"
"""

from demoplainclass import DemoPlain

print(DemoPlain.__annotations__)
try:
    print(DemoPlain.a)
except Exception as e:
    print("Tried to execute DemoPlain.a and got an error: ", e)

print(f"Accesing class b attribute {DemoPlain.b}")
example = DemoPlain()
# This class attribute is accessible from the object
example.b


class DemoTyped(NamedTuple):
    a: int
    b: str
    c: float = 0.3


print(DemoTyped.__annotations__)

print("Returns a tuplegetter but no error is raised (even though there's"
      f" no value){DemoTyped.a}") # This returns a descriptor

# In case of a plain class, the attribute is not defined, while a class extending NamedTuple has the attribute defined
# In this case, a is a descriptor. A descriptor is an object attribute with "binding behavior", one whose attribute access has been overridden by methods in the descriptor protocol.
print(f"Getting attribute a from DemoTyped: {DemoTyped.a}")

try: 
    print("When trying to instantiate a NamedTuple with a missing attribute, it throws an error")
    typeinstance = DemoTyped()
except Exception as e:
    print("Error when trying to instantiate a NamedTuple with a missing attribute: ", e)

typeinstance = DemoTyped(1, 'hey')
print(f"Correctly instantiation of NumedTuple: {typeinstance}")

try:
    print("When trying to set a value to a NamedTuple attribute, it throws an error")
    typeinstance.a = 2
except Exception as e:
    print("Error when trying to set a value to a NamedTuple attribute: ", e)
