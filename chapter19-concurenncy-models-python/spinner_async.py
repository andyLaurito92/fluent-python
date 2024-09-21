import asyncio
import itertools
import time

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

async def slow() -> int:
    await asyncio.sleep(3)

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
