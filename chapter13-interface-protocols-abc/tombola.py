from abc import ABC, abstractmethod


"""
Note: An abastract method can have an implementation. If this happens, the subclass will be eitherway forced to implement it but the subclass can call the superclass implementation using super().method_name()
"""

class Tombola(ABC):

    @abstractmethod
    def load(self, iterable):
       """Add items from an iterable"""

    @abstractmethod
    def pick(self):
        """Remove item at random, returning it

        This method should raise `LookupError` when the instance is empty
        """

    # This is a silly method but it shows something:
    # We can rely on the Tombola interface to implement
    # this method without the need to force it's implementation
    # in a subclass. The subclass can, and should, override
    # this method to provide a more efficient implementation
    # based on it's internal data structure
    def inspect(self):
        """ Return a sorted tuple with the items currently inside"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError: # Generic error in Python's hierarchy. This is done on purpose so subclasses can raise a more specific error
                break
        self.load(items)
        return tuple(items)

    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise"""
        return bool(self.inspect())





"""
Note: The abc package also provides @abstractclassmethod, @abstractstaticmethod and @abstractproperty decorators. These last three are deprecated in python 3.3 because now it's possible to stack decorators on top of @abstractmethod


class MyABC(ABC):
   @classmethod
   @abstractmethod
   def an_abstract_classmethod(cls, ...):
       pass

The order of stacked decorators matters: When abstractmethod is applied in combination w/other methods descriptors, it must be the innermost, because it's the one that actually modifies the method's behavior.
"""
