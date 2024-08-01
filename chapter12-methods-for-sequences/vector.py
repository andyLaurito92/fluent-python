"""
This class implements a multidimensional vector. In chapter 11 we implemented a 2D vector,
and the idea here is to be backwards compatible with that class
"""

import array
import math
import reprlib

class Vector:
    typecode = 'd'

    def __init__(self, elements):
        """ Expects an iterable of _elements that represent this N-dimensional vector"""
        self._elements = array.array(self.typecode, elements)

    def __len__(self):
        """ Returns the len of this vector """
        return len(self._elements)

    def __iter__(self):
        return iter(self._elements)

    def __eq__(self, other):
        match other:
            case bool():
                return bool(self) == other
            case _:
                return tuple(self) == tuple(other)

    def __repr__(self):
        str_repr = reprlib.repr(self._elements)
        str_repr = str_repr[str_repr.find('['):-1]
        return f'Vector({str_repr})'

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._elements))

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def fromBytes(clss, octets):
       typecode = chr(octets[0])
       memv = memoryview(octets[1:]).cast(typecode)
       return cls(memv)
