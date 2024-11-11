"""
__slots__ in a class holds a sequence of attribute names.
These attributes are stored in a hidden array of references
that use less memory than a dict
"""

class Pixel:
    __slots__ = ('x', 'y')

p = Pixel()


"""
When defining attribute __slots__, the class doesn't have a
__dict__ attribute
"""
try:
    p.__dict__
except AttributeError as e:
    print(e)

try:
    print(p.x)
except AttributeError as e:
    print(e) # Cannot access a slot if it wasn't assigned

p.x = 3
p.y = 10

print(p.y)

try:
    p.z = 10
except AttributeError as e:
    print(e) # cannot assign attributes that are not present in __slots__


"""
If we inherit from the above class slots can be accessed as well, and
the child class will have __dict__ defined
"""

class ColorPixel(Pixel):
    pass


coloredpixel = ColorPixel()

print(coloredpixel.__dict__)

coloredpixel.x = 3

print(coloredpixel.x) # value assigned to a slot of the instance

# The slot doesn't appear in the __dict__ of the instance
print(vars(coloredpixel))

# Defining a new attribute defines it in the __dict__ of the instnace
coloredpixel.color = 'green'

# As oppose to a class defining __slots__, we do can assign
# new attributes to the instnace
print(vars(coloredpixel))


"""
The moral is this: If you ColorPixel to behave as Pixel, meaning, don't
allow for new attributes to be set and to disallow the __dict__, you need
to define __slots__ = ()
"""

class ColorPixel2:
    __slots__ = ('color')


colorpixel2 = ColorPixel2()

colorpixel2.color = 'red'

print(colorpixel2.color)

try:
    colorpixel2.__dict__
except AttributeError as e:
    print(e)
