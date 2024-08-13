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
"""
