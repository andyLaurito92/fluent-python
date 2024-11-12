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
