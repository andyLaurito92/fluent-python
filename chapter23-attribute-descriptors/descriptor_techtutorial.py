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

def find_name_in_mro(cls, name, default):
    "Emulate _PyType_Lookup() in Objects/typeobject.c"
    for base in cls.__mro__:
        if name in vars(base):
            return vars(base)[name]
    return default

def object_getattribute(obj, name):
    "Emulate PyObject_GenericGetAttr() in Objects/object.c"
    null = object()
    objtype = type(obj)
    cls_var = find_name_in_mro(objtype, name, null)
    descr_get = getattr(type(cls_var), '__get__', null)
    if descr_get is not null:
        if (hasattr(type(cls_var), '__set__')
            or hasattr(type(cls_var), '__delete__')):
            return descr_get(cls_var, obj, objtype)     # data descriptor
    if hasattr(obj, '__dict__') and name in vars(obj):
        return vars(obj)[name]                          # instance variable
    if descr_get is not null:
        return descr_get(cls_var, obj, objtype)         # non-data descriptor
    if cls_var is not null:
        return cls_var                                  # class variable
    raise AttributeError(name)

To make a read-only data descriptor, define both __get__() and __set__() with the __set__() raising an AttributeError when called. Defining the __set__() method with an exception raising placeholder is enough to make it a data descriptor.

Instance Lookup:

Instance lookup scans through a chain of namespaces giving data descriptors the highest priority, followed by instance variables, then non-data descriptors, then class variables, and lastly __getattr__() if it is provided.
If a descriptor is found for a.x, then it is invoked with: desc.__get__(a, type(a)).

Important: Review invocation from [class|instance|super] for a better explanation on attribute resolution from
each of these objects
"""
