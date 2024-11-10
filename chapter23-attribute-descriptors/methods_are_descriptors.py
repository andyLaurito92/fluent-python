from collections import UserString

class Text(UserString):
   def __repr__(self):
       return 'Text({!r})'.format(self.data)

   def reverse(self):
       return self[::-1]


mytext = Text('Amelia')

mytext.reverse()

print(mytext.reverse) # This is a bounded method

print(Text.reverse) # But this is a function!

print("Types of method reverse in instance and class")
print(type(mytext.reverse), type(Text.reverse))

# What is the difference? That in the bounded method,
# we have bounded the obj instance!

# Given that reverse is a descriptor, we can call __get__ on it
# and bound the function to an instance object!
bounded_method = Text.reverse.__get__(mytext, None)


# We can call function reverse from Text class by calling it
# with an instance of Text
print(Text.reverse(Text("mounstrito")))

# We can use Text.reverse as a normal function!
print(list(map(Text.reverse, ("hellohowareyou", ["ho", "ha", "hi"], "dunder"))))

# Now we have a bounded method, not a function anymore
print(bounded_method)

# And we compare our bounded method to method mytext.reverse
# to see if they are equal
print(bounded_method == mytext.reverse)

# However if we compare a bounded method to a function

print(bounded_method == Text.reverse)

print(type(bounded_method.__self__), bounded_method.__self__)

# You can access the underlying function of a bounded method by
# accessing __func__
print(bounded_method.__func__)

print(bounded_method.__func__ is Text.reverse)

print(bounded_method.__call__)


"""
The bound method object also has a __call__ method, which handles
the actual invocation. This method calls the original function
referenced in __func__, passing the __self__ attribute of the
method as the first argument. That's how the implicit binding
of the conventional self argument works
"""
