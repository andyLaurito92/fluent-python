from collections.abc import Callable
from typing import Any, NoReturn, get_type_hints

class Field:
    """ Descriptor that dynamically checks the type of the field """
    def __init__(self, name: str, constructor: Callable) -> None:
        if not callable(constructor) or constructor is type(None):
            raise TypeError(f'{name!r} type hint must be callable')
        self.name = name
        self.constructor = constructor

    def __set__(self, instance: Any, value: Any) -> None:
        if value is ...:
            value = self.constructor()
        else:
            try:
                value = self.constructor(value)
            except (TypeError, ValueError) as e:
                type_name = self.constructor.__name__
                msg = f'{value!r} is not compatible with {self.name}:{type_name}'
                raise TypeError(msg) from e
        instance.__dict__[self.name] = value


class Checked:
    @classmethod
    def _fields(cls) -> dict[str, type]:
        return get_type_hints(cls)

    # Documentation of this special method can be found here
    # https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__
    def __init_sublclass__(subclass) -> None:
        """ Method call when a subclass of this class is defined.
        It gets that new subclass as its first argument"""
        super().__init_subclass__()
        for name, constructor in subclass._fields().items():
            setattr(subclass, name, Field(name, constructor))

    def __init__(self, **kwargs: Any) -> None:
        for name in self._fields():
            # Return ... if no value (instead of None)
            # With this, we make a difference between "no value"
            # and "user set the value to None"
            value = kwargs.pop(name, ...) 
            setattr(self, name, value)
        if kwargs:
            self.__flag_unkown_attrs(*kwargs)

    def __setattr__(self, name: str, value: Any) -> None:
        if name in self._fields():
            cls = self.__class__
            descriptor = getattr(cls, name)
            descriptor.__set__(self, value)
        else:
            self.__flag_Unkown_attrs(name)

    def __flag_unkown_attrs(self, *names: str) -> NoReturn:
        plural = 's' if len(names) > 1 else ''
        extra = ', '.join(f'{name!r}' for name in names)
        cls_name = repr(self.__class__.__name__)
        raise AttributeError(f'{cls_name} object has no attribute{plural} {extra}')

    def _asdict(self) -> dict[str, Any]:
        return {
            name: getattr(self, name)
            for name, attr in self.__class__.__dict__.items()
            if isinstance(attr, Field)
        }

    def __repr__(self) -> str:
        kwargs = ', '.join(
            f'{key}={value!r}' for key, value in self._asdict().items()
            )
        return f'{self.__class__.__name__}({kwargs})'
