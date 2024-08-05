"""
This class implements a multidimensional vector. In chapter 11 we implemented a 2D vector,
and the idea here is to be backwards compatible with that class
"""

import array
import math
import reprlib
from typing import Iterable, NoReturn

class Vector:
    __match_args__ = ('x', 'y', 'z', 't')
    typecode = 'd'
    
    def __init__(self, elements: Iterable) -> NoReturn:
        """ Expects an iterable of _elements that represent this N-dimensional vector"""
        self._elements = array.array(self.typecode, elements)

    def __len__(self) -> int:
        """ Returns the len of this vector """
        return len(self._elements)

    def __getitem__(self, index):
        match index:
            case int():
                return self._elements[index]
            case slice():
                # Instead of hardcoding Vector class, we get dynamically
                # the class of self in case this class is later extended
                clss = type(self)
                return clss(self._elements[index])
            case _:
                # Example on when this would be triggered: Recieveing a float
                raise Exception(f"__getitem__ recieved {index} which is not expected")

    def __iter__(self) -> Iterable:
        return iter(self._elements)

    def __getattribute__(self, attribute):
        cls = type(self)
        try:
            idx = cls.__match_args__.index(attribute)
        except ValueError:
            idx = -1

        if 0 <= idx < len(__match_args__):
            return self._elements[idx]

        msg = f"{cls.__name__!r} object has not attribute {attribute!r}"
        raise AttributeError(msg)
        

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
