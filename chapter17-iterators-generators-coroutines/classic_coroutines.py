from collections.abc import Generator
from typing import TypeAlias, NamedTuple

def averager() -> Generator[float, float, None]:
    total = 0
    sum = 0.0
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

"""
The .close() method raises GeneratorExit at the suspended yield expression.
If not handled in the coroutine function, the exception terminates it.
GeneratorExit is caught by the generator object that wraps the coroutine,
that's why we don't see it
"""
coro_avg.close()

try: 
    print(coro_avg.send(17))
except Exception as e:
    print("Exception raised ", type(e))


"""
Second averager example: Instead of returning partial results, return a
complete result after receiveing multiple numbers
"""

class Result(NamedTuple):
    """
    We need to type ignore this field because NamedTuple is a subclass of
    tuple, and tuple implements method count, which counts the number of
    repetitions of the argument in the tuple
    """
    count: int # type: ignore
    average: float

class Sentinel:
    def __repr__(self):
        return "Sentinel()"


FloatsOrStop: TypeAlias = float | Sentinel

# Remember Generator nomenclature: Generator[YieldType, ReceiverType, ReturnType]
def averager2() -> Generator[None, FloatsOrStop, Result]:
    total = 0
    sum = 0.0
    average = 0.0
    while True:
        term = yield
        if isinstance(term, Sentinel):
            break

        sum += term
        total += 1
        average = sum / total
    return Result(total, average)


avg2 = averager2()
# Priming the averager
next(avg2)

for i in range(10):
    # Now the yield type is None
    print(avg2.send(i))

# Until we don't send the sentinel, we don't get the average
try:
    avg2.send(Sentinel())
except StopIteration as e:
    res = e.value

print("Res was ", res)
# A this point the averager2 has returned, which means that
# we cannot send more values to the coroutine

try:
    avg2.send(10)
except Exception as e:
    print("Exception raised when sending 10: ", type(e))


"""
Note that if we call close on a coroutine object produced by
averager2 it won't return a result. This is bc when calling close(),
GeneratorExit exception is raised at the yield line in the coroutine
"""

testing_coroutine = averager2()
next(testing_coroutine)
print(testing_coroutine.send(10))
print(testing_coroutine.send(11))

# Doesn't return an average
print(testing_coroutine.close())


"""
If we want to directly read the value returned by a coroutine, we can
use yield from like follows:
"""

def compute_avg():
    avg = averager2()
    res = yield from avg
    return res

compute_gen = compute_avg()
for i in [None, 1, 2, 3, 4, 5, Sentinel()]:
    try:
        compute_gen.send(i)
    except StopIteration as e:
        res = e.value

print("Avg is: ", res)
