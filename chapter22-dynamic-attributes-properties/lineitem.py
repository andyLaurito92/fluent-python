class LineItem0:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


"""
First problem w/implementation above: weight can be introduced
as negative value
"""

class LineItem1:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight # setter is already in use
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')


item0 = LineItem0("some cool description", 30, 23.3)

item1 = LineItem1("some cool description", 30, 23.3)

vars(item1) # get the variables from this object


"""
Properties are always class attributes, but they actually manage attribute
access in the instances of the class
"""


class Example:
    class_attribute = "something cool"

    def __init__(self) -> None:
        self.text = "an instance attribute"

    @property
    def myprop(self) -> str:
        return "hey yo!"

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, val: str) -> None:
        if len(val) == 0:
            raise ValueError('No empty strings allowed') 
        self.__text = val


myexample = Example()
# Only displays the instance attribute
print(vars(myexample))

# However we can call the class attribute
print(myexample.class_attribute)

myexample.class_attribute = "shadowing class attribute"

print(myexample.class_attribute)
vars(myexample)

# The class attribute remains the same as before, we just
# shadowed the class attribute
print(Example.class_attribute)


"""
With the example above, let's remember that properties are class attributes.
What happens if we tried to override the text attribute on the instance?
"""

print(Example.text)

print(myexample.text)

myexample.__dict__['_Example__text'] = "hacking the matrix!"

print(myexample.text)

print(vars(myexample))

print(myexample.myprop)
print(Example.myprop)

try:
    myexample.myprop = "overriding something that I can't override"
except AttributeError as e:
    print(e)

myexample.__dict__['myprop'] = "You can't with me"

# This demonstrates that overriding a property in an instance doesn't
# override the property getter. The property is not shadowed by the instance
# attribute
print(myexample.myprop)
print(vars(myexample))
print(Example.myprop)

# For overriding its value, you need to change the property instance
# in the class
Example.myprop = 'overriding the property instance'

# Because the class doesn't have myprop property anymore, now we can
# get the overrided value
print(myexample.myprop)


# We can add properties on runtime that override the resolution of that
# attribute in all instances of the class

myexample2 = Example()

try: 
    print(myexample2.property_on_the_fly)
except AttributeError as e:
    print(e)

myexample2.property_on_the_fly = "created only in myexample2 instance"
print(myexample2.property_on_the_fly)

Example.property_on_the_fly = property(lambda x: "I was created on the fly", doc="Some cool documentation here")

# Property overrides properties of instances
print(myexample2.property_on_the_fly)
print(myexample.property_on_the_fly)

# Help extracts the documentation from the __doc__ special method
print(help(Example.property_on_the_fly))

del Example.property_on_the_fly

print(myexample2.property_on_the_fly)

try:
    print(myexample.property_on_the_fly)
except AttributeError as e:
    print("Back to no having property_on_the_fly")


"""
The moral in this last example is this: When doing obj.my_property, the search starts
in the class of obj, obj.__class__.my_property, and not in the instance itself! Only
when the class doesn't have defined the property in it, it fallbacks to search in
the instance
"""

# Factory method for building quantity attributes
def quantity(storage_name):
    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


class LineItem3:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


item3 = LineItem3("some cool description", 30, 23.3)


class House:
    def __init__(self):
        self.name = "The house"

    def __delattr__(self, name):
        print("Deleting attribute ", name)
        super().__delattr__(name)

    def __dir__(self):
        return "Some super cool documentation"

    def __getattr__(self, name):
        print(f"Attribute {name} was not found, let's define it!")
        self.__dict__[name] = "Here you go"

    def __getattribute__(self, name):
        print(name, " attribute was found :)")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        print("Setting attribute ", name, "To ", value)
        super().__setattr__(name, value)


myhouse = House()
