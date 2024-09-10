from collections.abc import Generator

def averager() -> Generator[float, float, None]:
    total = 0
    sum = 0
    average = 0.0
    while True:
        term = yield average
        sum += term
        total += 1
        average = sum / total


coro_avg = averager() # We instantiate the coroutine object

"""
PRIMING THE COROUTINE

Priming -> The act of making sht ready

The line that does next(coro_avg) is called "priming the coroutine".
You can prime a coroutine either by calling next or by doing
coro_avg.send(None) (this is what the next() function does), but you can't
send any value other than None. This is bc the coroutine can only accept a
sent value when it's suspended at a yield line.
"""
initial_value = next(coro_avg) # We initialize it
print("Initial value is: ", initial_value)

for i in range(15):
    print(coro_avg.send(i))


"""
Because of how we coded our generator, it will never end. The question that
could come up is: How do we finish our coroutine?

The easy answer is: we don't :). We just let the instante to be garbaged
collected (which will happen when it's reference count reaches 0)

BUT: If you want to terminate it, you can use .close() on the coroutine
"""

print(coro_avg.send(16))
coro_avg.close()

try: 
    print(coro_avg.send(17))
except Exception as e:
    print("Exception raised ", type(e))
