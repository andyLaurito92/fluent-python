"""
concurrent.futures.Executor encapsulate the pattern of: "Spawning a bunch of independent
threads and collecting the results in a queue"

In chapter19/prime_check_process.py we build ourselves a ProcessPoolExecutor. Let's instead
use class ThreadPoolExecutor and see the result
"""

import sys
from time import perf_counter
from typing import NamedTuple, TypeAlias
from concurrent import futures

from primes import is_prime, NUMBERS

class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float

def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    prime = is_prime(n)
    return PrimeResult(n, prime, perf_counter() - t0)

def main() -> None:
    if len(sys.argv) < 2:
        workers = None
    else:
        workers = int(sys.argv[1])

    executor = futures.ProcessPoolExecutor(workers)
    actual_workers = executor._max_workers # type: ignore

    print(f'Checking {len(NUMBERS)} numbers with {actual_workers} processes')

    t0 = perf_counter()
    numbers = sorted(NUMBERS, reverse=True)
    with executor:
        for n, prime, elapsed in executor.map(check, numbers):
            label = 'P' if prime else ' '
            print(f'{n:16} {label} {elapsed:9.6f}s')

    elapsed = perf_counter() - t0
    print(f'Took {elapsed:.2f}s')


if __name__ == '__main__':
    main()
