import re
import reprlib 

WORD = re.compile(r'\w+')
class Sentence:
    def __init__(self, text: str) -> None:
        self.text = text
        self.words = WORD.findall(text)

    def __getitem__(self, idx: int) -> str:
        return self.words[idx]

    def __len__(self) -> int:
        return len(self.words)

    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)
                

mysentence = Sentence("Some cool text insert here")

aniter = iter(mysentence)

print(list(aniter))
"""
Why Sentence is iterable? Because of the iter built-in function.
When Python needs to iterate over an object x, it automatically calls iter(x).
The iter built-in function does this:

1. Checks wether the object implements __iter__, and calls that to obtain an
iterator

2. If __iter__ is not implemented, but __getitem__ is, then iter() creates an
iterator that tries to fetch items by index, starting from 0 (This is defined
in cpython here: https://github.com/python/cpython/blob/b1930bf75f276cd7ca08c4455298128d89adf7d1/Lib/_collections_abc.py#L1032)

3. If that fails, Python raises TypeError, usually saying: "C object is not
iterable", where C is the class of the target object

Because all python sequences implement __getitem__, they all end up being iterable
because of item 2.

The iter built in function is defined in Cpython here: https://github.com/python/cpython/blob/main/Python/bltinmodule.c#L1667
"""

class Spam:
    def __getitem__(self, i):
        """ Showing that this also returns an iterator"""
        print("-->" , i)
        raise IndexError()

spam = Spam()

list(spam)
