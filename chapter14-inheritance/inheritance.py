from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
    """ Stores items in the order they were last updated """

    def __setitem__(self, key, value):
        res = super()
        print(res)
        self.res = res
        res.__setitem__(key, value)
        self.move_to_end(key)

"""
Another way of doing the above thing would be:
"""

class LastUpdatedOrderedDict2(OrderedDict):
    """ Stores items in the order they were last updated """

    def __setitem__(self, key, value):
        OrderedDict.__setitem__(key, value)
        self.move_to_end(key)

"""
The above works, but it's not recommended at all. Some of the problems:
1. You're hardcoding the base class name, so if you change the inheritance, you need to remember to change it in this method
2. If you have multiple inheritance, this might not work as expected
"""

"""
Note: super is a class :O. Read the documentation here: https://docs.python.org/3/library/functions.html#super

Calling super() is anologous since Python3 to calling super(CurrentClass, self) and it
returns a super instance that delegates method calls to the MRO of the class. This instance
is said to be a proxy because it proxies the attribute lookup to the next class in the MRO.

When calling super with arguments, the method resolution order is computed based on the
class of the first argument, not the class of the calling instance. The second argument
is the receiver of the method call.
"""


"""
Subclassing built-in types is tricky, since cpython is implemented in C, and the built-in types are implemented in C,
the C implementation of the built-in types don't call the methods of the subclass.

Pypy explains this here: https://doc.pypy.org/en/latest/cpython_differences.html#subclasses-of-built-in-types
"""

class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value]*2)

dd = DoppelDict(one=1)
print(dd)
dd['two'] = 2
print(dd)
dd.update(three=3)
print(dd)



"""
The problem is not limited to calls within an instance
"""

class AnswerDict(dict):
    def __getitem__(self, key):
        return 42

ad = AnswerDict(a='foo')
print(ad['a'])

d = {}
d.update(ad)
# Returns foo!
print(d['a'])
