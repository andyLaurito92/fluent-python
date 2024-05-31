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
