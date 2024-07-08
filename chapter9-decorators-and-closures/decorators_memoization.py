"""
functools.cache decorator implements memoization: Optimization technique that
works by saving the results of previous invocations of an expensive function,
avoiding repeat calculations.

Let's see an exampley by applying cache to fibonacci
"""

from typing import Callable
import time
from functools import wraps

def timer(func: Callable) -> Callable:
    @wraps(func)
    def time(*args, **kwargs):
        global time
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        positional_args = ', '.join((str(x) for x in args))
        print(f"Execution time of {func.__name__}({positional_args}): {end - start}ms")
        return res
    return time


@timer
def fibonacci(n: int) -> int:
    if n < 1:
        return 0
    elif n < 2:
        return 1
    else:
        return fibonacci(n -1 ) + fibonacci(n - 2)


fibonacci(8)

"""
The above function calculates many repeated times fibonacci when we
could reuse previous calculation (this is memoization).
Let's use the cache decorator
"""

print("*" * 10)
print("fibonacci2")
print("*" * 10)

from functools import cache, lru_cache

@timer
@cache
def fibonacci2(n:int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)


fibonacci2(8)


"""
Note: In order to use …@cache, all the argument values of the function
must be cachable. @cache uses underneath a dictionary

Problem with this cache is that is unbounded, meaning that it could grow
up to cause an out of memory exception. This is why we should use lru_cache
"""

from functools import lru_cache

print("*" * 20)
print("fibonacci3 with lru cache")
print("*" * 20)

"""
maxsize stands up for the number of entries before applying LRU (least
recently used)

Typed stands up for storing arguments of different types: For example,
calling fibonacci3(1) & fibonacci3(1.0) would cause 2 new entries if
typed=True.
"""
@timer
@lru_cache(maxsize=2**9, typed=False)
def fibonacci3(n: int) -> int:
    if n < 2:
        return 1
    else:
        return fibonacci3(n -1) + fibonacci3(n-2)

fibonacci3(8)
