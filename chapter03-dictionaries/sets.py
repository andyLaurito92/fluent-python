haystack = {1, 2, 4,  6, 8, 9, 39, 29, 1 , 2, 9, 94, 2, 3, }
needles = {1, 3, 5}

print("Find out how many needles are in our haystack using the membership property of sets")
len(haystack & needles)

print("Iterable solution with for would be")
count = 0
for elem in haystack:
    if elem in needles:
        count += 1
count


## Disasembly function. Read the bytecode that python generates
from dis import dis
dis('{1}')

dis('set([1])')


"""
View objects returned by .keys() and .items() are similar to frozenset, meaning that we can do
set operations with dict_keys & dict_items :)
"""
