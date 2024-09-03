import re
import reprlib 

WORD = re.compile(r'\w+')
class Sentence:
    def __init__(self, text: str) -> None:
        self.text = text
        self.words = WORD.findall(text)

    def __getitem__(self, idx: int) -> str:
        return self.words[idx]

    def __len__(self) -> int:
        return len(self.words)

    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)
                
