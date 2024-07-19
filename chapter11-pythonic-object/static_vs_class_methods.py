"""
The difference between decorators @staticmethod and @classmethod are the
arguments they take. The first one takes no arguments, while the second one
takes a class as an argument.
"""

class Example:
    @staticmethod
    def static(*args):
        print(args)

    @classmethod
    def cls(*args):
        print(args)

print("Calling static method without arguments")
Example.static()

print("Calling class method without arguments")
Example.cls()

print("Calling static method with arguments")
Example.static(1, 2, 3)

print("Calling class method with arguments")
Example.cls(1, 2, 3)


"""
Question would be: If we are not receiving the class as an argument, why would we
define this method as a static method inside our class? 

For a discussion about this, see this post: https://dzone.com/articles/definitive-guide-how-use
"""
