"""
Remember that in Java we can do method overlaoding which allows us to have the O of
SOLID? Open for extension, closed to modification? Well, in Python we have the
single dispatch closure. Let's take a look at it with the following example:

We want to generate HTML dipsplays for different types of Python objects. For doing
this, we will use the single dispatch instead of doing a lot of if/elif/else
"""

from functools import singledispatch


@singledispatch
def htmlize(obj: object) -> str:
    return f"<pre>{repr(obj)}</pre>"


@htmlize.register
def _(astr: str) -> str:
    newstr = astr.replace('\n', '<br/>')
    return f"<p>{newstr}</p>"
