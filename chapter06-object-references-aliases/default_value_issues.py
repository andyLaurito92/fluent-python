"""
Instead of defining the default value as an empty list, we should define it as None and then check if it is None in the __init__ method and assign an empty list to it.
"""
class Programmer:
    def __init__(self, name, programming_languages_in_study=[]):
        self.name = name
        self.programming_languages_in_study = programming_languages_in_study

    def add_programming_language(self, language):
        self.programming_languages_in_study.append(language)

    def remove_programming_language(self, language):
        self.programming_languages_in_study.remove(language)

andy = Programmer('Andy', ['Python', 'Java'])
print(andy.programming_languages_in_study)  # ['Python', 'Java']

george = Programmer('George')
print(george.programming_languages_in_study) 
george.add_programming_language('Scala')
george.add_programming_language('Elisp')
print(george.programming_languages_in_study)  # ['Scala', 'Elisp']

new_programmer = Programmer('New Programmer')
print("Our new programmer shouldn't have any programming languages in study yet. Let's check it:")
print(new_programmer.programming_languages_in_study)  # ['Scala', 'Elisp']

print("We remove Scala from George's programming languages in study. Let's check if it also affects the new programmer:")
george.remove_programming_language('Scala')
print(f"New programmer languages: {new_programmer.programming_languages_in_study}")  # ['Elisp']

print("Default parameters of Programmer constructor")
print(Programmer.__init__.__defaults__)


"""
Example on using del and checking when an object is garbage collected
"""

print("Example on using del and checking when an object is garbage collected")
import weakref

s1 = {"hola", "mundo"}
another = s1

def bye():
    print("Gone with the wind...")

ender = weakref.finalize(s1, bye)
print(ender.alive)  # True

del s1
print(ender.alive)  # True

print("Deleting last reference to the object")
del another

print(ender.alive)  # False

"""
What about the reference we are passing as argument to finalize? It's a weak reference, so it doesn't count as a reference to the object. That's why the object is garbage collected. Weak references don't increment the reference count of the object.
"""

t1 = (1, 2, 3)
t2 = tuple(t1)

print(f"Note that when creating a tuple from another using tuple(), we get an alias: {t1 is t2}")  # True

"""
Look at these examples
"""

t3 = (4, 5, 6)
t4 = (4, 5, 6)

print(f"Different tuples created, but: {t3 is t4}")

s1 = 'hello'
s2 = 'hello'

print(f"Different strings, but: {s1 is s2}")

"""
The above is called interning. It's a technique Python uses to save memory. It's done for small integers and strings. It's done at compile time, so it's not something you can do in your code.
"""
