from abc import abstractmethod, ABC

class Validator(ABC):
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        else:
            return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    @abstractmethod
    def validate(self, value):
        raise NotImplementedError("validate must be implemented by sublcasses")


class NonBlank(Validator):
    def validate(self, value):
        if value is None or len(value) == 0:
            raise ValueError("Field cannot be blank")

class Age(Validator):
    def validate(self, value):
        if 0 > value or value > 150:
            raise ValueError("Age cannot be less than 0 or be Matusalen")

class Person:
    name = NonBlank()
    age = Age()

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, student_id):
        self.student_id = student_id


class Employee(Person):
    def __init__(self, social_security_id):
        self.social_security_id = social_security_id


andy = Employee(1234)

ramon = Student("xxd32")


print(Employee.__bases__)

print(Person.__subclasses__())

print(Student.mro())

print(Student.__class__)
# Given that a class is an object, it's class is type, the
# built-in class factory

print(andy.__class__)



"""
type is a class, and it's the built-in class of all classes in Python
Type is a metaclass (class of classes)
"""
