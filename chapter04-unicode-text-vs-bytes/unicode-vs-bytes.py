import os
import locale
import sys

"""
Let's start this unit with some definitions:

A string is a sequence of characters

A character from a human perspective is easy to define: Is what we write: letters, numbers, symbols, emojis. From a computer perspective, a character is the representation of what we write in a language called Unicode character. Unicode separates the identity of the character from it's actual representations.

An identity of a character, also called it's code point, is a number from 0 to 1,114,111 (base 10). This number is usually showed in the Unicode standard as 4 to 6 hex digits with a U+ prefix. Example: code point for A is \U+0041

The actual bytes that represent a cahracter DEPENDS ON the ENCODING in use.

An ENCODING is an algorithm that converts code points to byte sequences and viceversa. For example, the code point of A is encoded:
- In UTF8 as Single byte \x41 
- In UTF-16LE as \x41 \x00

Converting from code points to bytes is encoding
Converting from bytes to code points is decoding
"""

s = 'Andrés'
len(s)

utf8_s = s.encode('UTF8')
len(utf8_s)
utf8_s

"""
In the above example, é is encoded with 2 bytes as \xc3\xa9 making the len of the utf8_s increment in 1
"""



"""
Byte essentials

2 basic built-in types for binary sequences:
1 - Ummutable type bytes
2 - Mutable bytearray

!! Each item in bytes or bytearray is an integer from 0 to 255
"""

cafe = bytes('café', 'UTF-8')

# Note how this line returns 99 and not c. 99 is the ascii representations of c
cafe[0]



"""
Python distribution bundles more than 100 codecs(encoder/decoders) for text to byte conversion and viceversa. Codec examples: 'utf_8', 'latin_1', 'ascii', 'cp1252', 'cp437', 'cp850'. These can be used as arguments in functions like open(), str.encode(), bytes.decode(), and so on.

Note: UTF-8 is the most common codec and the default for Python 3. It's designed to handle all Unicode characters. It's backward compatible with ASCII, meaning that UTF-8 is a superset of ASCII. UTF-8 is the best choice for encoding text files.
"""

for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')


"""
Unicode exceptions: UnicodeEncodeError (when converting str to binary sequences) and UnicodeDecodeError (when converting binary sequences to str)

If a character is not defined in the target encoding, UnicodeEncodeError is raised.
"""
name = "Iñaqui"

print(name.encode('utf_8'))

## UnicodeNcodeError. ñ does't exist in ascii
print(name.encode('ascii'))

## Replace unkown characters with ?
name.encode('ascii', errors='replace')

## Ignore unkown characters
name.encode('ascii', errors='ignore')

"""
Replace unkown characters with xml reference.  (i.e., a numeric character reference)

When an unencodable character is encountered, it replaces it with its corresponding XML character reference. This reference is in the form of &#NNNN; where NNNN is the decimal Unicode code point of the character.

In the example below, 241 is the decimal Unicode code point for ñ.
"""

name.encode('ascii', errors='xmlcharrefreplace')


"""
If a byte sequence is not valid in the target decoding, UnicodeDecodeError is raised.
"""

octets = b'Montr\xe9al'

octets.decode('cp1252')

## This wrong codec produces a "gremlin" (a character that doesn't exist in the target encoding but it's still decoded and an error is not raised)
octets.decode('iso8859_7')

## Raises an error
octets.decode('utf_8')

## Replace any character that can't be decoded with a ?
octets.decode('utf_8', errors='replace')

from weird_encoding import *

# Example of bug
bytes_written = open('cafe.txt', 'w', encoding='utf_8').write('café')

res = open('cafe.txt', encoding='ascii', errors='replace').read()
res

file_descriptor = open('cafe.txt', 'w', encoding='utf_8')
## play w/it in the console
file_descriptor.close()

fp2 = open('cafe.txt')
## play w/it in the console
fp2.close()

fp3 = open('cafe.txt', 'rb')
## play w/it in the console
fp3.close()

## Get the number of bytes the file has
os.stat('cafe.txt').st_size


## Explore default encodings in OS. This is just to show how many encodings are available in the system

locale.getpreferredencoding() ## This is what text file use by default
sys.stdout.encoding

"""
The isatty() method in Python is used to determine if a file descriptor is connected to a terminal (TTY) device. In the context of sys.stdout.isatty(), it checks whether the standard output (stdout) is connected to a terminal.

The isatty() method returns True if the file descriptor is connected to a terminal, and False otherwise. This is useful in scripts and programs to decide whether to produce output that is suitable for a terminal (such as colorized text or interactive prompts) or not.
"""

