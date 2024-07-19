import math
from array import array
from typing import Iterable

class Vector2D:
    typecode = 'd'

    @classmethod
    def frombytes(cls, octets: bytes) -> 'Vector2D':
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def angle(self) -> float:
        return math.atan2(self.x, self.y)

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

    def __bytes__(self) -> bytes:
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __format__(self, fmt_spec: str = '') -> str:
        """ If p is provided in the fmt_spec, we return polar coordinates """
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coordinates = (abs(self), self.angle())
            outer_fmt = "<{}, {}>"
        else:
            coordinates = self
            outer_fmt = "({}, {})"
        components = (format(c, fmt_spec) for c in coordinates)
        return outer_fmt.format(*components)

    def __eq__(self, other) -> bool:
        match other:
            case bool():
                return bool(self) == other
            case Vector2D():
                return tuple(self) == tuple(other)
            case _:
                return False
