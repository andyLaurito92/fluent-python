"""
This first implementation of a Scheme interpreter cannot handle string data, comments
macros, and other features of standard Scheme that make parsing more complicated
"""

import sys
import math
import operator as op
from collections import ChainMap
from itertools import chain
from typing import Any, TypeAlias, NoReturn

"""
Types
"""

Symbol: TypeAlias = str
Atom: TypeAlias = float | int | Symbol
Expression: TypeAlias = Atom | list

MATHS_OPERATORS = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

"""
The parser
"""
def parse(program: str) -> Expression:
    "Read a Scheme expression from a string"
    return read_from_tokens(tokenize(program))

def tokenize(s: str) -> list[str]:
    "Convert a string into a list of tokens"
    return s.replace('(', ' ( ').replace(')', ' ) ').split()

def read_from_tokens(tokens: list[str]) -> Expression:
    "Read an expression from a sequence of tokens"
    if len(tokens) == 0:
        raise SyntaxError('Unexpected EOF while reading')
    token = tokens.pop(0)
    if '(' == token:
        exp = []
        while tokens[0] != ')':
            exp.append(read_from_tokens(tokens))
        tokens.pop(0) # discard ')'
        return exp
    elif ')' == token:
        raise SyntaxError('Unexpected')
    else:
        return parse_atom(token)

def parse_atom(token: str) -> Atom:
    "Numbers become numbers; every other token is a symbol"
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
           return Symbol(token)
        


"""
Eval
"""
def eval(expression: Expression) -> Expression:
    if not isinstance(expression, list):
        return expression
    
    if len(expression) == 0:
        return None

    symbol = expression.pop(0)
    match symbol:
        case int(a):
            return a 
        case float(a):
            return a
        case '+' | '-' | '*' | '/':
            first_operand = expression.pop(0)
            second_operand = expression.pop(0)
            operator = MATHS_OPERATORS[symbol]
            return operator(eval(first_operand), eval(second_operand))
        case _:
            return expression
    

"""
Environment variables
"""
class Environment(ChainMap[Symbol, Any]):
    "A ChainMap that allows changing an item in-place"

    def change(self, key: Symbol, value: Any) -> None:
        "Find where key is defined and change the value there."
        for map in self.maps:
            if key in map:
                map[key] = value
                return
        raise KeyError(key)


def standard_env() -> Environment:
    "An environment with some Scheme standard procedures."
    env = Environment()
    env.update(vars(math))
    env.update({
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,
        '//': op.floordiv,
        '>': op.gt,
        '<': op.lt,
        '>=': op.ge,
        '<=': op.le,
        '=': op.eq,
        'abs': abs,
        'append': lambda *args: list(chain(*args)),
        'apply': lambda proc, args: proc(*args),
        'begin': lambda *x: x[-1],
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:],
        'cons': lambda x, y: [x] + y,
        #'display': lambda x: print(lispstr(x)),
        'eq?': op.is_,
        'equal?': op.eq,
        'filter': lambda *args: list(filter(*args)), # What about the fn?
        'length': len,
        'list': lambda *x: list(x),
        'list?': lambda x: isinstance(x, list),
        'map': lambda *args: list(map(args)),
        'max': max,
        'min': min,
        'not': op.not_,
        'null?': lambda x: x == [],
        'number?': lambda x: isinstance(x, (int, float)),
        'procedure?': callable,
        'round': round,
        'symbol?': lambda x: isinstance(x, Symbol)
        })
    return env

"""
Repl
"""
def repl():
    msg_stop = "Stopping interpreter"
    try:
        print("Starting scheme interpreter")
        while True:
            exp = input("lis.py> ")
            if exp == 'exit()':
                print(msg_stop)
                return
            print(eval(parse(exp)))
    except KeyboardInterrupt as e:
        print("\n", msg_stop)

if __name__ == '__main__':
    if len(sys.argv) == 1: # Only file received 
        repl()
    elif len(sys.argv) == 2: # this file + .lisp containig program to parse
        lisp_file = sys.argv[1]
        print(f"Executing file {lisp_file}")
        with open(lisp_file) as fp:
            print(parse(fp.readall()))
    else:
        raise ValueError(f"Expecting either 1 file or no argument to start the interpreter. Received: {sys.argv}")
