"""
Remember that in Java we can do method overlaoding which allows us to have the O of
SOLID? Open for extension, closed to modification? Well, in Python we have the
single dispatch closure. Let's take a look at it with the following example:

We want to generate HTML dipsplays for different types of Python objects. For doing
this, we will use the single dispatch instead of doing a lot of if/elif/else
"""

from functools import singledispatch
from collections import abc
import decimal
from fractions import Fraction


@singledispatch
def htmlize(obj: object) -> str:
    return f"<pre>{repr(obj)}</pre>"


@htmlize.register
def _(astr: str) -> str:
    newstr = astr.replace('\n', '<br/>')
    return f"<p>{newstr}</p>"

@htmlize.register
def _(anint: int) -> str:
    return f"<pre>{anint} ({hex(anint)})</pre>"

@htmlize.register
def _(abool: bool) -> str:
    return f"<pre>{abool}</pre>"

@htmlize.register(decimal.Decimal)
@htmlize.register
def _(afloat: float) -> str:
    frac = Fraction(afloat).limit_denominator()
    return f"<pre>{afloat} ({frac.numerator}/{frac.denominator})</pre>"

@htmlize.register
def _(seq: abc.Sequence) -> str:
    html_elements = ''.join([f"<li>{htmlize(elem)}</li>"
                             for elem in seq])
    return f"<ul>{html_elements}</ul>"
