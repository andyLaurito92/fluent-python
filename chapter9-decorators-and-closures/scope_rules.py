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
