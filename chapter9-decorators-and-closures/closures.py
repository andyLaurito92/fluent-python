from typing import Callable
"""
Closures are functions with an extended scope that encompasses nonglobal variables
referenced in the body of the function but not defined there.

Let's see an example of a closure by defining an averager: a higher-order function
that returns a function that computes the average of all arguments passed to it
accumulative

Let's see first the OOP way of doing it
"""

class Averager:
    def __init__(self):
       self.series = []

    def __call__(self, value):
        self.series.append(value)
        total = sum(self.series)
        return total / len(self.series)

avg = Averager()

print(avg(10))
print(avg(11))
print(avg(12))


"""
In contrast, the functional way of doing it is by using a closure
"""

def make_averager():
    series = []

    def averager(value):
        series.append(value)
        total = sum(series)
        return total / len(series)

    return averager

avg_fun = make_averager()
print(avg_fun(10))
print(avg_fun(11))
print(avg_fun(12))


"""
In the above example, series is a free variable of the closure. This means a variable
that is not bound in the local scope. 
"""

print(avg_fun.__code__.co_varnames) # local variables

print(avg_fun.__code__.co_freevars) # free variables

print(avg_fun.__closure__) # the cells of the free variables

avg_fun.__closure__[0].cell_contents



"""
Making make_averager more efficient
"""
def make_averager2() -> Callable[[float], float]:
    count: float = 0
    total: float = 0

    def averager(value: float) -> float:
        nonlocal count, total
        count += 1
        total += value
        return total / count

    return averager

avg_fun2 = make_averager2()
print(avg_fun2(10))
print(avg_fun2(11))
print(avg_fun2(12))


"""
Defining a decorator to measure amount of time it takes
a function to run
"""
def time(fun:Callable) -> Callable:
    def timer(*args):
        import time
        start = time.time()
        result = fun(*args)
        end = time.time()
        fun_name = fun.__name__
        args_str = ', '.join(str(arg) for arg in args)
        print(f"Elapsed time for {fun_name}({args_str}): {end - start} ms")
        return result
    return timer

@time
def waste_some_time(num:int) -> int:
    return sum(range(num))

print(waste_some_time(1000000))


"""
Notice how the above function, waste_some time
was actually replaced by timer

This is bc usually when we call a decorator, such as above, what
it actually happends under the hood is this:

@decorator
def my_fun(args):
    ... something ...

def my_fun(args):
    ... something ...

my_fun = decorator(my_fun)

Where decorator returns a decorated function
"""

print(f"waste_some_time function name: {waste_some_time.__name__}")
