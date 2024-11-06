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

print(mya.x)

print(mya.y)


"""
How does the above example works?
"""
