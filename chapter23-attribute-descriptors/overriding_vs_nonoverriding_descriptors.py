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
