"""
Strange behaviour :D
"""

b = 9

def myfun1(name):
    print("myfun1")
    print(name)
    print(b)

myfun1("Andres")


def myfun2(name):
    """In this example the function fails becuase I define b inside the
    function's local scope"""
    print("myfun2")
    print(name)
    print(b)
    b = 3

# myfun2("Andres")


def myfun3(name):
    """ Same example as above, but we define b as global"""
    global b
    print("myfun3")
    print(name)
    print(b)
    b = 3

myfun3("Andres")


"""
A good thing to understand what Cython is doing is to use
the dis module
"""

from dis import dis

dis(myfun1)
dis(myfun2)
dis(myfun3)


"""
Example on why python is not dynamically scoped
"""

print("We define a function getx with a free variable x")
def getx():
    return x


x = 8

"""
Because python is lexical scoped, x is always defined according to
where the function getx was defined. This means that x will always
be attached to the global variable x
"""

def myconfusingfunction():
    x = 4
    y = 5
    z = getx()
    print(f"x: {x}, y: {y}, z:{z}")

print("What wil this function return?")
myconfusingfunction()

mystr = (
    "Why?, because python is lexical scoped, meaning that even though "
    "we defined x inside myconfusingfunction, python always binds "
    "variables to values by where the function was defined, not where "
    "is being executed")

x = 1
myconfusingfunction()


"""
What would a dynamic scoped language do? Bind x dynamically according to
the execution of the program

Example: elisp :).
See more here: https://www.gnu.org/software/emacs/manual/html_node/elisp/Dynamic-Binding.html
"""
