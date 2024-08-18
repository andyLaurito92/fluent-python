from fractions import Fraction
"""
Without types
"""

def double(x):
    return x * 2

print(double('A'))
print(double(1.5))
print(double([1, 2, 3]))
print(double(Fraction(1, 3)))

"""
Initial implementation of type hints in Python was a nominal type system

It's impossible to name all types that implement a protocol by supporting the required methods, therefore duck typing could not be described by type hints

Now it's possible thx to typing.Protocol
"""

from typing import Protocol, TypeVar

T = TypeVar('T')

class Repetable(Protocol):
    # We typed self just to make sure that the return type is the same than the class
    def __mul__(self: T, n: int) -> T: ...

RT = TypeVar('RT', bound=Repetable)

def double_typed(x: RT) -> RT:
    return x * 2


"""
The above is a good example on why Protocol is considered structural subtyping as it was introduced in PEP 544: https://peps.python.org/pep-0544/

In order to make a protocol support isinstance/issubclass checks at runtime, we can use @runtime_checkable decorator. This works because typing.Protocol is an ABC, therefore it supports the _subclasshook__ method
"""

try:
    issubclass(list, Repetable)
except TypeError as e:
    """ Instance and class checks can only be used with @runtime_checkable protocols """
    print(e)

from typing import runtime_checkable

@runtime_checkable
class RepetableV2(Protocol):
    def __mul__(self, n: int) -> T: ...


"""
Here, the issubclass semantic is more a "consistent with" than a "is-a" relationship
"""
issubclass(list, RepetableV2)


"""
The typing module includes 7 ready to use protocols, see https://docs.python.org/3/library/typing.html#protocols
"""


import numpy as np
from typing import SupportsComplex

c = np.complex64(3+4j)

issubclass(type(c), complex)

isinstance(c, SupportsComplex)

"""
Because we know that c supports complex, we can call complex over the instance
"""
acomplex = complex(c)


"""
Better way to check if instance supports convertion to complex:
"""

isinstance(c, (complex, SupportsComplex))


"""
An alternative to use structural typing would be to use nominal typing, this is, check if the instance is subclass of the complex built in type defined in numbers

Note: The numpy complex type is registered as a virtual subclass of complex
"""

import numbers

isinstance(c, numbers.Complex)
