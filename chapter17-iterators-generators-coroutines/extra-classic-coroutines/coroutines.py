from typing import Generator
"""
The exercises of this script come from https://www.fluentpython.com/extra/classic-coroutines/

Why does it make sense to study classic coroutines when you have native coroutines (asyncio lib) nowadays in Python?
This is the why by Guido van Rossum:

[...] Understanding coroutines as they were first implemented in Python 3.4, using pre-existing language facilities, is the foundation to tackle Python 3.5’s native coroutines.
"""

"""
A Python coroutine is essentially a generator driven by calls to its .send() method.
In a coroutine, "to yield" means to give away - to hand control to some other part
of the program and wait until notified to resume

Coroutines are usually data consumers VS Generators are usually data producers

Difference between generator and coroutine:
1. In a coroutine, the yield expression usually is in the right side of the expression (awaits for a value)
2. A coroutine may not produce any value (example of averager2)
"""

def naive_coroutine():
    print("Starting my coroutine")
    name = yield # This is equivalent to name = yield None
    print(f"Hello {name}!, What's your last name?")
    lastname = yield
    print(f"Good to know you {name} {lastname}, see you soon!")

my_coroutine = naive_coroutine()
# Shows the generator object
print(my_coroutine)

# Priming the coroutine
next(my_coroutine)

# Our coroutine doesn't produce any value
try:
    # Printing output of first send just to show that
    # it returns None, bc yield w/nothing is equivalent
    # to yield None
    print(my_coroutine.send("Andres"))
    my_coroutine.send("Laurito")
except StopIteration as e:
    print("Coroutine finished")


"""
We can inspect the state of a coroutine using inspect.getgeneratorstate()

There are 4 states:

1 - GEN_CREATED -> waiting to start execution
2 - GEN_RUNNING -> currently being executed by the interpreter (only makes sense when having multiple threads)
3 - GEN_SUSPENDED -> waiting in a yield expression
4 - GEN-CLOSED -> execution completed
"""
import inspect
# GEN_CLOSED
print(inspect.getgeneratorstate(my_coroutine))

my_coroutine = naive_coroutine()

#GEN_CREATED
print(inspect.getgeneratorstate(my_coroutine))

next(my_coroutine)
#GEN_SUSPENDED
inspect.getgeneratorstate(my_coroutine)

# empty dict {}
inspect.getgeneratorlocals(my_coroutine)

my_coroutine.send("Gabriel")

# {'name': 'Gabriel'}
gen_locals = inspect.getgeneratorlocals(my_coroutine)
type(gen_locals)


my_coroutine = naive_coroutine()

"""
If you try to send a non-None value to a coroutine in GEN_CREATED
you get:
"""

try:
    my_coroutine.send("hello")
except Exception as e:
    print(type(e), e)


def another_coroutine(received: int) -> Generator[int, int, None]:
    print("This is ", received)
    first = yield received + 10
    print("first value is  ", first)
    second = yield first + received 
    print("Last one is ", second)
    

second_coroutine = another_coroutine(11)
# priming coroutine
first_yielded_value = next(second_coroutine)

second_yielded_value = second_coroutine.send(4)

try: 
    second_coroutine.send(8)
except StopIteration as e:
    print(first_yielded_value, second_yielded_value)

