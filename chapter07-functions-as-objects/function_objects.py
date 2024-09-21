from functools import reduce
"""
Functions are objects, let's see why
"""

def bubble_sort(arr):
    """ Applies bubble sort in the given array sorting in ascending order. Note
    that the array will be modified by this function"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


myarray = [3, 7, 9, 1, 0, -3]
bubble_sort(myarray)
print(myarray)

print("Getting the docstring of bubble_sort:")
print(bubble_sort.__doc__)

print("__doc__ is used in the help function:")
help(bubble_sort)

array_of_arrays = [
    [3, 7, 9, 1, 0, -3],
    [3, 7, 9, 1, 0, -3, 10],
    [3, 7, 9, 1, 0, -3, 10, 1],
    [3, 7, 9, 1, 0, -3, 10, 1, 4],
    [3, 7, 9, 1, 0, -3, 10, 1, 4, 2],
    ]

def sum_all(arr):
    sum = 0
    for elem in arr:
        sum += elem
    return sum

"""
In Python 3, map and filter return generators.
"""
map_object = map(sum_all, array_of_arrays)

# See how map is actually an object!
help(map_object)

for sums in map_object:
    print(sums)


def times_3(val):
    return val * 3

numbers = [1, 2, 3, 4, 5]

"""
With map and filter
"""
print(list(map(times_3, numbers)))
print(list(filter(lambda x: x % 2 == 0, numbers)))

"""
With list comprehension
"""

print([times_3(x) for x in numbers])
print([x for x in numbers if x % 2 == 0])


"""
Actually, given that map and filter return generators, the proper way
of doing the above would be:
"""

multiplied_by_3 = (times_3(x) for x in numbers)
for initial, by3 in zip(numbers, multiplied_by_3):
    print(f"Initial was: {initial}, by 3 is: {by3}")

print("Defiining my substract function")
substraction = lambda x, y: x - y 
print(substraction(3, 2))

print(f"Applying reduce: {reduce(substraction, [1, 2, 3, 4, 5], -1)}")

print("Testing if all elements are even")
all([x % 2 == 0 for x in [2, 4, 6, 8, 10]])

print("Testing if any element is even")
any([x % 2 == 0 for x in [1, 3, 5, 7, 8]])

"""
Anonymous functions cannot contain other python statements such as while, try,
for, etc. Only pure expressions
"""

print("In order to find out if an object is callable, use the callable method")
print(callable(times_3))
help(callable)
