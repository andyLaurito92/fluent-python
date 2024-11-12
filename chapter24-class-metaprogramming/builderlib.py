print('@ builderlib module start')

class Builder:
    print('@ Builder body')

    def __init_subclass__(cls):
        print(f'@ Builder.__init_subclass__({cls!r})')

        def inner_0(self):
            print(f'@ SuperA.__init_subclass__:inner_0({self!r})')

        cls.method_a = inner_0


    def __init__(self):
        super().__init__()
        print(f'@ Builder.__init__({self!r})')


def deco(cls):
    print(f'@ deco(({cls!r})')

    def inner_1(self):
        print(f'@ deco:inner_1({self!r})')

    cls.method_b = inner_1
    return cls
