"""
Examples on how to add type hints when having iterators,
iterables or generators
"""

from typing import TypeAlias
from collections.abc import Iterable

FromTo: TypeAlias = tuple[str, str]

def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text.replace(from_, to)
    return text
