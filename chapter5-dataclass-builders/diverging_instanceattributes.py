"""
Python only way to define instance variables is in methods (plz do it in __init__), by using self.
"""

class Student:
    name = 'Jonh' # class attribute, all instances are named Jhon
    age = 20 # class attribute, all instances are 20
    def __init__(self, age):
        self.age = age # What happens? Do I have 2 ages?

print(Student.__dict__)
first_student = Student(21)

print(f"Instance age: {first_student.age}")
print(f"Class age: {first_student.__class__.age}")

