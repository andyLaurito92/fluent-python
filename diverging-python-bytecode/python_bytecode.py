"""
Python is both an interpreter and compile language in the sense that we work with
Python interpreter, but underneath python converts our functions into bytecode.
This bytecode is the code you can find in directory __pycache__

But: How does python bytecode look like? We can use module dis to answer this question
"""

import dis


def fib(n: int) -> int:
    """ Only positive integers"""
    if n  < 2:
        return n
    current, next = 0, 1
    while (n != 0):
        current, next = next, current + next
        n -= 1
    return current


"""
The below line prints python bytecode that is executed in Cpython

Cpython is a stack-oriented VM, having 2 stack: 1 for evaluation and
another one for block stack, which tracks how many "blocks" (loops,
try/except/with, etc.) are active.
"""

dis.dis(fib)

"""
Way more information here: https://docs.python.org/3/library/dis.html
"""

"""
One cool thing we can do: We can dissasemble a code that failed
by calling dis.distb()
"""

#1/0

dis.distb()


"""
dis.distb dissasembles a callback. For our previous example,
calling the above function returns python bytecode with a pointer 
explicitly showing which was the line that cause the exception
"""


"""
What can we learn from dissasembly? We can understand how to make
our code faster :)
"""


def low_function():
    SECONDS_PER_DAY = 86400
    return SECONDS_PER_DAY * 7


def fast_week():
    return 86400 * 7

"""
Why the first function is slower than the second one? Let's
see how python compiles both functions :)
"""

print("="*20)
print("Seeing bytecode of example functions")
print("="*20)

print("slow function")
dis.dis(low_function)

print("fast function")
dis.dis(fast_week)

"""
What we can see from the bytecode above, is that the first function,
the slower one, has more bytecode operations than the faster one.

Interesting facts:
1- In the first function:
A- we first need to load the constant, store it in variable
B- we then read it from the variable and use it

2- While in the second function python directly loads the result of the
multiplication. This is because the compiler already figures it out that
those constant won't change, so it directly stores the result as a constant


Last but not least, interesting book to understand more about the python virtual machine: https://leanpub.com/insidethepythonvirtualmachine/read
"""
