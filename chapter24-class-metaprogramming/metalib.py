from collections import UserDict
import logging

logging.basicConfig(level=logging.INFO)

class NosyDict(UserDict):
    def __setitem__(self, key, item):
        args = (self, key, item)
        print(f'% NosyDict.__setitem__({args!r})')
        super().__setitem__(key, item)

    def __repr__(self):
        return '<NosyDict instance>'

        
class MetaKlass(type):
    print('% MetaKlass body')

    @classmethod
    def __prepare__(meta_cls, cls_name, bases): 
        """ Method being called by Python before the creation of the class object.
        This method should return the namespace of the class"""
        args = (meta_cls, cls_name, bases)
        print(f'% MetaKlass.__prepare__({args!r})')
        return NosyDict()

    def __new__(meta_cls, cls_name, bases, cls_dict):
        args = (meta_cls, cls_name, bases, cls_dict)
        print(f'% MetaKlass.__new__({args!r})')
        def inner_2(self):
            print(f'% MetaKlass.__new__:inner_2({self!r})')

        cls = super().__new__(meta_cls, cls_name, bases, cls_dict.data)
        cls.method_c = inner_2

        return cls

    def __repr__(cls):
        cls_name = cls.__name__
        return f"<class {cls_name!r} built by MetaKlass>"

print('% metalib module end')
