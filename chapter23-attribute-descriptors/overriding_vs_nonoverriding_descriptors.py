def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return f'<class {obj.__name__}>'
    elif cls in (type(None), int):
        return repr(obj)
    else:
        return f'<{cls_name(object)} object>'

def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print(f'-> {cls_name(args[0])}.__{name}__({pseudo_args})')


class Overriding:
    """ Data descriptor """
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:
    """ Data descriptor without get"""
    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:
    """ non-data descriptor """
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print(f'-> Managed.span({display(self)})')


# Overriding descriptor

obj = Managed()

obj.over
obj.over = 7

print(vars(obj))
obj.__dict__['over'] = 8

print(vars(obj))
obj.over
# Doesn't matter that we have an attribute in the
# instance of obj called "over", the descriptor
# overrides the lookup of the attribute triggering
# obj.over.__get__(descriptor, obj, None)
# That's why we Luciano calls it "Overriding descriptor"


# Overriding descriptor without __get__

print("======== Overriding descriptor without __get__ ========")
obj.over_no_get

print(vars(obj))
print(obj.over_no_get) # Get the descriptor instance
obj.over_no_get = 3

print(vars(obj))
print(obj.over_no_get) # get the descriptor instance

obj.__dict__['over_no_get'] = "something"

print(obj.over_no_get) # get the attribute value in obj.__dict__

obj.over_no_get = "I will overwrite what you did!"

print(obj.over_no_get)
# Setup was called, but bc __set__ is not doing anything, we still have the old value

# In this last case, because we don't have the __get__ method
# in the descriptor, therefore we can get the value we setup
# by directly writing to the obj__dict__
