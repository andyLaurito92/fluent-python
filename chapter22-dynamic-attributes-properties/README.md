Interesting references of this chapter:

1. [Key-sharing dictionary PEP 412](https://peps.python.org/pep-0412/)
2. Libraries for accessing key in dictionaries as attributes
    - https://pypi.org/project/attrdict/
	- https://github.com/mewwts/addict
3. [Page](https://github.com/ActiveState/code/tree/master/recipes/Python) which contains Python receipes (code snippets useful for different cases)
	
	
Note about `__init__` and `__new__`:

In Python, `__init__` is not the constructor method as other programming languages.

`__init__` gets self as the first argument, which means that the object already exists when calling this method!

Where the self instance is then created? In method `__new__`! It's a class method. This is the real constructor in Python!

Python takes the instance returned by `__new__` and then passes it as the first argument self of `__init__`

Why don't we code `__new__` instead? Because the implementation inherited from object suffices the vast majority of use cases
