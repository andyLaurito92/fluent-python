from random import randint

def roll_dice():
    return randint(1, 6)

# When you provide a second argument
# to iter, this acts as a sentinel: When
# the value is return by __next__, the
# iterator stops
myiter = iter(roll_dice, 1)

for num in myiter:
    print(num)


"""
Notice that this iterator is of type callable_iterator
"""
print(type(myiter))
