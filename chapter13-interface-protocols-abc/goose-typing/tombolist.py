"""
Tombolist is a virtual subclass of Tombola. This means that
this class is registered as a subclass of Tombola by calling the register method.
"""

from random import randrange
from tombola import Tombola

@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return len(self) == 0

    def inspect(self):
        return tuple(self)


# Another way of registering a subclass
# Tombola.register(TombolaList)

myTombola = TomboList(range(100))

# Register makes the following methods to work as we would expect

isinstance(mytombola, Tombola)
issubclass(TomboList, Tombola)

"""
Registering a virtual subclass has some drawbacks:
- The method resolution order (MRO) is not changed. This means that the subclass will not inherit from the superclass. This is because the subclass is not a subclass of the superclass. It's just registered as one. If you check TombolaList.__mro__ you won't see Tombola in it.
- Virtual subclasses do not inherit from their registered ABCs and are not checked for conformance to the ABC interface at any time
- Static type checkers can't handle virtual subclass at this time. See https://github.com/python/mypy/issues/2922 for more details on this in Mypy
"""
