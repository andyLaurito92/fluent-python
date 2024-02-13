"""
The standard library offers sequencey types implemented in C. Primarly we can distinguish:

- Container Sequences --> Can hold items of different types, including nested containers. Examples: list, tuple, collections.deque

- Flat Sequences --> hold items of one simple type. Examples -> str, bytes, array.array
"""

## Container sequence, holds references to the objects it contains
mylist = [9.46, 0.8] 

from array import array

## Flat sequence: Stores the value of its contentes in its own memory space
a = array('d', [9.46, 0.8])

## The above is a single object holding a C language array of 2 doubles


## Doesn't work
#a.insert(0, 'a')



"""
Q: What do * and ** before a variable name mean in a function signature? 

Inside a function header:

* collects all the positional arguments in a tuple.

** collects all the keyword arguments in a dictionary.
"""
def functionA(*a, **kw):
    print(a)
    print(kw)


functionA(1, 2, 3, 4, 5, 6, a=2, b=3, c=5)
# (1, 2, 3, 4, 5, 6)
# {'a': 2, 'c': 5, 'b': 3}
"""
In a function call:

* unpacks a list or tuple into position arguments.

** unpacks a dictionary into keyword arguments.
"""

lis=[1, 2, 3, 4]
dic={'a': 10, 'b':20}
functionA(*lis, **dic)  #it is similar to functionA(1, 2, 3, 4, a=10, b=20)

#(1, 2, 3, 4)
#{'a': 10, 'b': 20}

"""
From Python3 we can apply * to grab arbitrary excess arguments in a parallel assignemt
"""
a, b, *rest = range(1,8)


# Note that the prefix can be in every position of the assignment

a, *middle, b, c = range(1,9)

"""

Python3 supports pattern matching over sequences! :)

"""

chess_pieces = [
    # chess piece, value, color, position
    ("horse", 3, "white", ("b", 2)), 
    ("bishop", 3, "black", ("c", 8)),
    ("king", 10, "black", ("e", 8)),
    ("queen", 10, "white", ("f", 5)),
    ("I should not be here", 32)
]

for piece in chess_pieces:
    match piece:
        case ("horse", value, color, position):
            # _ to express that we don't care about that value # We can destructure a tuple inside an element of the sequence!
            print(f"Horse was at position {position}")
        case ("king", _, _, (column, row)): 
            print(f"King is at {column, row}")
                # In this case we match a first element being a string, we don't care about the middle piece, and the last piece has to be a tuple
        case (str(chess_piece), *_, (column, row)):
            print(f"The piece was {chess_piece} which is located at {column, row}")
            # cath the lefover cases
        case __:
            print("None of the above")
        
## Each case contains a destructuring of a tuple

"""

Be aware that objects of classes str, bytes & bytearray are not handled as sequences by match/case
"""

mystring = "hey, how's that going?"
match mystring:
    case "a":
        print("should be an a")
    case _:
        print("Why?")


"""
Slicing

Python convention is to exclude the last item in slices and ranges

Slicing uses the slice class + the special method __getitem__
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list[:3] # Up to 3

my_list[1::2] # pairs

my_list[:4:2] # Up to fourth element by 2

my_list[::-1] # Revert!

my_list[::-2] # Grab even numbers in descendent order

my_list[2:4] = ['a', 'b'] # slices can be assigned!

del my_list[7:9] # And also deleted

my_list[0:4] = [10] # Doesn't need to be the same side, but it has to be an iterable element

# This will fail --> my_list[0:4] = 10

"""

Be aware of expressions like [mutable_object] * n ! The new list created referentiates to the same mutable object :)
"""

a = [[]]
b = a * 3
print(a)
print(b)
b[0].append("a")
print(a)
print(b)

"""

elipsis class and Elipsis object (recognised as ... by the python parser)

"""

"""

Augmented assignemt with sequences

Special methods __imul__ & __iadd__ allow the in-place multiplication/addition of elemnts in the same list. Be aware that if the class doesn't implement these special methods, the interepreter fallsback to __mul__ & __add__ which are not in place, meaning that you're copying the whole structure again. Concretely:

When __imul/iadd__ are implemented, a += b is in place, but if they are not, the operation a += b equals a = a + b where a + b generates a new reference to a new object

NOTE: str is an exception to the above bc string building with += in loops is so common in real codebases that Cpython is optimized for this use case
Instances of str are allocated in memory with extra room, so that concatenation does not require copying the whole string everytime

"""
l = [1, 2, 3]
id(l)
l *= 2 # Given that l is a sequence, and sequence implements __imul__, original reference is kept and list is modified in place
l
id(l)

# Here tuple is unmutable, therefore it doesn't implement either iadd or imul
t = (1, 2, 3)
id(t)
t *= 2
t # tuple is (1 2 3 1 2 3), but the reference is a new one
id(t)

"""

pythontutor.com --> Super nice tool for seeing what's happening in each executed instruction in a python script

"""


""""
list.sort vs sorted built-in function
"""

unordered_list = [-3, 9, -12, 8, 1, 4, 2023, -2020]

my_new_sorted_list = sorted(unordered_list)
print(f"In contrast of list.sort, sorted returns a new sequence with the sorted list. The original list reamins unmodified. Sorted: {my_new_sorted_list}, original: {unordered_list}")

# Does a sort in place and returns None as python ideomatic convention (all methods that modify the instance received by parameter should return None)
res = unordered_list.sort()
print(f"Result of applying in-place sort: {res}, original list now is: {unordered_list}")
