import re
import sys
import os
from collections import Counter

BOOK = f"{os.getcwd()}/chapter3-dictionaries/francais_en_argentine.txt"
WORD_RE = re.compile(r'\w+')

## Counting ocurrences using the default way
def ocurrences_normaldict():
    index = {}
    with open(BOOK, encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for word_match in WORD_RE.finditer(line):
                word = word_match.group()
                column_no = word_match.start() + 1
                location = (line_no, column_no)
                ## Bad example to show an idea. It's a bad example
                # We are using two searches to the dict when we could
                # be using just 1, as seen in the next example
                ocurrences = index.get(word, [])
                ocurrences.append(location)
                index[word] = ocurrences
    return index

def ocurrences_normaldict_usingsetdefault():
    index = {}
    with open(BOOK, encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for word_match in WORD_RE.finditer(line):
                word = word_match.group()
                column_no = word_match.start() + 1
                location = (line_no, column_no)
                ## Only 1 search to the key
                ocurrences = index.setdefault(word, []).append(location)
    return index
    

## Counting ocurrences using the Counter class
def ocurrences_counter():
    counter = Counter()
    with open(BOOK, 'r') as mybook:
        for line in mybook:
            for word_match in WORD_RE.finditer(line):
                word = word_match.group()
                counter.update([word])
    return counter

