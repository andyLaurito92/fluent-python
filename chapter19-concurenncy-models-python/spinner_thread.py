import itertools
import time
from threading import Thread, Event

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

# Call by the main thread. This could be a slow API call over
# the network. Calling sleep blocks the main thread, but releases
# the GIL, allowing other Python threads to run
# 
def slow() -> int:
    time.sleep(3)
    return "Done!"


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
