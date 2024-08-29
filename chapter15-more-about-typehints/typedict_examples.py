"""
Examples on typedict class from typing module: Reality is that is not very useful given
that it doesn't apply runtime checks. If you want to validate json-like structures using
type hints at runtime, use pydantic instead. Link: https://pydantic-docs.helpmanual.io/
"""
from typing import TypedDict
import inspect

class BookDict(TypedDict):
    title: str
    isbn: int
    price: float
    authors: list[str]

"""
Note how can I set author:str instead of authors:list[str] and nothing happens in runtime. This is a clear
example of why TypedDict is not very useful for runtime checks

However, if you run mypy on this file you will get:

typedict_examples.py:19: error: Missing key "authors" for TypedDict "BookDict"  [typeddict-item]
typedict_examples.py:19: error: Extra key "author" for TypedDict "BookDict"  [typeddict-unknown-key]
"""
harry_potter = BookDict(title='Harry Potter', isbn=123456789, price=39.99, author='J.K. Rowling')

print(f"Typedict create dict with annotations: {type(harry_potter)}, {inspect.get_annotations(BookDict)}")

"""
Using BookDict as a type hint for a function
"""

AUTHOR_ELEMENT = '<AUTHOR>{}</AUTHOR>'
def to_xml(book: BookDict) -> str:
    elements: list[str] = []
    for key, value in book.items():
        if isinstance(value, list):
        #if key == 'authors':
        # Validate if key = authors doesn't work for mypy, it returns:
        # typedict_examples.py:37: error: "object" has no attribute "__iter__"; maybe "__dir__" or "__str__"? (not iterable)  [attr-defined]
        # This is bc mypy inferred the type of key as object
            elements.extend(AUTHOR_ELEMENT.format(author) for author in value)
        else:
            tag = key.upper()
            elements.append(f'<{tag}>{value}</{tag}>')
    xml = '\n\t'.join(elements)
    return f'<BOOK>\n\t{xml}\n</BOOK>'


"""
Let's consider this other example
"""

import json
def from_json(data: str) -> BookDict:
    whatever = json.loads(data)
    return whatever

from_json('{"name":"John", "age":30, "car":null}')

"""
The above of course that it works, and mypy doesn't raise an error. The reason on why is
because whatever is inferred as Any, and Any is compatible with BookDict.

If you run mypy with flag --disallow-any-expr you get:

typedict_examples.py:55: error: Expression has type "Any"  [misc]
typedict_examples.py:56: error: Expression has type "Any"  [misc]
"""

def from_json2(data:str) -> BookDict:
    abook: BookDict = json.loads(data)
    return abook

from_json('{"name":"John", "age":30, "car":null}')

"""
An important lesson to learn from the above example: Static type checking is unable
to prevent errors with code that is inherently dynamic, such as json.loads() which
builds objects at runtime.

This problem is something that also happens in other programming languages such as Java.

It's also a good reminder that not all problems can be solved by a static type checker ;)
"""