sys.stdout.isatty()
sys.stdin.encoding
sys.stderr.encoding
sys.getdefaultencoding()
sys.getfilesystemencoding()

my_file = open('example.txt', 'w')
my_file.encoding
my_file.close()



"""
\N{} escape for Unicode literals. Inside curly braces, you can use the Unicode name of the character. This is much better than writing the hexadecimal code point. If the name doesn't exist, python raises SyntaxError
"""

print('\N{INFINITY}')
print('\N{CIRCLED NUMBER FORTY TWO}')

"""
Text normalization: Normalization is the process of transforming text into a canonical (standard) form. This is important because Unicode allows multiple ways to represent the same character. For example, the character é can be represented as a single code point (U+00E9) or as two code points (U+0065 U+0301). Both representations should be treated as the same character.

"""

s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'
s1, s2

# First string is encoding w/4 unicode characters while second is encoded w/5 unicode characters
len(s1), len(s2)

"""
For strings with Unicode characters, len counts each character, not the number of bytes they may occupy in memory.
"""

s1 == s2

s1.encode('utf_8'), s2.encode('utf_8')


"""
How to solve the above problem in order to get what we expect?

unicodedata.normalize() function. This function takes two arguments: the form parameter and the string to normalize. The form parameter specifies the normalization form to use. There are four normalization forms defined in Unicode: NFC, NFD, NFKC, and NFKD.

NFC (Normalization Form Canonical Composition) is the most common normalization form. It composes characters and replaces them with a single code point if possible. This is the form you should use for most text processing tasks.
"""

from unicodedata import normalize, combining
len(normalize('NFC', s1)), len(normalize('NFC', s2))

len(normalize('NFD', s1)), len(normalize('NFD', s2))

normalize('NFC', s1) == normalize('NFC', s2)


"""
Utility functions when working w/different languages
"""

def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())

s1 == s2

nfc_equal(s1, s2)

nfc_equal('A', 'a')

s3 = 'Straße'
s4 = 'Strasse'

s3 == s4

nfc_equal(s3, s4)

fold_equal(s3, s4)
fold_equal(s1, s2)
fold_equal('A', 'a')


"""
To better understand normalize forms in unicode visit https://unicode.org/reports/tr15/#Norm_Forms

"""


"""
Taking out diacritics (accents, cedillas, etc) from characters. This is useful when you want to compare strings without considering diacritics. For example, you may want to treat café and cafe as equal strings.

The unicodedata module provides the normalize() function to remove diacritics from characters. The function takes two arguments: the form parameter and the string to normalize. The form parameter specifies the normalization form to use. There are four normalization forms defined in Unicode: NFC, NFD, NFKC, and NFKD.

The combining method from the unicodedata module returns a non-zero value if the character is a combining character. Combining characters are characters that are combined with the preceding character to produce a new character. Diacritics are examples of combining characters.
"""

def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = normalize('NFD', txt)
    haved = ''.join(c for c in norm_txt if not combining(c))
    return normalize('NFC', shaved)

order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
shave_marks(order)

greeks = 'Ζέφυρος, Zéfiro'
shave_marks(greeks)

"""
Often the reason to remove diacritics is to change lating text to purse ASCII, but shave_marks also changes non-latin characters. It makes sense to analyze each case.

"""
import string


"""
Note: combining characters in unicode seem to come after the base character, example: in café, the unicode represntation is ('c', 0)
'c' 'a' 'f' 'f' 'e' (''̀', 230), where the last tuple represents the unicode combining character for é

"""
def shave_marks_latin(txt):
    """Remove all diacritic marks from Latin base characters"""
    norm_txt = normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if combining(c) and latin_base:
            continue # ignore diacritic on Latin base char and continue with next char
        keepers.append(c)
        if not combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return normalize('NFC', shaved)

# The below maps are used to replace characters that are not in the ascii table by using the translate() method
single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""", """'f"*^<''""---~>""")
translation_map = str.maketrans({'Œ': 'OE', 'œ': 'oe', 'æ': 'ae', 'Æ': 'AE', 'ß': 'ss', 'ſ': 'ss'})
translation_map.update(single_map)

def dewinize(txt):
    """Replace Win1252 symbols with ASCII chars or sequences"""
    return txt.translate(translation_map)

def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    return unicodedata.normalize('NFKC', no_marks)

text = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
dewinize(text)
asciize(text)


print(f"Listing strings: {os.listdir('.')}")

print(f"Listing bytes: {os.listdir(b'.')}")

"""
In case of weird name in paths, you can use os.fsencode() to convert a string to bytes. This is useful when you need to pass a path to a function that expects bytes. There's also os.fsdecode() to convert bytes to string.
"""

import os
os.fsencode('café.txt')
