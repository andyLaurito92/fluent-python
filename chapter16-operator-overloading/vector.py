"""
This class implements a multidimensional vector. In chapter 11 we implemented a 2D vector,
and in chapter 12 we extended the class. Now we will overload operators so we can use our
vector with mathematical operators
"""

import array
import math
import reprlib
from typing import Iterable, NoReturn
from functools import reduce
from operator import xor

class Vector:
    typecode = 'd'
    __match_args__ = ('x', 'y', 'z', 't')
    
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

    def __getattr__(self, attribute):
        cls = type(self)
        try:
            idx = cls.__match_args__.index(attribute)
        except ValueError:
            idx = -1

        if 0 <= idx < len(self._elements):
            return self._elements[idx]
        msg = f"{cls.__name__!r} object has not attribute {attribute!r}"
        raise AttributeError(msg)

    def __setattr__(self, name, val):
        cls = type(self)
        if len(name) == 1:
            if name in cls.__match_args__:
                error = 'Trying to set readonly attribute {attr_name}'
            elif name.islower():
                error = "Can't set attributes a to z in {cls_name!r}"
            else:
                # We allow to set this attribute
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
        super().__setattr__(name, val)
        
    def __hash__(self):
        hashes = (hash(x) for x in self._elements)
        return reduce(xor, hashes, 0)
        
    def __eq__(self, other) -> bool:
        match other:
            case bool():
                return bool(self) == other
            case _:
                if len(self) != len(other):
                    return False
                # In this way me make the equality function to work
                # more efficiently. Instead of copying all elements
                # in a tuple as we did before, we compare elements
                # 1 by 1
                for a, b in zip(self, other):
                    if a != b:
                        return False
                return True

        #Another way of implementing this would be:
        # len(a) == len(b) && all(a == b for a, b in zip(self._elements, other))
        
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

    """
    Chapter 16 methods
    """

    def __neg__(self) -> 'Vector':
        return Vector(-x for x in self)

    def __pos__(self) -> 'Vector':
        return Vector(self)

    @classmethod
    def fromBytes(cls, octets) -> 'Vector':
       typecode = chr(octets[0])
       memv = memoryview(octets[1:]).cast(typecode)
       return cls(memv)
