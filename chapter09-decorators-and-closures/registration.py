"""
A decorator is nothing more than a function that takes another function and
extends its behavior or does sht with it.
"""

from typing import Callable, Any

registry = []

def register(func: Callable) -> Callable:
    print(f"Registering {func}")
    registry.append(func)
    return func

def say_hello(fn: Callable) -> Callable:
    def wrapper() -> Any:
        print("Hello!")
        return fn()
    return wrapper
    
@register
def f1():
    print("Running f1")

@register
def f2():
    print("Running f2")

@say_hello
def f3():
    print("Running f3")

def main():
    print("Running main")
    print("Registry:", registry)
    f1()
    f2()
    f3()

if __name__ == "__main__":
    main()

"""
The above code shows the follwing: The decorator is called when the module is
imported at the definition of the function, while the functions are called
when the module is executed as a script.

You can run it by running it from the console with python registration.py
"""
