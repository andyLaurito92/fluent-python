"""
Studying generics in python, which is better explain in the typing module
documentation here: https://docs.python.org/3/library/typing.html#user-defined-generic-types
"""

from typing import TypeVar, NoReturn, Generic

T = TypeVar('T')

"""
According to the documentation, each type variable to generic must be distinct
(meaning we don't define Point[T, T], we just say Point[T]
"""
class Point(Generic[T]):
    def __init__(self, first:T, second:T) -> None:
        self.first = first
        self.second = second

    def x(self) -> T:
        return self.first

    def y(self) -> T:
        return self.second


"""
For defining a type for our point, we use nomeclature Point[mytype](value1, value2)
"""

point1 = Point[int](3, 4)

"""
Spotted as an error by mypy
Of course type hints are for static checkers, therefore this is not an
error in runtime
"""
mypoint = Point[int]("hey", 3)
