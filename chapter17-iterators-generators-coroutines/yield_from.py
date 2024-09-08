"""
Introducing yield from syntax, which delegates work to a subgenerator
"""

"""
Before yield from
"""
def sub_gen():
    """
     Subgenerator
    """
    yield "hello"
    yield "ciao!"

def gen():
    """
    Gen is the delegating generator
    """
    yield "Starting"
    for val in sub_gen():
        yield val
    yield "Ending"

"""
This represents the client code
"""
for x in gen():
    print(x)
    

"""
Instead of the above, since Python 3.3 you can use yield from
"""

print("\n", "Using yield from", "\n")
def sub_gen():
    yield "hello"
    yield "ciao!"

def gen():
    yield "Starting"
    yield from sub_gen()
    yield "Ending"

for x in gen():
    print(x)


"""
If the subgenerator contains a return statement, it can
be captured with the yield from as part of an expression
"""

print("\n", "Returning a value in the subgenerator", "\n")
def sub_gen():
    yield "hello"
    yield "ciao!"
    return "Finito"

def gen():
    yield "Starting"
    output = yield from sub_gen()
    print(output)
    yield "Ending"

for x in gen():
    print(x)



"""
Example 1 of yield from use: Implementing itertools.chain

Note: Usually itertools are implemented in C, meaning they
are way faster than doing this
"""

def mychain(*iterables):
    """ Without yield from """
    for it in iterables:
        for elem in it:
            yield elem

for elem in mychain([1, 2, 3], 'abc', itertools.repeat(8, times=3)):
    print(elem)
    

"""
In the above example, we could use yield from
"""

def mychain2(*iterables):
    for it in iterables:
        yield from it

for elem in mychain2([1, 2, 3], 'abc', itertools.repeat(8, times=3)):
    print(elem)
    
"""
Using yield from for building base exception hierarchy tree. You can
see the hierarchy here: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
"""

from operator import attrgetter

def get_exception_hierarchy_tree():
    """
    Traverse the exception hierarchy tree of BaseException
    using a bfs algorithm lazily
    """
    classes_to_visit = [BaseException]
    while classes_to_visit:
        myclass = classes_to_visit[0]
        classes_to_visit.remove(myclass)
        classes_to_visit.extend(sorted(myclass.__subclasses__(), key=attrgetter('__name__')))
        yield myclass
    return "All classes visited"

for exception_class in get_exception_hierarchy_tree():
    print(exception_class)
        
