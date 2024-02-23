from collections import ChainMap

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
