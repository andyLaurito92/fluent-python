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
