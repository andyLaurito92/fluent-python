"""
We start this chapter talking about from typing import overload. This decorator allows
describing functions that can receive arguments of different types, as explained in the
documentation here: https://docs.python.org/3/library/typing.html#overload

Note: Typing overlaoding is not the same as method overloading :).
Method overloading is what we call as a class defining the same method with
different signatures. For example in java we could do something like this:

class MyClass {
    public void myMethod(int x) {
        System.out.println(x);
    }

    public void myMethod(int x, int y) {
        System.out.println(x + y);
    }
}

The above is not possible in Python. We saw in a previous chapter that something similar
can be achieved by using the singledispatch decorator from functools.
For more than one argument, you can use the multipledispatch library which you can find
here: https://github.com/mrocklin/multipledispatch

The typing.overload decorator is used to define multiple signatures for a single
function. The implementation of the function is not defined in the overload
"""

from typing import overload

@overload
def foo(x: int) -> int: ...

@overload
def foo(x: str) -> str: ...

# Note that the function of the implementation doesn't have
# any type hint
def foo(x):
    return x * 2

print(foo(1))
print(foo('hey'))


"""
A more interesting example
"""

import functools
import operator
from collections.abc import Iterable
from typing import TypeVar

T = TypeVar('T')
S = TypeVar('S')

@overload
def sum(it:Iterable[T]) -> T | int: ...

@overload
def sum(it: Iterable[T], /, start: S) -> S | T: ...

def sum(it, /, start=0):
    return functools.reduce(operator.add, it, start)

print(sum(range(10), start=4))
print(sum(range(10)))
