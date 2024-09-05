"""
This is how class Iterator is implemented in _collections_abc.py
See https://github.com/python/cpython/blob/b1930bf75f276cd7ca08c4455298128d89adf7d1/Lib/_collections_abc.py#L271
"""

from collections.abc import Iterable

"""
Implementation can be found here: https://github.com/python/cpython/blob/b1930bf75f276cd7ca08c4455298128d89adf7d1/Lib/_collections_abc.py#L78
"""
from _collections_abc import _check_methods

class Iterator(abc.Iterable):
    __slots__ = ()

    @abstractmethod
    def __next__(self):
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration

    def __iter__(self):
        return self

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            return _check_methods(C, '__iter__', '__next__')
        return NotImplemented
