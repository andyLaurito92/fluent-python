"""
In python we have class weakref for creating objects that don't increase the counter of references. This is useful for creating caches, because you don't want the cache object to be kept in memory if it's not being used.

More info:http://pymotw.com/3/weakref/ 
"""


# Documentation of this class can be found here: https://docs.python.org/3/library/weakref.html
import weakref

a_list = {1, 2, 3}

# Create a weak reference to the list
a_weakref = weakref.ref(a_list)

print(a_weakref)

# Get the object from the weak reference
print(a_weakref())

# Delete the list

del a_list

"""
The object is still available through the weak reference. This is because it's bound to
variable _ from the interactive shell
"""

print(a_weakref()) # We bind the object to the variable _, unreferencing our set

# The object is no longer available
print(a_weakref() is None)


"""
Usually instead of directly interacting with this class, we sill be using the
WeakKeyDictionary and WeakValueDictionary classes.
"""

# Example of using WeakKeyDictionary

class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return f'Cheese({self.kind})'
    
stock = weakref.WeakKeyDictionary()

catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese] = cheese.kind

print(sorted(stock.keys(), key=lambda x: x.kind))

del catalog

print("After deleting the catalog, the stock is: ")
print(sorted(stock.keys(), key=lambda x: x.kind))
print("Again, be aware that it's not empty yet bc the last object is still bound to _ in the interactive shell")

"""
Example of using WeakValueDictionary. Same concept than before, but this time
applies for the values instead of the keys
"""
stock = weakref.WeakValueDictionary()
my_favourite_cheese = Cheese('Red Leicester')
stock['Red Leicester'] = my_favourite_cheese

print("Using weak value dictionary")
print(list(stock.keys()))

del my_favourite_cheese

print(list(stock.keys()))


"""
Another collection: WeakSet. It's a set that holds weak references to its elements.
"""

class Subject:
    # If instead of a WeakSet we use a normal set, the instances will never be deleted
    instances = weakref.WeakSet()

    @classmethod
    def count(cls):
        return len(cls.instances)

    def __init__(self, name):
        self.name = name
        self.instances.add(self)

    def __repr__(self):
        return f'Subject({self.name})'


print("Using WeakSet to count the number of instances of a class")

s1 = Subject('Math')
s2 = Subject('History')
s3 = Subject('Physics')

print(f"Number of subjects: {Subject.count()}")

print("Deleting math subject")

del s1

print(f"Number of subjects: {Subject.count()}")


"""
Not every python object can be weakly referenced. For example, integers, strings,
lists and dictionaries can't be weakly referenced.

To understand why, see the documentation and https://docs.python.org/3/extending/newtypes.html#weakref-support
"""
