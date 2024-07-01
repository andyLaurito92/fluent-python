"""
To annotate callback parameters or callable objects returned by hihg-order
functions, we can use the Callable type from the typing module

The Callable type takes two arguments: the first one is a tuple of the
function's arguments, and the second one is the return type
Callable[[arg1, arg2, ...], return_type]

The parameter list can have 0 or more types
"""

from typing import Callable


def my_high_order_function(myfun: Callable[[str, str], str]) -> str:
    return myfun("Hello", "World")


my_high_order_function(lambda x, y: f"{x} {y}")


"""
Defining positional only arguments by using 2 underscores before the argument name.
See https://peps.python.org/pep-0484/#id38

The above example works in runtime, but it's detected as call-arg error by mypy
The error says: 
callable.py:32: error: Unexpected keyword argument "__c" for "my_function"  [call-arg]
"""

def my_function(__a, __c):
    return __a + __c

print(my_function(__a=1, __c=3))
print(my_function(1, 3))
