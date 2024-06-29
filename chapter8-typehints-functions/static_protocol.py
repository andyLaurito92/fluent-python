"""
Static protocols in Python are similar to those ones in Go. In the context of Python, they are used to define the expected behavior of a class (interface that a type checker can verify)

Protocol definition is written as a typiong.Protocol subclass, however tclasses
that implement a protocol don't need to inherit from it. It's up to the type checker
to find the available protocol types and enforce their usage.
"""

"""
Problem statement: We want to return the top n largest element of an iterable

Let's try a first solution
"""

from typing import Iterable, TypeVar, Protocol

T = TypeVar('T')

def top_n1(data: Iterable[T], n: int) -> list[T]:
    result = sorted(data, reverse=True)
    return result[:n]

"""
The problem with the above code is that it doesn't work for all T types.
The sorted function requires that the elements of the iterable are comparable,
so we need to define a protocol that enforces this behavior
"""

class SupportsLessThan(Protocol):
    def __lt__(self, other: object) -> bool: ...

T2 = TypeVar('T', bound=SupportsLessThan)

def top_n2(data: Iterable[T2], n: int) -> list[T2]:
    result = sorted(data, reverse=True)
    return result[:n]
