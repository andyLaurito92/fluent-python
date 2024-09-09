"""
Using iterators from itertools
"""
import os
from itertools import count, takewhile

"""
itertools.count yields numbers, preety much as
our arithmetic progression class/function

Note: itertools.count never stops! So calling
list(itertools.count()) would cause a
memory error
"""
for i in count(10, .5):
    print(i)
    if i > 12:
        break

"""
itertools.takewhile -> returns a generator that
consumes another generator and stops when a given
predicate evaluates to False
"""

for i in takewhile(lambda n: n < 11, count()):
    print(i)


"""
os.walk -> yields filenames while traversing a directory tree,
making recursive filesystem searches as simple as a for loop

documentation can be found here: https://docs.python.org/3/library/os.html#os.walk
"""

for path, dirnames, filenames in os.walk(os.getcwd()):
    print(path, dirnames, filenames)
