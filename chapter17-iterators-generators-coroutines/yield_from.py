#type: ignore
"""
Introducing yield from syntax, which delegates work to a subgenerator. When delegating work,
the subgen takes over and will yield values to the caller of gen. The caller will in effect
drive subgent directly. Meanwhile gen will be blocked, waiting until subgen terminates.

yield from connects the subgenerator directly to the client code, bypassing the delgating generator. 

To read: https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-yield-from-syntax-in-python-3-3

IMPORTANT NOTE

The newer await keyword is very similar to yield from, however await does not completely replace yield from.
Each of them has its own use cases, and await is more strict about its context and target: await can
only be used inside a native coroutine, and its target must be ana waitable object. In contrast, yield from
can be used in any function (which then becomes a generator), and its target can be any iterable. 
"""
print("Example of a fn that can be written with yield from but not with await")

def example():
    yield from [1, 2, 3]

print(list(example()))

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
    using a bfs algorithm lazily. This approach doesn't take into account
    pretty printing
    """
    classes_to_visit = [BaseException]
    while classes_to_visit:
        myclass = classes_to_visit[0]
        classes_to_visit.remove(myclass)
        classes_to_visit.extend(sorted(myclass.__subclasses__(), key=attrgetter('__name__')))
        yield myclass
    return "All classes visited"

# for exception_class in get_exception_hierarchy_tree():
#     print(exception_class)
        

"""
Second approach: We care about showing identation, for this we can
use yield from for generating the branches of the subclasses
"""

def tree(clss, level=0):
    yield clss, level
    for subclass in clss.__subclasses__():
        """ We generate recursively each branch of the subclasses and yield it's value using yield from """
        yield from tree(subclass, level + 1)

def display(class_generator):
    for cls_name, level in class_generator:
        print(" "*2*level, cls_name)
        
#display(tree(BaseException, 1))
#display(tree(Exception, 1))

"""
Third approach: We care about identation + making the algorithm iterative instead
of recursive for performance purposes
"""

def tree(clss, level=0):
    classes_to_visit = [(clss, level)]
    while classes_to_visit:
        current, level = classes_to_visit[0]
        classes_to_visit = classes_to_visit[1:]
        yield (current, level)

        classes_to_visit = list(zip(current.__subclasses__(), itertools.repeat(level + 1))) + classes_to_visit
    return "Finished"

display(tree(BaseException, 1))


"""
What's doing underneath the "yield from x" expression?

The first thing it does is to to call iter(x) to obtain an iterator from it.

This means that x can be any iterable ! <--- IMPORTANT!

Note something: Because yield from opens a bidirectional channel from
the outermost caller to the innermost subgenerator, exceptions can be
thrown all the way in without adding a lot of exception handling
boilerplate code in the intermediate coroutines!

Let's see the above in an example:
"""

# For logging the last traceback
import traceback

def co_boom():
    print("Will explode everything!")
    yield 3
    raise TypeError("Oops!")

def co_inner():
    print("Running an inner coroutine")
    yield 1
    # delegates to other coroutine
    yield from co_boom()

def co_outer():
    print("I'm visible to the caller")
    yield 30
    yield from co_inner()
    
print("I'm the caller!")
my_co = co_outer()

print("Priming the coroutine")
print("30!, ", next(my_co))
try:
    print("Starting iteration")
    for elem in my_co:
        print(elem)
except Exception as e:
    print("Something happened inside!", e, traceback.format_exc())
