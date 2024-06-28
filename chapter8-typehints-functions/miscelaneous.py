from collections.abc import Sequence


def columnize(sequence: Sequence[str], columns: int = 0
              )-> list[tuple[str, ...]]:
    if columns == 0:
        columns = round(len(sequence) ** 0.5)
    rows, extra = divmod(len(sequence), columns)
    if extra:
        rows += 1
    return [tuple(sequence[i::columns]) for i in range(columns)]


print(columnize(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], 3))

print(columnize(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], 4))



"""
Inverted index -> https://en.wikipedia.org/wiki/Inverted_index
"""

import sys
import re
import unicodedata
from collections.abc import Iterator

RE_WORD = re.compile(r'\w+')
STOP_CODE = sys.maxunicode + 1

"""
We define a generator function
"""
def tokenize(text: str)-> Iterator[str]:
    for match in RE_WORD.finditer(text):
        yield match.group()

def name_index(start: int = 32, end: int = STOP_CODE)-> dict[str, set[str]]: 
    index: dict[str, set[str]] = {}
    for code in range(start, end):
        char = chr(code)
        name = unicodedata.name(char, None)
        if name is not None:
            for word in tokenize(name):
                index.setdefault(word, set()).add(char)
    return index

index = name_index(32, 128)

print(f"Digits are: {index['DIGIT']} ")


"""
We can define type alias for the return type of the function
"""

from collections.abc import Iterable

# Type alias
Code = str

def tokenize_code(code: Code)-> Iterable[str]:
    return RE_WORD.findall(code)

tokens = tokenize_code("import this")

print(tokens)
    

"""
Another way of defining type alias. This is the recommended way
"""
from typing import TypeAlias

Code: TypeAlias = str
