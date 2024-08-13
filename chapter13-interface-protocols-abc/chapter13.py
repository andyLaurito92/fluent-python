"""
There is no need to inherit from an abc to make it a subclass of it!
"""
from collections.abc import Sized, MutableSequence
from typing import NamedTuple

class Example:
    def __len__(self):
        return 0


"""
This is a type of goose typing. The other way of doing it is to inherit
from the abstract base class. 
"""

myexample = Example()
isinstance(myexample, Sized)

"""
Rewriting french deck by inheriting from MutableSequence

By doing this, we are forced to implement the following methods:
- __len__
- __getitem__
- __setitem__
- __delitem__
- insert

This is because these methods are abstract methods in MutableSequence
"""

Card = NamedTuple('Card', [('rank', str), ('suit', str)])

class FrenchDeck(MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, position, value):
        self._cards.insert(position, value)


"""
Note: Python doesn't check for the implementation of the abstract
methods at import time but at runtime
"""
