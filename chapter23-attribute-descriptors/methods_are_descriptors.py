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

# Now we have a bounded method, not a function anymore
print(bounded_method)

# And we compare our bounded method to method mytext.reverse
# to see if they are equal
print(bounded_method == mytext.reverse)

# However if we compare a bounded method to a function

print(bounded_method == Text.reverse)

print(type(bounded_method.__self__), bounded_method.__self__)
