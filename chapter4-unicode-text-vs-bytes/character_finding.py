#!/usr/bin/env python3

import os
import sys
import unicodedata 

START, END = ord(' '), sys.maxunicode + 1

def find_emoji_containing(words):
    # Convert to set for not repeating words
    upper_case_words = {word.upper() for word in words}
    for code in range(START, END):
        char = chr(code)
        char_name = unicodedata.name(char, None)
        """
        If the character name is not None, we uppercase the name and split it by spaces to get a list of words
        """
        if char_name is not None and upper_case_words.issubset(char_name.upper().split()):
            print(f"U+{code:04X}\t{char}\t{char_name}")

           
if __name__ == "__main__":
    words = sys.argv[1:]
    if not words:
        print("Usage: python character_finding.py <word1> <word2> ...")
        sys.exit(1)
    find_emoji_containing(words)
   
