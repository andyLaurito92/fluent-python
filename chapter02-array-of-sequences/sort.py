""""
list.sort vs sorted built-in function
"""

unordered_list = [-3, 9, -12, 8, 1, 4, 2023, -2020]

my_new_sorted_list = sorted(unordered_list)
print(f"In contrast of list.sort, sorted returns a new sequence with the sorted list. The original list reamins unmodified. Sorted: {my_new_sorted_list}, original: {unordered_list}")

# Does a sort in place and returns None as python ideomatic convention (all methods that modify the instance received by parameter should return None)
res = unordered_list.sort()
print(f"Result of applying in-place sort: {res}, original list now is: {unordered_list}")


## Nice resource to read: https://docs.python.org/3/howto/sorting.html

"""

More about sorting: Both sorted and list.sort provides a key argument which is a function called in each object to use
as comparable.

Let's see some examples:
"""

sorted("This is a test string from Andrew".split(), key=str.lower)

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sorted(student_tuples, key=lambda student: student[2])

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

sorted(student_objects, key=lambda student: student.age)

"""
Operator module function: Python provides convenience functions to make accessor functions easier and faster :). The operator module has itemgetter(), attrgetter() & methodcaller() function

Let's see some examples
"""

from operator import itemgetter, attrgetter

sorted(student_tuples, key=itemgetter(2))

sorted(student_objects, key=attrgetter('age'))

"""
Note: Both sorted and list.stor accept a reverse parameter with a boolean value
"""

sorted(student_tuples, key=itemgetter(2), reverse=True)


"""
Given that sorting in python is stable, we can perform multiple sorts over a same sequence knowing that order will be kept. 

Let's asssume that we want to sort the student data by descending grade and then ascending age, do the age sort first and then sort again using grade:
"""


def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=attrgetter(key), reverse=reverse)
    return xs

multisort(list(student_objects), (('grade', True), ('age', False)))


"""
The Timsort algorithm used in Python does multiple sorts efficiently because it can take advantage of any ordering already present in a dataset.
"""


"""
Note that in Python 2 there were comparisson functions as well (like in Java). This is not the default in Python 3 anymore. However, if a comparisson function is needed to be used in the sorting, you can use functools.cmp_to_key to wrap the comparison function to make it usable as a key function:
"""
