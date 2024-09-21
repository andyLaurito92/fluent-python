"""
Python sorts sequences of any type by comparing their elements. The comparison is done by comparing the first elements of each sequence. If they are equal, the next elements are compared, and so on.

This means that in strings, Python compares the Unicode code points of the characters. This can lead to unexpected results when sorting strings.
"""

fruits = ['caju', 'atemoia', 'cajá', 'acerola']
res = sorted(fruits)

print(f"In this result, 'cajá' should come before caju: {res}")

"""

The standard way to sort non-ASCII strings is to use the locale.strxfrm() function. This function transforms a string into a form that can be compared lexicographically. The transformation is done using the current locale.

"""

import locale
# We first set the locale before using the sorted function
my_locale = locale.setlocale(locale.LC_COLLATE, 'es_ES.UTF-8')

"""
From the documentation:

locale.LC_COLLATE: Locale category for sorting strings. The functions strcoll() and strxfrm() of the locale module are affected.

Note: collate meaning is: to assemble in proper order
"""

res2 = sorted(fruits, key=locale.strxfrm)
print(f"Using locale.strxfrm, the result is: {res2}")


"""
Notes:
1. Locale settings are global
2. The locale must be installed on the OS, otherwise setlocale will raise a locale.Error: unsupported locale setting
3. The locale must be set before using the sorted function
4. You must know how to spell the locale correctly. For example, 'es_ES.UTF-8' is correct, but 'es_ES.UTF8' is not.
"""

"""
There's a pure python implementation of the Unicode collation algorithm called PyUCA (https://github.com/jtauber/pyuca/tree/master). 

The unicode collation algorithm is a specification for comparing strings in Unicode. It's used to sort strings in a way that is consistent with the expectations of users worldwide. The algorithm is complex and takes into account the different ways that characters can be combined, such as accents, diacritics, and ligatures.

"""

"""
unicodedata module has functions to retrieve chatarter metadata. For example, the name of a character.
"""
from unicodedata import name

name('A')
name('Á')
