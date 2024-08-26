from collections import UserDict, Counter

def _upper(key):
    try:
        return key.upper()
    except AttributeError:
        return key

"""
A mixin class is designed to be subclassed together with at least
one other class in a multiple inheritance arrangement.
A mixin is not supposed to exist independently of a class because
it doesn't provide all the functionality for a concrete object,
but only adds or customizes the behavior of child or sibling classes.
"""

class UpperCaseMixin:
    """ Mixin that convert keys in uppercase """
    def __setitem__(self, key, value):
        super().__setitem__(_upper(key), value)

    def __getitem__(self, key):
        return super().__getitem__(_upper(key))

    def get(self, key, default=None):
        return super().get(_upper(key), default)

    def __contains__(self, key):
        return super().__contains__(_upper(key))
        


"""
Note: Given that a mixin depends on other classes to exists,
it's important to understand which is the order of the MRO of
class inheriting from a mixin.
Usually the mixin is the first class in the inheritance list
"""
class UpperDict(UpperCaseMixin, UserDict):
    pass


class UpperCounter(UpperCaseMixin, Counter):
    """ Specialization of Counter that converts keys to uppercase """

d = UpperDict([('a', 'letter A'), (2, 'digit two')])

c = UpperCounter('aAAbBBcCC')
