"""
Type hints in Python are defined by it's supporting operations
"""

def times_3(val: int):
    return val * 3

numbers = [1, 2, 3, 4, 5]

times_3(numbers)

"""
Mypy throws this error: times_in_sequence.py:10: error: Argument 1 to "times_3" has incompatible type "list[int]"; expected "int"  [arg-type]

While if you try to execute this code in runtime, it works.
"""
