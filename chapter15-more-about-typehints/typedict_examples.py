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
