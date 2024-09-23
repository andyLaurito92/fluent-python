import sys
from time import perf_counter
from typing import NamedTuple, TypeAlias
from multiprocessing import Process, SimpleQueue, cpu_count
from multiprocessing import queues
from threading import Thread

from primes import is_prime, NUMBERS

class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float

JobQueue: TypeAlias = queues.SimpleQueue[int]
ResultQueue: TypeAlias = queues.SimpleQueue[PrimeResult]


def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    prime = is_prime(n)
    return PrimeResult(n, prime, perf_counter() - t0)

def worker(jobs:JobQueue, results: ResultQueue) -> None:
    while n := jobs.get(): # n = 0 is a poision pill to stop this process
        results.put(check(n))
    results.put(PrimeResult(0, False, 0.0))


def start_jobs(
        procs: int, jobs: JobQueue, results: ResultQueue,
        worker_type: Process | Thread
        ) -> None:
    for n in NUMBERS:
        jobs.put(n)

    for _ in range(procs):
        proc = worker_type(target=worker, args=(jobs, results))
        proc.start()
        jobs.put(0) # A posion pill to kill a process

def parse_args() -> tuple[int, Process|Thread]:
    if len(sys.argv) < 2:
        procs = cpu_count()
        procs_type = Process
    else:
        procs = int(sys.argv[1])
        try:
            procs_type = sys.argv[2]
            if procs_type == 'process':
                procs_type = Process
            else:
                procs_type = Thread
        except IndexError:
            procs_type = Process

    return (procs, procs_type)
    
        
def main() -> None:
    procs, procs_type = parse_args()

    print(f'Checking {len(NUMBERS)} numbers with {procs} processes with {procs_type}:')

    t0 = perf_counter()
    jobs: JobQueue = SimpleQueue()
    results: ResultQueue = SimpleQueue()

    start_jobs(procs, jobs, results, Process)

    checked = report(procs, results)
    elapsed = perf_counter() - t0
    print(f'{checked} checks in {elapsed:.2f}s')

def report(procs: int, results: ResultQueue) -> int:
    checked = 0
    procs_done = 0
    while procs_done < procs:
        # get is a blocking method. if we want to make it non blocking,
        # we can send a False as first argument, but this returns an
        # Empty exceptin in case of none result. See
        # https://docs.python.org/3/library/queue.html#queue.SimpleQueue.get
        # for more info
        n, prime, elapsed = results.get() 
        if n == 0:
            procs_done += 1
        else:
            checked += 1
            label = 'P' if prime else ' '
            print(f'{n:16} {label} {elapsed:9.6f}s')
    return checked

if __name__ == '__main__':
    main()
