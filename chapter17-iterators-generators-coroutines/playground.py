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
