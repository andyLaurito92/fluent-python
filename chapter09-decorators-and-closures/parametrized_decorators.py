"""
How do you make a decorator to take arguments? You need to create a
decorator factory

Let's see an example:
"""

from typing import Callable
from collections import abc

registry = []

def register(fun: Callable) -> Callable:
    print(f"Registering {fun}")
    registry.append(fun)
    return fun


@register
def f1():
    print("Running f1")

"""
What if we want register functions given a boolean value?
We can do the following:
"""

# Register is now a decorator factory
def register(is_active:bool):
    def decorator(fun: Callable) -> Callable:
        if is_active:
            print(f"Registering {fun}")
            registry.append(fun)
        return fun
    return decorator

@register(True)
def f2():
    print("Running f2")

@register(False)
def f3():
    print("Running f3")

f1()
f2()
f3()

"""
The above is the same as the following:
"""

def f4():
    print("Running f4")

f4 = register(True)(f4)

"""
We can build complex decorators using classes. Let's see the following example
where we create a class for doing session injection into a function :)

In the below example, we use the method __call__ studied in chapter 7,
functions as objects, in particular in script callable_objects.py
"""

class get_session:
    def __init__(self, user: str, password: str) -> None: 
        self.user = user
        self.password = password
        self.is_valid = self.login(user, password)
        if self.is_valid:
            self.session = {"token": "12345"}

    def login(self, user: str, paswword: str) -> bool:
        return True

    def __call__(self, func: Callable) -> Callable:
        def decorator(*args, **kwargs):
            print(f"Injecting session {self.session}")
            kwargs.update({"session": self.session})
            return func(args, kwargs)
        return decorator


@get_session(user="myuser", password="1234")
def list_options(names: abc.Sequence, session=None) -> None:
    print(f"Session injected is {session}, with names: {names}")


list_options(["shoes", "trousers"])
