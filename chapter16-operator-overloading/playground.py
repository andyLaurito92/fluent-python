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

try: 
    vec2 + 1
except Exception as e:
    print(e)


"""
Augmented operators:

By default, when you do a += b, this equals to a = a + b if
the __iadd__ is not implemented. In other words, the a += b
is just syntaxis sugar.
It's important to understand this because you're creating a new
object if the object doesn't implement in-place operations
"""

vec1 = Vector(1, 2, 3)
print(vec1)
print(id(vec1))

vec1 += Vector([1] * 3)

print(vec1)
print(id(vec1))


"""
Example of an in-place addition method for Vector:

Note: This is a bad practice and I'm doing it just for the sake
of showing how it should be implemented. In practice, our Vector
class should be immutable and shouldn't allow the in-place infix
operands.

Notice that inplace operators should return self and we are more
relax with the type of the argument receieved (in contrast with
common addition, where we do enforce the other argument to be of
the same type of the instance)
"""
def inplace_addition(self, other):
    from typing import Iterable
    """
    Because this is a in-place addition, we only care
    about other being iterable
    """
    self._elements.extend(other)
    return self
    

Vector.__iadd__ = inplace_addition



print(f"Before extending {vec1}")
vec1 += (2, 4)
print(f"After extending {vec1}")
