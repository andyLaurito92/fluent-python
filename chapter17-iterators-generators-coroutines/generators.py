def gen_123():
    yield 1
    yield 2
    yield 3

print(gen_123)

"""
This returns a generator object
"""
my_generator = gen_123()

print(my_generator)

for elem in gen_123():
    print(elem)

print("doing it again")

for elem in gen_123():
    print("1. Printing elem: ", elem)

for elem in my_generator:
    print("2. Printing elem: ",elem)


"""
Be aware that in the following loop, instead of raising an exception
we got a generator that returns nothing!
"""

for elem in my_generator:
   print("3. Printing elem: ", elem)


"""

Something to take into account: generators are much slower
than list comprehensions because they have to call several
times a function, while a list comprehension just calls the
function once.

If you don't have a memory limit with the data you're managing,
list comprehensions are probably a better suit for your case. If
memory is a concern and CPU is not, then generator expressions
is the right choise
"""

import cProfile

print("List comprehension")
cProfile.run('sum([i * 2 for i in range(10000)])')


print("Generator expression")
cProfile.run('sum(i * 2 for i in range(10000))')

"""
In the profile above, take a look at the number of calls each expression does

The generator expression performs 10005 calls vs only 5 function calls with the
list comprehension
"""
