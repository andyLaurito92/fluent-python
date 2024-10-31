"""
Useful class for defining things in an attribute manner
"""

class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)


# Example of usage
sht = Bunch(x=3, y="hola que tal", z=[1, 2, 3])
sht.z

# This can be really useful when treating with JSONs!
