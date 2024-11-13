from builderlib import Builder, deco, Descriptor
from metalib import MetaKlass

print(f'# evaldemo_meta module start')

@deco
class Klass(Builder, metaclass=MetaKlass):
    print('# Klass body')

    attr = Descriptor()

    def __init__(self):
        super().__init__()
        print(f'# Klass.__init__({self!r})')

    def __repr__(self):
        return '<Klass instance>'


obj = Klass()
obj.method_a()
obj.method_b()
obj.method_c()
obj.attr = 999

print("# evaldemo_meta module end")
