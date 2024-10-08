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



"""
Given that we always need to prime a coroutine to make it work,
we could build a decorator for this:
"""

from functools import wraps

"""
Note: The original decorator from the fluentpython webpage doesn't stores the
result of next because it assumes that it's None (and for the case being used,
this is true :) ) I'm storing the result of next and returning a tuple to make
this decorator more generic and to remember and important concept: When next()
is called in a coroutine object, this call makes the generator run until the
first yield expression. This expression MIGHT OR MIGHT NOT yield a value. If it
doesn't, then res will be None. If it does, res will have that value and won't
get lost
"""

def coroutine(func):
    """
    Decorator to prime a coroutine. This decorator expects the generator factory
    and returns a generator factory that primes the gnerator objects created
    """
    @wraps(func)
    def prime(*args, **kwargs):
        my_coroutine = func(*args, **kwargs)
        # we prime the coroutine
        res = next(my_coroutine)
        return (my_coroutine, res)
    return prime

@coroutine
def coroutine_decorated(sht: str) -> Generator[str, str, None]:
    print("Hey ", sht)
    val = yield sht + ", ho"
    print("Received ", val)
    last_val = yield val + sht
    print("Last val: ", last_val, " finishing now.")
    

co, res = coroutine_decorated("ho")

inspect.getgeneratorstate(co)


"""
Note: When using yield from, the expression automatically primes the coroutine called
by it, making the above decorator incompatible with the yield from expression
"""

"""
Unhandled exceptions in a coroutine are propagated to the caller of next()|send(val)
"""

try: 
    co.send(10)
except Exception as e:
    # Exception raised in the coroutine and propagated here
    print(e)

"""
After raising the exception, the coroutine exites and it's state becomes GEN_CLOSED
"""
inspect.getgeneratorstate(co)


"""
The above suggests that sentinels are a good way for terminating a coroutine. An
example of a sentinel could be StopIteration class itself
"""

co, res = coroutine_decorated("hello")

try:
    co.send(StopIteration)
except Exception as e:
    print("Coroutine terminated ", inspect.getgeneratorstate(co))


"""
Using throws method of coroutines
"""

@coroutine
def coroutine_with_exception():
    try:
        a = yield
        b = yield a + 10
        yield a + b
    except TypeError as e:
        print("A type error was raised, handling it")
        c = yield 30
        print("Finishing normally, last value was ", c)

print("Testing coroutine throw method")
myco, res = coroutine_with_exception()
print(myco.send(2), 12)
myco.throw(TypeError)
try:
    myco.send(30)
except StopIteration as e:
    print("Finished normally")

myco, res = coroutine_with_exception()

print("Closing my coroutine normally by using close")
print("No StopIteration is raised here")
myco.send(10)
myco.close()

class MyException(Exception):
    """ This is my exception """

"""
Remember that calling close() to a coroutine causes the yield expression
where the generator was paused to raise a GeneratorExit exception.
No error is reported to the caller if the generator does not handle that
exception or raises StopIteration
"""

print("==== Another example ======")
@coroutine
def demo_exec_handling():
    print("Starting")
    """
    This is the only way of running always a piece of code inside a coroutine
    before it gets terminated
    """
    try:
        while True:
            try:
                x = yield
            except MyException as e:
                print("Got my exception, but I don't care :D")
            except GeneratorExit as final:
                # Case when the caller calls close() method
                print("Got it, I'm stopping!")
                raise final
            else:
                print("No exception recieved, but ", x)
    finally:
        print("I'll just run when the coroutine get's terminated")

myco, res = demo_exec_handling()
myco.send(10)
myco.send("Hello")
myco.throw(MyException)
myco.send(40)
myco.close()


