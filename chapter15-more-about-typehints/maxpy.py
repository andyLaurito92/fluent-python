"""
This example does 2 things:
1. Implements the max function in python. This function is implemeted in Cpython. It has some interesting
logic that shows duck typing in action (way of thinking)
2. Types the max function using typing.overload
"""

from typing import Iterable, overload, Callable, TypeVar, Protocol

class SupportsLessThan(Protocol):
    def __lt__(self, other: object) -> bool: ...

MISSING = object()

# Type for when we receive a key function
T = TypeVar('T') 

# Type for elements that support less than
LT = TypeVar('LT', bound=SupportsLessThan) #

# Type for the default valu
DT = TypeVar('DT')

@overload
def mymax(__arg1: LT, __arg2: LT, *args: LT, key: None = ...) -> LT: ...
@overload
def mymax(__arg1: T, __arg2: T, *args: T, key: Callable[[LT], LT]) -> T: ...
@overload
def mymax(__iter: Iterable[T], *, key: Callable[[T], LT]) -> T: ...
@overload
def mymax(__iter: Iterable[LT], *, key: None = ...) -> LT: ...
@overload
def mymax(__iter: Iterable[T], *, key: Callable[[T], LT], default: DT) -> T | DT: ...
@overload
def mymax(__iter: Iterable[LT], *, key: None = ..., default:DT) -> LT | DT: ...

def mymax(first, *args, key=None, default=MISSING):
    if args:
        # If args is not empty, then max was used like max(1, 2, 3)
        # meaning that first represents already the first element in the series
        series = args
        candidate = first
    else:
        # If we are here, then first should be an iterable. We assume this and
        # in case it's not the case, we handle the error

        # Note: If first is not an iterable, iter will return a TypeError
        # that's declarative enough
        series = iter(first)
        try:
            candidate = next(series)
        except StopIteration:  # Case when the iterable is empty
            if default is MISSING: # User didn't provide a default value
                raise ValueError('max() arg is an empty sequence')
            return default

    if key is None:
        for item in series:
            if candidate < item:
                candidate = item
    else:
        candidate_key = key(candidate)
        for item in series:
            item_key = key(item)
            if candidate_key < item_key:
                candidate = item
    return candidate
        

# Mypy detects this
max(None, None)
max([None, None])
