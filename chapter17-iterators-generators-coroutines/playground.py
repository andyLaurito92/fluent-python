from random import randint
import itertools
import operator

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
=============================================
Filtering generator functions
=============================================
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
=============================================
Mapping generator functions
=============================================
"""
sample = [1, 2, 3, 0, 4, 1, 2, 8, 5, 3, 9 , -2, 9, 3]

"""
accummulate(it, [func]) -> yields accumulated sums; if func is provided,
yields the result of applying it to the first pair of items, then to the
second, and so on
"""

list(itertools.accumulate(sample))

#list(itertools.accumulate(sample, min))

"""
So we can get the min of a list in python by doing this
"""

for mymin in itertools.accumulate(sample, min):
    print("Min so far ", mymin)


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

# If we want to re-write the above using map, we should do sht like this:
# list(map(lambda x: x[0] * x[1], enumerate('andres', 1)))

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


"""
Calculating avg on a list of numbers
"""

sample = [3, 8, 2, 1, 10, 5]

list(itertools.starmap(lambda a, b: b / a,
                       enumerate(itertools.accumulate(sample), 1)))


"""
=============================================
Merge generators

Note: chain and chain.from_iterable consume
the input iterables sequentially, while
product, zip, and zip_longest consume the
input iterables in parallel
=============================================
"""

"""
chain -> yields all items from it1, then from it2, etc
"""
list(itertools.chain('ABC', range(2)))
list(itertools.chain(enumerate('ABC')))


"""
itertools.chain.from_iterable -> yields all items from
each iterable produced by it, one after the other, seamlessly
"""
list(itertools.chain.from_iterable(enumerate('ABC')))

"""
Cartesian product between iterables built LAZILY
"""
list(itertools.product([1, 3, 5, 2], range(5), 'Andres'))


"""
=============================================
Generator functions that expand each input into
multiple output items
=============================================
"""

"""
itertools.count -> We saw it in arithmetic progression, it
returns a generator of infinite count
"""

mycount = itertools.count()
for i in mycount:
    if i > 12:
        break
    print(i)

"""
itertools.cycle -> yields items from it, storing a copy of each,
then yields the entire sequence repeatedly, indefinitely
"""
idx = 0
for elem in itertools.cycle('ABC'):
    print(elem)
    idx += 1
    if idx > 10:
        break


"""
Mixing the above generators with islice
"""

list(itertools.islice(itertools.count(1, .3), 3))

list(itertools.islice(itertools.cycle('ABC'), 7))


"""
itertools.pairwise -> for each item in the input, pairwise
yields a 2-tuple with that item and the next -if there is a next
item. Available in Python3.10 >
"""

list(itertools.pairwise(range(10)))

"""
itertools.repeat --> repeat an element infinitely
"""

list(itertools.islice(itertools.repeat(9), 10)) # Faster to do [9] * 10

# Repeat can be limited by passing the times argument
list(itertools.repeat(9, 4))

"""
Common use of repeat: To use it for fixing a value with map
"""

list(map(operator.mul, [1, 3, 5, 6, 8], itertools.repeat(4)))



"""
=============================================
Combinatorics generators, see documentation
https://docs.python.org/3/library/itertools.html
=============================================
"""

list(itertools.combinations('ABC', 2))

list(itertools.combinations_with_replacement('ABC', 2))

list(itertools.permutations('ABC', 2))

list(itertools.product('ABC', repeat=2))

"""
=============================================
Rearranging generator functions
=============================================
"""

"""
itertools.groupby(it, key=None) -> yields 2 tuples
of the form (key, group), where key is the grouping
criterio and group is a generator yielding the items
in the group

Note: itertools.groupby assumes that the input iterable
is sorted by the grouping criterion, or at least that
the items are clustered by that criterion - even if not
completely sorted
"""

for val, group in itertools.groupby('LLLLAAAAGGGGG'):
    print(val, " -> ", len(list(group)))

"""
Group words by their len. Note that we need to sort first
the names, otherwise we can get multiple groups of unique
length
"""

names = ['Andres', 'Gabriela', 'Jorge', 'Ramon', 'Aldana']
names.sort(key=len)
for val, group in itertools.groupby(names, key=len):
    print(val, " -> ", list(group))


"""
reversed -> only works for sequences
"""

for name in reversed(names):
    print(name)


"""
itertools.tee(it, n=2) -> yields a tuple of n generators, each
yielding the items of the input iterable independently
"""

"""
Build a tuple which contains each element in the iterable
"""
list(zip(*itertools.tee('ABC')))



"""
=============================================
Reducing generator functions
=============================================
"""
