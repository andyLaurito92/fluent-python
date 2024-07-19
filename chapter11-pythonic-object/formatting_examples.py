pesos = 1.0 / 1000.0  # Pesos argentinos

print(pesos)

format(pesos, "0.4f")

print('1 peso = {rate:0.2f} USD'.format(rate=pesos))

print(f'1 peso = {pesos:0.2f} USD')

""""
The notation used in the formatting specifier is called Fromat Specification Mini-Language.
More info can be found here: https://docs.python.org/3/library/string.html#formatspec

f-strings documentation can be found here: https://docs.python.org/3/reference/lexical_analysis.html#f-strings

str.format() documentation can be found here: https://docs.python.org/3/library/string.html#format-string-syntax
"""

"{:>30}".format("right aligned")
"{:<30}".format("left aligned")
"{:^30}".format("center aligned")
"{:*^100}".format("center aligned with fill in asterik")


"""
Int type supports b and x for base 2 and base 16 output
"""

format(42, 'b')

format(42, 'x')

format(2 / 3, '.1%')
