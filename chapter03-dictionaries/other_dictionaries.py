from collections import ChainMap
from collections import Counter

"""
ChainMap: Holds a list of mappings that can be searched as one

Lookup is performed on each input mapping in the order it appears in the constructor call and succeds
as soon as the element is found

This map doesn't copy the input mappings, but holds references to them
"""

d1 = dict(a=1, c=3)
d2 = dict(z=10, y=-3)

chain = ChainMap(d1, d2)
chain['y']

"""
Note: ChainMap is useful to implement interpreters for languages with nested
scopes, where each mapping represets a scope contex, from the innermost enclsoing
scope to the outermost scope. See https://fpy.li/3-8 for more info
"""

# Snippet that shows the basic rules of variable lookup in Python
import builtins
pylookup = ChainMap(locals(), globals(), vars(builtins))

"""
Counter: A mapping that holds an integer count for each key. Updating an existing key adds to its count
"""

mycounter = Counter("This is a string")
mycounter.most_common(3)

mycounter.update("aaeebbccc")
mycounter.most_common(4)


"""
shelve.Shelf persisten sotrage for a mapping of string keys to python objects
serialized in the pickle binary format. It's a key-value DBM

Ref:https://docs.python.org/3/library/shelve.html

Note: Pickle has several drawbacks that are detail at this post: https://nedbatchelder.com/blog/202006/pickles_nine_flaws.html
"""

"""
If a custom class is needed that knows how to answer all dictionary methods, UserDict should be extended instead of dict. This is because dict has built-in implementation shortcuts that end up forcing us to override methods that we can just inherit form UserDict

UserDict doesn't inherit from dict but uses composition (meaning, it has an internal dict instance)
"""

from collections import UserDict

## Convenient class to use either number or strings as keys of a dictionary.
## This class can be used for Arduino, where the class represents a mapping of
## the board pins to it's respective numbers
class StrKeyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

myboard = StrKeyDict()
myboard[3] = 20
'3' in myboard

# Ends up calling __setitem__ of dictionary for each key, value pair. It's also called by init
# when a dictionary is provided to the constructor
myboard.update({10:'hey'})
myboard['10']


"""
Given that the builtins python dictionaries are mutable, in case immutability is needed, we can use
types.MappingProxyType. This is a wrapper of the original mapping which returns a read-only but dynamic proxy
for the original mapping (this means that updates in the original dictionary are seen in the mappingProxyType
instance)
"""

from types import MappingProxyType
mydictionary = { '1': 'A', '2': 'B', '3':'C' }
immutable_dictionary = MappingProxyType(mydictionary)
immutable_dictionary['1']
# This throws a TypeError (read-only dictionary)
immutable_dictionary['1'] = 3

mydictionary['4'] = 'D'
immutable_dictionary['4']


"""
Methods .keys(), .values() and .items() of dictionary return a dictionary view which is a dynamic proxy :)

The dictionary view class only implements __len__, __iter__ and __reversed__ special methods and cannot be
instantiated by the user
"""

dict_vals = mydictionary.values()
dict_vals
mydictionary['5'] = 'E'
dict_vals

# Remove duplicates from list and preserve order in which they appear
l = ['hola', 'hola', 'chau', 'chau', 'hey', 'hola', 'hey']
dict.fromkeys(l).keys()
