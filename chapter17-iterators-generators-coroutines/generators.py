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
