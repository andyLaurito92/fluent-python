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
"""
