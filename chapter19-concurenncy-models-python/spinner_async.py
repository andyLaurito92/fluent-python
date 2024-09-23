import asyncio
import itertools
import time
import math

async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

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
        # If we want to make is_prime a native coroutine,
        # we could implement the following:
        # if n % 100_000 == 0: # After 50.000 iterations
        #    await asyncio.sleep(.5)
        # The above will make the is_prime function to give
        # back control to the event loop, but it will also cause
        # the function to be more slow
    return True

async def slow() -> int:
    is_prime(5_000_111_000_222_021)
    #await asyncio.sleep(3)

    # If you uncomment the below line, and comment the above line
    # (await asyncio.sleep) you won't see any processing message at all!
    # Why? Because coroutines are cooperative, and this coroutine
    # won't be cooperative with the others on releasing control!

    #time.sleep(3)
    return 42

def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')

async def supervisor() -> int:
    spinner = asyncio.create_task(spin('Processing!'))
    print(f'spinner object: {spinner}')
    result = await slow()
    spinner.cancel()
    return result

if __name__ == '__main__':
    main()
