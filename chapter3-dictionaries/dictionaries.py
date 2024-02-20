"""
Python is basically dicts wrapped in loads of syntatic sugar
"""

print("Class and instances attributes, module namespaces, and function keyword arguments are some of the core Python constructs represented by dictionaries in memory")
print("The __builtins__.__dict__ stores all built-in types, objects and functions")

print(__builtins__.__dict__)

print("Hash tables is how dictionaries are implemented in Python")

print("Other built-in types absed on hash tables are set and frozenset")

from collections import frozenset

myset = set()
myset.add(3)
myset.add(1)
myset.add(3)
myset.add(2) 
myset.add(2) 
myset.add(1)
myset.add(9)



"""
- We can do pattern matching with mappings

- Since Python 3.6, dict keeps the key insertion order

An interesting article regarding internals of sets and dicts can be found here --> https://www.fluentpython.com/extra/internals-of-sets-and-dicts/
"""


# We can build dict using dict comprehension
from string import ascii_lowercase
my_dict = { i : letter for i, letter in enumerate(ascii_lowercase) }

def char_range(start_letter, last_letter):
    for next_char in range(ord(start_letter), ord(last_letter) + 1):
        yield chr(next_char)

my_dict_of_chars = { mychar : ord(mychar) for mychar in char_range('c' , 'y') }

letters_in_last_positions = { my_dict[i] : i for i in my_dict.keys() if i > 20 }


"""
Unpacking
"""

def dump(**kwargs):
    return kwargs

dump_set= dump(**{'x' : 1}, b=2, **{ 'c' : 3, 'd' : 4})


"""
Python 3.9 supports merging by doing | & |=
"""
another_dict = {'x': 4, 'z': 5}
dump_set | another_dict
# In the line above, dump_set is not being modified. A new dictionary is returned

dump_set |= another_dict

"""
Note: the match/case supports subjets that are mapping objects. Patterns for mappings look like dict literals, but they can match instances of any actual or virtual subclass of collections.abc.Mapping

The above is supper useful for JSONs and databases with semi-structured schemas
"""

responses = [
    { "message": "This is an api message", "status": 404, "my_secret_key": "This is my secret key" },
    { "message": "All good over here", "status": 200, "my_secret_key": "rabbit1123" },
    { "message": "All good over here", "status": 303, "my_secret_key": "rabbit1123" }
]

for response in responses:
    match response:
        case { "status" : 404 }:
            print("Ooops!, not found")
        case { "message" : my_message, "status": 200}:
            print(f"The message is {my_message}")
        case { "my_secret_key": the_key }:
            print(f"The secret key is {the_key}")

