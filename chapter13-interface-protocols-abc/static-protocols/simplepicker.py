from random import shuffle
from typing import Any, Iterable

class SimplePicker:
    def __init__(self, items: Iterable):
        self._items = list(items)
        shuffle(self._items)

    def pick(self) -> Any:
        return self._items.pop()

