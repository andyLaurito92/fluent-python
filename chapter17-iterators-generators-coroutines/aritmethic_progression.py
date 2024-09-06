class ArithmeticProgression:
    def __init__(self, begin, step=1, end=None):
        self.next_elem = begin
        self.step = step
        self.end = end

    def __iter__(self):
        while self.end is None or self.next_elem < self.end:
            yield self.next_elem
            self.next_elem += self.step


"""
Note: The above implementation works fine if we just care
about integers. If we plan to use our arithmetic progression
with real numbers, then we migh find some issues with the
accumulative sum. For example:
"""

print("Cumulative effect of floating-points errors after successive additions")

print(100 * 1.1)

print(sum(1.1 for _ in range(100)))

print(1000 * 1.1)

print(sum(1.1 for _ in range(1000)))

"""
Therefore, a better implementation would be to avoid this cumulative problem
by calculating every time the exact result by multiplying the operands

Note: The above is a simplifaciton that doesn't use a class (which ends up
being boilerplate code)
"""

def aritprog_gen(begin, step=1, end=None):
    result = type(begin + step)(begin) # Coerce the return value
    forever = end is None
    idx = 0
    while forever or result < end:
        yield result
        idx += 1
        result = begin + step * index
