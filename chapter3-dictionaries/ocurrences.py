import re
import sys
import os
from collections import Counter
from collections import defaultdict

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

"""
Automatic handling of missing keys with defaultdict. The callable provided as argument to the constructor
is call whenever __getitem__ is passed a nonexisten key argument.
Internally, when __getitem__ doesn't find the key, it calls to the special method __missing__ (this happens also
in dict)

Note: The default_factory is only invoked to provide default values for __getitem__ cals, meaning that
methods like dd.get(k) and k in dd still returns false if k is not defined in dd
"""
def occurrences_defaultdict():
    index = defaultdict(list)
    with open(BOOK, encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for word_match in WORD_RE.finditer(line):
                word = word_match.group()
                column_no = word_match.start() + 1
                location = (line_no, column_no)
                index[word].append(location)
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


"""
Note: a search like k in my_dict.keys() is efficient for large mappings because dict.keys() returns a view. However, is more efficient to just do k in my_dict. It does the same job and it avoids the attribute lookup to find the .keys method
"""
