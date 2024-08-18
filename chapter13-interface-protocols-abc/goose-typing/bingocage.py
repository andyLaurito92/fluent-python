import random
from tombola import Tombola

"""
We decide not to implement inspect just to show that BingoCage can decide to do so
"""

class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from empty bingocage')

    def __call__(self):
        return self.pick()
