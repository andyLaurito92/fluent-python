import random

from tombola import Tombola

class LottoBlower(Tombola):
    def __init__(self, iterable):
        # We create a list from the iterable to make sure that the
        # object is a list. This is important because we are going to
        # use the pop method from the list object
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LottoBlower')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(self._balls)

    def __call__(self):
        return self.pick()
            
