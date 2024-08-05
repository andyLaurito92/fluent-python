"""
This class implements a multidimensional vector. In chapter 11 we implemented a 2D vector,
and the idea here is to be backwards compatible with that class
"""

import array
import math
import reprlib
from typing import Iterable, NoReturn

class Vector:
    typecode = 'd'

    def __init__(self, elements: Iterable) -> NoReturn:
        """ Expects an iterable of _elements that represent this N-dimensional vector"""
        self._elements = array.array(self.typecode, elements)

    def __len__(self) -> int:
        """ Returns the len of this vector """
        return len(self._elements)

    def __iter__(self) -> Iterable:
        return iter(self._elements)

    def __eq__(self, other) -> bool:
        match other:
            case bool():
                return bool(self) == other
            case _:
                return tuple(self) == tuple(other)

    def __repr__(self) -> str:
        str_repr = reprlib.repr(self._elements)
        str_repr = str_repr[str_repr.find('['):-1]
        return f'Vector({str_repr})'

    def __bytes__(self) -> bytes:
        return (bytes([ord(self.typecode)]) +
                bytes(self._elements))

    def __abs__(self) -> float:
        return math.hypot(*self)

    def __bool__(self) -> bool:
        return bool(abs(self))

    @classmethod
    def fromBytes(clss, octets) -> 'Vector':
       typecode = chr(octets[0])
       memv = memoryview(octets[1:]).cast(typecode)
       return cls(memv)
