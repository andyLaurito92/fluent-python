"""
When you change the context of a decimal in python, the unary operator + which
should always return x == +x becomes False :)
"""

import decimal

ctx = decimal.getcontext()
ctx.prec = 40
one_third = decimal.Decimal('1') / decimal.Decimal('3')
print(one_third)

print(f"This is equal {one_third == +one_third}")

ctx.prec = 28
print(f"This is not {one_third == +one_third}")
print(+one_third)


"""
Why does the above happen? Because each occurrence of the
expression +one_third produces a new decimal instance from
the value of one_third, but using the precision of the current
arithmetic context
"""
