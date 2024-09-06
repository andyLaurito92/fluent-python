class ArithmeticProgression:
    def __init__(self, begin, step=1, end=None):
        self.next_elem = begin
        self.step = step
        self.end = end

    def __iter__(self):
        while self.end is None or self.next_elem < self.end:
            yield self.next_elem
            self.next_elem += self.step
