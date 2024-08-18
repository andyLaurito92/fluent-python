from randompick import RandomPicker

from typing import Protocol, runtime_checkable

"""
Note: To create a protocol that subclasses another protocol,
we need to use multiple inheritance: Base classes need to be
Protocol + the protocol we want to subclass.

Protocol has always need to be declare explicitly in the
inheritance list as exposed in
https://peps.python.org/pep-0544/#merging-and-extending-protocols
"""

# We create a protocol that inherits from RandomPicker
@runtime_checkable
class LoadableRandomPicker(Protocol, RandomPicker):
    def load(self, items: list) -> None: ...



