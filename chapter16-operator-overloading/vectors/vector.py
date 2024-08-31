"""
This class implements a multidimensional vector. In chapter 11 we implemented a 2D vector,
and in chapter 12 we extended the class. Now we will overload operators so we can use our
vector with mathematical operators
"""

import array
import math
import reprlib
import itertools
from typing import Iterable, NoReturn, Iterator
from functools import reduce
from operator import xor

class Vector:
    typecode = 'd'
    __match_args__ = ('x', 'y', 'z', 't')
    
    def __init__(self, elements: Iterable = None, *args) -> None:
        values = elements
        if not isinstance(elements, Iterable):
            if len(args) > 0:
                values = [elements] + list(args)
            else:
                raise ValueError("Expected either iterable or list of elements to initialize vector. None given")
        self._elements = array.array(self.typecode, values)

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

    def __iter__(self) -> Iterator:
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

    def __radd__(self, other) -> 'Vector':
        """
        Reverse add allows to perform operation other + vector when
        other doesn't support method __add__

        Given an expression a + b, the interpreter will perform these steps:
        1. if a has __add__, call a.__add__(b) and return result unless it's NotImplemented
        2. if a doesn't have __add__, or calling it returns NotImplemented, check if b has
        __radd__, then call b.__radd__(a) and return result unless it's NotImplemented
        3. if b doesn't have __radd__, or calling it returns NotImplemented, raise TypeError
        with an unsupported operand types message
        """
        return self + other

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        This method could be typed with other as an Iterable. This would allow a vector
        to be added to whatever iterable that can be added to the elements stored in the vector.
        This is an excellent example where we could apply duck typing an allow this vector class
        to support being container of whatever element that supports a set of operators (even though,
        we could define a generic type and specify what we expect from an element)
        Given that my intention is to represent a mathematical vector, we will enforce other to be a
        vector instance
        """
        pairs = itertools.zip_longest(self, other, fillvalue=0)
        return Vector(a + b for a, b in pairs)

    def __mul__(self, other) -> 'Vector':
        """ Implements scalar multiplication in vector"""
        return Vector(x * other for x in self)

    def __rmul__(self, other) -> 'Vector':
        return self * other

    @classmethod
    def fromBytes(cls, octets) -> 'Vector':
       typecode = chr(octets[0])
       memv = memoryview(octets[1:]).cast(typecode)
       return cls(memv)
