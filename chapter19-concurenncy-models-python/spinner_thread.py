import itertools
import time
from threading import Thread, Event
import math

# This is the function that runs in a separate thread
# done is instance of threading.Event, an object used
# to syncrhonie threads
def spin(msg: str, done: Event) -> None:
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
    return f"Done! was, {res}"


def supervisor():
    done = Event() # This is the object that coordinates the threads
    spinner = Thread(target=spin, args=('Processing!', done))

    """
    The output is <Thread(Thread-1 (spin), initial)> , where initial
    is the state of the thread - meaning not started yet
    """
    print(f'spinner object: {spinner}')
    spinner.start()

    # This blocks the main thread and release the GIL
    # Meanwhile, the spinner thread will be running
    result = slow()

    # Sets the internal flag to true, which will terminate the for
    # loop inside the spin function
    done.set()

    # Wait until spinner thread finishes
    spinner.join()
    return result

def main():
    result = supervisor()
    print(f'Answer {result}')


if __name__ == '__main__':
    main()
