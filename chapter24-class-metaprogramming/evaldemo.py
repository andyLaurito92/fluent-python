"""
At import time the interpreter:
1. Parses the source code of a .py module in one pass from top to bottom.
This is when a SyntaxError may occur.

2. Compiles the bytecode to be executed

3. Executes the top-level code of the compiled module

If there is an up-to-date .pyc file available in the local __pycache__ ,
parsing and compiling are skipped because the bytecode is ready to run

The import statement is not merely a declaration -> something that let the compiler
 known that certain packages are required (as it happens in Java), but it actually
runs all the top-level code of a module

Further imports of the same module will use a cache, and then th eonly effect will be
binding the imported objects to names in the client module
"""

#import builderlib

from builderlib import Builder, deco, Descriptor

print('# evaldemo module start')

@deco
class Klass(Builder):
    print('# Klass body')

    attr = Descriptor()

    def __init__(self):
        super().__init__()
        print(f'# Klass.__init__({self!r})')


    def __repr__(self):
        return '<Klass instance>'


def main():
    obj = Klass()
    obj.method_a()
    obj.method_b()
    obj.attr = 999


if __name__ == '__main__':
    main()

#main()
print('# evaldemo module end')


"""
The steps for creating a class object are documented here:
https://docs.python.org/3/reference/datamodel.html#creating-the-class-object
"""
