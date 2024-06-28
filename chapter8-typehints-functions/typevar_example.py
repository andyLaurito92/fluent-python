from collections.abc import Sequence
from random import shuffle
from typing import TypeVar

T = TypeVar('T')

def sample(seq: Sequence[T], k: int) -> list[T]:
    if k < 1:
        raise ValueError('k must be greater than 0')
    result = list(seq)
    shuffle(result)
    return result[:k]


"""
Let's now re-define the statistics.mode function. You can find more about it here:
https://docs.python.org/3/library/statistics.html#statistics.mode
"""

from collections import Counter
from typing import Iterable

def my_mode(data: Iterable[float]) -> float:
    list_pair = counter = Counter(data).most_common(1)
    if len(list_pair) == 0:
        raise ValueError('no unique mode; found %d equally common values' % len(counter))
    return list_pair[0][0]

my_mode([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10])

print(f"Mode for integers: {my_mode([1, 2, 3, 4])}")

"""
The above typing works, but! What if we want to get the mode of an Iterable of fractions? We can't use the above function because it only works for types consistent with floats!, let's see how can we fix it:
"""

from fractions import Fraction
from decimal import Decimal

Numbers = TypeVar('Numbers', float, Decimal, Fraction)

def my_mode2(data: Iterable[Numbers]) -> Numbers:
    list_pair = counter = Counter(data).most_common(1)
    if len(list_pair) == 0:
        raise ValueError('no unique mode; found %d equally common values' % len(counter))
    return list_pair[0][0]


print(f"Mode for fractions: {my_mode([Fraction(3, 2), Fraction(3, 2), Fraction(1, 2), Fraction(4, 2)])}")

"""
Better, but we should define our mode function to also accept string arguments. How can we do this? Well, we could use the same TypeVar as above and define in the same list str, but this wouldn't be a good solution.
If we define a super generic type, such as T = TypeVar('T'), then we would be introducing a bug, because that type would match also with types that are not hashable, which is a requirement for the Counter class.
On the other hand, if we define the type as Hashable, then we have the problem that we would also be returning a Hashable type, which is not what we want.

For these type of cases, TypeVar provides the bound key-word argument, which allows us to specify the type of the TypeVar. Let's see how we can use it:
"""

from typing import TypeVar

HashableT = TypeVar('HashableT', bound='Hashable')

def my_mode2(data: HashableT) -> HashableT:
    list_pair = counter = Counter(data).most_common(1)
    if len(list_pair) == 0:
        raise ValueError('no unique mode; found %d equally common values' % len(counter))
    return list_pair[0][0]


"""
The above type is pretty much close to what we have here: https://github.com/python/typeshed/blob/e1e99245bb46223928eba68d4fc74962240ba5b4/stdlib/3/statistics.pyi#L15
"""
