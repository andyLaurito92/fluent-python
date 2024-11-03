"""
Sample test for showing @cached_property decorator. I'm also showing
something interesting: cached_property doesn't work as expected with
mutable sequences. It do works, but the difference is that what is being
cached is the VALUE, which is a list, which can be mutated. The VALUE (
which is the list) doesn't chage. What it changes is the content of it


cached_property decorator creates a nonoverriding descriptor. See its
implementation here:
https://github.com/python/cpython/blob/e6d0107e13ed957109e79b796984d3d026a8660d/Lib/functools.py#L926

The cached_property decorator only runs on lookups and only when an
attribute of the same name doesn't exist

A descriptor is an object that manages the access to an attribute in
another class.
"""

from functools import cached_property
from collections.abc import Iterable
from random import choice
from string import ascii_lowercase

def generate_random_string(n:int) -> str:
    return ''.join((choice(ascii_lowercase) for i in range(n)))


class Store:
    def __init__(self, name: str, initial_stock: Iterable):
        self.name = name
        self.internal_stock = list(initial_stock)
        self.sum = 50

    def update_stock(self, items: Iterable) -> None:
        self.internal_stock.extend(items)

    @cached_property
    def increase(self):
        self.sum += 50
        return self.sum

    @cached_property
    def stock(self) -> list[str]:
        return self.internal_stock


mystore = Store("Andy Supermarket",
                (generate_random_string(5) for i in range(10)))

print("Current stock ", mystore.stock)

mystore.update_stock(["something"])

print("Current stock ", mystore.stock)


print(mystore.increase)
print(mystore.increase)
print(mystore.increase)
print(mystore.increase)
