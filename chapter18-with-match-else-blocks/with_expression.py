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
    # print(1/0)
    # raise ZeroDivisionError("Something")

print(what)
print("What was that!?")


"""
Note: If __exit__ returns None or any falsy value, any exception
raised in the with block will be propagated
"""

"""
An example of a context manager for temporarily redirecting sys.stdout
otuput to another file-like object is contextlib.redirect_stdout:

https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout
"""
from contextlib import redirect_stdout
import io

with redirect_stdout(io.StringIO()) as f:
    help(pow)
s = f.getvalue()

print(s)


"""
Note: Since Python 3.10 we can write

with (
 ctxmanager1() as ctx1,
 ctxmanager2() as ctx2,
 ctxmanager3() as ctx3,
):
 something

This is thx to the replacement of LL(1) parser to
a PEG based parser https://peps.python.org/pep-0617/

"""

"""
Review the contextlib library which contains many context
manager classes than can be useful :)

https://docs.python.org/3/library/contextlib.html
"""

"""
Implementing the looking glass class with decorator contextlib.contextmanager
"""

from contextlib import contextmanager

@contextmanager
def looking_glass2():
    original_write = sys.stdout.write
    sys.stdout.write = lambda txt: original_write(txt[::-1])
    """
    Up to this point we have the __enter__ method of our
    context manager. The below yielded value will be assigned
    to the variable in the AS statement. Yield gives back
    control to the with statement
    """
    yield 'ABRACADABRA'

    """
    From now own, this code represents the __exit__ part of
    our context manager
    """
    sys.stdout.write = original_write

    """
    What about the 3 values that the __exit__ method receives?
    raise_type, raise_exce, traceback. How do we handle those
    here?
    """

with looking_glass2() as magic_word:
    print("magic_word is ", magic_word)
    print("Looks weird")
    print("Goodbye!")

print("Back to normal :)")
print("magic word was: ", magic_word)