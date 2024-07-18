import math
from typing import Iterable

class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        """ Returns programmer representation of vector 2d """
        class_name = type(self).__name__
        return f"{class_name}({self.x}, {self.y})"

    def __str__(self) -> str:
        """ Returns user representatino of a vector 2d """
        return str(tuple(self))

    def __iter__(self) -> Iterable:
        return (i for i in (self.x, self.y))

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        # Truthy nomenclature in python
        return bool(abs(self))

    def __eq__(self, other) -> bool:
        match other:
            case bool():
                return bool(self) == other
            case Vector2D():
                return tuple(self) == tuple(other)
            case _:
                return False
