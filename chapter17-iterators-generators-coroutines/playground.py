from random import randint

def roll_dice():
    return randint(1, 6)

"""
When you provide a second argument
to iter, this acts as a sentinel: When
the value is return by __next__, the
iterator stops. More info can be found
here: https://docs.python.org/3.10/library/functions.html#iter
"""
myiter = iter(roll_dice, 1)

for num in myiter:
    print(num)


"""
Notice that this iterator is of type callable_iterator
"""
print(type(myiter))


"""
Important note: Python obtains iterators from iterables (that's the relationship
between iterators and iterables)
"""


"""
When we do a for loop like this
"""

for letter in "Andres":
    print(letter)


"""
What is actually happening underneath is:
"""

print("The reality behind the Matrix")
s = "Andres"
myiter = iter(s)
while True:
    try:
        print(next(myiter))
    except StopIteration:
        del myiter
        break


"""
Difference between using a generator expression
in a list (eager evaluation) vs a tuple (lazy
evaluation)
"""

def gen_names():
    print("First")
    yield "Andres"
    print("Second")
    yield "Juan"
    print("That's it")

# In this example, you get 3 prints right away
# This is because the list comprehesion eagerly iterates
# over the items yielded by the generator
mylist = [name for name in gen_names()] 

print(mylist)

mytuple = (name for name in gen_names())

# In this second example, no print was executed
# and we get a generator object instead
print(mytuple)

for name in mytuple:
    print(name)


"""
Filtering generator functions
"""

def vowel(c):
    return c.lower() in 'aeiou'

mystr = 'Abra cadabra, hehe'
list(filter(vowel, 'Abra cadabra, hehe'))

"""
Drop while the predicate is truthy. Once it get's falsy, stop
checking and return everything
"""
list(itertools.dropwhile(vowel, 'Aaaabra cadabra, hehe'))


"""
compress(it, selector_it)
Consumes two iterables in parallel; yields items from it
whenever the corresponding item in selector_it is truthy
"""
list(itertools.compress('AbraCadabra', (0, 1, 1, 0, 1, 1, 1, 0, 0)))



"""
Mapping generator functions
"""

sample = [1, 2, 3, 0, 4, 1, 2, 8, 5, 3, 9 , -2, 9, 3]

"""
accummulate(it, [func]) -> yields accumulated sums; if func is provided,
yields the result of applying it to the first pair of items, then to the
second, and so on
"""

list(itertools.accumulate(sample))

list(itertools.accumulate(sample, min))

"""
So we can get the min of a list in python by doing this
"""

for min in itertools.accumulate(sample, min):
    print("Min so far ", min)


"""
Calculating a product of all elements in a list would be
"""
from operator import mul

list(itertools.accumulate(sample, mul))

names = ["Andres", "Gabriela", "Amelia", "Jorge"]

for idx, val in enumerate(names, start=3):
    print(idx, val)


"""
map returns a generator. As argument, it can take N iterables and
the function must take the same amount of iterables provided by argument
"""

lastnames = ["Lastname1", "Lastname2", "Lastname3"]

for full_name in map(operator.add, names, lastnames):
    print(full_name)


"""
Repeat each letter in the word according to its place in it
"""
list(itertools.starmap(operator.mul, enumerate('andres', 1)))
# 'a' * 1, 'n' * 2, 'd' * 3

"""
Concatenating 2 lists of strings 
"""
list(itertools.starmap(operator.add, zip(names, lastnames)))

"""
Difference between starmap and map: Map provides a unique argument to
the function, while starmap is equal of doing func(*args) where *args
represent an object that can be destructured
"""
# This doesn't work
# list(map(operator.mul, enumerate('andres', 1)))
