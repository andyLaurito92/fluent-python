"""
Python provides a cast function in the typing module. This function
is used to coerce a value to a specific type. This function is only
useful for the static type checker.
"""

from typing import cast

x: float = 3.0
print(x)
y = cast(int, x)

print(y)

"""
At runtime cast does nothing at all:
https://github.com/python/cpython/blob/bee66d3cb98e740f9d8057eb7f503122052ca5d8/Lib/typing.py#L1340
It's merely an indication to the static checker as it explains PEP 484, in the cast section: https://peps.python.org/pep-0484/#casts
"""
# Example of an useful cast
def find_first_str(a: list[object]) -> str:
    index = next(i for i, x in enumerate(a) if isinstance(x, str))
    # We only get here if there's at least one string in a
    return cast(str, a[index])


"""
Same example but without enumerate. This is just to show that mypy can
infer correctly that elem is of type str.

In the previous example, enumarate is used on purpose to confuse mypy
"""
def find_first_str_v2(a: list[object]) -> str:
    for elem in a:
        if isinstance(elem, str):
            return elem

"""
Note: We can either write down types as comments, such as:

for x, y in points:  # type: int, int
    print(x + y)

or ask mypy to ignore a concrete line with the #type: ignore comment:

for x, y in points:
    print(x + y)  # type: ignore
"""
