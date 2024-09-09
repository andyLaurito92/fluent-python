"""
Examples on how to add type hints when having iterators,
iterables or generators
"""

from typing import TypeAlias, TYPE_CHECKING
from collections.abc import Iterable, Iterator
from keyword import kwlist

FromTo: TypeAlias = tuple[str, str]

def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text.replace(from_, to)
    return text


"""
Note that the type Iterator is used for generators coded as functions
with yield, as well as iterators written "by hand" as classes with __next__
be used)
"""
def fibonacci() -> Iterator:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for fibnum, idx in zip(fibonacci(), range(11)):
    print(fibnum)


"""
Iterator type is really a simplified special case of the Generator type
"""

short_kw = (k for k in kwlist if len(k) < 5)


"""
typehints_generators.py:40: note: Revealed type is "typing.Generator[builtins.str, None, None]"
"""
if TYPE_CHECKING:
    reveal_type(short_kw)

long_kw: Iterator[str] = (k for k in kwlist if len(k) >= 4)

"""
typehints_generators.py:45: note: Revealed type is "typing.Iterator[builtins.str]"
"""
if TYPE_CHECKING:
    reveal_type(long_kw)


"""
abc.Iterator[str] is consistent-with abc.Generator[str, None, None], therefore
Mypy issues no errors for type checking.

Iterator[T] is a shortcut for Generator[T, None, None]. Both annotations mean:
"A generator that yields items of type T, but that does not consume or return values"

Generators able to consume and return values are coroutines
"""
