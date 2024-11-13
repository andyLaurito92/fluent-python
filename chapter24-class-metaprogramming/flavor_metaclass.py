class WilyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__next_value = 0

    def __missing__(self, k):
        if k.startswith('__') and k.endswith('__'):
            raise KeyError(k)
        self[k] = value = self.__next_value
        self.__next_value += 1
        return value

class AutoConstMeta(type):
    def __prepare__(name, bases, **kwargs):
        return WilyDict()


class AutoConst(metaclass=AutoConstMeta):
    pass


class Flavor(AutoConst):
    sambayon
    dulce_de_leche
    limon


Flavor.dulce_de_leche


"""
TODO:
1 - Make it possible to retrieve the constant name if you have the value
2 - Support iteration over the class
3 - Implement a new Enum variant
"""
