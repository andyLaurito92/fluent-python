from math import sqrt
from typing import Iterable

class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """ Returns programmer representation of vector 2d """
        return f"Vector2D({self.x}, {self.y})"

    def __str__(self) -> str:
        """ Returns user representatino of a vector 2d """
        return f"({self.x}, {self.y})"

    def __iter__(self) -> Iterable:
        return (i for i in (self.x, self.y))

    def __abs__(self) -> float:
        return sqrt(self.x ** 2 + self.y **2)
