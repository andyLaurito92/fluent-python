from typing import Optional, overload
from dataclasses import dataclass


@dataclass
class Foo:
    id: int


# """
# The below definitions are just for mypy so it doesn't trigger the
# error 
# """
# @overload
# def get_foo(x: int) -> Foo:
#     pass


# @overload
# def get_foo(x: None) -> None:
#     pass


def get_foo(x: Optional[int]) -> Optional[Foo]:
    if x is None:
        return None
    return Foo(x)

myfoo = get_foo(3)
"""
If we try to access myfoo.id, mypy will raise an error, even if we know
that in this particular case that won't happen because we have provided
an int. An option for this case is to use the overload decorator
"""
myfoo.id

# Uncomment the code previos to the get_foo definition to see how
# mypy doesn't throw the error anymore
