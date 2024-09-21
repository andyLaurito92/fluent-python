import random

class Bingo:
    def __init__(self):
        self._numbers = list(range(1, 76))
        random.shuffle(self._numbers)

    def pick(self):
        try:
            return self._numbers.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

bingo = Bingo()
print(bingo())
"""
Calling an object as if it were a function
"""
bingo()
bingo()

callable(bingo)


# In this example, cls is a keyword-only argument
def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    attrs_str = ''.join(f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    if content:
        return '\n'.join(f'<{name}{attrs_str}>{c}</{name}>' for c in content)
    else:
        return f'<{name}{attrs_str} />'

print(tag('br'))
print(tag('p', 'hello'))

my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
print(print(tag(**my_tag)))

tag.__kwdefaults__


"""
Keyword-only arguments are defined after the argument prefixed with *
"""

def another_test(a, *b, keyword_only_1=None, keyword_only_2=None):
    print(a, b, keyword_only_1, keyword_only_2)

print(another_test(1, 2, 3, keyword_only_1=4, keyword_only_2=5))

print(another_test.__kwdefaults__)

# In this example, the keyword-only arguments are not bound to 4 and 5
# This is because we explicitly need to use the keyword
print(another_test(1, 2, 3, 4, 5))

def f(a, *, b):
    return a, b

print(f(1, b=2))

try: 
    print(f(1, 2))
except Exception as e:
    print(f"Something went wrong {e}")


"""
Defining positional-only arguments. Use / to separate positional-only arguments from the rest
All arguemnts to the left of the / are positional-only. After the /, you may specify other arguemnts
which work as usual.
"""
def f(a, b, /, c, d, *, e, f):
    return a, b, c, d, e, f

print(f(1, 2, 3, 4, e=5, f=6))

print(f(5, 4, c=3, d=2, e=1, f=0))

try:
    print(f(1, 2, 3, 4, 5, 6))
except Exception as e:
    print(f"Something went wrong {e}")
