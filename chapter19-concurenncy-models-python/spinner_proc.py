import itertools
import time
import math
from multiprocessing import Process, Event
from multiprocessing import synchronize # We need to import this to write a type hint

# Same as in thread
def spin(msg: str, done: synchronize.Event) -> None:
    # Infinite loop: itertools will cycle forever
    for char in itertools.cycle(r'\|/-'): # This is a raw string literal
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

# Intensive CPU function
# This function is coming from here: 
# https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor-example
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

# Call by the main thread. This could be a slow API call over
# the network. Calling sleep blocks the main thread, but releases
# the GIL, allowing other Python threads to run
# 
def slow() -> int:
    #time.sleep(3)
    res = is_prime(5_000_111_000_222_021)
    return f"Done!, {res}"

def supervisor():
    done = Event()
    spinner = Process(target=spin, args=('Procssing!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

def main():
    result = supervisor()
    print(f'Answer {result}')

if __name__ == '__main__':
    main()

"""
The above code shows something important: The multiprocessing library
simulates the threading API, making it easy to convert programs from
threads to processes

Remember that this example spawns processes, in contrast to threads
as in the script spinner_thread.py: When we create a new Process here,
a whole new Python interpreter is started as a child process in the
background. Since each python process has its own GIL, this allows
a program to use all available CPU cores
"""
