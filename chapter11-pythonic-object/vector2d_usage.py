from vector2d import Vector2D

def matching_vector(avector: Vector2D) -> None:
    match avector:
        case Vector2D(x=0):
            print("Vector with null x coordinate")
        case Vector2D(y=0):
            print("Vector with null y coordinate")
        case Vector2D(x=3, y=y):
            print(f"Vector has 3 as x and {y} as y coordinate")
        case Vector2D(_, y=3):
            # In order to support this case, vector2d has to has class attribute __match_args__ 
            print(f"y is 3")
            

    
matching_vector(Vector2D(3.0, 4.0))
matching_vector(Vector2D(0, 3))
matching_vector(Vector2D(5, 3))


"""
See name mangling in vector2d by showing internal dict
"""

myvec = Vector2D(2.3, 4.8)

"""
See in the following example how the class name is appended to
the so called "private variables".

Remember that there are no private variables in Pytho, as there are
in Java. What Python provides is this name mangling that allows
variables to not clash in object inheritance
"""
print(myvec.__dict__)


"""
So the reason why I cannot access variable myvec.__x is not
because it's private
"""
# Comment line to see error
#myvec.__x

"""
But because it was defined with another name by Python
"""

myvec._Vector2D__x
