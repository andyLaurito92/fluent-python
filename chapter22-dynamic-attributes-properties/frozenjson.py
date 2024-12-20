from collections import abc
import keyword

class FrozenJSON:
    """ A read-only facade for navigating a JSON-like
    object using attribute notation """

    def __init__(self, mapping):
        self.__data = {}
        for key, val in mapping.items():
            if keyword.iskeyword(key):
                key = key + '_'
            if not str.isidentifier(key):
                raise KeyError(f"Cannot convert {key} in a valid dictionary key. Please clean up the data before converting it")
            self.__data[key] = val

    def __getattr__(self, name):
        try:
            return getattr(self.__data, name) # Access dictionary attributes/methods
        except AttributeError:
            try:
                value = self.__data[name]
            except KeyError:
                # See docs https://docs.python.org/3/tutorial/errors.html#exception-chaining
                raise AttributeError('Mapping doesn\'t have key ', name) from None
            else:
                return FrozenJSON.build(value)

    def __dir__(self):
        """Supports dir() built-in. Returns the keys of this dictionary """
        return self.__data.keys()

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj
