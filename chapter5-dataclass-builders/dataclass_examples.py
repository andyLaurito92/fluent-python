from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int = 31
    city = 'Buenos Aires'


# Only attributes name & age become annotations
print(Person.__annotations__)

try: 
    print(Person.name)
except Exception as e:
    print("When the attribute is not defined in the class, Python returns an"
    " attribute error instead of returning None", e)

"""
Note how the above behavior is different from the one in the NamedTuple example,
where the attribute was returned as a descriptor.
"""

print(Person.age)

"""
From the dataclass annotation, the parameters that are passed are:
- frozen: Makes the class immutable. If you try to change an attribute, it will raise an exception.
- eq: If True, the class implements __eq__() method. Default is True.
- order: If True, the class implements __lt__(), __le__(), __gt__(), and __ge__() methods. Default is False.
- init: If True, the class implements a __init__() method that initializes the attributes. Default is True.
- repr: If True, the class implements a __repr__() method. Default is True.
- unsafe_hash: If True, the class implements a __hash__() method. Default is False.

Frozen and order are the more likely to be changed.
"""


"""
Hashing dataclasses

Note the difference between the following two classes:
"""

@dataclass
class UnhashableCity:
    name: str
    population: int
    country: str
    coordinate: tuple

@dataclass(frozen=True)
class City:
    name: str
    population: int
    country: str
    coordinate: tuple


buenosaires_hashable = City('Buenos Aires', 2891000, 'AR', (-34.61, -58.38))
buenosaires_unhashable = UnhashableCity('Buenos Aires', 2891000, 'AR', (-34.61, -58.38))

print(f"Hash of buenos aires: {hash(buenosaires_hashable)}")

try: 
    print(hash(buenosaires_unhashable))
except Exception as e:
    print("When trying to hash a dataclass which can be mutable (frozen = False), then an exception is thrown ", e)


"""
The code below is a bug in most cases:

The default value of the collection attribute is a mutable object (list). This means that all instances of MutableField share the same list object. If you change the list in one instance, it will change in all instances, which is probably not what you want.
"""

try: 
    @dataclass
    class MutableField:
        name: str
        collection: list = []
except Exception as e:
    print("When trying to define a mutable field in a dataclass, Python throws an exception: ", e)

"""
Correct way of implementing a mutable field in a dataclass
"""

from dataclasses import field

@dataclass
class MutableField:
    name: str
    collection: list = field(default_factory=list)

mutable = MutableField('mutable', [1, 2, 3])

print("Showing problem with having a mutable field in a dataclass")

@dataclass
class BuggyClass:
    name: str
    collection = []

user1 = BuggyClass('user1')
user2 = BuggyClass('user2')

print(f"User 1 adds something new to the collection")
user1.collection.append(1)
print(f"And nos user 2 list look like this :) -> {user2.collection}")

"""
Again, the problem above is that we are sharing the same instance of list across all instances of the class. The correct way of doing this is by using the field function from the dataclasses module.
"""

"""
Field has other parameters, such as:
- default: The default value of the field.
- default_factory: A function that returns the default value of the field.
- repr: If True, the field is included in the string returned by the __repr__() method. Default is True.
- hash: If True, the field is included in the hash of the object. Default is True.
- init: If True, the field is included as a parameter in the __init__() method. Default is True.
- compare: If True, the field is included in comparison methods (__eq__(), __gt__(), etc.). Default is True.
- metadata: A dictionary with metadata about the field.
"""

@dataclass
class Student:
    name: str
    age: int = field(default=20, repr=False) # age is not included in the repr
    grades: list = field(default_factory=list, metadata={'unit': 'grades'})


student = Student('John')
print(student)


"""
In case a more complex init is needed, you can override the __post_init__ method
"""

@dataclass
class BachelorStudent(Student):
    degree: str = 'science'
    valid_degrees = ['science', 'arts']

    def __post_init__(self):
        self.degree = self.degree.lower()
        if self.degree not in self.valid_degrees:
            raise ValueError(f'Degree must be one of {self.valid_degrees}')

try: 
    engeneering_student = BachelorStudent('John', degree='Engineer')
except Exception as e:
    print("When trying to instantiate a BachelorStudent with an invalid degree, Python throws an exception: ", e)

valid_student = BachelorStudent(name='John', age=27, degree='arts')
print(f"Valid student: {valid_student}. Age is: {valid_student.age}")


"""
Be aware of the following problem

Let's assume that we want to collect the movies watched by us
"""

@dataclass
class Movies:
    watched = set()

my_movies = Movies()
my_movies.watched.add('The Godfather')
my_movies.watched.add('The Godfather II')

your_movies = Movies()
your_movies.watched.add('The Shawshank Redemption')
your_movies.watched.add('The Dark Knight')

print(f"Watched movies by us: {my_movies.watched}")


"""
The above dataclass wouldn't pass mypy checks. In particular it throws the following error:

dataclass_examples.py:169: error: Need type annotation for "watched" (hint: "watched: set[<type>] = ...")  [var-annotated]

If we add a type to the watched attribute, the class instance would become a instance variable!
"""

from typing import ClassVar
@dataclass
class MoviesTyped:
    #watched: set = field(default_factory=set) # If you try without the default_factory, it will throw an error
    watched: ClassVar[set[str]] = set()

my_movies = MoviesTyped()
my_movies.watched.add('The Godfather')
my_movies.watched.add('The Godfather II')

your_movies = MoviesTyped()
your_movies.watched.add('The Shawshank Redemption')
your_movies.watched.add('The Dark Knight')

print(f"Watched movies by us: {my_movies.watched}")

"""
If we want to have a typed class variable, we can use the ClassVar type hint. This way, the watched attribute is shared among all instances of the class. This was introduced in PEP 526 (https://peps.python.org/pep-0526/)
"""

"""
The are only 2 places were dataclasses care about typehints:
1. If an atribute is a ClassVar, then an instance field will not be generated
2. When declaring init-only variables. See https://docs.python.org/3/library/dataclasses.html#init-only-variables
"""


"""
Bigger example on dataclasses
"""

from enum import Enum, auto
from datetime import date
from typing import Optional

class ResourceType(Enum):
    VIDEO = 'video'
    IMAGE = 'image'
    TEXT = 'text'

@dataclass
class Resource:
    identifier: str
    type: ResourceType = ResourceType.TEXT
    tags: list = field(default_factory=list)
    date: Optional[date] = None

    def __repr__(self):
        return f'Resource(\n identifier={self.identifier!r}, \n type={self.type!r}, \n tags={self.tags!r}, \n date={self.date!r}\n)'

my_resource = Resource('123', ResourceType.VIDEO, ['python', 'dataclasses'], date(2021, 1, 1))
print(my_resource)
