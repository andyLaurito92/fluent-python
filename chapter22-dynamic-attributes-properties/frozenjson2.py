from collections import abc
import keyword

# Instead of implementing a builder by using a static method
# we implement the __new__ special method

class FrozenJSON2:
    """ A read-only facade for navigating a JSON-like
    object using attribute notation """

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

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

    
