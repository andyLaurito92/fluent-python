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


type(andy) what it does actually is return andy.__class__

type is a class that creates a new class when invoked with 3 arguments
"""

class Hibrid(Student, Employee):
    working_hours = 30 # Defaults to part-time
    class_hours = 20

    def hours_studying_working(self):
        return self.working_hours + self.class_hours


"""
The above is equivalent of doing the following
"""

runtime_hibrid = type('NewHibrid', (Student, Employee), 
                      {'working_hours': 30, 'class_hours': 20,
                       'hours_studying_working': lambda self: self.working_hours + self.class_hours})


new_hibrid = runtime_hibrid('studentid')

new_hibrid.hours_studying_working()


"""
With the above, we can build a factory class. Something super similar is done
by collections.namedtuple, typing.NamedTuple and dataclass
"""

def dog_factory():
    def dog_init(self, name, weight, owner):
        self.name = name
        self.weight = weight
        self.owner = owner

    new_dog_instance = type('Dog', (),
                            {'__init__': dog_init})

    def new_dog(name, weight, owner):
        return new_dog_instance(name, weight, owner)
        
    return new_dog


dog_creator = dog_factory()

mila = dog_creator('Mila', 12, 'Andy')
firulais = dog_creator('Firulais', 10, 'Home')

print(type(mila))
print((mila.owner, mila.weight, mila.name))


"""
The above can be refactor to abstract the creation of a record to a general use case,
pretty similar to what collection.namedtuple, typing.NamedTuple or dataclass do
"""

def record_factory(clssname, *args):
    attribute_names = tuple(args)
    def init(self, *args):
        for attr_name, val in zip(attribute_names, args):
            setattr(self, attr_name, val)

    def __repr__(self):
        repr_str = f'{clssname}('
        repr_str += ', '.join(f'{key}={value}' for key, value
                              in self.__dict__.items())
        repr_str += ')'
        return repr_str

    return type(clssname, (), {'__init__': init, '__repr__': __repr__})


Dog = record_factory('Dog', 'name', 'weight', 'owner')

rex = Dog('Rex', 5, 'Bob')

print(rex.owner, rex.weight, rex.name)

print(rex.__dict__)

print(rex)
