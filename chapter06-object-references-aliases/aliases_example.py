andres_student = { 'name' : 'Andres', 'lastname': 'Laurito', 'age': 32 } 
andres_software_engineer = andres_student

"Same objects"
print(f"Ids: {id(andres_student)}, {id(andres_software_engineer)}")

print(andres_student is andres_software_engineer)

impostor = { 'name' : 'Andres', 'lastname': 'Laurito', 'age': 32 }

"Same values, different objects"
print(f"Equality: {andres_student == impostor}")
print(f"Identity: {andres_student is impostor}")

"""
Let's see an example a bit more problematic:
"""

from typing import NamedTuple

student = NamedTuple('Student', [('name', str), ('lastname', str), ('age', int)])

andres_student = student('Andres', 'Laurito', 32)

print(f"variable type: {type(andres_student)}, value: {andres_student}")

andres_tuple = ('Andres', 'Laurito', 32)

print(f"Equality between named tuple and tuple: {andres_student == andres_tuple}")
print(f"Identity between named tuple and tuple: {andres_student is andres_tuple}")
print(f"Types of variables: {type(andres_student)}, {type(andres_tuple)}")

"""
Note: Copies are shallow by default. This means that the copied object is a new object, but it references the same objects that the original object references.
"""

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)

l1.append(100)
print("Appending 100 to l1")
print(f"l1: {l1}")
print(f"l2: {l2}")

# But
l1[1].remove(55)
print("Removing 55 from l1[1]")
print(f"l1: {l1}")
print(f"l2: {l2}")
## The above happens because l1[0] and l2[0] are pointing to the same object

l1[2] += (10, 11)
print("Adding (10, 11) to l1[2]")
print(f"l1: {l1}")
print(f"l2: {l2}")
print("Interesting thing of last operation: When concatenating to a tuple, python creates a new instance with the old elements + the new elements. This means that concatenating to a tuple is a costly operation")

"""
Why would we want something like the above? Because if the elements are immutable, the above
is way faster than having to copy each element. Think that there can be some nested data
structures which make the copy really expensive in time
"""

"""
When working with function parameters, remember that parameters are passed by object reference, meaning that parameters are aliases
"""

def f(a, b):
    a += b
    return a

x = 1
y = 2
print(f"Result of f(x, y): {f(x, y)}")
print(f"x: {x}, y: {y}")

a = [1, 2]
b = [3, 4]
print(f"Result of f(a, b): {f(a, b)}")
print(f"a: {a}, b: {b}")

t1 = (10, 20)
t2 = (30, 40)
print(f"Result of f(t1, t2): {f(t1, t2)}")
print(f"t1: {t1}, t2: {t2}")

"""
Avoid using mutable objects as default parameters in functions
"""

def f(a, data=[]):
    data.append(a)
    return data

print(f"Result of f(1): {f(1)}")
print(f"Result of f(2): {f(2)}")
print(f"Result of f(3): {f(3)}")
print(f"Result of f(4): {f(4, [1])}")

"""
Where does data live? In the frame that loads the function. The default value is created when the function is imported. Every time a function is called, then a frame is created and the parameters of the function are binded in the frame. For data, this means that either we bind the reference of the object passed by parameter or the list created when the module was defined, which lives again in the frame of the module.

See this stackoverflow for more info on this: https://stackoverflow.com/questions/38937721/global-frame-vs-stack-frame
"""
