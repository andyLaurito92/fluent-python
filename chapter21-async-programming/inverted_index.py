import sys
import unicodedata
from collections import defaultdict
from collections.abc import Iterator

STOP_CODE: int = sys.maxunicode + 1

Char = str
Index = defaultdict[str, set[Char]]


def tokenize(text: str) -> Iterator[str]:
    """Return iterator of uppercased words"""
    for word in text.upper().replace('-', ' ').split():
        yield word


class InvertedIndex:
    entries: Index

    def __init__(self, start:int = 32, stop: int = STOP_CODE):
        entries: Index = defaultdict(set)
        for char in (chr(i) for i in range(start, stop)):
            name = unicodedata.name(char, '')
            if name:
                for word in tokenize(name):
                    entries[word].add(char)
        self.entries = entries

    def search(self, query:str) -> set[Char]:
        if words := list(tokenize(query)):
            found = self.entries[words[0]]
            return found.intersection(*(self.entries[w] for w in words[1:]))
        else:
            return set()


def format_results(chars: set[Char]) -> Iterator[str]:
    for char in sorted(chars):
        name = unicodedata.name(char)
        code = ord(char)
        yield f'U+{code:04X}\t{char}\t{name}'


def main(words: list[str]) -> None:
    if not words:
        print('Please give one or more words to search')
        sys.exit(2)
    index = InvertedIndex()
    chars = index.search(' '.join(words))
    for line in format_results(chars):
        print(line)
    print('-' * 66, f'{len(chars)} found')


if __name__ == '__main__':
    main(sys.argv[1:])
