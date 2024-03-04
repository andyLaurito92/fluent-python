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

# Note how this line returns 99 and not c
cafe[0]

