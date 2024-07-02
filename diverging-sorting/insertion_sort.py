"""
While using types to define insertion sort, I wondered why Python used
a key function instead of a comparison function to sort elements.

The answer is that key functions are more efficient than comparison functions
because it uses the Schwartzian transform to avoid calling the comparison function.

Read more about this here: https://stackoverflow.com/questions/52911036/how-are-key-functions-more-efficient-than-comparison-functions-in-pythons-sor

But in essence it works like this:
"""

# We define insertion sort
from collections.abc import Sequence
from typing import TypeVar, Iterable, Any, NoReturn, Protocol, Callable
from random import shuffle

class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...

T = TypeVar('T', bound=SupportsLessThan)

# Note that we need myIterable to be a sequence because we need
# the argument to have method len implemented
def my_insertion_sort(myIterable: Sequence[T]) -> NoReturn:
    for i in range(1, len(myIterable)):
        elem = myIterable[i]
        j = i
        while j > 0 and elem < myIterable[j-1]:
            myIterable[j] = myIterable[j-1]
            j -= 1

        if (j == -1):
            j = 0
        myIterable[j] = elem

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [chr(i) for i in range(65, 91)]

lists_to_sort = [a, b]
for list_to_sort in lists_to_sort:
    shuffle(list_to_sort)
    print(list_to_sort)
    my_insertion_sort(list_to_sort)
    print(list_to_sort)



"""
From the above, the question came up: Why sorted or list.sort uses key, a function
that returns a unique value, and not comprabale like Java?

The answer is in the below code:
"""

def schawartzian_transform(myseq: Sequence[T], key:Callable[[Any], Any]) -> list[T]:
    # We decorate the list by using the key function received + the index
    decorated_list = [(key(myseq[i]), i, myseq[i]) for i in range(0, len(myseq))]

    # We sort the decorated list. Because how tuple works, it will sort by first elem
    # and if tie, it unties with the index, making this sort algorithm stable
    my_insertion_sort(decorated_list)

    # We undecorate the list
    return [elem[2] for elem in decorated_list]


schawartzian_transform(a, lambda x: x)
