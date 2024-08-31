vec1 = Vector(range(2, 5))

"""
Even though we have defined addition to only support another vector,
because these checks only are for the type checker, we can safely
add a tuple to our vector in runtime without any issue

Update: We have updated the function to stop this behaviour by
checking in runtime the type of the argument
"""

try: 
    print(vec1 + (2, 3))
except Exception as e:
    print(e)

"""
However, we cannot add our vector to a tuple
"""

try: 
    print((2, 3) + vec1)
except Exception as e:
    print(e)

"""
One of the reasons why I don't like for this particular case
to enable vectors to be added against other types (it's weird that I can
add a tuple to a vector, but not otherwise from a user point of view).
A better implementation would be to add a runtime check to see if
the instance got by argument is a vector. Let's do this
by monkey patching our vector class
"""

def new_add(self, another):
    import itertools
    if not isinstance(another, Vector):
        raise TypeError(f"Vectors can only be added to other vectors. Received {another} which is {another.__class__}")
    pairs = itertools.zip_longest(self, another, fillvalue=0)
    return Vector(a + b for a, b in pairs)

Vector.__add__ = new_add

vec2 = Vector(range(2, 5))

try:
    print(vec1 + (2, 3))
except TypeError as e:
    print(e)


"""
What if I want to add this Vector against the Vector2D implemented in chapter 11?

We need to implement __radd__ (reverse add) special method in vector to do so
"""

"""
What if we sum to vector a non-iterable element?
"""

vec2 + 1
