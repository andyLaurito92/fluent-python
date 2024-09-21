"""
How can we do pattern matching against classes in python?

There are three variations: simple, keyword and positional
"""

"""
Simple pattern matching: See https://peps.python.org/pep-0634/#class-patterns.
This can be used against buil-int types, these are:

bytes, dict, float, int, list, set, frozenset, str, tuple
"""

def matching_floats(x):
    match x:
        case float():
            print(f"Float: {x}")
        case _:
            print(f"Not a float: {x}")

matching_floats(3.14)  # Float: 3.14        
matching_floats(42)  # Not a float: 42

"""
The below code has a bug: the case matches any object,
becuase python binds float as a variable and not as a type

Since newer versions of Python, the error is detected by the
interpreter and you cannot define the function. To show the problem,
uncomment the code below and try to run it.
"""

"""
def matching_all_objects(x):
    match x:
        case float: 
            print(f"Float: {x}")
        case _:
            print(f"Not a float: {x}")
"""


"""
Keyword pattern matching
"""

from dataclasses import dataclass

@dataclass
class Country:
    name: str
    population: int
    continent: str

def matching_american_countries(c: Country):
    match c:
        case Country(continent='America'):
            print(f"American country: {c.name}")
        case Country(continent='Europe', population=pop_number):
            print(f"European country with population: {pop_number}")
        case _:
            print(f"Not an American country: {c.name}")
countries = [
    Country('Argentina', 45000000, 'America'),
    Country('Germany', 83000000, 'Europe'),
    Country('Brazil', 210000000, 'America'),
    Country('France', 67000000, 'Europe'),
    Country('USA', 328000000, 'America')
]

for country in countries:
    matching_american_countries(country)


"""
Positional pattern matching
"""

from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int
    country: str

def match_people(p: Person):
    match p:
        case Person('Andres'):
            print(f"Person named Andres: {p.name}")
        case Person(name, _, 'Argentina'):
            print(f"Argentinian person spotted: {name}")
        case _:
            print(f"Not an Argentinian person: {p.name}")

people = [            
    Person('John', 42, 'USA'),
    Person('Andres', 35, 'Argentina'),
    Person('Juan', 28, 'Argentina'),
    Person('Bob', 50, 'USA')
] 

for person in people:
    match_people(person)


print("Positional arguments can be used in classes thanks to the __match_args__ attribute")
print(Person.__match_args__)
print("See how the __match_args__ attribute has the attributes of the class defined in the order they were defined")
