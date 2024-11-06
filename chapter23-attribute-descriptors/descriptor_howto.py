"""
Studying the howto descriptor of python docs
"""

"""
Remember that a descriptor is a class that implements some of the following methods:

__get__, __set__, __delete__
"""

class Ten:
    def __get__(self, obj, objtype=None):
        return 10


class A:
    x = 5
    y = Ten()


mya = A()

print(mya.x) # Here, the lookup finds the value of x in __dic__

# Here, the dot operator finds a descriptor instance, recognized by its
# __get__ method.
print(mya.y)

# Note: The value 10 is not stored in neither the class dictionary nor
# the instance dictionary

print(vars(mya))

print(vars(A))

del mya

print(vars(A))


"""
How does the above example works?
"""


