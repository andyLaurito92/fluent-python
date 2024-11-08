"""
Definition of descriptor:

Whatever object that implements some of the descriptor protocol methods, these are: __get__, __set__, __delete__, it is a descriptor


Default behaviour of attribute access:

Given object a, when we do a.x, the lookup attribute algorithm in Python works as follows:
1. Lookup chain with a__dict__['x'], then type(a).__dict__['x'], and so on
until either is found or not found in the chain
2. If the looked-up value is an object defining one of the descriptor methods:
2.1. Override the default behaviour and invoke the descriptor method instead


Descriptor protocol:

descr.__get__(self, obj, type=None)

descr.__set__(self, obj, value)

descr.__delete__(self, obj)


Note:
Objects that defines __set__ or __delete__ are considered a data descriptor.
Objects that define only __get__ are called non-data descriptors

Data and non-data descriptors differ in how overrides are calculated with
respect to entries in an instance's dictionary
If an instance's dictionary has an entry with the same name as a data descriptor (set, delete),
the data descriptor takes precedence.
If an instance's dictionary has an entry with the same name as a non-data descriptor (get),
the dictionary entry takes precedence

def attribute_lookup(self, name):
    if name in self.__dict__:
	return self.__dict__[name]
    else:
	if name in type(self).__dict__ and type(self).__dict__[name] is a descriptor:
	descr = type(self).__dict__[name]
	descr.__get__(name)

To make a read-only data descriptor, define both __get__() and __set__() with the __set__() raising an AttributeError when called. Defining the __set__() method with an exception raising placeholder is enough to make it a data descriptor.
"""
