"""
This chapter uses mypy to check the type hints of the functions

You need to run from the terminal by running mypy typehints_functions.py

There are other type checkers implemented, such as:

1. Google pytype --> https://github.com/google/pytype
2. Microsoft pylance -> https://github.com/microsoft/pylance-release
3. Facebook pyre --> https://pyre-check.org/

"""
from typing import Optional

def show_count(count: int, word: str,
               plural: Optional[str] = None) -> str:
    if count == 1:
        return f"{count} {word}"
    count_str = str(count) if count else "no"
    if plural is not None:
        return f"{count_str} {plural}"
    return f"{count_str} {word}s"
