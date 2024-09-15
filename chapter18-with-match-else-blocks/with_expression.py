"""
Context manager objects exist to control a with statement, just like
iterators exist to control a for loop statement

Context manager interface consists of methods

__enter__
__exit__

when the with block clopletes or terminates for any reason, Python calls
__exit__ on the context manager object
"""
import inspect
import os

# Most common example of with: Read a file
file_path = inspect.getfile(lambda: None)
dir_path = os.path.dirname(file_path)
os.chdir(dir_path)
with open("example.txt", "w") as myfile:
    myfile.write("sht")

"""
myfile still exists! Difference between functions: with blocks don't define
a new scope
"""
print(myfile)

"""
File is closed because after with statement, TextIOWrapper.__exit__ method was
called
"""
print(myfile.closed, myfile.encoding)

"""
myfile is bound to the opened text file, because the file's __enter__ method
returns self.
"""

"""
Note: The as close of the with statement is optional. In the case of open, we
need it to get the reference to the file, but it won't be always the case that
we will need to define it
"""

from mirror import LookingGlass
import sys

"""
In the following example, we show the difference between a
context manager object (LookingGlass, object who implements both
__enter__ and __exit__ methods) and the object RETURNED by method 
__enter__ 
"""
with LookingGlass() as what:
    print('Something, is going to happen')
    print(what)
    # The zero division error is handled by the
    # context manager object
    print(1/0)

print(what)
print("What was that!?")
