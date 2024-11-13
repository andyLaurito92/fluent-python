"""
By default, python classes are instances of type
"""

print(type(str))

print(type(int))

class Test:
    pass

print(type(Test))

print(type(type)) # type is instance of itself :)

print(type(object))


class ProgrammingLanguage(type):
    def __new__(meta_cls, cls_name, bases, cls_dict):
        print('ProgrammingLanguage.__new__', meta_cls, cls_name, bases, cls_dict)
        res = super().__new__(meta_cls, cls_name, bases, cls_dict)
        print('ProgrammingLanguage class created ', res)
        return res



class Lisp(metaclass=ProgrammingLanguage):
    def __init__(self, name):
        self.name = name

class Scheme(Lisp):
    name = 'Scheme'

    def __init__(self, num_users):
        super().__init__(self.name)
        self.num_users = num_users


# From https://www.scheme.org/
scheme_mit = Scheme(10)
scheme_bigloo = Scheme(30)
scheme_chicken = Scheme(5)

print(myscheme_mit)

"""
To process class Scheme, Python calls

ProgrammingLanguage.__new__(ProgrammingLanguage, 'Scheme', (Lisp,), cls_dict)

When you implement ProgrammingLanguage.__new__, you can manipulate the parameters
before calling super().__new__ which will eventually end up calling type.__new__
"""
