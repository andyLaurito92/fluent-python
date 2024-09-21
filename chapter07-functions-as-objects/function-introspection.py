"""
Personal studies from https://www.fluentpython.com/extra/function-introspection/
"""

"""
Functions are first-class objects in Python, let's see what that means :)
"""

def my_function(a, b):
    """ My function sums two numbers """
    return a + b

print("Methods of my_function:")
dir(my_function)

print("We can define attributes to functions:")
my_function.category = "math"
print(my_function.category)

"""
The above is used in djano here: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#the-display-decorator
"""

print("Getting the docstring of my_function:")
print(my_function.__doc__)
print("The above is used in the help function:")
help(my_function)


"""
Let's see those methods that are only available to functions
"""

class C: pass
obj = C()

print(f"Methods only available in functions: {set(dir(my_function)) - set(dir(obj))}")

def my_function_with_defaults(a, b=42, c=[]):
    my_local_var = "something"
    return a + b

print(f"Default arguments for positional arguments of the function as a tuple: {my_function_with_defaults.__defaults__}")


print(f"Default values for keyword-only arguments: {my_function_with_defaults.__kwdefaults__}")


print(f"Vriable names of the function as a tuple: {my_function_with_defaults.__code__.co_varnames}")

print(f"Count of argument variables: {my_function_with_defaults.__code__.co_argcount}")

## With co_argcount we know that the first co_argcount variables are positional arguments, the rest are local variables

"""
Getting which default value corresponds to which argument is super ugly by using the above. Luckily we have the inspect module
"""

import inspect

sig = inspect.signature(my_function_with_defaults)
print(f"Signature of function: {sig}")

for name, param in sig.parameters.items():
    print(param.kind, ":", name, "=", param.default)

"""
inspect._empty stands for no default value
"""

"""
We can bind the signature of a function to a dictionary of arguments
"""

args = {
    'a': 1,
    'b': 2
}

bound_args = sig.bind(**args)
print(bound_args)
